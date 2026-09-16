---
name: evidence-chains
description: Extract typed paper claims into lemmalog and discuss multi-paper evidence chains (A said X→Y, B said Y→Z). Use when extracting facts from papers or reviews, asserting claims, querying two-hop or three-hop links, or explaining chains of evidence across papers.
---

# Evidence chains

Schema: [`lemmalog/SCHEMA.md`](../../../lemmalog/SCHEMA.md). Rules: [`lemmalog/rules/evidence-chains.dl`](../../../lemmalog/rules/evidence-chains.dl). Graphify may *suggest* paths; only lemmalog stores provenance.

## Setup

If `lemmalog_*` MCP tools are missing, print the one-line register command from the lemmalog skill and continue: still write claims into the review, do not block. Prefer MCP in the parent; use `lemmalog-cli` for sub-agents. Do not write from MCP and CLI at once.

On first corpus session: `lemmalog_observe` the `describes` lines from SCHEMA.md; install rules batch `evidence-chains` from the `.dl` file; `lemmalog_query` one goal to confirm backfill.

## Extract and assert

From a review **Claims** table or from canonical text you just checked:

1. Canonicalize concept names (`alias_of` if a synonym already exists). Do not mint a second node for the same idea.
2. Assert paper `title` / `year`, the reified `edge`, `located`, and the closable `X --rel[conf]--> Y`.
3. Tag confidence honestly. Never assert an unread hop.

## Query chains

Do not close transitivity in your head.

```text
two_hop(X, Z, P1, P2)
three_hop(X, W, P1, P2, P3)
```

Then `lemmalog_why` on a derived fact. Re-read the **weakest** `located` anchors in the papers. If an endpoint was a false name, retract and alias.

Graphify: `graphify path "A" "B"` or surprising connections are **candidates** only. Promote to lemmalog after reading the papers.

## Discuss (do not invent the middle node)

In chat (perspectives files come later): name X, Y, Z; papers P1/P2; quote or paraphrase each hop with anchors; product confidence from the why-tree; say what would break the chain. Optional: a short appendix under the relevant `reviews/{id}.md`.
