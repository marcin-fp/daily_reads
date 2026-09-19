---
schema_version: 1
paper: slug:25debate
title: "DEBATE: A Large-Scale Benchmark for Role-Playing LLM Agents in Multi-Agent, Long-Form Debates"
authors:
  - Yun-Shiuan Chuang
  - Ruixuan Tu
  - Chengtao Dai
  - Smit Vasani
  - Binwei Yao
  - Michael Henry Tessler
  - Sijia Yang
  - Dhavan Shah
  - Robert Hawkins
  - Junjie Hu
  - Timothy T. Rogers
publication:
  first_public_date: "2025-10-29"
  first_public_date_precision: day
  venue: "NeurIPS 2025 Workshop: Scaling Environments for Agents (SEA)"
  status: workshop
  reviewed_version: v1
  reviewed_version_date: "2025-10-29"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-06-09/25debate.md
raw: papers/raw/2026-06-09/25debate-pdf.md
source_url: https://arxiv.org/abs/2510.25110
organizations:
  - name: University of Wisconsin-Madison
    sector: academia
    roles: [author_affiliation, funder]
    authors: [Yun-Shiuan Chuang, Ruixuan Tu, Chengtao Dai, Smit Vasani, Binwei Yao, Sijia Yang, Dhavan Shah, Junjie Hu, Timothy T. Rogers]
    grants: []
  - name: Stanford University
    sector: academia
    roles: [author_affiliation]
    authors: [Robert Hawkins]
    grants: []
  - name: Google DeepMind
    sector: industry
    roles: [author_affiliation]
    authors: [Michael Henry Tessler]
    grants: []
  - name: U.S. Department of Defense
    sector: government
    roles: [funder]
    authors: [Timothy T. Rogers]
    grants: ["W911NF2110317"]
artifacts: []
facets:
  domains: [machine-learning, natural-language-processing, computational-social-science]
  paper_type: [benchmark, dataset, experiment]
  methods: [role-playing-llm-agents, multi-agent-simulation, supervised-fine-tuning, llm-as-judge]
  models: [gpt-4o-mini, Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct, Llama-3.1-Tulu-3-8B-SFT, Mistral-7B-Instruct-v0.3, Qwen2.5-32B-Instruct]
  benchmarks: [DEBATE]
assessment:
  extract_quality: partial
  extract_limitations: [figures-not-visually-assessed, equations-damaged]
  critical_flags: [same-family-judge, narrow-evaluation]
metadata_notes: "The extracted text (29,417 messages, 107 topics) matches the arXiv v1 submission (2510.25110, 2025-10-29); later revisions of this paper expanded the dataset to 37,357 messages, which is not reflected in the reviewed content, so reviewed_version is set to v1 rather than a later version. The Depth dataset is described as containing scientific-consensus 'ground truth' topics, including at least one topic the paper itself characterizes as a false claim (astrology-adjacent); this framing is the paper's own and is preserved as such rather than adopted as this review's judgment. The dataset is described as being released upon acceptance with no URL given in the extracted text, so no data artifact entry is created here. The raw extraction of this file contains a short block of clearly out-of-place, unrelated text partway through the appendix (referencing a LaTeX 'Advantage (GAE) Computation' insert) that has nothing to do with this paper's content; it appears to be a PDF-extraction artifact and was disregarded when writing this review."
---

Citation: Chuang, Y.-S., Tu, R., Dai, C., Vasani, S., Yao, B., Tessler, M. H., Yang, S., Shah, D., Hawkins, R., Hu, J., and Rogers, T. T. DEBATE: A Large-Scale Benchmark for Role-Playing LLM Agents in Multi-Agent, Long-Form Debates. NeurIPS 2025 Workshop on Scaling Environments for Agents (SEA).

## What this paper is about

If a language model role-plays as a specific person and is dropped into a multi-round group conversation with other role-playing agents, does the resulting group behave like the real group of humans it is supposed to represent? Prior work had already noticed that individually convincing role-playing agents can produce strange group behavior, such as everyone's opinions collapsing toward agreement too quickly, but lacked a large, naturalistic benchmark to measure this against real human data. This paper builds one: a dataset of thousands of real people debating controversial topics in small groups, with both their public tweet-like messages and their privately reported opinions recorded over time, and uses it to test how well LLM "digital twins" of those same people reproduce the real humans' conversational behavior and opinion trajectories.

## Extended summary

