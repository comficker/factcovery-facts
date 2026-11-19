import { test } from 'node:test'
import assert from 'node:assert/strict'
import { facts, topics, randomFact, factOfTheDay, factsByTopic, search, getFact } from '../src/index.js'

test('dataset shape', () => {
  assert.ok(facts.length >= 500)
  for (const f of facts) {
    assert.ok(f.id && f.title && f.summary, f.id)
    assert.match(f.source, /^https?:\/\//)
    assert.match(f.factcovery, /^https:\/\/www\.factcovery\.com\/facts\//)
  }
  assert.equal(new Set(facts.map((f) => f.id)).size, facts.length)
})

test('helpers', () => {
  assert.ok(randomFact())
  assert.ok(factOfTheDay(new Date('2026-12-25')))
  assert.ok(factsByTopic('space').length > 0)
  assert.ok(topics.length > 0)
  assert.ok(search('octopus').length > 0)
  assert.equal(getFact('does-not-exist'), null)
})
