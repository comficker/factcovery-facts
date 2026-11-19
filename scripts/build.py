#!/usr/bin/env python3
"""Build the factcovery-facts dataset from the public Factcovery API.

Only facts listed in the Factcovery sitemap are included (the curated, indexable set).
Each record keeps a short summary (first sentence), the cited source and a link to the
full fact page; the full article text stays on factcovery.com.

Usage: python3 scripts/build.py
"""
import json
import re
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

SITE = "https://www.factcovery.com"
API = "https://touch.ninosaur.com/fact"
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
UA = {"User-Agent": "factcovery-facts-build/1.0", "Accept-Language": "en"}


def get(url, as_json=True):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read().decode("utf-8")
            return json.loads(body) if as_json else body
        except Exception:
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"failed: {url}")


def sitemap_fact_slugs():
    index = get(f"{SITE}/sitemap-index.xml", as_json=False)
    slugs = []
    for loc in re.findall(r"<loc>([^<]+)</loc>", index):
        if "sitemap-fact" not in loc:
            continue
        xml = get(loc.replace("&amp;", "&"), as_json=False)
        for url in re.findall(r"<loc>([^<]+)</loc>", xml):
            m = re.match(rf"{re.escape(SITE)}/facts/([^/?#]+)$", url)
            if m:
                slugs.append(m.group(1))
    return list(dict.fromkeys(slugs))


def first_sentence(text, limit=240):
    text = re.sub(r"\s+", " ", (text or "").strip())
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    if len(s) > limit:
        s = s[: limit - 1].rsplit(" ", 1)[0] + "…"
    return s


def domain(url):
    m = re.match(r"https?://(?:www\.)?([^/]+)", url or "")
    return m.group(1) if m else None


def sitemap_topics():
    xml = get(f"{SITE}/sitemap-topic.xml", as_json=False)
    return [m for m in re.findall(rf"{re.escape(SITE)}/topics/([^/<?#]+)", xml)]


def main():
    import sys
    if "--skip-fetch" in sys.argv and (DATA / "facts.json").exists():
        facts = json.loads((DATA / "facts.json").read_text())
        write(facts)
        return
    slugs = sitemap_fact_slugs()
    print(f"{len(slugs)} facts in sitemap")
    facts = []
    for i, slug in enumerate(slugs, 1):
        d = get(f"{API}/facts/{slug}/")
        if d.get("status") != "public" or not d.get("source"):
            continue
        topics = [t["id_string"] for t in d.get("topics", [])]
        facts.append({
            "id": d["id_string"],
            "title": d["name"].strip(),
            "summary": first_sentence(d.get("content")),
            "topics": topics,
            "source": d["source"],
            "source_domain": domain(d["source"]),
            "factcovery": f"{SITE}/facts/{d['id_string']}",
            "updated": (d.get("updated") or "")[:10],
        })
        if i % 50 == 0:
            print(f"  {i}/{len(slugs)}")
        time.sleep(0.15)

    facts.sort(key=lambda f: f["id"])
    write(facts)


def write(facts):
    DATA.mkdir(exist_ok=True)
    (DATA / "topics").mkdir(exist_ok=True)
    (DATA / "facts.json").write_text(json.dumps(facts, ensure_ascii=False, indent=1) + "\n")

    # Topic files only for the curated topic hubs listed in the Factcovery sitemap.
    hubs = sitemap_topics()
    for old in (DATA / "topics").glob("*.json"):
        old.unlink()
    by_topic = defaultdict(list)
    names = {}
    for f in facts:
        for t in f["topics"]:
            if t in hubs:
                by_topic[t].append(f)
    topic_meta = {t["id_string"]: t for t in get(f"{API}/topics/?page_size=500").get("results", [])}
    index = []
    for t, items in sorted(by_topic.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        name = topic_meta.get(t, {}).get("name") or t.replace("-", " ").title()
        if name == name.lower():
            name = name.replace("-", " ").title()
        names[t] = name
        (DATA / "topics" / f"{t}.json").write_text(json.dumps({
            "topic": t,
            "name": name,
            "count": len(items),
            "factcovery": f"{SITE}/topics/{t}",
            "facts": items,
        }, ensure_ascii=False, indent=1) + "\n")
        index.append({"topic": t, "name": name, "count": len(items),
                      "file": f"data/topics/{t}.json", "factcovery": f"{SITE}/topics/{t}"})

    (DATA / "index.json").write_text(json.dumps({
        "name": "factcovery-facts",
        "description": "Short, sourced interesting facts from Factcovery",
        "license": "CC-BY-4.0",
        "credit": "Facts by Factcovery (https://www.factcovery.com)",
        "factcovery": SITE,
        "total": len(facts),
        "topics": index,
    }, ensure_ascii=False, indent=1) + "\n")

    with (DATA / "facts.csv").open("w") as fh:
        import csv
        w = csv.writer(fh)
        w.writerow(["id", "title", "summary", "topics", "source", "factcovery"])
        for f in facts:
            w.writerow([f["id"], f["title"], f["summary"], "|".join(f["topics"]), f["source"], f["factcovery"]])
    print(f"wrote {len(facts)} facts, {len(index)} topics")


if __name__ == "__main__":
    main()
