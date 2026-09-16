# PVRE — Project Notes & Open Questions
 
Context doc combining Moinul Rahat's "PVRE" (Physics Verifiable Training
Environment) pilot presentation with the discussion that followed in the
Aug 18, 2026 Verification Squad meeting. Captures ideas + open questions
in one place to revisit later — not a one-sided critique; the overall
direction (deterministic, step-level physics verification) was well
received.
 
**Framing:** Take PRM-style training from formal math (e.g. work using Z3
to generate verified proof steps) and port the idea to physics, where a
fully formal verification channel doesn't exist. Instead, build an
*approximate/partial* deterministic verifier that labels individual steps
of a physics derivation as correct, incorrect, or undecided — then use
that either to train models (PRM / dense-reward RLV) or as a harness
bolted onto the existing agentic system (Collaborator/Theos).
 
**Hard rule going in:** every verdict must come from a deterministic
check (dimensional consistency, numerical/algebraic entailment, known
oracle), never from an LLM acting as judge. Being "undecided" is fine;
false positives/negatives are not.
 
---
 
## 1. Pilot Setup
 
**Question it answers:** Can deterministic step-level verification work
well enough, on a small scope, to be worth building further?
 
**Setup:**
- 10 coupled-oscillator problems (undergrad level, deliberately simple —
  chosen so a human could hand-check everything), sampled 3x each with a
  Qwen-30B (MoE) model → 30 trajectories, 206 total steps.
- Two of the ten problems were deliberately out-of-domain, to test
  whether the model would correctly decline to adjudicate rather than
  force a verdict.
- Model required to freely reason, then emit a final answer in a fixed
  schema so a parser could extract steps for the verifier tools.
- 75 documented rules built (agentically, with Claude, plus automated
  checks) to define what the verifier tools can and cannot adjudicate.
- Pre-registered thresholds: coverage ≥50% (below 30% → question whether
  to continue as a training-data project at all), precision ≥90%.
**Deterministic checks implemented:** dimensional consistency (LHS vs.
RHS units) and numerical entailment (does this step follow from the
previous one, e.g. via substitution/limit/approximation, checked by
plugging in arbitrary parameter values for algebraic steps).
 
---
 
## 2. Headline Results
 
- **Coverage: 27.2%** (56/206 steps adjudicated) — below both the 50%
  target and the 30% "still worth training on" floor.
- **Precision:** of 12 steps flagged wrong across the 30 trajectories,
  8 were true positives and 4 were false positives — but the false
  positives all traced back to schema bugs, not verifier logic; once
  repaired, precision was effectively 100% on this pilot.
- **Recall (via error injection):** among steps the tool *could*
  adjudicate, injected errors were caught 100% of the time. Within its
  coverage, the tooling is reliable — the open problem is coverage, not
  correctness.
**Where coverage was lost (four channels):**
1. **Premise/initial steps** (~18 steps) — e.g. "here is the equation of
   motion I'm starting from." No previous step to check against, so
   numerical entailment can't apply; dimensional consistency can rule
   things out but can't confirm correctness. This was the single largest
   category of loss.
2. **Extraction/schema failures** (41 total: 30 primary + 7 cascading) —
   22 of the 30 were the model breaking an explicit prompt rule (e.g.
   forgetting to declare a new symbol's dimensions) even when stated
   twice in the system prompt; 8 were correct model output that the
   schema simply couldn't parse (e.g. writing "d2/dt2" as prose instead
   of sympy notation, or ambiguous integral notation).
3. **Design-choice ambiguities** — mid-derivation steps the current
   schema can't cleanly represent.
4. **Confusing provenance** — a step that clearly follows from *some*
   earlier step, but the tool can't mechanically tell which one (trivial
   for a human, hard to encode deterministically).
5. (Separately, ~51 steps involved derivatives/integrals of functions
   without a known closed form — no way to numerically check LHS=RHS at
   a point without knowing the function. Unsolved in the pilot.)