The DEBATE dataset was collected from 2,792 U.S.-based Prolific participants, organized into 797 four-person groups, each assigned one of 107 controversial discussion topics and IRB-approved compensation of $10/hour. Each group session follows four phases: participants report an initial opinion on a 6-point Likert scale with a free-text justification; they complete three rounds of dyadic conversation, rotating partners each round so every participant interacts with every other group member exactly once, writing a public tweet-like message and then holding a private two-person conversation each round; they report a final opinion and justification; and they complete a demographic survey. Two topic sets are used: a Depth set of seven topics tied to an established scientific consensus (used to test whether agents drift toward or away from the "correct" view), assigned to an average of 26.43 groups each, and a Breadth set of 100 topics drawn from the World Values Survey and Pew Global Attitudes Survey with no ground-truth answer, assigned to an average of 6.12 groups each. The resulting reviewed version of the dataset totals 29,417 messages.

Role-playing LLM "digital twin" agents are conditioned on a memory module containing the corresponding participant's demographics, initial opinion and justification, initial tweet, and the conversational history so far. Three simulation modes vary only in whether that conversational history comes from real human data or from the model's own prior generations: Mode 1 (Next Message Prediction) conditions on real human tweets and conversations throughout and predicts only the next utterance; Mode 2 (Tweet-guided Conversation Simulation) keeps real human tweets but simulates the private conversations; Mode 3 (Full Conversation Simulation) simulates both tweets and conversations recursively from only the initial human-reported opinion onward, mirroring a classic opinion-dynamics simulation setup. Evaluation is restricted to on-topic utterances and uses semantic similarity (cosine similarity of sentence embeddings), stance difference (absolute difference in scalar stance scores on the 6-point scale), signed and absolute length difference, ROUGE-L, and on-topic rate; stance scores and topic-relevance judgments throughout are produced automatically by gpt-4o-mini, which the authors state was validated against human annotations in an appendix not detailed in the extracted text. Six models are compared: gpt-4o-mini, Llama-3.1-Tulu-3-8B-SFT, Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct, Mistral-7B-Instruct-v0.3, and Qwen2.5-32B-Instruct.

Across both topic sets, gpt-4o-mini shows the strongest alignment on semantic similarity, ROUGE-L, and stance difference, confirmed by a Friedman test followed by Wilcoxon signed-rank tests across six experimental settings, though it produces systematically longer messages than the humans it simulates. Alignment consistently degrades from Mode 1 to Mode 2 to Mode 3, meaning more real human context in memory produces better behavioral alignment and increasing reliance on the model's own generated history makes alignment worse. An ablation on gpt-4o-mini over the Depth topics shows that in Mode 1, where real conversation history is fully available, removing prior chats or private profile information barely changes alignment, but in Modes 2 and 3, where history is recursively simulated, removing private-profile information (demographics and initial opinion) consistently degrades both semantic similarity and stance alignment.

A second analysis, restricted to the Depth topics, Simulation Mode 3, and gpt-4o-mini, compares group-level opinion trajectories between each human group and its LLM-simulated counterpart using paired t-tests. LLM groups show a significant increase in average public tweet stance from round 1 to round 3 (t(30) = 2.23, p = .03), drifting toward endorsing the Depth topics' non-consensus claims, while human groups show no significant change (t(30) = -0.55, p = .59), and the difference between the two trends is itself significant (t(30) = 2.66, p = .01). LLM groups also show a significant reduction in the standard deviation of tweet stance across rounds (t(30) = -2.27, p = .03, indicating within-group convergence), which human groups do not show (t(30) = 0.02, p = .98), with the difference again significant. The same pattern holds for privately reported opinions: neither LLM nor human groups show a significant average shift, but LLM groups show a significant reduction in opinion standard deviation (t(30) = -4.65 in the main text, though the corresponding figure caption reports t(30) = -4.19 for the apparently same comparison) while human groups show none. Individual-level analysis finds that both humans and LLM agents show regression toward the midpoint for extreme initial stances and a directional shift toward their first conversational partner's stance, with a control (absolute rather than directional distance to the partner) showing no effect for either group, but the LLM correlations are consistently stronger than the human correlations for both effects across public tweets and private opinions (for example, partner-influence correlation on tweet stance is r = 0.50 for LLM agents versus r = 0.38 for humans).

Finally, a supervised fine-tuning experiment on gpt-4o-mini and Llama-3.1-8B-Instruct, evaluated under round, group, and topic held-out generalization settings, finds that fine-tuning on real human conversational data consistently improves surface-level alignment metrics (message length moving closer to human length, ROUGE-L increasing) but simultaneously reduces semantic similarity and increases stance difference, including on the training partition itself in several settings, which the authors read as evidence that the fine-tuning induces surface-form mimicry rather than genuine behavioral or opinion alignment.

