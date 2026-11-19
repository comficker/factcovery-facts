# factcovery-facts

**English** · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [Deutsch](i18n/README.de.md) · [Português](i18n/README.pt.md) · [Tiếng Việt](i18n/README.vi.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [中文](i18n/README.zh.md)

500+ short, sourced fun facts as JSON and CSV, with a tiny JavaScript API, a CLI and an MCP server.

Every fact has a one-sentence summary, the source it was checked against, topics, and a link to the full article on [Factcovery](https://www.factcovery.com), a site with a new interesting fact every day.

```json
{
  "id": "octopuses-have-three-hearts-blue-blood-and-neurons-throughout-their-arms",
  "title": "Octopuses Have Three Hearts, Blue Blood and Most of Their Neurons in Their Arms",
  "summary": "An octopus has three hearts, blue blood and a nervous system in which most neurons sit outside the brain.",
  "topics": [
    "biology",
    "marine-life",
    "zoology",
    "neuroscience"
  ],
  "source": "https://en.wikipedia.org/wiki/Octopus",
  "factcovery": "https://www.factcovery.com/facts/octopuses-have-three-hearts-blue-blood-and-neurons-throughout-their-arms"
}
```

## Topics

| Topic | Facts | JSON | Read online |
|---|---:|---|---|
| History | 61 | [`history.json`](data/topics/history.json) | [History facts](https://www.factcovery.com/topics/history) |
| Marine Life | 40 | [`marine-life.json`](data/topics/marine-life.json) | [Marine Life facts](https://www.factcovery.com/topics/marine-life) |
| Science | 40 | [`science.json`](data/topics/science.json) | [Science facts](https://www.factcovery.com/topics/science) |
| Animals | 38 | [`animals.json`](data/topics/animals.json) | [Animals facts](https://www.factcovery.com/topics/animals) |
| Space | 35 | [`space.json`](data/topics/space.json) | [Space facts](https://www.factcovery.com/topics/space) |
| Ocean | 20 | [`ocean.json`](data/topics/ocean.json) | [Ocean facts](https://www.factcovery.com/topics/ocean) |
| Hedgehogs | 18 | [`hedgehogs.json`](data/topics/hedgehogs.json) | [Hedgehogs facts](https://www.factcovery.com/topics/hedgehogs) |
| Lion | 18 | [`lion.json`](data/topics/lion.json) | [Lion facts](https://www.factcovery.com/topics/lion) |
| Owls | 18 | [`owls.json`](data/topics/owls.json) | [Owls facts](https://www.factcovery.com/topics/owls) |
| Platypus | 18 | [`platypus.json`](data/topics/platypus.json) | [Platypus facts](https://www.factcovery.com/topics/platypus) |
| Sharks | 18 | [`sharks.json`](data/topics/sharks.json) | [Sharks facts](https://www.factcovery.com/topics/sharks) |
| Tiger | 18 | [`tiger.json`](data/topics/tiger.json) | [Tiger facts](https://www.factcovery.com/topics/tiger) |
| Bee | 17 | [`bee.json`](data/topics/bee.json) | [Bee facts](https://www.factcovery.com/topics/bee) |
| Cat | 17 | [`cat.json`](data/topics/cat.json) | [Cat facts](https://www.factcovery.com/topics/cat) |
| Dinosaurs | 17 | [`dinosaurs.json`](data/topics/dinosaurs.json) | [Dinosaurs facts](https://www.factcovery.com/topics/dinosaurs) |
| Mars | 17 | [`mars.json`](data/topics/mars.json) | [Mars facts](https://www.factcovery.com/topics/mars) |
| Moon | 17 | [`moon.json`](data/topics/moon.json) | [Moon facts](https://www.factcovery.com/topics/moon) |
| Butterfly | 16 | [`butterfly.json`](data/topics/butterfly.json) | [Butterfly facts](https://www.factcovery.com/topics/butterfly) |
| Christmas | 16 | [`christmas.json`](data/topics/christmas.json) | [Christmas facts](https://www.factcovery.com/topics/christmas) |
| Earth | 16 | [`earth.json`](data/topics/earth.json) | [Earth facts](https://www.factcovery.com/topics/earth) |
| Japan | 16 | [`japan.json`](data/topics/japan.json) | [Japan facts](https://www.factcovery.com/topics/japan) |
| Canada | 15 | [`canada.json`](data/topics/canada.json) | [Canada facts](https://www.factcovery.com/topics/canada) |
| Engineering | 15 | [`engineering.json`](data/topics/engineering.json) | [Engineering facts](https://www.factcovery.com/topics/engineering) |
| Giraffe | 15 | [`giraffe.json`](data/topics/giraffe.json) | [Giraffe facts](https://www.factcovery.com/topics/giraffe) |
| Penguins | 15 | [`penguins.json`](data/topics/penguins.json) | [Penguins facts](https://www.factcovery.com/topics/penguins) |
| Sports | 15 | [`sports.json`](data/topics/sports.json) | [Sports facts](https://www.factcovery.com/topics/sports) |
| Human Body | 14 | [`human-body.json`](data/topics/human-body.json) | [Human Body facts](https://www.factcovery.com/topics/human-body) |
| Mexico | 14 | [`mexico.json`](data/topics/mexico.json) | [Mexico facts](https://www.factcovery.com/topics/mexico) |
| Volcano | 14 | [`volcano.json`](data/topics/volcano.json) | [Volcano facts](https://www.factcovery.com/topics/volcano) |
| Ancient Egypt | 13 | [`ancient-egypt.json`](data/topics/ancient-egypt.json) | [Ancient Egypt facts](https://www.factcovery.com/topics/ancient-egypt) |
| Festivals | 12 | [`festivals.json`](data/topics/festivals.json) | [Festivals facts](https://www.factcovery.com/topics/festivals) |
| Octopus | 11 | [`octopus.json`](data/topics/octopus.json) | [Octopus facts](https://www.factcovery.com/topics/octopus) |
| World War Ii | 8 | [`world-war-ii.json`](data/topics/world-war-ii.json) | [World War Ii facts](https://www.factcovery.com/topics/world-war-ii) |

## Install

```bash
npm install factcovery-facts
```

## Usage

```js
import { randomFact, factOfTheDay, factsByTopic, search } from 'factcovery-facts'

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

## Data files

- `data/facts.json` · `data/facts.csv`
- `data/index.json`
- `data/topics/<topic>.json`
- CDN: `https://cdn.jsdelivr.net/npm/factcovery-facts/data/facts.json`

## MCP server

Use the facts from Claude, Cursor or any MCP client:

```json
{ "mcpServers": { "factcovery-facts": { "command": "npx", "args": ["-y", "-p", "factcovery-facts", "factcovery-facts-mcp"] } } }
```

Tools: `random_fact`, `fact_of_the_day`, `search_facts`, `facts_by_topic`, `get_fact`, `list_topics`.

## About Factcovery

[Factcovery](https://www.factcovery.com) publishes short, sourced facts about animals, space, history, science and the human body. Browse [random facts](https://www.factcovery.com/random), [weird facts](https://www.factcovery.com/weird-facts) or [funny facts](https://www.factcovery.com/funny-facts), or get one fact a day with the [Android app](https://play.google.com/store/apps/details?id=com.factcovery.app).

Found a wrong fact? [Open an issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md) with a better source.

## License

Code: MIT. Data: CC BY 4.0. Please credit: **Facts by [Factcovery](https://www.factcovery.com)**. [SOURCES.md](SOURCES.md)