**Family oracles as a lever:** implementing one oracle (Lagrangian →
equations of motion, plus a correctness check on the resulting
differential equation) for a single family covered 2 of the 10 problems
and recovered 12 previously-unadjudicated steps, moving coverage from
27% → 33%. Projected (optimistically) to ~50% if extended to all
premise-step cases — noted explicitly as likely coincidental and not to
be over-extrapolated.
 
**Family assignment is the harder problem than the oracle itself.**
Concrete failure case: a 3-mass problem where only 2 masses were
attached to springs; the model, given only a "masses on springs" family
to choose from, wrongly force-fit the problem into it and then
mislabeled a correct step as wrong. Lesson: near-adjacent families are
genuinely confusing for a model to disambiguate on its own, so letting
the model pick its own family should be treated as a last resort — better
to say "undecided" than to force a wrong family match. This problem
mostly disappears if the tool is used as a *label factory* (i.e. the
problem author assigns the family at curation time) rather than as a
general-purpose evaluator of problems it didn't create.
 
---
 
## 3. Two Paths Forward (as presented)
 
1. **Training path (longer-term):** use family oracles to generate large
   synthetic problem sets per family (template Lagrangian + varying
   parameters/masses/springs/friction terms), where coverage is high
   because the family is known by construction. Use this to build a PRM
   or dense per-step reward for RLV training, and/or to build a
   repair loop that patches a derivation at the exact step it broke.
2. **Harness path (shorter-term):** attach the current deterministic
   checks (dimensional consistency + numerical entailment, plus
   near-term additions like limit-checking) to the existing
   agentic/Collaborator system as-is, with no family oracle, purely to
   catch/flag likely errors in live use.
Presenter's recommendation: pursue the harness path now for near-term
value; treat the label-factory/training path as the higher-payoff
longer-term investment.
 
---
 
## 4. Discussion
 
### Marcin — is "wrong" actually wrong? (biggest pushback of the meeting)
- In physics, the *most interesting* derivations often deliberately
  "break the rules" — dropping terms, neglecting effects, introducing
  idealized fields — because that's the art of building a tractable
  theory (e.g. neglecting inter-layer coupling to isolate a
  superconductivity effect in cuprates, or switching to natural units and
  dropping all the k_B terms). A purely deterministic checker, without
  broader context, will flag these as errors when they're actually
  intentional, defensible choices.
- Concern: if this verifier is wired into the Collaborator as a hard
  gate, it risks suppressing exactly the kind of creative/non-standard
  physics reasoning that matters most — "you can kill your ability to do
  anything modern and new if you treat verification as a strict
  pass/fail."
- Moinul's response: agreed this is out of scope for a purely
  deterministic layer; this is where an LLM-as-orchestrator (not
  LLM-as-judge) comes in — the LLM's job is to notice *that* an
  assumption changed ("let's move to natural units") and route to the
  right tool/arguments, while the actual check stays mechanical.
- Resulting design idea (Alex + Marcin): never present verifier output as
  a correctness verdict ("this equation is wrong"); present it as a
  neutral highlight ("dimensions changed here") and let the user/model
  decide whether that was intentional. Possibly gate on repeated failure
  only — e.g. allow ~3 retries before surfacing a flag to the user, and
  weight how much to trust a flag by how reliable that specific check is
  known to be (a 100%-reliable deterministic check can be trusted more
  directly than a fuzzier one).
### Marcin — problem difficulty / domain coverage
- Asked whether problems tested go beyond college level toward the
  frontier of current research, where the qualitative character of
  "acceptable approximation" may differ. Moinul confirmed the pilot was
  deliberately kept undergraduate-level so failures could be fully hand-
  checked; this was a test of the verifier's *systematic* correctness,
  not of model capability on hard problems.
