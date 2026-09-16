# Verify — Project Notes & Open Questions
 
Context doc combining the "Verify" deck content with initial critical discussion.
Goal: capture ideas + open questions in one place to revisit later, not a
one-sided critique — the overall proposal is good.
 
**Tagline:** The step that checks whether an AI's physics answer is actually
trustworthy — instead of trusting the answer, it interrogates it.
 
Example from the deck:
- Plain assistant: "The answer is 4.2."
- Verify: "About 4.2 ± 0.3. It conserves energy, the approximation is valid
  in this range, and friction was ignored — which could shift the result by ~5%."
---
 
## 1. Missing-Physics Detector
 
**Question it answers:** Did we forget any physics?
**Deck example:** falling ball, ignoring air resistance → flags that this is
fine at low speed but matters at high speed.
**Framed as:** acts like a physics checklist; flags effects a model quietly
left out.
 
**Open questions / discussion:**
- Is everything kept in plain text end-to-end (input as text, e.g. SKILL.md
  for the LLM; output as text), or is there a more structured/complex data
  representation somewhere in the pipeline?
- This tool may be the most important one in the set.
- The given example is only correct in one regime (low-speed, large,
  low-viscosity object). Need to check how detection generalizes to other
  regimes — e.g. small object diameter or high viscosity, where different
  physics (Stokes drag, not quadratic drag) dominates. Does the detector
  reason about regime, or just pattern-match "air resistance ignored"?
---
 
## 2. Uncertainty Engine
 
**Question it answers:** How sure are we?
**Deck example:** 500 K → 500 ± 30 K; or "Uncertainty is unknown" when it
can't be computed.
**Framed as:** no false confidence — keeps the AI from sounding surer than
the evidence allows.
 
**Open questions / discussion:**
- Very important tool. Are intervals stored/represented as plain text, or
  as structured objects (value, error, distribution type, etc.)?
- Broader context matters a lot for interpreting an error bar correctly:
  - **Convention**: is the reported error 1σ or 3σ? Different papers use
    different conventions — a bare number is ambiguous without this.
  - **Type of quantity**: error of a single measurement vs. error of the
    estimate of the mean (differ by a factor of 1/√N, N = number of
    measurements). Conflating these is a common and consequential mistake.
  - **Assumption-driven error**: error is often tied to an approximation,
    not just a number. Example: neglecting second-order hopping terms when
    modeling magnetic order in cuprates — the associated error can be
    <1% in some parameter regions, but can determine the phase order in
    others. So the "size" of this kind of error is itself regime-dependent.
- **Bigger point (lesson from IAIFI):** a single number for the error is
  not enough. What physicists actually care about is *what contributes to*
  the error — e.g., random vs. systematic breakdown.
  - Neglecting the second-order hopping term → systematic error.
  - Grid discretization error → unclear/debatable whether it's random or
    systematic (arguments exist for both) — worth digging into.
  - Measurement errors are often a mix of both.
  - Implication: the Uncertainty Engine's output schema may need to carry
    error *provenance/type*, not just magnitude.
---
 
## 3. Inverse-Problem Solver
 
**Question it answers:** What hidden parameters probably caused the
measurements we see?
**Deck example:** forward = mass + stiffness → oscillation; inverse =
measured oscillation → estimate stiffness.
**Pipeline:** observed data → physics model → best explanation/parameters.
 
**Reaction:** very cool, genuinely (not sarcasm).
 
**Open questions / discussion:**
- There are regimes where inverse calculation is fundamentally not possible
  or ill-posed — e.g., in the vicinity of critical points, where the
  forward map becomes non-invertible / highly degenerate.
  - Reference: https://www.nature.com/articles/s41524-022-00889-2
  - Does the solver detect and flag this kind of non-invertibility, or does
    it risk returning a spurious confident answer near criticality?
---
 
## 4. Active Experiment Designer
 
**Question it answers:** What experiment should we do next?
**Deck framing:** two theories fit the same data; rather than collecting
more data at random, Verify identifies which single measurement would best
discriminate between them. Pipeline: Theory A / Theory B → current data
can't decide → best next experiment → one theory wins.
**Claimed benefit:** could save researchers a lot of time.
 
