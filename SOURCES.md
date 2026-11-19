# Sources

Every fact in this dataset was written by [Factcovery](https://www.factcovery.com) and checked against
at least one published source, stored in the `source` field of each record. The full article for each fact,
with more context, is at its `factcovery` URL (for example [the octopus fact](https://www.factcovery.com/facts/octopuses-have-three-hearts-blue-blood-and-neurons-throughout-their-arms)).

Summaries are short paraphrases, not quotations. If a source has moved or a fact is wrong,
please [open an issue](https://github.com/comficker/factcovery-facts/issues/new?template=wrong-fact.md).

## Most cited sources

| Domain | Facts |
|---|---:|
| en.wikipedia.org | 257 |
| sciencedaily.com | 16 |
| nationalgeographic.com | 10 |
| news.mongabay.com | 6 |
| sciencenews.org | 5 |
| eurekalert.org | 5 |
| ielc.libguides.com | 5 |
| journals.plos.org | 5 |
| space.com | 5 |
| nasa.gov | 5 |
| pubs.usgs.gov | 4 |
| science.nasa.gov | 4 |
| jpl.nasa.gov | 4 |
| animaldiversity.org | 4 |
| nbcnews.com | 4 |
| nps.gov | 4 |
| guinnessworldrecords.com | 4 |
| pmc.ncbi.nlm.nih.gov | 4 |
| scientificamerican.com | 3 |
| sci.news | 3 |
| news.cornell.edu | 3 |
| animals.sandiegozoo.org | 2 |
| nssdc.gsfc.nasa.gov | 2 |
| earthmagazine.org | 2 |
| iflscience.com | 2 |
| universetoday.com | 2 |
| history.com | 2 |
| downtoearth.org.in | 2 |
| nippon.com | 2 |
| lindahall.org | 2 |

152 source domains in total. How Factcovery checks facts: [About Factcovery](https://www.factcovery.com/about).

## Regenerating the data

`python3 scripts/build.py` reads the public Factcovery sitemap and API and rewrites `data/`.
`python3 scripts/readme.py` regenerates the READMEs.
