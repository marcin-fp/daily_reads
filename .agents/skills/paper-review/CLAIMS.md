# Claims (lemmalog)

Machine section. **May be empty** (`None.` under `## Claims`). Do not invent edges to look productive. Prefer claims that could participate in cross-paper chains (implies / contradicts / uses / improves / evaluates).

`from` / `to`: ≤8 words. `anchor`: space-free, prefer canonical (`papers/canonical/2310.01798.md:ABSTRACT` or `…md:L42`).

`relation`: `implies` | `improves` | `contradicts` | `uses` | `evaluates`.

```markdown
## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| intrinsic self-correction | reasoning accuracy | contradicts | 0.9 | papers/canonical/2310.01798.md:ABSTRACT | No external feedback; accuracy often falls |
```

When asserting: mint `e:{id-without-prefix:}:{short}` (no spaces); set `source_paper`, `from`, `to`, `kind`, `located`, and `from --{relation}[conf]--> to`. See [`lemmalog/SCHEMA.md`](../../../lemmalog/SCHEMA.md).
