---
schema_version: 1
paper: slug:25mcpsim
title: "A self-correcting multi-agent LLM framework for language-based physics simulation and explanation"
authors:
  - Donggeun Park
  - Hyeonbin Moon
  - Seunghwa Ryu
publication:
  first_public_date: "2025-06-22"
  first_public_date_precision: day
  venue: "npj Artificial Intelligence"
  status: journal
  reviewed_version: null
  reviewed_version_date: null
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-06-09/25mcpsim.md
raw: papers/raw/2026-06-09/25mcpsim-pdf.md
source_url: https://doi.org/10.1038/s44387-025-00057-z
organizations:
  - name: Korea Advanced Institute of Science and Technology (KAIST)
    sector: academia
    roles: [author_affiliation]
    authors: [Donggeun Park, Hyeonbin Moon, Seunghwa Ryu]
    grants: []
  - name: National Research Foundation of Korea
    sector: government
    roles: [funder]
    authors: []
    grants: ["RS-2025-16070951"]
  - name: Ministry of Science and ICT (Republic of Korea)
    sector: government
    roles: [funder]
    authors: []
    grants: ["N10250154"]
  - name: Korean Society of Mechanical Engineers
    sector: nonprofit
    roles: [funder]
    authors: []
    grants: []
artifacts:
  - type: code
    url: https://github.com/KAIST-M4/MCP-SIM
  - type: code
    url: https://doi.org/10.5281/zenodo.15645333
facets:
  domains: [physics, mechanical-engineering, machine-learning]
  paper_type: [system, experiment]
  methods: [multi-agent-orchestration, plan-act-reflect-revise-loop, shared-memory-coordination, llm-code-generation, finite-element-method]
  models: [GPT-4o]
  benchmarks: [MCP-SIM-12-task-suite]
assessment:
  extract_quality: partial
  extract_limitations: [table-extraction-damaged, figures-not-visually-assessed]
  critical_flags: [weak-baseline, incomplete-reporting]
metadata_notes: "First public date uses the EngrXiv preprint (2025-06-22, confirmed via WebFetch); the reviewed content is the final npj Artificial Intelligence version (received 2025-08-07, accepted 2025-11-22, published as volume 2, article 10, 2026 per web search), which is not versioned like an arXiv preprint, so reviewed_version and reviewed_version_date are left null since the exact online-publication day could not be confirmed; the paper is published in 2026, volume 2, article 10. Funding grants are stated for the group as a whole (NRF grant RS-2025-16070951, MSIT InnoCORE grant N10250154, and the KSME Yoon Young Kim AI Innovation Fund) without naming which specific authors each grant covers, so no per-author attribution is recorded. Table 1 (the twelve-task overview) is extracted with severely scrambled character ordering due to a vertical or multi-column PDF layout; its content (task levels, challenges, objectives) was reconstructed from the surrounding prose rather than the damaged table itself."
---

Citation: Park, D., Moon, H., and Ryu, S. A self-correcting multi-agent LLM framework for language-based physics simulation and explanation. npj Artificial Intelligence 2, 10 (2026).

## What this paper is about

Setting up a physics simulation normally requires knowing the governing equations, boundary conditions, and numerical solver settings well enough to specify them precisely. This paper asks whether a large language model can bridge that gap when given only a vague natural-language description, such as "simulate fluid flow in an L-shaped pipe," by filling in the missing physics itself, writing and running working solver code, catching and fixing its own errors, and explaining what it did in plain language. The authors build MCP-SIM, a system of six specialized LLM agents coordinated through a shared, persistent memory, and test it on twelve physics simulation tasks of increasing ambiguity, reporting that it solves all twelve where simpler one-shot and human-assisted baselines solve fewer, and that it also produces multilingual explanatory reports alongside the working code.

## Extended summary

