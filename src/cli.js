#!/usr/bin/env node
import { randomFact, factOfTheDay, search, topics, formatFact } from './index.js'

const [cmd, ...rest] = process.argv.slice(2)

function help() {
  console.log(`factcovery-facts — short, sourced fun facts

  factcovery-facts                 random fact
  factcovery-facts random [topic]  random fact (optionally from a topic)
  factcovery-facts today           fact of the day
  factcovery-facts search <words>  search titles and summaries
  factcovery-facts topics          list topics
  factcovery-facts mcp             run the MCP server (stdio)

More facts every day: https://www.factcovery.com`)
}

switch (cmd) {
  case 'mcp':
    await import('./mcp.js')
    break
  case undefined:
  case 'random': {
    const f = randomFact(rest[0])
    console.log(f ? formatFact(f) : `No facts for topic "${rest[0]}". Try: factcovery-facts topics`)
    break
  }
  case 'today':
    console.log(formatFact(factOfTheDay()))
    break
  case 'search': {
    const hits = search(rest.join(' '))
    if (!hits.length) console.log('No match.')
    for (const f of hits) console.log(`- ${f.title}\n  ${f.factcovery}`)
    break
  }
  case 'topics':
    for (const t of topics) console.log(`${t.topic.padEnd(16)} ${String(t.count).padStart(3)}  ${t.factcovery}`)
    break
  default:
    help()
}
