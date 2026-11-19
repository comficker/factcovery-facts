import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'

const root = join(dirname(fileURLToPath(import.meta.url)), '..')
const load = (p) => JSON.parse(readFileSync(join(root, p), 'utf8'))

/** All facts: { id, title, summary, topics, source, source_domain, factcovery, updated } */
export const facts = load('data/facts.json')

/** Topic hubs with counts and their Factcovery page. */
export const topics = load('data/index.json').topics

export const SITE = 'https://www.factcovery.com'
export const CREDIT = 'Facts by Factcovery (https://www.factcovery.com)'

const byId = new Map(facts.map((f) => [f.id, f]))

/** Get one fact by its id (slug). */
export function getFact(id) {
  return byId.get(id) ?? null
}

/** Facts tagged with a topic, e.g. "space", "penguins". */
export function factsByTopic(topic) {
  const t = String(topic).toLowerCase()
  return facts.filter((f) => f.topics.includes(t))
}

/** A random fact, optionally limited to a topic. */
export function randomFact(topic) {
  const pool = topic ? factsByTopic(topic) : facts
  return pool.length ? pool[Math.floor(Math.random() * pool.length)] : null
}

/** The same fact for everyone on a given day (UTC), handy for "fact of the day" widgets. */
export function factOfTheDay(date = new Date()) {
  const day = Math.floor(Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate()) / 86400000)
  return facts[day % facts.length]
}

/** Case-insensitive search in title and summary. */
export function search(query, limit = 20) {
  const q = String(query).toLowerCase().trim()
  if (!q) return []
  return facts
    .filter((f) => f.title.toLowerCase().includes(q) || f.summary.toLowerCase().includes(q))
    .slice(0, limit)
}

/** Plain-text line with credit, for bots and widgets. */
export function formatFact(f) {
  return `${f.title}. ${f.summary}\nSource: ${f.source}\nMore: ${f.factcovery}`
}