### Jonathan — symmetry/point-group checks
- Suggested adding invariance-under-point-group checks (e.g. Hamiltonian
  terms respecting a crystal's symmetry) as a natural deterministic
  addition.
- Follow-up concern: a derivation might legitimately switch context
  mid-stream (e.g. from a square to a hexagonal lattice, or relaxing an
  assumption a few lines later) — would the deterministic checker
  misflag the "old" symmetry as violated?
- Moinul: symmetry/current calculations are mechanical *given* a known
  family (they fall out of the Lagrangian → equations of motion recipe
  already built for one family), so this is really the same
  family-assignment problem, not a new one. Detecting an explicit
  in-text change of assumption ("if we now relax that constraint...")
  is a job for the LLM-as-orchestrator, not something to hand-code as a
  rule.
### Rise — instruction-following and long-term trust
- Framed this as necessarily an iterative product loop, not a
  build-once-and-ship tool: ship something imperfect, use real usage
  (plus the RLVR data generated from the product itself) to improve it.
- Flagged that a lot of coverage loss traces back to the base model's
  instruction-following (e.g. failing to declare variable dimensions
  despite being told twice) — suggests training/selecting a model
  specifically strong at following structured verification protocols
  could be a higher-leverage fix than expanding rules.
- Cautioned that orchestrating only deterministic tools is a limited
  ambition; at some point the team will need to trust a physics-capable
  model directly rather than deterministic tools indefinitely — called
  this out as a real, longer-term research problem worth owning.
### Andy — framing
- Noted the parallel: "100% certainty check is like 100% QA coverage" —
  i.e. useful but not the achievable bar; partial, well-characterized
  coverage is still valuable if its reliability is known.
### Shay — good enough to ship
- Argued the bar shouldn't be perfection, just "better than the vanilla
  API-call baseline" (drawing an analogy to hidden verification/tooling
  that consumer products like ChatGPT's web app have on top of their raw
  API, which isn't otherwise accessible). Advocated shipping the harness
  version soon rather than waiting for a fully general system.
### Alex — grounding / next steps
- Reiterated a prior team conclusion: physics verifiers will never reach
  100% coverage — the goal is to build as much MVP coverage as feasible,
  serving both the training-data purpose and the agentic-harness purpose.
- Asked Xingyang to speak to verifiers already present in the Agentic
  Research system at Thursday's presentation, as a natural follow-on.
- Closing ask to the group: how do we "supercharge" this — more checks,
  more families — and eventually turn it into a shared tool/platform
  across products, without necessarily over-formalizing it prematurely.
---
 
## Cross-cutting themes to revisit
 
- **Deterministic-only is a deliberate, load-bearing constraint** — no
  LLM-as-judge — but the meeting surfaced real cases (natural units,
  neglected terms, deliberate idealizations) where a purely mechanical
  check will misfire without broader context. Current resolution: LLM as
  *orchestrator* (routes to the right deterministic tool / supplies
  context) rather than LLM as *judge* (renders the verdict itself).
- **Presentation of verdicts matters as much as the verdicts.** Emerging
  consensus: never phrase output as "this is wrong" — phrase it as a
  neutral flag ("dimensions changed here") and let a retry policy / the
  user decide. Reliability of a given check should modulate how strongly
  a flag is presented.
- **Family assignment, not the oracle math, is the bottleneck.** Building
  a family oracle is comparatively easy once a family is known; reliably
  classifying an unseen problem into the right family (especially among
  closely related families) is the hard, still-open part. This problem
  mostly dissolves in the label-factory/training setting (family is
  known at curation time) but persists in the general harness setting.
- **Coverage vs. precision are decoupled and behave differently.**
  Precision/recall within the current tool's scope look strong (100%
  recall under error injection, ~100% precision after fixing schema
  bugs); the open problem is almost entirely about *coverage* — how much
  of a derivation the tools can even attempt to judge.
- **Schema/extraction fragility is a real, model-specific tax.** A
  meaningful share of lost coverage came not from physics reasoning
  failures but from the model breaking explicit formatting rules or
  writing notation (e.g. derivatives, integrals) the parser couldn't
  handle — likely to recur differently per base model, implying the
  tooling may need per-model variants.
- **Ship-now vs. build-for-training is not either/or** — treat the
  harness (attach current deterministic checks to the existing agentic
  system) as the near-term deliverable, and the label-factory/PRM path
  as the longer-term, higher-effort investment.