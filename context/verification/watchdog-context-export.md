# Agentic-Trace Verification ("Watchdog") — Context Export
 
**Owner:** Marcin Abram (FirstPrinciples, Physics Verification Squad)
**Status:** proposal / pre-experiment. Shared with R&D director (Alexander Tessier) Aug 2026.
**Purpose of this document:** a single self-contained context dump so a fresh agent session (or a
human collaborator) can pick up the thread without the original chat history. Written primarily for
an agent; readable by a human reviewer.
 
**How to use this document.** Sections 1–3 are background and can be skimmed if you already know the
programme. Section 4 is the proposal. Sections 5–7 are the actual work to be done and contain the
decisions already made — do not re-litigate them unless new information arrives. Section 10 lists
what is genuinely still open.
 
---
 
## 1. Organizational context
 
**FirstPrinciples** builds AI systems for physics research. Relevant products:
 
- **Theo** (formerly/internally *Collaborator*) — the agentic research platform. Shipping target was
  end of September 2026, with updates every 2–3 weeks after. Report-heavy output today.
- **Conjecture** — a hypothesis/idea-generation tool. Known weaknesses: novelty detection and
  "common knowledge laundering" (restating established results as new findings). Also had a real
  incident where a small-grid numerical result was treated as having zero discretization error.
- **Verification Squad** — cross-functional group formed July 2026. Members referenced throughout:
  Alexander Tessier (R&D director, runs the squad), Moinul Hossain Rahat (PVRE / deterministic
  step verification), Shay Sadeghi (Verify tool suite, citation verification), Marcin Abram (author
  of this doc), Rise Adhikari, Collin Farquhar, Xingyang Yu (HEP theorist, internal customer),
  Nickvash Kani (math representation/embeddings), Jyothis Vasudevan, Randy Davila,
  Jonathan Clepkens, Andy Woo, Sankar Mahadevan (PM), Ildar Shar (exec, wants a platform/API).
**Competitor of record:** Physical Superintelligence (PSI), and specifically their open-source
**get-physics-done (GPD)** — https://github.com/psi-oss/get-physics-done. Assessment from the squad:
GPD defaults to frontier models and packages skills/tools for easy integration with popular tools
(e.g. Cursor). It is a distribution play more than a technical one. It consumes **human-authored
output** and checks it.
 
**Strategic frame that has been agreed:** physics verification will never reach 100% coverage. The
goal is well-characterized partial coverage. Verifier output should feed two consumers: product
(trust surface in Theo) and training (RLVR / PRM data).
 
---
 
## 2. The three existing streams
 
These are complementary, not competing. New work must position relative to all three.
 
### 2.1 Moinul — PVRE (Physics Verifiable Reward Environments) — "bottom-up, deterministic"
 
Deterministic, reference-free, **step-level** verification of physics derivations. Hard rule: every
verdict comes from a deterministic check (dimensional consistency, numerical entailment, oracle),
never from an LLM acting as judge. "Undecided" is acceptable; false verdicts are not.
 
Pilot results (10 coupled-oscillator problems, 30 trajectories, 206 steps, Qwen-30B MoE):
 
- **Coverage 27.2%** (56/206 steps adjudicated) — below the 50% target and the 30% floor.
- **Precision** effectively 100% after schema bugs fixed (12 flagged wrong, 8 TP, 4 FP all traceable
  to schema bugs).
- **Recall** 100% under error injection, within the checks' scope.
- Coverage lost to: premise/initial steps (~18), extraction/schema failures (41), design-choice
  ambiguity, confusing provenance, and ~51 steps involving derivatives/integrals of functions with
  no closed form.
- **Family oracles** (Lagrangian → EoM for one family) recovered 12 steps, 27% → 33%.
- **Family assignment, not the oracle math, is the bottleneck.** Concrete failure: a 3-mass problem
  where only 2 masses had springs; the model force-fit it into "masses on springs" and mislabeled a
  correct step wrong. Mostly dissolves in a *label-factory* setting (family known at curation time),
  persists in a general harness.
Full proposal (July 2026 draft) extends this to a label factory for PRM training + dense GRPO
rewards, with experiments E0 (verifier audit / go-no-go gate), E1 (execution vs knowledge failure
diagnostic), E2 (label-source comparison: executable vs Monte Carlo vs LLM judge), E3 (RLVR),
E4 (three-ring transfer + frontier parity). Two named paths: **training path** (label factory) and
**harness path** (attach current checks to Theo now).
 
Next check Moinul wants to build: verification of **differential-equation solutions** (numerical
solve + compare, so blame can be localized). He observes an equation-of-motion-plus-proposed-solution
pattern in ~40% of cases.
 
