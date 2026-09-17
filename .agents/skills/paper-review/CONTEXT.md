# Review context: who we are and how to read a paper

This file is background for `## Relevance to us`, not for judging whether the paper is sound. It is not a checklist.
Do not force a paper into our language. If nothing here fires, write `None.` in that section.
The paper's scientific merits belong in `## Critical discussion` and do not depend on this file.

When company bets and the personal framing disagree, prefer the company list for "what we are building," and still report the personal framing if the paper speaks to it. If the paper contradicts both, say that plainly.

## Who we are

FirstPrinciples is a small company building Theo: tools for theoretical and mathematical physics (AI Scientist loops; an AI Collaborator with the scientist in control). We cannot out-scale OpenAI, Google, Anthropic, Microsoft, or NVIDIA. The opening is depth in one niche: shape every layer around how physics actually reasons, rather than being adequate everywhere.

Giants are rewarded for being adequate everywhere. A small team can win by going deep. The bitter lesson is not "never add structure." Structure that enables further scaling (symmetries, solvers, conservation) is in the spirit of the lesson; hand-crafted trivia is not. Google has reported that among agentic configurations they tried, the simplest that still worked often won. Simplest here means simplest that works, not simplest possible: a tight feedback loop and a small memory can still matter.

Moonshot direction (personal, not a product claim in every review): unifying quantum theory with gravity is an example of the kind of work we care about. Do not require papers to point at it.

Scope is itself a tension. A system "for all natural sciences" buys data and cross-field synergies and puts us next to Google. A narrower physics system lets us make sharper interventions. The border is thin; a paper that forces the question is useful.

## Physics is not math plus noise

Useful only when the paper actually touches them.

Physics lives in permanent approximation. A typical derivation rests on many assumptions, often implicit. A single anomaly rarely kills a theory (Popper: you need a reproducible counter-effect; Duhem–Quine: the core can always be protected by blaming an auxiliary assumption). Conjecturing here is messier and more probabilistic than in math.

The questions are wider than classification or optimization: why, what if, construct, generalize. Not every physics question is an ML-shaped optimization problem. An idealization is judged by whether it predicts something real back in the world, which is a signal you cannot read from the equations alone.

Not only text. Equations are hierarchical, not a string. Data carry units, plots, symmetries, causal structure, and instrument quirks. Neighboring pixels and conservation laws are structure you can use, the way convolutions used translation. Which representation to use is a first-class design question, not a post-MVP polish.

Emergence: a system tuned at one Anderson level (say mathematical physics) may not scale to materials or chemistry without that level's laws and data. Superconductivity is not a few-particle extrapolation.

Verifier wall: cheap exact checks exist in a narrow band (counterexamples, planted problems, clean linear algebra). Many interesting physics questions have no cheap ground truth (many-body, strongly correlated, claims about nature). Partial, well-characterized coverage is the goal, not 100% pass/fail. See [VERIFICATION.md](VERIFICATION.md).

## Competitive opening

Typical giant recipe: frontier backbone, agentic loop, test-time compute, a human somewhere. Gains, when ablated, often collapse to a few mechanisms (compiler or solver feedback, retry treated as diagnosis, a short lab notebook), not agent count. Multi-agent pipelines can degrade on sequential tasks through coordination overhead.

Missing baselines are endemic: a crippled single agent, no frontier-plus-tools, no LoRA-plus-replay control. Judge circularity (same model family writes and grades) recurs. LLM Elo ranking is biased against counterintuitive-but-correct hypotheses.

Hard to copy: verified corpora, training pipelines, eval harnesses, expert interaction traces (edits, re-runs, verifier-validated corrections). Easy to copy: published orchestration recipes, routers, prompt templates.

A paper from a big lab is interesting when it shows where they stopped (no domain structure, no verifier, weak baseline) or when it falsifies the "they only do bags of tricks" story. Specialization papers are often distillation in disguise: the teacher wrote the data and the judge, so the teacher is the ceiling. Distillation can shed calibration and abstention even when scores match.

Physics demonstrations in general agent papers are often the weakest domain. Biomedicine, materials, and chips have money and empirical leaderboards; that is why those architectures skip formal checking.

## What future users said (IAIFI and interviews, meta)

Not a requirements spec. Recurring signals:

The gap is often named as calibration, not capability. Models are too convincing. They comply where a collaborator would push back. Long-horizon failure is often a plausible shortcut at an intermediate step, not a wrong final answer. Outcome-only eval is blind to that.

They will take wider error bars for fewer unvalidated assumptions. Confidence-as-UX is the thing they distrust. A single error number is not enough; physicists care what contributes (random vs systematic vs assumption-driven; 1σ vs 3σ; error of a measurement vs error of the mean).

