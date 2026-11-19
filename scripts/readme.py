#!/usr/bin/env python3
"""Generate README.md and i18n/README.<lang>.md from data/index.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
idx = json.loads((ROOT / "data/index.json").read_text())
facts = json.loads((ROOT / "data/facts.json").read_text())
TOTAL = idx["total"] // 100 * 100
SAMPLE = next(f for f in facts if f["id"].startswith("octopuses-have-three-hearts")) if any(
    f["id"].startswith("octopuses-have-three-hearts") for f in facts) else facts[0]

LANGS = {
    "en": ("English", "README.md"),
    "es": ("Español", "i18n/README.es.md"),
    "fr": ("Français", "i18n/README.fr.md"),
    "de": ("Deutsch", "i18n/README.de.md"),
    "pt": ("Português", "i18n/README.pt.md"),
    "vi": ("Tiếng Việt", "i18n/README.vi.md"),
    "ja": ("日本語", "i18n/README.ja.md"),
    "ko": ("한국어", "i18n/README.ko.md"),
    "zh": ("中文", "i18n/README.zh.md"),
}

T = {
    "en": dict(
        tagline=f"{TOTAL}+ short, sourced fun facts as JSON and CSV, with a tiny JavaScript API, a CLI and an MCP server.",
        intro="Every fact has a one-sentence summary, the source it was checked against, topics, and a link to the full article on [Factcovery](https://www.factcovery.com), a site with a new interesting fact every day.",
        topics="Topics", col_topic="Topic", col_n="Facts", col_json="JSON", col_page="Read online",
        page_anchor="{name} facts", install="Install", usage="Usage", data="Data files",
        mcp="MCP server", mcp_text="Use the facts from Claude, Cursor or any MCP client:",
        license="License", credit_text="Code: MIT. Data: CC BY 4.0. Please credit:",
        about="About Factcovery",
        about_text="[Factcovery](https://www.factcovery.com) publishes short, sourced facts about animals, space, history, science and the human body. Browse [random facts](https://www.factcovery.com/random), [weird facts](https://www.factcovery.com/weird-facts) or [funny facts](https://www.factcovery.com/funny-facts), or get one fact a day with the [Android app](https://play.google.com/store/apps/details?id=com.factcovery.app).",
        report="Found a wrong fact? [Open an issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md) with a better source.",
    ),
    "es": dict(
        tagline=f"Más de {TOTAL} datos curiosos breves y con fuente, en JSON y CSV, con una pequeña API de JavaScript, CLI y servidor MCP.",
        intro="Cada dato incluye un resumen de una frase, la fuente consultada, los temas y un enlace al artículo completo en [Factcovery](https://www.factcovery.com), un sitio con un dato curioso nuevo cada día.",
        topics="Temas", col_topic="Tema", col_n="Datos", col_json="JSON", col_page="Leer en línea",
        page_anchor="Datos curiosos: {name}", install="Instalación", usage="Uso", data="Archivos de datos",
        mcp="Servidor MCP", mcp_text="Usa los datos desde Claude, Cursor o cualquier cliente MCP:",
        license="Licencia", credit_text="Código: MIT. Datos: CC BY 4.0. Cita así:",
        about="Sobre Factcovery",
        about_text="[Factcovery](https://www.factcovery.com) publica datos curiosos breves y con fuente sobre animales, el espacio, historia, ciencia y el cuerpo humano. Prueba los [datos aleatorios](https://www.factcovery.com/random) o la [app para Android](https://play.google.com/store/apps/details?id=com.factcovery.app).",
        report="¿Un dato incorrecto? [Abre un issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md) con una fuente mejor.",
    ),
    "fr": dict(
        tagline=f"Plus de {TOTAL} anecdotes courtes et sourcées, en JSON et CSV, avec une petite API JavaScript, une CLI et un serveur MCP.",
        intro="Chaque anecdote comporte un résumé d'une phrase, sa source, ses thèmes et un lien vers l'article complet sur [Factcovery](https://www.factcovery.com), un site qui publie une nouvelle anecdote chaque jour.",
        topics="Thèmes", col_topic="Thème", col_n="Anecdotes", col_json="JSON", col_page="Lire en ligne",
        page_anchor="Anecdotes : {name}", install="Installation", usage="Utilisation", data="Fichiers de données",
        mcp="Serveur MCP", mcp_text="Utilisez les anecdotes dans Claude, Cursor ou tout client MCP :",
        license="Licence", credit_text="Code : MIT. Données : CC BY 4.0. Merci de citer :",
        about="À propos de Factcovery",
        about_text="[Factcovery](https://www.factcovery.com) publie des faits courts et sourcés sur les animaux, l'espace, l'histoire, la science et le corps humain. Essayez les [faits aléatoires](https://www.factcovery.com/random) ou l'[application Android](https://play.google.com/store/apps/details?id=com.factcovery.app).",
        report="Une erreur ? [Ouvrez une issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md) avec une meilleure source.",
    ),
    "de": dict(
        tagline=f"Über {TOTAL} kurze, belegte Fun Facts als JSON und CSV, mit kleiner JavaScript-API, CLI und MCP-Server.",
        intro="Jeder Fakt hat eine Ein-Satz-Zusammenfassung, die geprüfte Quelle, Themen und einen Link zum vollständigen Artikel auf [Factcovery](https://www.factcovery.com), einer Website mit jeden Tag einem neuen interessanten Fakt.",
        topics="Themen", col_topic="Thema", col_n="Fakten", col_json="JSON", col_page="Online lesen",
        page_anchor="Fakten: {name}", install="Installation", usage="Verwendung", data="Datendateien",
        mcp="MCP-Server", mcp_text="Nutze die Fakten in Claude, Cursor oder jedem MCP-Client:",
        license="Lizenz", credit_text="Code: MIT. Daten: CC BY 4.0. Bitte nenne:",
        about="Über Factcovery",
        about_text="[Factcovery](https://www.factcovery.com) veröffentlicht kurze, belegte Fakten über Tiere, Weltraum, Geschichte, Wissenschaft und den menschlichen Körper. Probiere [zufällige Fakten](https://www.factcovery.com/random) oder die [Android-App](https://play.google.com/store/apps/details?id=com.factcovery.app).",
        report="Fehler gefunden? [Issue öffnen](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md) mit einer besseren Quelle.",
    ),
    "pt": dict(
        tagline=f"Mais de {TOTAL} curiosidades curtas e com fonte, em JSON e CSV, com uma pequena API JavaScript, CLI e servidor MCP.",
        intro="Cada curiosidade tem um resumo de uma frase, a fonte consultada, os temas e um link para o artigo completo no [Factcovery](https://www.factcovery.com), um site com uma curiosidade nova todos os dias.",
        topics="Temas", col_topic="Tema", col_n="Fatos", col_json="JSON", col_page="Ler online",
        page_anchor="Curiosidades: {name}", install="Instalação", usage="Uso", data="Arquivos de dados",
        mcp="Servidor MCP", mcp_text="Use as curiosidades no Claude, Cursor ou qualquer cliente MCP:",
        license="Licença", credit_text="Código: MIT. Dados: CC BY 4.0. Cite assim:",
        about="Sobre o Factcovery",
        about_text="O [Factcovery](https://www.factcovery.com) publica fatos curtos e com fonte sobre animais, espaço, história, ciência e o corpo humano. Experimente os [fatos aleatórios](https://www.factcovery.com/random) ou o [app Android](https://play.google.com/store/apps/details?id=com.factcovery.app).",
        report="Achou um erro? [Abra uma issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md) com uma fonte melhor.",
    ),
    "vi": dict(
        tagline=f"Hơn {TOTAL} sự thật thú vị ngắn gọn, có nguồn, dạng JSON và CSV, kèm API JavaScript nhỏ, CLI và MCP server.",
        intro="Mỗi fact có tóm tắt một câu, nguồn đã đối chiếu, chủ đề và liên kết tới bài đầy đủ trên [Factcovery](https://www.factcovery.com), trang mỗi ngày một sự thật thú vị mới.",
        topics="Chủ đề", col_topic="Chủ đề", col_n="Số fact", col_json="JSON", col_page="Đọc online",
        page_anchor="Sự thật thú vị về {name}", install="Cài đặt", usage="Cách dùng", data="Tệp dữ liệu",
        mcp="MCP server", mcp_text="Dùng dữ liệu trong Claude, Cursor hoặc client MCP bất kỳ:",
        license="Giấy phép", credit_text="Code: MIT. Dữ liệu: CC BY 4.0. Vui lòng ghi nguồn:",
        about="Về Factcovery",
        about_text="[Factcovery](https://www.factcovery.com) đăng các sự thật ngắn, có nguồn về động vật, vũ trụ, lịch sử, khoa học và cơ thể người. Xem [fact ngẫu nhiên](https://www.factcovery.com/random) hoặc [app Android](https://play.google.com/store/apps/details?id=com.factcovery.app).",
        report="Thấy fact sai? [Mở issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md) kèm nguồn tốt hơn.",
    ),
    "ja": dict(
        tagline=f"出典付きの短い雑学 {TOTAL} 件以上（JSON・CSV）。小さな JavaScript API、CLI、MCP サーバー付き。",
        intro="各雑学には一文の要約、確認した出典、トピック、そして毎日新しい雑学を届ける [Factcovery](https://www.factcovery.com) の記事へのリンクが含まれます。",
        topics="トピック", col_topic="トピック", col_n="件数", col_json="JSON", col_page="オンラインで読む",
        page_anchor="{name}の雑学", install="インストール", usage="使い方", data="データファイル",
        mcp="MCP サーバー", mcp_text="Claude、Cursor などの MCP クライアントから使えます：",
        license="ライセンス", credit_text="コード: MIT。データ: CC BY 4.0。クレジット表記:",
        about="Factcovery について",
        about_text="[Factcovery](https://www.factcovery.com) は動物、宇宙、歴史、科学、人体についての出典付きの短い雑学を公開しています。[ランダム雑学](https://www.factcovery.com/random) や [Android アプリ](https://play.google.com/store/apps/details?id=com.factcovery.app) もどうぞ。",
        report="間違いを見つけたら、より良い出典とともに [issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md) を開いてください。",
    ),
    "ko": dict(
        tagline=f"출처가 있는 짧은 재미있는 사실 {TOTAL}개 이상(JSON·CSV), 작은 JavaScript API, CLI, MCP 서버 포함.",
        intro="각 사실에는 한 문장 요약, 확인한 출처, 주제, 그리고 매일 새로운 사실을 소개하는 [Factcovery](https://www.factcovery.com)의 전체 글 링크가 있습니다.",
        topics="주제", col_topic="주제", col_n="개수", col_json="JSON", col_page="온라인에서 읽기",
        page_anchor="{name} 재미있는 사실", install="설치", usage="사용법", data="데이터 파일",
        mcp="MCP 서버", mcp_text="Claude, Cursor 등 MCP 클라이언트에서 사용하세요:",
        license="라이선스", credit_text="코드: MIT. 데이터: CC BY 4.0. 출처 표기:",
        about="Factcovery 소개",
        about_text="[Factcovery](https://www.factcovery.com)는 동물, 우주, 역사, 과학, 인체에 관한 출처 있는 짧은 사실을 소개합니다. [랜덤 사실](https://www.factcovery.com/random)이나 [Android 앱](https://play.google.com/store/apps/details?id=com.factcovery.app)도 확인해 보세요.",
        report="틀린 사실을 발견했나요? 더 나은 출처와 함께 [issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md)를 열어 주세요.",
    ),
    "zh": dict(
        tagline=f"{TOTAL} 多条附出处的简短冷知识（JSON、CSV），附带小型 JavaScript API、命令行工具和 MCP 服务器。",
        intro="每条冷知识都有一句话摘要、核对过的出处、主题标签，以及指向 [Factcovery](https://www.factcovery.com) 完整文章的链接——一个每天更新有趣冷知识的网站。",
        topics="主题", col_topic="主题", col_n="数量", col_json="JSON", col_page="在线阅读",
        page_anchor="{name}冷知识", install="安装", usage="用法", data="数据文件",
        mcp="MCP 服务器", mcp_text="在 Claude、Cursor 或任何 MCP 客户端中使用：",
        license="许可", credit_text="代码：MIT。数据：CC BY 4.0。请注明：",
        about="关于 Factcovery",
        about_text="[Factcovery](https://www.factcovery.com) 发布关于动物、太空、历史、科学和人体的简短、附出处的冷知识。试试 [随机冷知识](https://www.factcovery.com/random) 或 [Android 应用](https://play.google.com/store/apps/details?id=com.factcovery.app)。",
        report="发现错误？请附上更好的出处 [提交 issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md)。",
    ),
}


def build(lang):
    t = T[lang]
    prefix = "" if lang == "en" else "../"
    def link(code, path):
        if lang == "en":
            return path
        return "../README.md" if code == "en" else path.replace("i18n/", "")
    nav = " · ".join(f"**{name}**" if code == lang else f"[{name}]({link(code, path)})"
                     for code, (name, path) in LANGS.items())
    rows = "\n".join(
        f"| {x['name']} | {x['count']} | [`{x['topic']}.json`]({prefix}{x['file']}) | [{t['page_anchor'].format(name=x['name'])}]({x['factcovery']}) |"
        for x in idx["topics"] if x["count"] >= 5
    )
    s = SAMPLE
    return f"""# factcovery-facts

