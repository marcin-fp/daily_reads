# Suggested reading structure (not a labelling system)

Scan these questions while reading. Surface only what the paper actually speaks to.
Do not dump this list into the review. Do not fill every bucket.
Scientific scrutiny of the paper itself lives in `## Critical discussion`. This file is only for deciding whether the paper speaks to our tensions and mechanisms in `## Relevance to us`.

---

## Tensions (personal; both sides exist)

Ask: does this paper add evidence, a mechanism, or a counterexample?

1. Frontier backbone vs small specialized models. A general model plus orchestration goes far. An 8B model with verification-aware training can rival frontier systems on-distribution, often with the decisive frontier-plus-tools baseline missing. Factual capacity seems to track parameter count; reasoning tracks architecture, post-training, and inference compute. Smaller models help on-prem, cost, and privacy. The risk is spending a year on a pipeline and getting leapfrogged. Engram-style lookup can make a small model punch up, but the jump from scaling active parameters is usually larger. Distillation inherits the teacher's ceiling.

2. Complex vs deliberately simple agents. Minimal loops with tight feedback often win. Twenty-three-stage pipelines exist. Gains often collapse to tool feedback, self-healing retry, notebook, not agent count. Maybe simplicity wins when the signal is tight, and extra structure earns its keep when it is not. Verify that, do not assume it.

3. Solving vs problem formulation. The literature crowds solving (code, proofs, QA). Formulation (why, what if, construct) is thinner. Automating a step is relief for one scientist and loss of agency for another. Dials vs one persona.

4. Control vs appliance. Scientists want the hood open, and they still use Matlab when it lets them control the calculation. Transparency vs cloneability (skills and prompts paraphrase around copyright). Demo too toy gets dismissed; too narrow and nobody generalizes.

5. Helper vs mentor vs skeptic. Warmth can raise error and sycophancy. Models override instructions and mimic compliance in the chain of thought. Prompting is not activation steering, and steering needs weights. A pushy reviewer can be the product, if that is what we claim to ship.

6. Data quantity vs quality. Quality as a multiplier on effective dataset size is a hypothesis, mostly from synthetic noise, with ceilings. Sparse physics jargon and multi-epoch overfitting are real. Not settled whether cleaning beats collecting.

7. Pre-built tools vs bridges vs bring-your-own. Tool-pool size kills selection accuracy (adaptive pruning can keep a handful in view). Bridges help continuous states that tokenize badly (atomic structures). Discrete and symbolic states usually want exact tool I/O. A community marketplace only works if the community exists.

A paper that breaks this list (new tension, or shows two poles are the same variable) is more valuable than one that maps cleanly.

---

## Customer-shaped probes

Only if the paper measures or designs for these:

- Calibration, assumption disclosure, shortcut at an intermediate step.
- Verifier economics (cheap filter vs no oracle).
- Representation search as the actual research.
- Diversity and mode occupancy under RL or scale.
- Reproducibility years later; convention locking; ship into existing runtimes (Claude Code, Jupyter, Modelica, Julia, MATLAB, not Python-only).
- Process vs outcome evaluation; harness gaming.
- Integrity under covert framing; evaluation awareness that the chain of thought does not admit.

---

## Optional mechanisms

Use when the paper contains a transferable trick. Skip otherwise. These are examples we already care about, not a hunt list:

- Verification-aware rewards; solver in the loop; hybrid symbolic plus LLM judges.
- Selective tuning / replay vs LoRA; early log-prob canaries for persona drift.
- Writable lookup memory vs RAG vs fine-tune.
- Fusion of N vs best of N (watch numerics).
- Lab-notebook memory vs sliding window; self-healing retry as diagnosis.
- Contrastive training on retrieval failures; quality-aware tool pruning.
- Independent or stronger critics (same-model self-critique is weak).
- Context-induced sycophancy; evaluation awareness vs verbalized CoT.
- Input-only safety filters vs output and trace monitoring.
- Self-improvement collapse without external signal; Darwinian search with a scorer.
- Multidimensional non-saturating eval (what failed, not one number).
- Interpretability used during training, not only after.

---

## How this should appear in Relevance to us

Write in ordinary scientific prose ([STYLE.md](STYLE.md)). You may name a tension, arc, or B-id once when it is load-bearing. You may say this supports or weakens a tension; this is a candidate mechanism for a bet; this disagrees with how we framed something; this is interesting science and not our problem.

Never: a bullet for each heading above.
