# Review context — who we are and how to read a paper

This file is background for the **Discussion** section of a review. It is not a checklist.
Do not force a paper into our language. If nothing here fires, say so.

## Authority (read in this order)

1. **Company-authoritative.** [`context/approved_research_bets.md`](../../../context/approved_research_bets.md) — approved projects/directions we actually run. When a paper clearly helps, hurts, or complicates one of these bets, name the bet (B01–B23). That is the only “we are doing this” list.
2. **Personal / provisional.** [`context/perspective/`](../../../context/perspective/) — tensions, landscape, arcs, and a *small* set of local bets. Informed by research, still one scientist’s framing. Treat as hypotheses. Incomplete on purpose: the papers we review *are* the interest set; listed bets are current focus, not a closed taxonomy.
3. **Customer / market (meta).** [`context/IAIFI/`](../../../context/IAIFI/), especially [`presentation.tex`](../../../context/IAIFI/presentation.tex) — what working physicists and a few industry partners said they need. Use this to notice product-shaping signals (calibration, verifiers, process vs outcome, diversity, ship-into-their-runtime). A paper can justify a *new* bet or arc; that is a success, not a taxonomy failure.

If (1) and (2) disagree, prefer (1) for “what the company is building,” and still report (2) if the paper speaks to the personal framing. If the paper contradicts both, say that plainly.

## Who we are

**FirstPrinciples** is a small company building **Theo**: tools for theoretical / mathematical physics (AI Scientist loops; AI Collaborator with the scientist in control). We cannot out-scale OpenAI, Google, Anthropic, Microsoft, NVIDIA. The opening is **depth in one niche**: shape every layer around how physics actually reasons, rather than being adequate everywhere.

Moonshot direction (personal, not a product claim in every review): unifying quantum theory with gravity is an *example* of the kind of work we care about; do not require papers to point at it.

## Physics is not “math plus noise”

From the personal landscape note, useful only when the paper actually touches them:

- Permanent **approximation**; many implicit **auxiliary assumptions** (Duhem–Quine / theory stickiness). A single anomaly rarely kills a theory.
- Questions include why / what if / construct / generalize — not only classification or optimization.
- **Not only text**: equations (hierarchical, not a string), units, plots, symmetries, causal structure, instrument quirks.
- **Emergence**: a system tuned at one Anderson level may not “just scale up” without that level’s laws and data.
- **Verifier wall**: cheap exact checks exist in a narrow band; many interesting physics questions have no cheap ground truth.

Structure that *enables* scaling (symmetries, solvers, conservation) is in the spirit of the bitter lesson; hand-crafted trivia is not.

## Competitive opening (personal reading of the field)

Giants typically ship: frontier backbone + agentic loop + test-time compute + a human somewhere. Gains often come from a few mechanisms (tool feedback, retry-as-diagnosis, notebook memory), not from agent count. Missing baselines are endemic (crippled single-agent, no frontier-plus-tools). **Hard to copy:** verified corpora, training pipelines, eval harnesses, expert interaction traces. **Easy to copy:** published orchestration recipes.

A paper from a big lab is interesting when it shows where they stopped (no domain structure, no verifier, weak baseline) *or* when it falsifies our “they only do bags of tricks” story.

## What future users said (IAIFI, meta)

Not a requirements spec. Recurring signals from the room our products are for:

- Gap named as **calibration, not capability**. Models are too convincing; they comply where a collaborator would push back; long-horizon failure is often a **plausible shortcut at an intermediate step**, not a wrong final answer. Outcome-only eval is blind to that.
- They will take **wider error bars** for **fewer unvalidated assumptions**. Confidence-as-UX is the thing they distrust.
- **Verifiers generalize where generators do not.** Cheap verifiers change architecture (wrong proposals can still be useful). Expensive/absent verifiers change the product toward robustness certificates, not answers. Verification cost, not raw IQ, may set which designs scale. Formal Lean-style proofs are *not* what MERL asked for: **verdict + physical explanation in their language + minimal runnable example**.
- The non-trivial research is often **encoding the scientific object**, not a fancy net. Search over representations lands on math/physics embeddings.
- **Diversity collapse** showed up across vision, particle resampling, and RL post-training in one day — relevant to conjecturing.
- Fine-tuned physics models only differentiate **outside** the base-model corpus; know that boundary. Collaborations adopt on a **year** scale; agent stacks turn over in **months**; results may need to regenerate **years later without us**.
- Distribution: a less “advanced” competitor already ships **into** coding agents physicists already run (convention locking, profile routing). “How we ship” can dominate “what we ship.”
- Institution-specific conventions (calibration, private schemas) are not on the public web and still must enter the flow.

Use these when a paper measures persuasiveness, process failure, representation choice, verifier economics, mode collapse, or install-into-existing-runtimes. Do not invent an IAIFI link.

## Approved bets (authoritative, short)

Full cards live in the approved file. One line each, for scanning — **do not treat as tags the paper must receive**.

| ID | One line |
|----|----------|
| B01 | Strong simple baseline vs Theo; fair, budget-matched. |
| B02 | Physics-attuned replaceable backbone + durable train/eval/verify pipeline. |
| B03 | Math-function embeddings for retrieval, comparison, context. |
| B04 | Universal physics-concept embeddings (multi-modal, regimes). |
| B05 | Intervention-capable physics world models. |
| B06 | Physics-native JEPA. |
| B07 | Heterogeneous specialist federation / latent orchestration. |
| B08 | Whole-literature reasoning, not top-k RAG. |
| B09 | Long-lived inspectable research runtime (DAG, dead ends). |
| B10 | Physics conjecturing + credence + cheap falsifying test. |
| B11 | Assumption ledger (propagate approximations/regimes). |
| B12 | Graded physics-native verification stack. |
| B13 | Grounded scientific skeptic (literature / ledger / solvers). |
| B14 | Exploratory retrieval + failure atlas. |
| B15 | Knowledge dial (suppress recall, then verify). |
| B16 | Diversity-preserving scientific generation. |
| B17 | Problem-formulation engine (hunch → testable program). |
| B18 | Scientific integrity metrology / red-teaming. |
| B19 | Adaptive collaborator from *verified* user traces. |
| B20 | TuringTrans — structured memory / looped computation for Transformers. |
| B21 | Self-improving frontier training for physics (verifier + interp + data loop). |
| B22 | MF-Engram — writable probabilistic memory, frozen backbone. |
| B23 | Tool-integrated reasoning for QI (QuTiP/Qiskit), small models. |

Also in the approved draft: diffusion surrogates with an agentic data path; quantum code-generation vs frontier labs. If a paper matches a card’s **kill criterion** or **missing baseline**, say that — it is more useful than a vague “relevant to B02.”

## What Discussion is allowed to conclude

- Evidence that a **tension is real**, a **proposed resolution**, or that **our framing is wrong/incomplete**.
- A paper is **irrelevant to us** (allowed and preferred to fake relevance).
- A paper suggests a **new direction** not yet in approved bets or personal arcs (flag it; do not silently absorb it into the nearest existing label).