Verifiers generalize where generators do not. Cheap verifiers change architecture (wrong proposals can still be useful). Expensive or absent verifiers push the product toward robustness certificates, not answers. Verification cost, not raw IQ, may set which designs scale. Formal Lean-style proofs are not what experimental groups asked for: a verdict, an explanation in their language, and a minimal runnable example.

The non-trivial research is often encoding the scientific object, not a fancy net. Search over representations lands on math and physics embeddings.

Diversity collapse showed up in vision, particle resampling, and RL post-training in one day. It may show up in conjecturing as "generically safe" themes, not just the most common ones.

Fine-tuned physics models only differentiate outside the base-model corpus. Collaborations adopt on a year scale; agent stacks turn over in months; results may need to regenerate years later without us.

How we ship can dominate what we ship. Competitors already drop skills into coding agents physicists run. Institution-specific conventions (units, private schemas) are not on the public web and still must enter the flow.

Scientists we interviewed want a fellow scientist or sparring partner, not an obedient intern. Decision-making stays with the person. Trust is central: papers contain errors, and models that believe the text 1:1 are not useful. Validation and pushback were named as more valuable than autonomous solving. Code drafts are delegatable with review. Literature overload is a shared pain. One engineer wanted a hint, not a complete answer.

Use these when a paper measures persuasiveness, process failure, representation choice, verifier economics, mode collapse, or install-into-existing-runtimes. Do not invent a customer link.

## Approved bets (authoritative, short)

This is the "we are doing this" list. One line each, for scanning. Do not treat as tags the paper must receive. If a paper matches a missing baseline or a kill-style failure (the cheap control already explains the gain; coverage too low to train on; learned reward no better than length), say that. It is more useful than "relevant to B02."

| ID | One line |
|----|----------|
| B01 | Strong simple baseline vs Theo; fair, budget-matched. |
| B02 | Physics-attuned replaceable backbone plus durable train/eval/verify pipeline. |
| B03 | Math-function embeddings for retrieval, comparison, context. |
| B04 | Universal physics-concept embeddings (multi-modal, regimes). |
| B05 | Intervention-capable physics world models. |
| B06 | Physics-native JEPA. |
| B07 | Heterogeneous specialist federation / latent orchestration. |
| B08 | Whole-literature reasoning, not top-k RAG. |
| B09 | Long-lived inspectable research runtime (DAG, dead ends). |
| B10 | Physics conjecturing plus credence plus a cheap falsifying test. |
| B11 | Assumption ledger (propagate approximations and regimes). |
| B12 | Graded physics-native verification stack. |
| B13 | Grounded scientific skeptic (literature / ledger / solvers). |
| B14 | Exploratory retrieval plus failure atlas. |
| B15 | Knowledge dial (suppress recall, then verify). |
| B16 | Diversity-preserving scientific generation. |
| B17 | Problem-formulation engine (hunch to testable program). |
| B18 | Scientific integrity metrology / red-teaming. |
| B19 | Adaptive collaborator from verified user traces. |
| B20 | TuringTrans: structured memory / looped computation for Transformers. |
| B21 | Self-improving frontier training for physics (verifier plus interp plus data loop). |
| B22 | MF-Engram: writable probabilistic memory, frozen backbone. |
| B23 | Tool-integrated reasoning for QI (QuTiP/Qiskit), small models. |

Also in the approved draft: diffusion surrogates with an agentic data path; quantum code-generation vs frontier labs. The model itself is perishable; the pipeline, data, and evals are what should compound.

## Personal arcs (hypotheses, not a roadmap)

1. Strong simple baseline. Compare against the strongest cheap alternative, not a crippled one.
2. Physics-attuned backbone. Evaluate inside the full workflow. Fair fight: same tools and budget as the frontier system. Obedience inside a long trajectory can beat a stronger but unsteerable model.
3. Reasoning over a literature. Not needle-in-haystack, not top-k. First-stage recall is the embedding bottleneck. Being in context is not being used.
4. Long-lived sessions. Multi-day DAG memory, dead-end post-mortems, collaboration. Wiki as lab notebook vs silent backstage. Privacy and prompt-injection via ingested papers.
5. Targeted scientific mechanisms. Conjecture plus credence, assumption ledger, graded verifier, grounded skeptic, exploratory retrieval, knowledge dial, diversity of hypotheses, problem formulation, integrity metrology.
6. Collaborator. Signal is verified edits and re-runs, not thumbs. Intent as an inspectable object. Desirable difficulty vs cognitive offloading. The user and the payer may be different people.

## What Relevance to us is allowed to conclude

- Evidence that a tension is real, a proposed resolution, or that our framing is wrong or incomplete.
- The paper is irrelevant to us (allowed and preferred to fake relevance).
- The paper suggests a new direction not on the lists above (flag it; do not silently absorb it).
- The paper says something useful about verification even if that is not its title.