MCP-SIM is built around six agents orchestrated by a "Memory-Centric Orchestrator": an Input Clarifier Agent that turns a vague prompt into a canonical problem specification (domain geometry, governing PDE, boundary conditions) and a structured JSON object; a Code Builder Agent that generates solver-ready Python code against the open-source FEniCS finite-element library using physics-aware prompt templates for mesh generation and solver configuration; a Simulation Executor Agent that runs the code in a sandbox and monitors both runtime errors and physically meaningful indicators such as conservation violations, residual divergence, and spurious field oscillations; an Error Diagnosis Agent that interprets failures in physical terms (for example, insufficient mesh resolution or a solver mismatch) and proposes targeted corrections; an Input Rewriter Agent that revises the original prompt when the problem stems from high-level ambiguity rather than a code bug, restarting the loop from clarification; and a Mechanical Insight Agent that generates a multilingual explanatory report once a simulation succeeds, covering the governing equations, boundary conditions, and solver choices. All agents run on GPT-4o and share a persistent, structured memory log of specifications, code versions, execution traces, and applied fixes, which the paper argues lets later corrections draw on the full history of prior attempts rather than treating each retry independently.

The evaluation uses a twelve-task benchmark, authored by the same team, spanning physics domains (linear elasticity, steady-state and transient heat conduction, incompressible and unsteady fluid flow, thermoelectric and piezoelectric multiphysics coupling, and phase-field fracture mechanics) arranged in order of increasing ambiguity, from fully specified textbook-style problems (Level 1) to a single-sentence prompt with no stated geometry, equations, or boundary conditions (Level 12: "simulate crack propagation in a square domain with a central circle"). Three baselines are constructed by disabling parts of the MCP-SIM pipeline: B1 (one-shot GPT) generates code once and leaves specification completion and error correction to the user; B2 (GPT plus automated clarifier) automates specification inference but leaves execution monitoring and error handling manual; B3 (GPT plus clarifier plus human diagnosis) automates diagnosis proposals but requires a human to review and accept each proposed fix before rerunning. Success is defined as solving a task under a numerical convergence criterion (a dimensionless solver residual, normalized by its initial value, dropping below 10⁻⁴) together with producing "physically plausible field distributions." Under these baselines, B1 solves 6 of 12 tasks, B2 solves 8 of 12, and B3 solves 10 of 12, while MCP-SIM solves all 12, and does so within five or fewer Plan-Act-Reflect-Revise cycles on most tasks, which the authors attribute to the shared memory letting agents consult prior error-fix mappings rather than treating each correction attempt independently.

The most demanding case, Level 12, is examined in detail: from the single-sentence prompt with no numerical values or boundary conditions stated, the Input Clarifier proposed a two-dimensional domain with a central void, Dirichlet conditions at the base, and traction-free boundaries elsewhere, and selected material constants and solver parameters; after a syntax error was caught and corrected by the Error Diagnosis Agent, the resulting phase-field fracture simulation, run through ten self-correcting cycles, is reported to produce crack propagation patterns in close visual agreement with a reference simulation of the same setup run in the commercial finite-element package ABAQUS, matching in crack initiation location and growth direction. The paper reports this as validating the correctness of the autonomously generated model, though no quantitative discrepancy metric (for example, a numerical comparison of crack angle, load-displacement curve, or field values) is given for this comparison in the text.

The system also produces structured, multilingual (English, Korean, and in supplementary material Japanese and German) explanatory reports after each successful run, combining code-level annotations with higher-level rationale, such as why a Dirichlet rather than Neumann boundary condition was used or why a particular solver was chosen for numerical stability, aimed at supporting simulation-based education. The authors explicitly acknowledge several limitations: MCP-SIM runs on a general-purpose LLM (GPT-4o) without domain-specific fine-tuning and may degrade on rarer material models or advanced multiphysics couplings; the reflective loop adds latency relative to one-shot generation; the evaluation is limited to a curated, synthetic twelve-task benchmark rather than experimental or safety-critical settings, which the authors say will require further domain-specific validation and human oversight; and long-horizon stability under noisy or adversarial inputs remains untested despite the persistent memory reducing regressions within the tested setup.

## Learnings

A deterministic, physics-grounded convergence check, here a solver residual normalized by its initial value and thresholded at 10⁻⁴, can serve as the objective trigger for an agentic reflect-and-revise loop instead of an LLM judging its own output. Anchoring the self-correction decision in a number the solver itself produces, rather than in a model's verbal self-assessment, is a directly reusable pattern for any pipeline built around an executable numerical backend.

