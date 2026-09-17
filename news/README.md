# News

Analytical articles centered on one reviewed paper. They explain what the paper changes, where it sits in the development of the field, how it connects to other reviewed work, and what its evidence does not establish. They are not abstract rewrites or press releases.

Invoke the `news-article` skill explicitly. It writes:

```text
news/YYYY-MM-DD-<paper-slug>.md
```

The date is the paper's first-public date, not the dump or review date. Do not overwrite an older article; add a version suffix.

## Inputs

- the schema-v1 review of the central paper
- related schema-v1 reviews
- lemmalog claims and `why` trees
- the reviews graph for candidate connections
- earlier synthesis documents as leads, not primary evidence

The central paper must be reviewed. Do not read canonical/raw papers or use the full-paper graph. If an important fact is missing, request a `paper-review` refresh.

## Standard

Find the story before writing the headline. Lead with the scientific issue or surprising implication, then explain what was done, how the work fits in space and time, the strongest limitation, and what comes next. Community significance comes before internal relevance. If no cross-paper connection is yet reviewed, write a focused single-paper article rather than inventing a lineage.

Use "reported" or "supported" for a single-paper result and reserve "corroborated" for independent agreement. Peer review may be worth mentioning, but it does not make every claim in the paper established.
