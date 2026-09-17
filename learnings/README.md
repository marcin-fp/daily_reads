# Learnings

Versioned snapshots of mechanisms, empirical findings, and warnings worth adapting or avoiding. The audience is researchers and engineers. This is the cross-paper successor to the short lessons list in the historical perspective material.

Invoke the `learning-synthesis` skill explicitly. It writes:

```text
learnings/YYYY-MM-DD-<scope-slug>.md
```

Never overwrite an earlier snapshot. Revisions on the same date get a version suffix.

## Inputs

- non-empty Learnings from schema-v1 reviews
- their Verification and Critical discussion sections for caveats
- lemmalog claims and `why` trees
- the reviews graph for semantic deduplication candidates
- an earlier learning snapshot
- `papers/index.md` for coverage counts

Do not read canonical/raw papers or use the full-paper graph. Missing details are review gaps for `paper-review`.

## Standard

Write one reusable finding per short paragraph: what happened, why it matters, and the condition that limits transfer. Merge genuinely equivalent findings and retain all independent review citations. Do not average away contradictory regimes or upgrade correlations into mechanisms.

Single-source learnings are allowed when clearly labeled and well supported by that review. Upgrade to corroborated only when meaningfully independent evidence agrees; venue prestige alone does not justify the upgrade.