## Learnings

How much a role-playing agent needs private grounding information (a participant's stated demographics and initial opinion) about the person it simulates is not fixed; it depends on how much real external context the model otherwise has access to. When real human conversation history is available in the prompt, removing private grounding barely changes alignment, but once the model must generate its own conversational trajectory recursively with no further real human text to lean on, removing that same private information reliably degrades alignment. This is a transferable design point for any persona-conditioned or digital-twin simulation: grounding data earns its keep specifically at the point where the model starts compounding on its own prior outputs.

Fine-tuning a role-playing agent on real human conversational data can make its outputs look more human by surface metrics (length, lexical overlap via ROUGE-L) while making its actual stance behavior and semantic content less aligned with the humans it is meant to model, even measured on the model's own training data. Surface-mimicry metrics and deeper content-alignment metrics can move in opposite directions under the same fine-tuning procedure, so an evaluation that only reports surface metrics could hide this trade-off entirely.

LLM agents simulating a group conversation exhibited the same qualitative social-influence mechanisms as the real humans they modeled, regression toward the midpoint for extreme initial opinions and a directional shift toward a conversational partner's stance, but with substantially larger magnitude for the LLM agents on every comparison reported. The mechanism is not invented by the simulation; its strength is inflated, which is a useful pattern to check for in any LLM-based behavioral simulation: does the human tendency exist at all, and if so, by how much is the model's version of it exaggerated.

## Verification

Verification is a minor thread in this paper, present mainly as validation of an automated annotator rather than as a check on the truth or consistency of what the agents say. Stance scores and topic-relevance labels, which every headline alignment metric in the paper depends on, are produced automatically by gpt-4o-mini and are stated to have been validated against human annotations, though the extracted main text does not report the resulting agreement statistic. Because gpt-4o-mini is simultaneously the automated judge scoring every model's utterances and one of the six models being scored, including its own, this is a same-family-judge situation that the stated (but not detailed here) human validation only partially addresses. Beyond that, the paper does not check whether an agent's generated opinions are internally consistent with its assigned persona, and it does not attempt anything like a confabulation or factuality check; the entire evaluation is behavioral similarity to a real recorded human trajectory, not a correctness check against an independent ground truth about the agent's own reasoning.

## Field context

This paper builds directly on the authors' own earlier work simulating opinion dynamics with networks of LLM-based agents and on aligning role-playing agents using human belief networks, both of which had already observed the premature-convergence problem this benchmark is designed to measure at scale with real, paired public and private human data. It responds to a literature that mostly evaluated role-playing LLM agents either in single-agent settings without interaction or on artificial, non-linguistic tasks such as numeric guesstimation, by contributing the first large empirical, multi-agent, naturalistic-topic benchmark with a real human ground truth for opinion trajectories. The paper is careful to distinguish itself from the separate multi-agent-debate literature aimed at boosting task performance (improving reasoning accuracy or factuality through agent critique, as in Du et al. and related work, examined critically in this corpus's review of 24selfcor), noting that this prior work uses debate as a performance technique rather than a test of authentic human-like social dynamics; the phrase "multi-agent debate" spans two largely unrelated research goals, and this paper belongs to the social-simulation-fidelity branch rather than the performance-boosting branch. Within this corpus, its central finding, that LLM groups converge and drift in specific, measurable, and consistent directions relative to the human groups they are meant to represent, adds a concrete data point to the broader recurring theme that LLM behavioral tendencies can look superficially human-like while diverging from human ground truth in systematic ways.

## Critical discussion

The benchmark's central design choice, pairing public tweet-like messages with privately reported Likert opinions from the same real participants across time, and separating a ground-truth Depth topic set from a values-based Breadth topic set, is a genuinely useful evaluation structure. It lets the authors separate "does the agent sound like the person" (semantic similarity, ROUGE-L) from "does the agent's opinion trajectory track the person's opinion trajectory" (stance difference, group-level convergence and drift), a distinction most prior role-play evaluations collapse into a single similarity score.

