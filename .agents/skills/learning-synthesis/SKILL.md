---
name: learning-synthesis
description: Produces dated catalogs of reusable scientific and engineering learnings from completed paper reviews. Use when asked to consolidate lessons, identify mechanisms worth adapting or avoiding, merge repeated findings, or update the cross-paper learnings record.
disable-model-invocation: true
---

# Learning Synthesis

Write a new snapshot to `learnings/YYYY-MM-DD-<scope-slug>.md`. Do not overwrite an older snapshot. If the same date and slug already exist, add a version suffix.

Audience: researchers and engineers deciding what to test, adapt, or avoid. A learning is a reusable mechanism or surprising result, not a paper summary and not a strategic thesis.

## Source boundary

Allowed:

- schema-v1 `reviews/*.md` ([review contract](../paper-review/SCHEMA.md)), especially Learnings, Verification, and Critical discussion
- `papers/index.md` for coverage counts
- lemmalog direct claims and `why` trees
- `reviews/graphify-out/` for semantic deduplication candidates
- earlier `learnings/*.md` for comparison

Never open `papers/canonical`, `papers/raw`, or the full-paper graph. A missing caveat or number is a review gap, not permission to reopen the paper.

## Workflow

1. Define the period/topic and identify reviews not represented in the prior snapshot.
2. Collect non-`None.` Learnings. Read Verification and Critical discussion before carrying a finding forward.
3. Merge semantic duplicates only when they make the same scoped claim. Keep multiple citations when independent papers support it.
4. Preserve the caveat that determines whether the mechanism transfers. Do not merge away conflicting regimes or metrics.
5. Surface contradictions explicitly. Query lemmalog and run `why` for multi-paper chains; do not invent an intermediate claim.
6. Calibrate causal language. A correlation, ablation, and mechanistic demonstration are not interchangeable.
7. Write one finding per short paragraph, normally two or three sentences: result, why it matters, and the limiting condition.

A learning does not need several papers to appear here. A strong single study can support a scoped, explicitly single-source learning. Upgrade it to corroborated only when independent evidence agrees; shared data, authors, model families, or judges do not count as independent confirmation. Peer review is useful context, not a mechanical trust multiplier.

Use exact `lemmalog_query` calls and `lemmalog_why`; use `lemmalog_context` only to discover candidates. Never consume `store.snapshot` or an unfiltered `lemmalog_dump`.

## Output

```markdown
---
synthesis_schema_version: 1
type: learnings
title: "..."
generated_at: "YYYY-MM-DD"
review_cutoff: "YYYY-MM-DD"
source_reviews: []
previous_snapshot: null
coverage:
  reviewed_papers: 0
  reviews_in_scope: 0
  reviews_with_learnings: 0
---

# Title

## New or strengthened learnings

[One short paragraph per finding, with review citations.]

## Revised or weakened learnings

[What new evidence changed from the previous snapshot. `None.` is allowed.]

## Contradictions and regime splits

[Do not average incompatible findings. `None.` is allowed.]

## Review gaps

[Paper ids whose reviews lack the evidence needed to retain a learning.]

## Sources

[Review paths and lemmalog claims/chains actually used.]
```

Do not begin each learning with a bold label. Do not pad a snapshot to look comprehensive. A small set of precise findings is better than a long list of recaps.
