# Perspectives

Versioned, provisional arguments about how the field works, what tensions remain, and which research directions deserve attention. The audience is fellow researchers. These documents are intended to evolve as reviewed evidence accumulates.

Invoke the `perspectives` skill explicitly. It writes:

```text
perspectives/YYYY-MM-DD-<topic-slug>.md
```

Never overwrite an older snapshot. A revision produced on the same date gets `-v2`, `-v3`, and so on.

## Inputs

- schema-v1 reviews
- lemmalog direct claims, `two_hop` / `three_hop`, and `why` trees
- the reviews graph for candidate connections
- an earlier perspective on the same topic
- `papers/index.md` for coverage counts

Do not read canonical/raw papers or use the full-paper graph. Missing evidence is recorded under `## Review gaps` and routed back through `paper-review`.

## Standard

A perspective is an argument, not a summary or paper list. It states what changed from the previous view, gives the strongest supporting and contrary evidence, separates paper results from synthesis, and says what would reverse the conclusion. With fewer than five relevant reviews, label the result exploratory and avoid field-wide claims.

The earlier LaTeX files under `context/perspective/` are historical working material. New perspectives live here as dated Markdown snapshots.
