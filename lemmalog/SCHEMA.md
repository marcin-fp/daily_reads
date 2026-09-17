# Lemmalog schema for papers

Typed claims live here. Graphify is a concept map; it does not store provenance or proof trees.

Install [`rules/evidence-chains.dl`](rules/evidence-chains.dl) once as batch `evidence-chains`. Assert `describes` only the first time you **use** a relation in a fact, not the whole table. Query with `lemmalog_query`; trust derived facts only after `lemmalog_why`.

Lemmalog stores scientific relations, their provenance, and one pointer from each paper id to its schema-v1 review. Titles, dates, authors, affiliations, funders, grants, venue, facets, and compute live in the review. Do not copy them here.

## Entity names

- Papers: `arxiv:2606.18195` (no version). Quote in rules: `"arxiv:2606.18195"`.
- Concepts: ≤8 words, natural language, quoted. Alias variants: `local --alias_of[conf]--> canonical`.
- Edges: `e:{paper-id}:{short}` with no spaces, e.g. `e:2606.18195:dopsd-sample-eff`.
- `located` objects: space-free, `papers/canonical/2606.18195.md:Abstract` or `…md:L42`.

Confidence: verified quotes `[1.0]`; fair paraphrases `[0.7]`–`[0.9]`; interpretive `[0.4]`–`[0.6]`. Untagged defaults to 0.9 and decays down the proof chain. Structural provenance (`reviewed_in`, `source_paper`, `from`, `to`, `kind`, `located`) is not uncertain once copied from a validated review; assert it at `[1.0]` so it does not dilute the scientific edge confidence.

## Relations

Assert `Relation --describes--> "one-line meaning"` the first time that relation appears in an asserted fact. Do not preload unused relation names.

### Per reviewed paper (thin pointer)

| Triple | Meaning |
|--------|---------|
| `paper --reviewed_in--> reviews/{id}.md` | Schema-v1 review that downstream synthesis may read. |

### Per Claims row (required)

| Triple | Meaning |
|--------|---------|
| `edge --source_paper--> paper` | Which paper asserted this edge. |
| `edge --from--> X` | Subject concept. |
| `edge --to--> Y` | Object concept. |
| `edge --kind--> implies` | `implies` \| `improves` \| `contradicts` \| `uses` \| `evaluates`. |
| `edge --located--> path:anchor` | Full-paper source anchor checked by paper-review. |
| `X --implies[c]--> Y` | Closable graph for `kind=implies` (same for other kinds as named rels). |
| `X --improves[c]--> Y` | Same pattern. |
| `X --contradicts[c]--> Y` | Same pattern. |
| `X --uses[c]--> Y` | Same pattern. |
| `X --evaluates[c]--> Y` | Same pattern. |
| `local --alias_of[c]--> canonical` | Vocabulary merge. |

Reify **every** closable triple as an `edge` so relation-specific provenance rules can name the paper. Do not assert `X --implies--> Y` without a matching edge.

Bibliography and competitive-landscape metadata stay in the review. If a future analysis genuinely needs metadata inside Datalog, add only the required facts in a dedicated, removable rule/analysis batch. Do not make them part of normal paper ingestion.

## Evidence strength

No minimum paper count determines whether a claim may be used. One strong study can be evidence; five papers sharing the same data, authors, judge, or failure mode are not five independent confirmations.

The confidence on `X --relation[c]--> Y` reflects how directly that paper's evidence supports that scoped relation. It does not encode journal prestige or the number of other papers making the claim. Peer review is a modest prior about scrutiny, not a multiplier and not a correctness certificate.

Downstream prose uses graded language:

- **reported**: one paper states the claim; evidence not independently assessed.
- **supported**: the paper provides direct evidence that survives its Critical discussion.
- **corroborated**: at least two meaningfully independent sources support the same scoped claim.
- **well-established**: diverse, independent evidence across methods or settings, with no unresolved strong contradiction.
- **contested**: credible reviews support incompatible conclusions or regimes.

Count independence, not citations: shared datasets, model families, authors, evaluators, or derived data reduce the value of repetition. Keep a single-source claim available to synthesis; label its support rather than suppressing it.

## Example (one paper, one claim)

```text
reviewed_in --describes[1.0]--> schema-v1 review for downstream reading
source_paper --describes[1.0]--> paper that asserted this edge
from --describes[1.0]--> edge subject concept
to --describes[1.0]--> edge object concept
kind --describes[1.0]--> implies improves contradicts uses evaluates
located --describes[1.0]--> space-free file anchor
implies --describes[1.0]--> source supports destination

arxiv:2606.18195 --reviewed_in[1.0]--> reviews/2606.18195.md
e:2606.18195:suffix-teacher --source_paper[1.0]--> arxiv:2606.18195
e:2606.18195:suffix-teacher --from[1.0]--> "d-OPSD suffix teacher"
e:2606.18195:suffix-teacher --to[1.0]--> "on-policy self distillation"
e:2606.18195:suffix-teacher --kind[1.0]--> implies
e:2606.18195:suffix-teacher --located[1.0]--> papers/canonical/2606.18195.md:Abstract
d-OPSD suffix teacher --implies[0.8]--> on-policy self distillation
```

## Derived (rules batch `evidence-chains`)

- `supported_by(X, Y, P)` — paper P asserts an `implies` edge from X to Y.
- `contradicted_by(X, Y, P)` / `improved_by` / `used_by` / `evaluated_by` — relation-specific source lookup.
- `review_for_edge(E, R)` — derive review R through edge E's `source_paper`; do not store the pointer on every edge.
- `two_hop(X, Z, P1, P2)` — `X -implies-> Y -implies-> Z` with **different** papers P1 ≠ P2.
- `three_hop(X, W, P1, P2, P3)` — same idea, three papers. No unbounded `reaches`: confidence products get noisy.

Same-paper two-hops are omitted on purpose (not the interesting case).

## Discipline

1. Paper-review checks the canonical (or raw fallback) text and writes a schema-v1 review. Assert from that review; other skills do not reopen full papers.
2. Canonicalize names with `alias_of` instead of minting synonyms.
3. After `two_hop`, run `lemmalog_why` and read the linked reviews. Never invent the middle node. If a review does not preserve enough evidence to trust a weak hop, request a paper-review refresh rather than opening canonical or raw text in a synthesis workflow.
4. Wrong facts: `lemmalog_retract`. A changed review path is re-asserted under `reviewed_in`.
5. Prefer exact `lemmalog_query` plus `lemmalog_why`. Use `lemmalog_context` only to discover candidates, then confirm them with exact queries. Never consume `store.snapshot` or an unfiltered `lemmalog_dump` as research context.