{nav}

{t['tagline']}

{t['intro']}

```json
{json.dumps({k: s[k] for k in ('id', 'title', 'summary', 'topics', 'source', 'factcovery')}, ensure_ascii=False, indent=2)}
```

## {t['topics']}

| {t['col_topic']} | {t['col_n']} | {t['col_json']} | {t['col_page']} |
|---|---:|---|---|
{rows}

## {t['install']}

```bash
npm install factcovery-facts
```

## {t['usage']}

```js
import {{ randomFact, factOfTheDay, factsByTopic, search }} from 'factcovery-facts'

randomFact()            // any fact
randomFact('space')     // a random space fact
factOfTheDay()          // same fact for everyone today
factsByTopic('penguins')
search('octopus')
```

```bash
npx factcovery-facts            # random fact
npx factcovery-facts today      # fact of the day
npx factcovery-facts topics
```

## {t['data']}

- `data/facts.json` · `data/facts.csv`
- `data/index.json`
- `data/topics/<topic>.json`
- CDN: `https://cdn.jsdelivr.net/npm/factcovery-facts/data/facts.json`

## {t['mcp']}

{t['mcp_text']}

```json
{{ "mcpServers": {{ "factcovery-facts": {{ "command": "npx", "args": ["-y", "-p", "factcovery-facts", "factcovery-facts-mcp"] }} }} }}
```

Tools: `random_fact`, `fact_of_the_day`, `search_facts`, `facts_by_topic`, `get_fact`, `list_topics`.

## {t['about']}

{t['about_text']}

{t['report']}

## {t['license']}

{t['credit_text']} **Facts by [Factcovery](https://www.factcovery.com)**. [SOURCES.md]({prefix}SOURCES.md)
"""


for code, (_, path) in LANGS.items():
    p = ROOT / path
    p.parent.mkdir(exist_ok=True)
    p.write_text(build(code))
print("ok")
