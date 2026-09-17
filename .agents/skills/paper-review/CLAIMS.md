# Claims (lemmalog)

Machine section for relations the paper itself asserts. May be empty (`None.` under `## Claims`). Do not invent edges to look productive. Do not put your critique here; that belongs in Critical discussion. Prefer claims that could participate in cross-paper chains (implies / contradicts / uses / improves / evaluates).

Verification-related edges are welcome when the paper actually states them (how a step is checked, what a reward measures, coverage/precision, LLM judge vs oracle). Do not mint a verification claim because we care about the topic.

`from` / `to`: ≤8 words. `anchor`: space-free, prefer canonical (`papers/canonical/2026-06-09/2605.26492.md:ABSTRACT` or `…md:L42`).

`relation`: `implies` | `improves` | `contradicts` | `uses` | `evaluates`.

`conf` measures how directly this paper's evidence supports the scoped relation. Do not increase it because the paper is peer-reviewed or appears in a prestigious venue. Cross-paper corroboration is assessed later and must consider independence, not just source count.

```markdown
## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| minimal story prompts | thematic diversity | contradicts | 0.9 | papers/canonical/2026-06-09/2605.26492.md:ABSTRACT | Weak prompts repeatedly produce the same narrow motifs |
```

When asserting: write only `paper --reviewed_in[1.0]--> reviews/{id}.md` for the paper pointer. Mint `e:{id-without-prefix:}:{short}` (no spaces); set `source_paper`, `from`, `to`, `kind`, and the canonical `located` anchor at confidence `[1.0]`, then assert `from --{relation}[conf]--> to` at the scientific confidence from the table. This keeps structural provenance from diluting the evidence score. Derive an edge's review through `source_paper`; do not store `reviewed_in` on every edge. All bibliography and landscape metadata stays in the review. See [`lemmalog/SCHEMA.md`](../../../lemmalog/SCHEMA.md).