Every headline stance-alignment number in Section 5 depends on labels produced by gpt-4o-mini, which is also the single best-performing model in the same evaluation and one of the six models whose outputs those labels score, including its own. The paper states this labeling was validated against human annotations, but the extracted main text does not report the resulting agreement rate, so a reader cannot independently judge how much of gpt-4o-mini's reported lead in stance alignment might be inflated by its own labels tracking its own phrasing more easily than a genuinely different model's outputs. The paper's most striking claims, that LLM groups converge and drift toward the Depth topics' non-consensus claims more than human groups, and that LLM agents show exaggerated regression-to-mean and partner-influence effects, are demonstrated only on the seven-topic Depth subset, only in Simulation Mode 3, and only using gpt-4o-mini, the single best-aligned model at the utterance level. It remains untested in this paper whether the other five, less-aligned models would reproduce the same dynamical pattern, or whether Breadth topics, which have no ground-truth position for an agent to drift toward, would show comparable convergence. The paper's framing implies a general property of role-playing LLM agents, but the dynamical evidence for that claim currently rests on one model, one topic subset, and one simulation mode. Two of the paper's own reported statistics also show small internal inconsistencies between the main text and the corresponding figure caption for what appears to be the same comparison (a tweet-stance standard-deviation difference reported as t(30) = -2.28 in text versus t(30) = -2.38 in the figure caption, and a self-reported-opinion standard-deviation difference reported as t(30) = -4.19 in text versus t(30) = -4.65 in the caption); both directions remain significant either way, so the qualitative conclusion is not threatened, but the exact magnitudes carry a small unresolved discrepancy between the two places they are reported. The supervised fine-tuning result is a well-earned negative finding rather than a simple null result: SFT does not merely fail to help, it specifically improves surface-level metrics while making semantic and stance alignment worse, including on the training partition in several configurations, pointing at a genuine failure mode (surface mimicry substituting for content alignment) rather than an absence of effect.

What remains well supported after these caveats: the finding that behavioral alignment degrades as an agent's memory relies more on its own generated history and less on real human context (Mode 1 > Mode 2 > Mode 3) holds across both topic sets and all six models under nonparametric significance testing, making it the paper's most broadly supported result, and the associated private-grounding ablation is consistent within its Depth-topic scope. The group- and individual-level opinion-dynamics findings are real, carefully instrumented results for the specific model, mode, and topic subset tested, but their generality across the other five models and across topics without a ground-truth answer remains an open question the paper itself has not yet closed.

## Relevance to us

The direct subject matter here, human opinion dynamics and social debate authenticity, is largely not our problem, and this review says so plainly rather than forcing a connection. One mechanism does transfer usefully, however: the finding that a persona- or context-grounded agent's dependence on injected private information is not fixed but grows sharply once the agent starts generating its own trajectory recursively rather than leaning on fresh external data. This is directly relevant to any long-horizon or multi-day research session we build, where a model increasingly reasons over its own prior generated content (derivation steps, assumption choices, prior conclusions) rather than fresh ground truth; this paper's result suggests that exactly this transition point, where an agent's context becomes dominated by its own outputs, is where grounding information (an assumption ledger, a scientist's stated preferences, prior verified derivation state) is likely to matter most for staying on track, and where unchecked drift is most likely to compound, in the same spirit as the opinion convergence and drift this paper documents. Beyond that specific, narrowly scoped mechanism, the paper's substantive results about human social behavior and role-play fidelity do not bear on our physics-reasoning work.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| role playing LLM agents in recursive simulation | opinion convergence relative to human groups | contradicts | 0.75 | papers/canonical/2026-06-09/25debate.md:L284 | LLM groups show significantly stronger convergence in both public tweet stance and private opinion than the human groups they simulate |
| recursively simulated conversation history without real human text | importance of private profile grounding for alignment | implies | 0.7 | papers/canonical/2026-06-09/25debate.md:L196 | Removing private profile information degrades alignment specifically in Modes 2 and 3, not in Mode 1 |
| more human grounded context in agent memory | utterance level behavioral alignment with humans | improves | 0.8 | papers/canonical/2026-06-09/25debate.md:L178 | Alignment consistently declines from Mode 1 to Mode 2 to Mode 3 across models and topic sets |
| supervised fine tuning on human conversational data | semantic similarity and stance alignment | contradicts | 0.7 | papers/canonical/2026-06-09/25debate.md:L729 | SFT improves surface metrics but reduces semantic similarity and increases stance difference, even on training data |
| role playing LLM agents | susceptibility to partner opinion influence relative to humans | implies | 0.65 | papers/canonical/2026-06-09/25debate.md:L333 | Partner-influence correlations are consistently stronger for LLM agents than for humans on both tweet stance and private opinion |