Persistent, structured memory of the full trajectory (clarifications, code versions, and specifically which error was fixed by which correction) appears to be the mechanism behind this system's reported efficiency advantage over baselines that only act on the current run: the memory-coordinated version solved all twelve benchmark tasks against six, eight, and ten out of twelve for the three progressively more automated baselines, which the authors attribute to agents being able to consult prior error-fix mappings and avoid repeating the same failed correction, a lab-notebook style of memory rather than a sliding context window.

Splitting "write correct simulation code from an ambiguous prompt" into narrower, separately checkable roles, clarification, code generation, execution and monitoring, error diagnosis, prompt rewriting, and explanation, let the system recover a plausible physical model (a phase-field fracture setup, appropriate geometry, and boundary conditions) from a single, fully unspecified sentence with no further human input. This suggests that decomposing an underspecified task into distinct subtasks, each with its own narrower check, can substitute for demanding that a request be fully specified up front.

## Verification

Verification here is concrete but narrow in scope: it is a numerical convergence check, not a check that the model chosen for a given ambiguous prompt is the physically correct or intended one. The Simulation Executor Agent's residual threshold is a deterministic, solver-computed number rather than an LLM judgment, which is a genuine strength distinguishing this design from LLM-as-judge approaches. However, the same check only confirms that whatever governing equation, geometry, and boundary conditions the Input Clarifier Agent inferred converged to a numerically stable solution; it does not by itself confirm that those inferred choices matched the user's actual (and, in the ambiguous cases, unstated) intent. The paper's secondary success criterion, "physically plausible field distributions," is not specified as being checked by a deterministic rule, a separate model, or a human, leaving open who or what actually judges plausibility beyond the residual threshold for eleven of the twelve tasks. The one case where the system's output is checked against an independent, trusted external computation, the Level 12 phase-field fracture simulation compared against ABAQUS, is reported only as a qualitative visual match in crack initiation and growth direction, without a quantitative discrepancy measure, so the strength of that particular verification claim is weaker than the paper's "validating the effectiveness of the autonomous solver" framing suggests.

## Field context

This paper positions itself against three lines of prior work it cites directly: physics-informed neural networks, which require a fully specified governing equation and cannot interpret ambiguous natural-language prompts; one-shot LLM code-generation methods, which lack iterative refinement and fail on underspecified problems; and existing multi-agent LLM simulation frameworks in specialized contexts, naming a two-agent system for self-correcting elasticity-problem code and a multi-agent self-review system for ultrasonic simulation, both of which the authors describe as domain-specific and requiring agents to manually correct each other. MCP-SIM's claimed advance relative to that landscape is generality across multiple physics domains within one architecture and full automation of the clarify-build-execute-diagnose-explain cycle without manual agent-to-agent correction, though neither of these two most directly comparable prior systems is run head-to-head against MCP-SIM in this paper; the comparison instead uses three ablated variants of MCP-SIM's own pipeline. The broader multi-agent architecture is explicitly inspired by multi-agent reinforcement learning successes outside physics (StarCraft II, turbulent-flow wall modeling) and by a separate bioinspired multi-agent scientific-discovery system (SciAgents), rather than by a shared benchmark or evaluation convention specific to physics-simulation agents, reflecting how early and fragmented this specific sub-area still is.

## Critical discussion

The ablation design (B1 through B3 as progressively more automated variants of the same underlying pipeline) is well suited to its actual purpose, isolating which components of MCP-SIM contribute to the reported gains, and it does that cleanly: automating clarification helps, automating diagnosis helps further, and removing the human review step entirely while adding persistent memory helps most. What this ablation does not establish is that MCP-SIM outperforms the field of physics-simulation multi-agent systems, since the two most directly comparable prior systems the paper itself cites (the two-agent elasticity self-correction system and the ultrasonic-simulation multi-agent self-review system) are described narratively as more limited but are never run on the same twelve tasks; the reported 12/12 versus 6/12, 8/12, and 10/12 comparison is a comparison against weakened versions of this same architecture, not against a competing published system (weak-baseline).

