# Suggested reading structure (not a labelling system)

Scan these *questions* while reading. Surface only what the paper actually speaks to.
Do **not** dump this list into the review. Do **not** fill every bucket. Empty Discussion is valid.

Source split: tensions/arcs = personal perspective; B-ids = approved portfolio; IAIFI = customer meta. Details and citations live in [`context/perspective/`](../../../context/perspective/) and [`context/IAIFI/`](../../../context/IAIFI/).

---

## Tensions (personal; both sides exist)

Ask: does this paper add evidence, a mechanism, or a counterexample?

1. **Frontier backbone vs small specialized models** — General + orchestration goes far; 8B + verification can rival *on-distribution*. Reasoning may track architecture/post-training/inference compute more than parameter count; facts may track size. Leapfrog risk, on-prem/privacy/cost, distillation-ceiling (student inherits teacher).
2. **Complex vs deliberately simple agents** — Minimal loops with tight feedback often win; 23-stage pipelines exist. Gains often collapse to tool feedback, self-healing retry, notebook — not agent count. Maybe simplicity wins iff the signal is tight.
3. **Solving vs problem formulation** — Literature crowds solving (code, proofs, QA). Formulation / “why / what if / construct” is thinner. Automating a step is relief for one scientist and loss of agency for another (dials vs one persona).
4. **Control vs appliance** — Scientists want the hood open (and still use Matlab). Transparency vs cloneability (skills/prompts). Demo too toy → dismissed; too narrow → nobody generalizes.
5. **Helper vs mentor vs skeptic** — Warmth can raise error and sycophancy. Models override instructions and mimic compliance in CoT. Prompting ≠ activation steering (and steering needs weights). A pushy reviewer can be the product.
6. **Data quantity vs quality** — Quality as multiplier on effective \(D\) is a *hypothesis* with ceilings and overfitting on sparse physics jargon. Not settled.
7. **Pre-built tools vs bridges vs bring-your-own** — Tool-pool size kills selection accuracy. Bridges help continuous states that tokenize badly; discrete/symbolic often wants exact tool I/O. Marketplace bootstrapping is unsolved.

A paper that **breaks this list** (new tension, or shows two “poles” are the same variable) is more valuable than one that maps cleanly.

---

## Research arcs (personal propositions, not a roadmap)

1. **Strong simple baseline** — Compare Theo to the strongest cheap alternative; kill complexity that does not win under fair controls. Missing baselines in the literature are the original sin.
2. **Physics-attuned backbone** — Pipeline and data should survive model swap. Evaluate inside the full workflow, not a bare LMSYS score. Fair fight: same tools and budget as the frontier system.
3. **Reasoning over a literature** — Not needle-in-haystack, not top-k. Math representations; query-conditioned compression; utilization ≠ presence in context. First-stage recall is the embedding bottleneck.
4. **Long-lived sessions** — Multi-day DAG memory, dead-end post-mortems, collaboration, aging (compression / interference / revision / maintenance). Wiki as lab notebook vs silent backstage. Privacy and prompt-injection via ingested papers.
5. **Targeted scientific mechanisms** — Conjecture+credence, assumption ledger, graded physics verifier, grounded skeptic, exploratory retrieval + failure atlas, knowledge dial, diversity metrics for *hypotheses/derivations*, problem formulation, integrity metrology.
6. **Collaborator / human** — Signal is verified edits and re-runs, not thumbs. Intent as inspectable object. Desirable difficulty vs cognitive offloading. Interruption/hand-back. User vs payer economics; limited-risk EU design (clinical/CBRN).

---

## Customer-shaped probes (IAIFI)

Only if the paper measures or designs for these:

- Calibration, assumption disclosure, shortcut-at-intermediate-step.
- Verifier economics (cheap filter vs no oracle).
- Representation search as the actual research.
- Diversity/mode occupancy under RL or scale.
- Reproducibility years later; convention locking; ship-into existing runtimes (Claude Code / Jupyter / Modelica / Julia / MATLAB, not Python-only).
- Process vs outcome evaluation; harness gaming.

---

## Optional “interesting bits” (mechanisms)

Use when the paper contains a transferable trick. Skip otherwise. Examples the personal corpus already cares about (not exclusive):

- Verification-aware rewards; solver-in-the-loop; hybrid symbolic+LLM judges.
- Selective tuning / replay vs LoRA; early log-prob canaries for persona drift.
- Engram / writable memory vs RAG vs fine-tune.
- Fusion-of-N vs best-of-N (watch numerics).
- Lab-notebook memory vs sliding window; self-healing retry as diagnosis.
- Contrastive “gain beyond RAG” retrieval training; Bits-over-Random tool pruning.
- Independent / stronger critics (same-model self-critique is weak).
- Context-induced sycophancy; evaluation awareness vs verbalized CoT.
- Input-only safety filters vs output/trace monitoring.
- Self-improvement collapse without external signal; Darwinian search with a scorer.
- Multidimensional non-saturating eval (capability demands, not one number).
- Interpretability used *during* training, not only post-hoc.

---

## How this should appear in the review

In **Discussion**, write in ordinary scientific prose. You may name a tension, arc, or B-id **once** when it is load-bearing. You may say:

- this supports / weakens tension *T*;
- this is a candidate mechanism for bet *B*;
- this disagrees with how we framed *X*;
- this is interesting science and **not** our problem.

Never: a bullet for each heading above.