### 2.2 Shay — "Verify" tool suite — "top-down, agentic, trust layer"
 
A broader trust layer over AI-generated answers rather than deep math checking. Five tools:
 
1. **Missing-Physics Detector** — flags terms/effects a model left out, with the regime where each
   matters.
2. **Uncertainty Engine** — calibrated intervals, propagated error, "unquantified" rather than
   "certain" when unknown.
3. **Inverse-Problem Solver** — infer parameters from observations; reports identifiability.
4. **Active Experiment Designer** — proposes the next most discriminating measurement.
5. **Reproducibility Auditor** — can this result actually be reproduced.
Plus a citation cluster: Source Matcher, Quote-Fidelity Checker, Citation-Relevance Judge, Coverage
Auditor. Claim–evidence alignment is **already shipped** into Collaborator (Alex P. + Shay).
Delivery mode: SKILL.md files plus MCP servers. Feasibility rated HIGH.
 
Standing critiques of this suite (mine, already given and accepted as open questions):
 
- Plain text vs structured objects end-to-end — affects composability across tools.
- The missing-physics example is regime-specific (low-speed, large, low-viscosity). Small diameter
  or high viscosity puts you in Stokes drag, not quadratic. Does the detector reason about regime or
  pattern-match "air resistance ignored"?
- Error bars need **provenance**, not just magnitude: 1σ vs 3σ convention; single-measurement error
  vs error of the mean (factor 1/√N); assumption-driven error (neglecting second-order hopping in
  cuprates can be <1% in some regions and phase-determining in others). Lesson from IAIFI: a single
  number is not enough — physicists care about *what contributes* (random vs systematic).
