# Claims (lemmalog)

Machine section for relations the paper itself asserts. May be empty (`None.` under `## Claims`). Do not invent edges to look productive. Do not put your critique here; that belongs in Discussion. Prefer claims that could participate in cross-paper chains (implies / contradicts / uses / improves / evaluates).

Verification-related edges are welcome when the paper actually states them (how a step is checked, what a reward measures, coverage/precision, LLM judge vs oracle). Do not mint a verification claim because we care about the topic.

`from` / `to`: ≤8 words. `anchor`: space-free, prefer canonical (`papers/canonical/2310.01798.md:ABSTRACT` or `…md:L42`).

`relation`: `implies` | `improves` | `contradicts` | `uses` | `evaluates`.

```markdown
## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| intrinsic self-correction | reasoning accuracy | contradicts | 0.9 | papers/canonical/2310.01798.md:ABSTRACT | No external feedback; accuracy often falls |
```

When asserting: mint `e:{id-without-prefix:}:{short}` (no spaces); set `source_paper`, `from`, `to`, `kind`, `located`, and `from --{relation}[conf]--> to`. See [`lemmalog/SCHEMA.md`](../../../lemmalog/SCHEMA.md).
