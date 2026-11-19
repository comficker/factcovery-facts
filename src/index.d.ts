export interface Fact {
  id: string
  title: string
  summary: string
  topics: string[]
  source: string
  source_domain: string | null
  /** Full fact page on Factcovery */
  factcovery: string
  updated: string
}

export interface TopicHub {
  topic: string
  name: string
  count: number
  file: string
  factcovery: string
}

export const facts: Fact[]
export const topics: TopicHub[]
export const SITE: string
export const CREDIT: string
export function getFact(id: string): Fact | null
export function factsByTopic(topic: string): Fact[]
export function randomFact(topic?: string): Fact | null
export function factOfTheDay(date?: Date): Fact
export function search(query: string, limit?: number): Fact[]
export function formatFact(fact: Fact): string