- Inverse problems are ill-posed near critical points (see npj Comput. Mater.
  https://www.nature.com/articles/s41524-022-00889-2). Does the solver detect non-invertibility?
- Reproducibility checks need weights (simulation settings > software versions) and *intervals*, and
  full re-runs can be prohibitively expensive (month-long simulations).
- The most interesting sentences in physics writing — novel claims, disagreements — have no citation
  by definition. Do not penalize un-cited-because-novel.
### 2.3 Marcin — human-facing verification + the toolkit list
 
A longer catalogue of checks organized as: (1) parse and normalize — Expression Parser, Symbol
Table, **Convention Profiler** (SI/CGS/Gaussian, natural units, metric signature, summation, sign
and angle conventions), Claim Segmenter (builds the derivation DAG); (2) structure and equivalence —
dimensional, index/tensor, symbolic equivalence, metamorphic relation testing; (3) physical laws —
conservation, symmetry/covariance, physicality; (4) limits and scales — known-physics limit
recovery, order-of-magnitude with per-field tolerance, asymptotics, **Approximation Certificate
Generator**, Regime Validity Checker; (5) numerical trust — discretization/convergence, independent
reimplementation; (6) formal methods where tractable.
 
Framing model offered in the Aug 25 meeting: the product should feel like a supervisor returning
your paper covered in red — or a "grammar checker for physics". Deliberately **not** latency-bound;
if we accept tens of dollars and minutes of compute per document, we can do things a real-time node
cannot.
 
**This document is a fourth angle, additive to the above.**
 
---
 
## 3. Prior positions worth carrying forward (they constrain the design)
 
- **Never present a verifier verdict as "this is wrong."** Present a neutral highlight ("dimensions
  changed here") and let the model/user interpret. A unit-check failure may mean a silent move to
  natural units, not an error. Gate on repeated failure; weight the flag by the known reliability of
  the check. (Agreed with Moinul and Alex.)
- **LLM as orchestrator, not judge.** The LLM notices *that* an assumption changed and routes to the
  right deterministic tool; the verdict stays mechanical.
- **The most interesting derivations break rules on purpose** — dropping terms, neglecting effects,
  idealized fields, natural units. A strict pass/fail gate suppresses exactly the physics that
  matters. Verifiers calibrated on established results suppress new physics (quasicrystals took
  years to publish). *Contradiction with the literature must be its own flagged verdict, examined
  rather than penalized.*
- **Layer 1 failing must not equal REFUTED.** Most verification failures in practice are extraction
  failures. Failing to show agreement is not demonstrating a mistake.
- **Symmetry is approximate, not exact.** From IAIFI 2026 Day 2: Plehn — "every good symmetry is
  broken, either by the Higgs mechanism or by the experiment; perfect symmetries in particle physics
  don't exist." Tahmasebi (ICLR 2026) — exact symmetry enforcement by group averaging requires the
  whole group; approximate symmetry needs a random subset of size ≈ 3 log|G|, sampled once offline,
  with the bound holding uniformly over the function class. Design rule: impose approximately
  correct structure, know which constraints are approximations, stop paying for exactness.
- **Family is not notation-invariant.** Three coupled masses between two walls is the same system as
  three independent oscillators in normal-mode coordinates. Defining a family as a group orbit under
  canonical transformations would fix the case but raises closure and coverage questions.
- **Xingyang's taxonomy** (his own framing, HEP): classify by *easy/hard to solve* × *easy/hard to
  machine-check*, crossed with *domain tags* × *task families*. Start with easy-to-solve and
  easy-to-check. He counts ~12 candidate vertical slices in high-energy theory. As internal customer
  he wants: **he** decides where the verification checkpoints are, not the system, and he will
  tolerate minutes of latency for a checkpoint he chose.
- **Collin's skepticism** (must be answered, not dismissed): scope and generality of the rules; how
  much coverage is achievable even within one topic; verification will be slow.
- **Rise's licensing view:** stay open-source permanently for individuals, license so nobody can
  build a commercial platform on top; enterprises pay.
---
 
## 4. The proposal: a watchdog on agentic traces
 
### 4.1 Core claim
 
All existing verification work in this space — ours and PSI's — consumes **artifacts**: a final
answer, a report, a paper, a derivation. Increasingly, physics work is produced by agentic loops
that emit far more intermediate data than a human will ever audit. Propose: **verify the agentic
data, not (only) the human-facing output.**
 
Differentiation from GPD: they consume output. We can consume intermediate artifacts (tool calls,
generated code, execution results, subagent outputs, files) and, for models we host, the **raw
chain of thought**.
 
### 4.2 The visibility grid
 
What the verification layer can see is two independent axes, not one ladder:
 
```
                    output only          + tool calls, files,
                                          code runs, subagents
─────────────────────────────────────────────────────────────
no introspection    GPD's regime         frontier agents
                                         (Claude Code + hooks)
 
+ CoT summary       frontier chat API    frontier agent,
                                         summarized thinking
 
+ raw CoT           open-weight          open-weight loop
                    single call          (full visibility)
```
 
The columns matter as much as the rows. Keeping them separate turns "open vs closed weights" into a
sharper and more useful question (see §5.1).
 
### 4.3 Modes of operation
 
1. **In-stream** — watchdog sits between nodes, consuming tokens as they flow, barking on issue.
   Latency is the problem. Possibly defensible with a cheap fast-model filter that escalates only
   suspicious segments.
2. **Background / out-of-band** — the preferred mode. Sniffs the log while work continues, raises
   warnings asynchronously. This changes the economics, not just the latency: expensive checks
   (independent reimplementation, numerical cross-checks — the ones tagged VERY HARD / BIG PAYOFF)
   become affordable because nobody is waiting.
   The right target is a **lag budget**, not a latency target: flag step *k* before the physicist has
   built so much on top of it that correcting *k* is expensive. For derivation work that is minutes.
3. **Hook / gate** — real interruption at a tool boundary (see §7.3). Best for demos and for
   high-stakes checkpoints the user opted into.
Explicitly **not** another critic node in the loop. That exists.
 
### 4.4 Why this fits the company
 
- Theo: a "verified / partially verified" surface with an audit trail of *what* was checked.
- Conjecture: trace-level access is exactly what novelty detection and common-knowledge-laundering
  detection need — the moment a model retrieves a known result and reframes it is visible in the
  trace and invisible in the output.
- Natural OSS/paid split: open-source = skills + MCP + IDE integrations operating at the
  "no introspection" level (matching GPD, establishing the floor, buying community feedback);
  paid platform = introspection, background operation, hosted compute.
---
 
## 5. Research question and experimental design
 
### 5.1 The question
 
> **Does raw chain-of-thought add anything over and above a rich behavioral trace, for catching
> physics errors?**
 
Sub-questions, in order of decreasing importance:
 
1. **Earliness.** How much earlier is an error detectable with trace access than with output access?
2. **Detectability.** Are there error classes detectable *only* with trace access?
3. **Compression.** Does a *summary* of the CoT retain the signal, or does compression destroy it?
   (Decides whether asking a frontier lab for full-thinking access is worth doing.)
4. **Cost.** Detection per verification token — does the trace advantage survive compute matching?
Outcome interpretation is symmetric and both directions are useful:
 
- **Raw CoT wins** → self-hosting is a moat; the paid platform has a capability the open-source floor
  and any frontier wrapper structurally cannot have.
- **Behavioral trace is enough** → the product is more general than assumed and works on frontier
  agentic systems; that is a *better* commercial story, just a different one.
### 5.2 Novelty check (do before writing anything)
 
Verification of reasoning traces for *correctness* appears unexplored. Adjacent literature to
position against:
 
- Reference-based step evaluation: PRISM-Physics (causal DAG + symbolic equivalence against a gold
  derivation — evaluation only).
- Learned step judges: Sci-PRM, DataPRM, Math-Shepherd, generative verifiers.
- Verifier-grounded labels in formal domains: FoVer.
- **CoT monitoring from the safety community** — monitoring chains of thought for reward hacking and
  misbehavior. This is the closest methodological relative and the strongest hook: that community
  monitors CoT for *intent*; nobody monitors CoT for *physics*.
- **CoT faithfulness literature** — the known result that stated reasoning may not reflect the
  computation actually performed. This is a limitation to state honestly, and it also generates a
  check (see §7.2, trace/output consistency).
### 5.3 Design: generate once, replay under masks
 
Do **not** run a factorial where trace access and verification are crossed by re-running generation.
Turning thinking off changes the trajectory, so the arms would be verifying different objects.
 
Instead:
 
1. Run each problem **once** at full visibility. Store the complete **trace envelope**.
2. Replay the same stored envelope through the watchdog under N **visibility masks**.
3. Compare paired, per problem.
This eliminates generation variance, makes the comparison genuinely paired, and pays generation cost
once instead of N times.
 
**Masks:**
 
| Mask | Sees |
|---|---|
| M0 | final artifact only |
| M1 | artifact + tool calls / code / execution results / files |
| M2 | M1 + *our own* summary of the raw CoT |
| M3 | M1 + raw CoT |
 
M2 is the control that isolates compression from concealment. If M2 ≈ M3, summarization is fine and
frontier agents are viable targets; if M2 ≈ M1, compression destroys the signal.
 
Verification-off is a **separate arm**, not a factor.
 
**Full arm list for the end-to-end plot:** bare model → model + "check your own work" prompt →
best-of-N self-consistency at matched token budget → watchdog M0 → M1 → M2 → M3 → M3 + repair loop.
The self-critique and best-of-N arms are the honest baselines most verification papers skip; if the
watchdog does not beat them at matched tokens, that is the finding.
 
### 5.4 Primary metric: earliness, not accuracy
 
Downstream accuracy is noisy and lagging; separating arms on it needs hundreds of problems.
 
**Primary:** *segment lag* = (index of first correct flag) − (index of the commitment segment where
the error entered). Report the distribution, and detection rate as a function of lag budget.
 
This is where trace access should dominate by construction: in M0 a wrong drag assumption is
invisible until it surfaces in a final expression; in M3 the model *says* "I'll neglect air
resistance" at segment 3.
 
**Secondary:** detection rate; precision; false-positive rate on the unconventional-but-correct
control set; coverage (fraction of segments adjudicable — comparable to PVRE's 27.2%); repair
success rate given a flag; end-to-end accuracy (reported last).
 
**Statistics:** paired across masks. McNemar for detection rate, Wilcoxon signed-rank for lag.
 
### 5.5 Compute control
 
Generation compute is identical by construction (single generation, replayed). Verification compute
is *not* — M3 hands the watchdog roughly an order of magnitude more tokens to read, so it wins
trivially unless controlled.
 
Two mitigations, use both:
 
1. **Token ledger** with three buckets logged per run — `generation`, `verification`, `repair` — so
   any plot can be produced post hoc.
2. **Matched verification budget:** give thinner masks the budget difference to spend on extra
   probing (more numerical draws, more sampled queries against the artifact, an LLM re-derivation).
   Report detection-vs-verification-token curves, not single points.
### 5.6 Threats to validity — build for these from day one
 
- **Considered vs committed.** Models think aloud about ideas they discard ("maybe include the
  radiation term — no, negligible here"). A naive M3 watchdog flags claims the model never committed
  to. **M3 may have worse precision than M1 for the same reason it has better recall.** Mitigation:
  every extracted claim carries `status ∈ {considered, committed, retracted}`; only committed claims
  are adjudicated; considered-and-dropped goes to a separate quieter channel. That channel is itself
  a product feature ("considered a relativistic correction, dropped it without justification").
- **Trace-exclusive checks inflate the delta.** Some checks cannot exist without trace access at
  all (§7.2). Including them makes the tier delta non-zero by construction. **Decompose the reported
  delta** into (a) same checks firing earlier and (b) checks only possible with trace access. Both
  are real contributions but they are different claims.
- **CoT unfaithfulness.** A flag derived from CoT is a flag about what the model *said* it was doing.
  State this. It does not invalidate the result — a stated-vs-done mismatch is itself detectable.
- **Contamination.** Any static benchmark partially measures prior exposure. Use fresh generated
  instances and parameter-dialed variants for the primary result.
- **Trap validity.** If the models do not actually fail on a trap, the trap measures nothing.
  Pilot-screen before committing (§6.5).
---
 
## 6. Data: generation and collection
 
This is the least-developed part of the plan and probably the critical path.
 
### 6.1 Requirements
 
A usable item needs all five:
 
1. Non-trivial physics, but with **ground truth we own** (constructed, not looked up).
2. A **decisive commitment** — an assumption or step that, if wrong, determines the answer — that
   occurs **mid-derivation**, not at the end. Without this the trace can offer no earliness
   advantage and the experiment is unmeasurable.
3. A demonstrated **non-trivial model failure rate** on the models we can run.
4. A **mechanical oracle** for both the right and the wrong branch, so we can quantify how much the
   error costs.
5. Freshness / parameterizability, to avoid contamination.
### 6.2 Source A (primary): regime-parameterized trap families
 
This is the recommended backbone, and it is a genuine design contribution rather than a data chore.
 
**Pattern:** a problem template with a **regime dial** — one physical parameter whose value flips
which physics applies. The same template generates both a positive instance (default reasoning is
wrong) and a negative instance (default reasoning is right). A model that pattern-matches the
template fails on one side of the dial; verification that reasons about regime handles both.
 
This directly answers the standing critique of the Missing-Physics Detector ("the example is correct
in one regime only"), and it doubles as the false-positive control set.
 
**Candidate families** (each needs: crossover expression, both-branch oracles, parameter ranges):
 
| # | Family | Dial | Default (wrong) | Correct in trapped regime |
|---|---|---|---|---|
| 1 | Terminal velocity of a droplet | diameter → Reynolds number | quadratic drag | Stokes drag |
| 2 | Coupled oscillator response | quality factor Q | undamped normal modes | damped, complex modes |
| 3 | Electron gas properties | T / T_F | Maxwell–Boltzmann | Fermi–Dirac |
| 4 | Kinetic energy / momentum | v / c | classical | relativistic |
| 5 | Diatomic heat capacity | T vs rotational/vibrational temp | equipartition | frozen-out modes |
| 6 | Thermal transport in a wire | mean free path / diameter | Fourier's law | ballistic / Casimir |
| 7 | Gas equation of state | proximity to critical point | ideal gas | van der Waals |
| 8 | Pendulum period | amplitude | small-angle | elliptic integral |
| 9 | Surface heat loss | temperature | convection-dominated | radiation-dominated |
| 10 | Projectile range | flight time / latitude | inertial frame | Coriolis included |
| 11 | Charge interaction in plasma | Debye length / separation | bare Coulomb | screened Yukawa |
| 12 | Speed of sound | thermal relaxation vs oscillation | isothermal (Newton's error) | adiabatic |
 
**Why this shape works:** ground truth is code-derived (implement both models, evaluate both, report
the ratio); difficulty is a knob (dial closer to the crossover, or compose two traps in one problem);
the commitment is textually locatable in the trace independent of the watchdog (the model *states*
which drag law it is using), which avoids circularity in the earliness measurement.
 
Target: 25–30 families × a few parameter settings each.
 
### 6.3 Source B: PVRE generator instances
 
Moinul's generator already emits problem packages with the full derivation graph, symbols with
dimensions, assumptions, conserved quantities, limit specifications and an outcome oracle. Step-level
ground truth exists by construction.
 
Use it for: coverage measurement comparable to his 27.2% number, and for algebraic-slip errors
(which are the *hard* case for the trace advantage — an arithmetic mistake is equally visible in
output and trace, so this set is a useful null).
 
Limitation: deliberately undergraduate-level, so natural failure rates are low. Crank the difficulty
knobs (mass count, damping, asymmetry, perturbative order) until failure rate lands in band.
 
**Reuse rather than rebuild.** Import his dimensional-consistency and numerical-entailment checks
directly; this is the point where the top-down and bottom-up streams physically meet.
 
### 6.4 Source C: natural harvest
 
Run the models at scale on Sources A and B, keep trajectories where the final answer disagrees with
the oracle. These are genuine, un-planted errors and are the external-validity set.
 
Labeling cost is the issue: the first-wrong-step must be identified without using the watchdog
(circularity). Two routes: mechanical alignment against the PVRE derivation graph where one exists,
and hand-audit of a bounded subset (~100–150 steps; Moinul's proposal budgets ~500 hand-audited
steps for a comparable purpose, so this is in line).
 
### 6.5 Source D: prompt-steered errors (calibration only)
 
Force a wrong commitment at a known segment index ("assume the drag is quadratic") and measure
detection lag against a known ground-truth position. Artificial, but it calibrates the lag metric
and lets you sanity-check the pipeline before natural errors exist. Not for headline numbers.
 
### 6.6 The control set: correct-but-unconventional traces
 
**Do not skip this.** 15–20 trajectories that are correct but violate naive checks:
 
- natural units (the `log(1/T)` case — a unit-check failure that is not an error)
- deliberate term-dropping with justification
- gauge / coordinate changes mid-derivation
- normal-mode coordinate switches (same physics, different apparent family)
- CGS vs SI, different Fourier-transform 2π conventions
- a legitimate mid-stream change of assumption ("if we now relax that constraint...")
- square → hexagonal lattice symmetry change mid-derivation
Metric: false-positive rate. This is the direct answer to the novelty-suppression concern and it is
what determines whether physicists keep the tool switched on. **Report it in the headline table, not
an appendix.**
 
### 6.7 External benchmarks (validation only, last)
 
PHYBench, ABench-Physics dynamic variants, CMPhysBench condensed-matter subset. Final-answer ground
truth only, contamination risk on static versions. Use to show the effect is not an artifact of our
own generator; never as the primary result.
 
### 6.8 Scale and screening
 
- Pilot 5 trap families first. Keep only families where model failure rate lands in **20–80%** on
  the models we run. Outside that band the item carries no information.
- Target corpus: ~30 traps + ~60 harvested natural errors + ~20 controls ≈ 110 items × 3 seeds.
- Models: **GLM and Qwen3-class served locally with vLLM** (`--reasoning-parser`, returns
  `reasoning_content`) for generation, since the replay design needs generation to be cheap;
  **Kimi via API** as the large-model point (also returns `reasoning_content`). Then frontier models
  for the M2-equivalent tier.
---
 
## 7. System design decisions already made
 
### 7.1 Separation of concerns
 
Three planes that must not be conflated:
 
| Plane | Question | Answer |
|---|---|---|
| Checks | how is the verification logic packaged | plain Python library; MCP is one wrapper over it |
| Ingestion | how does the trace get in | **not MCP** — proxy, hooks, or our own loop |
| Control | warn / report / interrupt | determined by the ingestion route |
 
**MCP is pull** — the host agent decides to call your tool. **A watchdog is push** — it fires when a
segment arrives whether or not the agent wants it. MCP therefore cannot be the trace intake. It is
fine for exposing checks in an IDE and later in Theo.
 
MCP is client-agnostic (same server in Cursor, VS Code Copilot agent mode, Claude Desktop, Claude
Code, Windsurf) — no Claude Desktop lock-in. Practical constraint: tool-count ceilings (Copilot 128,
Windsurf 100, Cursor degrades earlier). **One server, ~5 coarse tools**, not twenty fine ones — also
because the checks share state (convention profile and symbol table) that would otherwise be
re-derived on every call.
 
### 7.2 What the watchdog consumes
 
Not the question, not the artifact. A **segment stream plus session state**:
 
```
Segment: {seq, kind: thinking|assistant|tool_call|tool_result|file_write,
          text, t, tokens, visibility_level}
Session: {problem_statement, convention_profile, symbol_table,
          claim_dag, claim_status_map, prior_verdicts, open_flags}
```
 
The accumulating session state is what makes this a watchdog rather than a critic node. It learns at
segment 3 that natural units were declared, so `log(1/T)` does not fire at segment 11; it noticed at
segment 5 that drag was dropped, so when the model claims high-velocity validity at segment 20 *that*
fires — an inconsistency invisible in either segment alone.
 
Segment on completed thinking blocks and tool boundaries, not on raw tokens. Same effect, far less
parsing pain, and it preserves the upgrade path to true streaming.
 
**Check selection** (spread across the cost/determinism axes rather than exhaustive):
 
1. Convention profiler + symbol table (LLM proposes, code stores) — substrate, not a check.
2. Dimensional consistency — pure code. *Reuse PVRE.*
3. Numerical entailment under random substitution — pure code. *Reuse PVRE.* Workhorse.
4. **Missing-physics / neglected-term estimator** — flagship. LLM proposes candidate omitted terms;
   code estimates each term's magnitude relative to the leading term across the stated regime and
   returns the crossover. Output shape: *"quadratic drag is ~10⁻³ of gravity here, but dominant below
   d ≈ 80 µm."* No skills-only version can fake this.
5. Assumption/ansatz auditor — enumerate assumptions; flag declared-but-unused, used-but-undeclared,
   and assumptions that do not survive to the conclusion.
6. Limit recovery — code plus a deliberately tiny curated table (5–10 reductions).
7. Order-of-magnitude and positivity sanity, with per-field tolerances.
8. **Trace/output consistency** — *trace-exclusive*: the model stated it would do X and the artifact
   does not contain X. Cannot exist at M0/M1. Flag as trace-exclusive in the results decomposition.
Conservation checks: gate on an explicitly stated Lagrangian and abstain otherwise. Modelling honest
abstention is more informative than faking family assignment.
 
**Output contract.** Never "wrong." Per-claim rows with a five-value verdict:
`consistent` / `inconsistent` / `convention-changed` / `unadjudicated-extraction` /
`unadjudicated-no-applicable-check`.
 
Splitting the two unadjudicated classes is the single most useful diagnostic we will produce — it
says whether to invest in the parser or in more checks, which is exactly where PVRE's coverage went.
Every flag carries the regime in which it applies and the reliability of the check that produced it.
 
### 7.3 Adapters (build in this order)
 
The joint between research and open source is the **trace envelope** — normalized JSON of segments
with kind, ordering, text and visibility level. Adapters emit envelopes; the watchdog consumes
envelopes and knows nothing about their origin. This is what lets the OSS repo and the research
share one codebase, and it makes the future-Theo case trivial: anything that can emit segments is a
supported source.
 
1. **Own instrumented loop** (`adapters/own_loop.py`) — vLLM-served GLM/Qwen, full `reasoning_content`.
   Owns seeds, temperature, token counts, on/off switch. **This is where the experiment lives.** Build first.
2. **Claude Code hooks** (`adapters/cc_hook.py`) — best live demo for ~50 lines. Hooks receive JSON on
   stdin including `session_id`, `transcript_path`, `cwd`, `hook_event_name`. Exit code 2 blocks and
   sends stderr back to the model. A `PreToolUse`/`PostToolBatch` hook reads `transcript_path`, feeds
   new segments to the watchdog, and exits 2 to halt before the next model call. A `Stop` hook can
   return `decision: "block"` to force continuation until the flag clears — that is the repair loop,
   in-agent, with no orchestration code. Caveat for the slide: the thinking in that transcript is a
   summary, so this demo is M2, not M3.
3. **Reverse proxy** (`adapters/proxy.py`) — LiteLLM or a small FastAPI shim; point `base_url` at
   localhost. Framework-agnostic, sees `reasoning_content` for open models. This is "watchdog on the
   stream" made general.
4. **File ingest** — drop a `.jsonl`, get a report. How Xingyang tries it without installing anything.
Manual pasting of traces appears nowhere.
 
### 7.4 Repo shape
 
```
watchdog/
  core/           # pure library, zero framework deps
    envelope.py   # trace envelope spec — the joint
    schema.py     # Claim, Verdict, Session, ClaimStatus
    extract.py    # LLM proposer -> typed claims + confidence
    session.py    # convention profile, symbol table, claim DAG
    checks/
    report.py
  mcp_server.py   # thin wrapper, one server, session-keyed
  adapters/       # own_loop, cc_hook, proxy, file
  skills/         # SKILL.md — the OSS floor / M0 arm
  bench/
    families/     # regime-parameterized trap families
    controls/     # correct-but-unconventional traces
    run.py        # arms x masks x seeds, token ledger
```
 
Skip LangGraph in `core`. Its value is the diagram and the interrupt primitives; add it as one
adapter later if a slide needs the picture. Locking the verifier to it buys nothing and costs
portability into Theo.
 
---
 
## 8. Verified facts about chain-of-thought availability
 
Checked August 2026. Re-verify before publishing; this area moves.
 
- **OpenAI** — raw chain-of-thought tokens are **not exposed**; only summaries. Stateless mode
  returns an `encrypted_content` blob that provides continuity without exposing raw reasoning. Azure
  documentation states that attempting to extract raw reasoning by other means is unsupported, may
  violate the Acceptable Use Policy, and may result in throttling or suspension. **Do not build a
  demo that depends on it.**
- **Anthropic** — Claude 4+ models return a **summary** of the thinking process by default;
  summarization is performed by a different model, and the thinking model does not see the summary.
  Claude Code's visible thinking is that same summary. However, a `display` field on the thinking
  configuration controls how thinking is returned, and the documentation directs customers needing
  full thinking output to contact sales. **Worth an ask** given this is a research use case.
- **Open weights** — vLLM returns `reasoning_content` via `--reasoning-parser` for DeepSeek-R1-class,
  Qwen3, GLM and others. Kimi's thinking models return `reasoning_content` and support preserved
  thinking across turns. Full raw CoT, no restriction.
**Consequence to state as a design principle:** raw-reasoning verification is only possible on
open-weight or self-hosted models. That is an architectural moat against a frontier-wrapper
competitor, and it aligns with the company's open-weight posture.
 
---
 
## 9. Demonstration plan
 
### 9.1 What to build for buy-in
 
A POC / narrow MVP, not production. It must show a *capability*, not a roadmap.
 
### 9.2 The 5-minute demo
 
The strongest beat available is **the research question rendered visually**: the same trajectory,
two masks, side by side.
 
| Time | Beat |
|---|---|
| 0:00–0:30 | Frame: agents produce more intermediate data than anyone audits. We watch it. |
| 0:30–2:00 | Live: agent solves a trap problem (20 µm droplet terminal velocity, Re ≈ 0.02). Two watchdog panels. **Left (M0/M1): silent.** **Right (M3): fires at segment 3**, the moment the model writes the quadratic drag term — `missing-physics · regime: quadratic drag assumed; Re ≈ 0.02, Stokes regime; crossover at d ≈ 80 µm; affects result by ~40×`. The agent has not produced an answer yet. |
| 2:00–3:00 | Let it run. M0 catches it at the end, or not at all. The gap between the two panels *is* the contribution. |
| 3:00–4:00 | Hook fires: agent halts, receives the flag, revises, watchdog goes green. |
| 4:00–5:00 | The plot: tokens on x, detection (or accuracy) on y, one curve per mask, plus the best-of-N baseline. |
 
Show the false-positive control in the same session if there is time: run a correct trajectory in
natural units and show the watchdog **not** barking. That single moment answers the objection
everyone in the squad will raise.
 
### 9.3 Rough sequencing
 
| Wk | Deliverable | What it proves |
|---|---|---|
| 1 | `core/` envelope + own loop + 3 checks on GLM/Qwen | ingestion works on raw CoT |
| 2 | Missing-physics probe with regime crossover; assumption auditor; claim-status tracking | the flagship check, and the considered-vs-committed problem handled |
| 3 | 5 pilot trap families + failure-rate screen | the corpus is viable |
| 4 | MCP wrapper + Claude Code hook + interruption | it is a watchdog, not a linter |
| 5 | Full corpus + controls; bench harness with token ledger | measurement exists |
| 6 | Replay across M0–M3; the plot; OSS floor packaged as the M0 arm | the claim |
 
---
 
## 10. Open questions
 
1. **Packaging determines the shape of input and output**, so it cannot be deferred indefinitely
   even though it is a separate discussion. Which comes first: MCP-in-Theo, standalone service,
   or OSS repo?
2. Does anyone else verify at CoT level? (Novelty check not yet done — §5.2.)
3. Is a fast-model pre-filter enough to make the in-stream mode defensible, or is background the
   only viable mode?
4. What is the right unit of "commitment"? Sentence, thinking block, or explicit schema declaration?
5. Should the considered-but-rejected channel be surfaced to users at all, or held as audit-only?
6. Do we ask Anthropic for full-thinking access, and does the M2 control make that decision for us?
7. How does this compose with Moinul's family oracles — does the trace tell us the family, removing
   his hardest bottleneck? (Plausible and worth testing: the model usually *states* what kind of
   system it thinks it has.)
8. Licensing shape (Rise's not-for-commercial-use proposal) — product decision, but it interacts
   with what goes in the OSS floor.
---
 
## 11. Glossary
 
- **CoT** — chain of thought; the model's reasoning tokens.
- **Trace envelope** — our normalized JSON representation of an agent run; the interface between
  adapters and the watchdog.
- **Mask (M0–M3)** — a visibility level applied at replay time to a stored envelope.
- **Segment lag** — first-correct-flag index minus commitment index; the primary metric.
- **Trap family** — a problem template with a regime dial whose value flips which physics applies.
- **Commitment vs consideration** — whether the model actually adopted a claim or merely floated it.
- **PVRE** — Moinul's Physics Verifiable Reward Environments.
- **GPD** — PSI's get-physics-done, the competitor artifact.
- **Theo / Collaborator** — the FirstPrinciples agentic research platform.