**Reaction:** cool — hadn't thought about this as a tool before.
 
**Open questions / discussion:**
- Is optimal-experiment-design of this kind actually tractable in general?
  This seems like a genuinely hard problem — arguably close to the core of
  what physicists do (deciding what's worth measuring next). Worth
  understanding what class of problems/models this is realistically
  tractable for, vs. where it's aspirational.
---
 
## 5. Reproducibility Auditor
 
**Question it answers:** Could another scientist reproduce this result?
**Checklist in deck:**
- Is the code available? / Is the data available?
- Are software versions recorded? / Are simulation settings recorded?
- Does the code actually run? / Do we get the same result again?
**Framed as:** scientific quality control — "if it can't be reproduced, it
isn't finished."
**Reaction:** very cool.
 
**Open questions / discussion:**
- The checklist items are not equally important — should probably be
  weighted rather than treated as a flat checklist:
  - "Simulation settings recorded" is more important than "software
    versions recorded," since the latter can often be inferred (e.g. from
    when the code was created/committed). In practice, most physicists
    don't bother recording exact versions anyway.
- "Do we get the same result again?" needs an *interval*, not a strict
  match — stochastic simulations won't reproduce bit-for-bit.
- Practical cost problem: computational physics often pushes the limits of
  what's feasible — simulations that run for months. Repeating such a run
  multiple times just to get reproducibility statistics could be
  prohibitively (even absurdly) expensive. The auditor needs a notion of
  "reproducibility check that's actually affordable" — maybe partial/
  statistical checks, or checks on cheaper sub-components, rather than
  full re-runs.
---
 
## 6–9. Citation / Sourcing tools (Source Matcher, Quote-Fidelity Checker,
Citation-Relevance Judge, Coverage Auditor)
 
**6. Source Matcher** — Is there a real source that supports this claim?
Example: AI states a material's melting point → matched to the NIST data
table that reports it, or flagged as unsupported if no real source exists.
 
**7. Quote-Fidelity Checker** — Does the source really say this? Example:
AI drops a qualifier ("5%" vs. source's actual "up to 5%") → caught and
corrected.
 
**8. Citation-Relevance Judge** — Is this the right citation for this
specific point? Example: a real, existing source (X-ray study in metals)
cited for an off-topic claim (X-ray dose in humans) → flagged as
irrelevant even though the source itself is legitimate.
 
**9. Coverage Auditor** — Is every key claim actually cited? Checklist:
each key claim cited, numbers sourced, sources reachable (DOI/link),
unsupported assertions flagged, quotes attributed, traceability by a
reader.
 
**Reaction:** cool set overall — direct synergy with prior TREC RAG work.
 
**Open questions / discussion:**
- The most interesting sentences in a piece of physics writing — novel
  ideas, points of disagreement, original claims — are, by definition,
  the ones least likely to have any existing "evidence"/citation attached.
  A citation-quality pipeline built around matching claims to sources
  needs to handle (or at least gracefully flag rather than penalize) this
  class of un-cited-because-novel content, rather than treating "no
  citation found" as uniformly bad.
---
 
## Cross-cutting themes to revisit
 
- **Data representation**: plain text vs. structured objects, for both
  uncertainty values and detected-physics flags — affects composability
  across tools 1–9.
- **Error taxonomy**: convention (1σ/3σ), statistic type (single
  measurement vs. mean estimate), and error source (random / systematic /
  assumption-driven) all need to be represented, not just magnitude.
- **Known failure regimes**: critical points (inverse problems),
  small-object/high-viscosity regimes (missing-physics detection) — the
  tools should ideally know when they're in a regime where they can't be
  trusted, not just when they can.
- **Cost-awareness**: some checks (full reproducibility runs) can be
  prohibitively expensive; may need cheaper proxies.
- **Novelty vs. evidence**: citation tools need a way to not penalize
  genuinely novel/original claims for lacking sources.
 