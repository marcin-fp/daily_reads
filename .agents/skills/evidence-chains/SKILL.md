---
name: evidence-chains
description: Extract typed claims from schema-v1 paper reviews into lemmalog and discuss multi-paper evidence chains (A said X→Y, B said Y→Z). Use when asserting reviewed claims, querying two-hop or three-hop links, or explaining chains of evidence across reviewed papers.
---

# Evidence chains

Schema: [`lemmalog/SCHEMA.md`](../../../lemmalog/SCHEMA.md). Rules: [`lemmalog/rules/evidence-chains.dl`](../../../lemmalog/rules/evidence-chains.dl). Graphify may *suggest* paths; only lemmalog stores provenance.

## Setup

If `lemmalog_*` MCP tools are missing, print the one-line register command from the lemmalog skill and continue: still write claims into the review, do not block. Prefer MCP in the parent; use `lemmalog-cli` for sub-agents. Do not write from MCP and CLI at once.

On first corpus session: `lemmalog_observe` the `describes` lines from SCHEMA.md; install rules batch `evidence-chains` from the `.dl` file; `lemmalog_query` one goal to confirm backfill.

## Extract and assert

From a schema-v1 review. Do not open `papers/canonical`, `papers/raw`, or the full-paper graph in this skill.

1. Assert paper metadata and `reviewed_in` from frontmatter, including publication date, authors, affiliations, funders, grants, and venue when present.
2. Canonicalize concept names (`alias_of` if a synonym already exists). Do not mint a second node for the same idea.
3. For each non-empty Claims row, assert the reified `edge`, its canonical `located` anchor, its `reviewed_in` path, and the closable `X --rel[conf]--> Y`.
4. Tag confidence honestly. Never assert a hop that is absent from the review.

## Query chains

Do not close transitivity in your head.

```text
two_hop(X, Z, P1, P2)
three_hop(X, W, P1, P2, P3)
```

Then `lemmalog_why` on a derived fact. Read the linked reviews and inspect the weakest claim's summary, critical discussion, and Claims row. If the review does not contain enough evidence, record the gap and invoke/request `paper-review` to refresh that review. Do not silently reopen a full paper. If an endpoint was a false name, retract and alias.

The reviews graph may suggest a path. Promote it to lemmalog only when the reviews contain the required claim edges. The full-paper graph is not a synthesis source.

## Discuss (do not invent the middle node)

In chat: name X, Y, Z; papers P1/P2; quote or paraphrase each hop from its review; product confidence from the why-tree; say what would break the chain. Do not edit a completed review during synthesis; gaps go back through `paper-review`.
