# Verification (standing interest)

Extract verification content whenever the paper actually has some, whether verification is the main subject or a side tool, reward, eval, or throwaway remark. If the paper does not speak to it, write `None.` under `## Verification`. Do not invent a verification angle.

Name B12 only when the paper actually bears on a graded physics verifier. The notes below are a snapshot of our interest, not a spec the paper must match. Some of this is still moving.

## What "verification" includes here

Anything that checks whether a scientific claim, step, derivation, simulation, citation, or agent trace is trustworthy. Examples (not a required list): dimensional, algebraic, numerical, limit, conservation, or symmetry checks; process vs outcome rewards and PRMs; LLM-as-judge vs executable oracles; coverage, precision, abstention, error injection; assumption and regime tracking; intentional approximations; citation and quote fidelity; missing-physics detectors; uncertainty with type and provenance; replication and reproducibility cost; inverse problems; next-experiment design; formal proof tools used on physics or as a contrast class.

## Where we currently stand

Three complementary streams, not competing ones. Physics verification will not reach 100% coverage. The goal is well-characterized partial coverage, feeding both product (trust in Theo) and training (labels for RLVR / PRMs).

Deterministic step checks (PVRE line). Take the process-reward idea from math, where a checker can label steps, and port it to physics, where there is no Lean for the interesting part. Verdicts must come from a deterministic procedure (dimensions, numerical entailment by random substitution, limits, conservation, a registry of known relations), never from an LLM acting as judge. Undecided is fine; false pass/fail is not. Models emit a structured schema (symbols with dimensions, assumptions, tagged steps) because free-form prose is hard to check. A pilot on undergraduate coupled oscillators got high precision after schema bugs were fixed, and high recall under error injection inside the tool's scope, but coverage around a quarter of steps. Losses: premise steps with nothing to entail from, extraction and notation, provenance of which parent a child uses, integrals without a closed form. Adding a family oracle (Lagrangian to equations of motion) recovered some steps. Family assignment, not the oracle math, is the bottleneck: near-adjacent families get force-fit, and a correct step can be marked wrong. That problem mostly disappears if the family is known at curation time (label factory) and persists in a general live harness.

Two paths: attach the current checks to the agent as a harness now; use family oracles to generate synthetic problems and train later. Executable labels are high-precision but partial. Monte Carlo continuation labels are complete but collapse on hard problems. LLM judges are complete, biased, and hackable. Whether precise-but-partial beats noisy-but-complete is an open empirical question we care about.

Top-down trust tools (Verify line). Missing-physics detector (did we forget an effect, and in which regime?). Uncertainty engine (how sure, and from what kind of error). Inverse-problem solver (hidden parameters from data; ill-posed near critical points). Active experiment designer (which measurement discriminates two theories). Reproducibility auditor (code, settings, can we afford to re-run?). Citation cluster: is there a real source, does the quote match, is the citation on-topic, are key claims sourced. Claim–evidence alignment is already in the collaborator product. Open issues: text vs structured objects; regime, not pattern-match, for neglected terms; error provenance; do not penalize novel uncited claims.

Trace / watchdog line. Checking the agent's trajectory, not only the derivation: whether numbers in a report match executed outputs, whether a small-grid numerical result was treated as exact, whether "common knowledge" is laundered as a discovery.

Presentation rule we have already agreed internally: do not phrase a check as "this equation is wrong." Phrase it as a neutral flag ("dimensions changed here"). A unit failure may mean a silent move to natural units. Let the user or an orchestrating model interpret. Weight the flag by how reliable that check is known to be. LLM as orchestrator (notices that an assumption changed, routes to the right tool), not LLM as judge.

Interesting physics often breaks exact rules on purpose: dropped terms, neglected couplings, idealized fields, natural units. A hard pass/fail gate can suppress the work that matters. Contradiction with the literature should be its own flagged verdict, examined rather than scored as failure. Failing to show agreement is often an extraction failure, not a demonstrated mistake.

Symmetry: exact constraints can be physically false (broken by dynamics or by the detector) and computationally expensive (full group averaging). Approximate structure, with the approximation named, is the design rule we currently believe. Family is not notation-invariant: three coupled masses and three independent oscillators in normal modes are the same physics, different templates.

Older interests, from before this programme was real (keep as topics, not as current architecture): replication exploiting the hidden-knowledge gap in papers; error detection with planted faults that are algebraically clean but physically wrong; assumption enumeration; planted-structure and constraint-modified problems that are hard to retrieve and easy to check; self-consistency across methods (necessary, not sufficient); process-level scoring, not only the final number; the known-problem vs unknown-problem bind (retrieval contaminates the first, the second has no ground truth). Interviews already said validation and a critical partner matter more than autonomous solving.

Self-improvement loops that refit their own unfiltered samples collapse as external signal vanishes. Solvers, proof checkers, execution, and experiment are the kind of external signal that can keep the loop honest.

## Questions to ask (surface only what is there)

What is being checked: final answer, intermediate step, citation, experiment, or the agent's trace?

Who issues the verdict: a deterministic procedure, a learned judge, a human, or an LLM? Can the policy hack that signal?

What happens when the checker cannot decide? Is abstention allowed?

Coverage vs precision: how much can they even attempt, and how often is a flag real?

Are "errors" sometimes the physics? Does the paper treat intentional approximations as failures?

Exact vs approximate structure, especially symmetries.

Is the hard part classifying the problem into a family, not running the oracle?

What ships at inference: internalized habit, a portable checker, a PRM, or only training-time labels?

Would process evaluation change the headline number? Is the eval contaminated? Is the cheap baseline missing?

## How this appears in the review

`## Verification` is for facts the paper states: methods, numbers, failure modes, what they refused to check. Keep it short. Slightly longer than a learning paragraph is fine if the numbers matter.

`## Critical discussion` is where you assess whether the check supports the claim, whether coverage is load-bearing, and whether an LLM judge is doing the real work.

`## Relevance to us` is where you say whether the result helps, hurts, or changes B12 or another part of our verification programme.

If verification is absent, write `None.` in the Verification section. Do not criticize a paper merely for lacking a verifier unless its central claim requires a check it did not perform.