The benchmark itself is authored, curated, and graded by the same team that built the system being evaluated, with no external or independently constructed test suite, and the paper is candid that this is a limitation of the current evaluation rather than a claim of broader validation. The headline "12/12 success" metric is a numerical-convergence and (loosely specified) plausibility criterion, not a demonstrated correctness-of-physics criterion, except in the one case checked against an independent computational reference (ABAQUS, Level 12), and even there the comparison is reported only qualitatively as visual agreement in crack initiation and growth direction, without a quantitative discrepancy metric the reader could use to judge how close "close agreement" actually is (incomplete-reporting). Because a numerically converged solution can still rest on an incorrect or unintended choice of geometry, boundary condition, or governing equation for a genuinely ambiguous prompt, the residual-threshold criterion used for the other eleven tasks verifies self-consistency of whatever model the system inferred rather than correctness of that inference against the user's actual intent, a distinction the paper does not draw explicitly. The evaluation also uses a single backbone model (GPT-4o) throughout, so it is untested whether the reported gains are a property of the multi-agent architecture generally or specific to that model's particular capabilities and failure modes.

What remains well supported after these caveats: within this specific twelve-task, single-backbone, self-authored benchmark, full automation of the clarify-build-execute-diagnose-explain loop with persistent shared memory does outperform one-shot and partially human-mediated variants of the same pipeline on both success rate and correction efficiency, and the qualitative demonstration that a single, fully unspecified sentence can be turned into a plausible, numerically convergent phase-field fracture model is a genuine and specific capability result, even if its precision is not quantified. The authors' own stated limitations (no domain-specific fine-tuning, added latency from the reflective loop, a curated synthetic benchmark rather than experimental or safety-critical settings, and untested long-horizon stability) are honest and match what the evaluation as described can and cannot support.

## Relevance to us

This is one of the closest prior-art matches to our own direction reviewed so far: a memory-coordinated, self-correcting multi-agent system built around a real physics solver backend is structurally similar to what B02 (a physics-attuned backbone plus a durable train/eval/verify pipeline) and B09 (a long-lived, inspectable research runtime) describe, applied here to finite-element simulation rather than open-ended derivation or conjecture. Two mechanisms are worth taking seriously as transferable design choices: using a deterministic, solver-computed residual as the trigger for revision rather than an LLM's self-judgment, directly aligned with our own preference (stated in VERIFICATION.md) for verdicts from a deterministic procedure over an LLM acting as judge, and using persistent, structured memory of specifically which error was fixed by which correction, rather than a raw context window, to avoid repeating failed attempts, which is a concrete instance of the lab-notebook-style memory in our own Arc 4. At the same time, this paper is a useful illustration of a gap in the current state of the art that we should not reproduce: its convergence check verifies that the model the system inferred is numerically self-consistent, not that it is the model the user actually intended, which is exactly the family-assignment and problem-formulation bottleneck our own PVRE-line work has already run into (family assignment, not the oracle math, tends to be the harder problem). A system whose only verification is downstream numerical convergence can converge cleanly on a wrong physical setup for an ambiguous prompt, so any comparable component we build should pair the deterministic convergence check here with an explicit check, or at least a flagged assumption, that the inferred problem formulation matches the stated or implied intent, not only that the resulting equations were solved consistently. The paper's self-authored, non-adversarial benchmark and its lack of a head-to-head comparison against the two directly competing multi-agent physics-simulation systems it cites are also a specific, worth-noting instance of the missing-strong-baseline pattern we try to avoid under B01.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| memory coordinated multi agent self correction loop | success rate versus one-shot and human-in-the-loop baselines | improves | 0.75 | papers/canonical/2026-06-09/25mcpsim.md:L32 | MCP-SIM solves 12 of 12 benchmark tasks versus 6, 8, and 10 of 12 for progressively more automated baselines |
| persistent shared memory of error fix history | convergence efficiency in Plan Act Reflect Revise cycles | improves | 0.6 | papers/canonical/2026-06-09/25mcpsim.md:L32 | History-aware correction lets MCP-SIM converge within five or fewer cycles on most tasks |
| numerical solver residual threshold | trigger for the error diagnosis reflect revise loop | uses | 0.7 | papers/canonical/2026-06-09/25mcpsim.md:L31 | A dimensionless residual below 10 to the minus 4, not an LLM judgment, defines numerical convergence and success |
| MCP-SIM autonomously generated crack propagation simulation | ABAQUS reference crack propagation simulation | evaluates | 0.5 | papers/canonical/2026-06-09/25mcpsim.md:L41 | Visual comparison shows agreement in crack initiation and growth direction, reported qualitatively without a quantitative discrepancy metric |
