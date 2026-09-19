---
schema_version: 1
paper: slug:26cosci
title: "Accelerating scientific discovery with Co-Scientist"
authors:
  - Juraj Gottweis
  - Wei-Hung Weng
  - Alexander Daryin
  - Tao Tu
  - Petar Sirkovic
  - Artiom Myaskovsky
  - Grzegorz Glowaty
  - Felix Weissenberger
  - Alessio Orlandi
  - Dan Popovici
  - Anil Palepu
  - Keran Rong
  - Ryutaro Tanno
  - Khaled Saab
  - Fan Zhang
  - Jacob Blum
  - Andrew Carroll
  - Kavita Kulkarni
  - Nenad Tomašev
  - Dina Zverinski
  - Ivor Rendulic
  - Elahe Vedadi
  - Florian Hasler
  - Luka Rimanic
  - Marina Boia
  - Ivan Budiselic
  - Ben Feinstein
  - Mathias Bellaiche
  - Tom Sheffer
  - Jan Freyberg
  - Jeremy Ratcliff
  - Ottavia Bertolli
  - Katherine Chou
  - Avinatan Hassidim
  - Burak Gokturk
  - Amin Vahdat
  - Yuan Guan
  - Vikram Dhillon
  - Eeshit Dhaval Vaishnav
  - Byron Lee
  - Tiago R D Costa
  - José R Penadés
  - Gary Peltz
  - Yossi Matias
  - James Manyika
  - Demis Hassabis
  - Yunhan Xu
  - Pushmeet Kohli
  - Annalisa Pawlosky
  - Alan Karthikesalingam
  - Vivek Natarajan
publication:
  first_public_date: "2025-02-26"
  first_public_date_precision: day
  venue: Nature
  status: journal
  reviewed_version: "Accelerated Article Preview"
  reviewed_version_date: "2026-05-19"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/26cosci.md
raw: papers/raw/2026-05-06/26cosci-pdf.md
source_url: https://doi.org/10.1038/s41586-026-10644-y
organizations:
  - name: Google Cloud AI Research, Zurich
    sector: industry
    roles: [author_affiliation]
    authors: [Juraj Gottweis, Alexander Daryin, Petar Sirkovic, Artiom Myaskovsky, Grzegorz Glowaty, Felix Weissenberger, Alessio Orlandi, Dina Zverinski, Ivor Rendulic, Florian Hasler, Luka Rimanic, Marina Boia, Ivan Budiselic, Burak Gokturk, Amin Vahdat]
    grants: []
  - name: Google DeepMind, Mountain View
    sector: industry
    roles: [author_affiliation]
    authors: [Wei-Hung Weng, Tao Tu, Keran Rong, Ryutaro Tanno, Khaled Saab, Nenad Tomašev, Elahe Vedadi, Jan Freyberg, Jeremy Ratcliff, Ottavia Bertolli, Demis Hassabis, Yunhan Xu, Pushmeet Kohli, Alan Karthikesalingam, Vivek Natarajan]
    grants: []
  - name: Google Research, Mountain View
    sector: industry
    roles: [author_affiliation]
    authors: [Dan Popovici, Anil Palepu, Fan Zhang, Andrew Carroll, Kavita Kulkarni, Ben Feinstein, Mathias Bellaiche, Tom Sheffer, Katherine Chou, Avinatan Hassidim, Yossi Matias, James Manyika, Annalisa Pawlosky]
    grants: []
  - name: Stanford University School of Medicine
    sector: academia
    roles: [author_affiliation]
    authors: [Jacob Blum, Yuan Guan, Gary Peltz]
    grants: []
  - name: Houston Methodist
    sector: nonprofit
    roles: [author_affiliation]
    authors: [Vikram Dhillon]
    grants: []
  - name: Sequome
    sector: industry
    roles: [author_affiliation]
    authors: [Eeshit Dhaval Vaishnav, Byron Lee]
    grants: []
  - name: Fleming Initiative and Imperial College London
    sector: academia
    roles: [author_affiliation]
    authors: [Tiago R D Costa, José R Penadés]
    grants: []
  - name: Alphabet Inc
    sector: industry
    roles: [funder]
    authors: []
    grants: []
  - name: National Institutes of Health
    sector: government
    roles: [funder]
    authors: [Gary Peltz]
    grants: ["1R01DC021133", "1R24OD035408"]
artifacts: []
facets:
  domains: [machine-learning, biomedicine, oncology, microbiology]
  paper_type: [system, experiment]
  methods: [multi-agent-llm, elo-tournament, self-play-debate, test-time-compute-scaling, retrieval-augmented-critique]
  models: [Gemini-2.0-Pro, Gemini-2.0-Flash-Thinking, OpenAI-o1, OpenAI-o3-mini, DeepSeek-R1]
  benchmarks: [GPQA-diamond, DepMap]
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: [same-family-judge, narrow-evaluation]
metadata_notes: "This paper first appeared as arXiv:2502.18864 under the title 'Towards an AI co-scientist' (v1 submitted 2025-02-26); v2 of that same arXiv entry was retitled 'Accelerating scientific discovery with Co-Scientist', matching this Nature paper exactly, confirming continuity. Web search corroborates the Accelerated Article Preview went online 2026-05-19 (the same day as the companion ERA paper reviewed elsewhere in this corpus, reviews/26empsw.md) and the paper appears in print as Nature 655, 487-496 (2026); the source text left the online-publication date as an unfilled placeholder ('Published online xx xx xxxx'). The Competing Interest Declaration states the study was funded by Alphabet Inc, that most authors are Alphabet employees who may hold stock, and separately that two authors (E.D.V., B.L.) are employees of Sequome and that B.L. is the founder of a private company, Dendra Therapeutics — a disclosed financial interest adjacent to the drug-repurposing and target-discovery findings reported. The full Co-Scientist source code is explicitly not released (cited reasons: proprietary infrastructure, compute cost, safety concerns about unmonitored agentic use); only pseudocode and prompts are provided in supplementary material not captured in this extract, so no code/data artifact is listed above."
---

Citation: Gottweis, J. et al. Accelerating scientific discovery with Co-Scientist. Nature 655, 487-496 (2026). https://doi.org/10.1038/s41586-026-10644-y

## What this paper is about

Scientists face a tension between needing deep expertise in a narrow area and needing broad cross-disciplinary knowledge to make creative leaps, while the volume of literature keeps growing. This paper introduces Co-Scientist, a Google system built on Gemini that acts as a research collaborator: given a research goal in plain language, it searches and reasons over relevant literature, then generates, debates, and iteratively refines novel, testable scientific hypotheses, functioning as a "scientist-in-the-loop" tool rather than a fully autonomous one. The paper's central claims are twofold: that letting the system "think" longer (more test-time compute, structured as a tournament of competing and evolving hypotheses) measurably improves the hypotheses it produces, and that hypotheses it generated led to real, wet-lab-validated findings in three biomedical areas — new drug-repurposing candidates and drug combinations for acute myeloid leukemia, novel therapeutic targets for liver fibrosis, and an independently-arrived-at mechanistic explanation for how a class of mobile genetic elements spreads antimicrobial resistance across bacterial species.

## Extended summary

Co-Scientist is a multi-agent system built on Gemini 2.0 models, coordinated by a Supervisor agent that assigns work to specialized worker agents running asynchronously: a Generation agent (produces initial hypotheses via literature search, synthesis, and simulated debate), a Reflection agent (critiques hypotheses for plausibility and novelty, acting as a simulated peer reviewer, with access to external search), a Ranking agent (runs an Elo-based tournament of pairwise, debate-mediated hypothesis comparisons), a Proximity agent (clusters and de-duplicates similar hypotheses), an Evolution agent (refines top-ranked hypotheses by combining ideas, analogy, or simplification, always generating new candidates rather than overwriting old ones), and a Meta-review agent (synthesizes patterns across all reviews and debates into feedback appended to other agents' prompts — the paper's stated mechanism for "learning" without gradient-based fine-tuning or RL). A persistent context memory supports long-horizon iterative computation. Scientists interact throughout via natural language: specifying the goal and constraints, contributing their own candidate hypotheses into the same tournament, and reviewing a final ranked list and synthesized "research overview." The authors report that setup for their three real-world validations took under an hour of expert time each, with final review of results taking roughly three hours.

Ablation studies (Supplementary Note 3, summarized in the main text) quantify several component contributions using two kinds of scoring: the objective, ground-truth GPQA-diamond multiple-choice benchmark, and an internal "auto-evaluation" score with no external ground truth. On a constructed dataset of already-published ideas that should score as non-novel, the Reflection agent without search tools incorrectly rated them 6.14/10 novel on average; with search access, it correctly rated them 2.38/10. The same search access raised average correctness auto-evaluation from 7.4 to 8.46/10 on known-correct ideas, and raised GPQA AUC for predicting a correct solution from 0.643 to 0.651 (using Gemini 2.0 Flash as the base LLM). Using a scientific-debate prompt rather than a simple comparison prompt in the Ranking agent reduced positional bias and improved ranking accuracy (not further quantified in this extract). The Evolution agent's iterative refinement raised GPQA precision from 70.9% to 75.4% and an internal hypothesis-quality auto-evaluation score from 4.7 to 5.6. The Meta-review agent raised AUC for predicting a correct solution from 0.521 to 0.597 on the constructed dataset and from 0.629 to 0.634 on GPQA diamond.

The paper's central "test-time compute scaling" result (Fig. 2a) tracks the Elo rating of Co-Scientist's own generated hypotheses across ten sequential time buckets of its own tournament computation, averaged over 203 distinct research goals (predominantly biomedical, with some mathematics and physics goals) submitted by February 3, 2025; both the average top-10 Elo and the single best Elo increase steadily with no observed saturation. On a curated subset of 15 especially challenging biomedical research goals (defined by seven domain experts, each providing their own "best guess" solution), the same trend held, and Co-Scientist's Elo rating eventually surpassed that of several other frontier models entered into the same tournament — Gemini 2.0 Pro Experimental, Gemini 2.0 Flash Thinking Experimental, OpenAI o1, OpenAI o3-mini-high, and DeepSeek R1 — with newer reasoning models (o3-mini-high, DeepSeek R1) noted as competitive despite using much less compute. Iteratively refining the experts' own "best guess" solutions with the same tournament process also raised their Elo over time, eventually surpassing Co-Scientist's self-generated solutions, which the authors describe as a preliminary finding suggesting human-AI collaborative refinement as a further direction. A separate, blinded evaluation asked the same seven experts to rank (1 = most preferred, 4 = least) and rate the novelty and impact (1-5 Likert) of outputs from Co-Scientist, Gemini 2.0 Flash Thinking Experimental, Gemini 2.0 Pro Experimental, and OpenAI o1 across 11 of the 15 goals: Co-Scientist received the best average preference rank (2.36) and the highest novelty (3.64/5) and impact (3.09/5) ratings. A further preference-ranking evaluation used four different LLMs as judges (OpenAI o3-mini, o1-preview, Gemini 2.0 Pro Experimental, Gemini 2.0 Flash Thinking Experimental) across all 15 goals; all four preferred Co-Scientist's outputs, though the authors note the small scale limits how much can be concluded.

The three "real-world validations" are the paper's most concrete evidence. For AML drug repurposing, Co-Scientist was constrained to a list of 2,300 approved drugs across 34 cancer types; after oncologist review, five candidates (Binimetinib, Pacritinib, Cerivastatin, Pravastatin, Dimethyl fumarate) were tested in vitro across four AML cell lines and one non-AML control line, with Binimetinib, Pacritinib, and Cerivastatin showing dose-dependent inhibition of cell viability (Binimetinib's IC50 as low as 2 nM in most AML lines, much higher in the non-AML control). In a second, less-supervised run (no external database inputs, no prior preclinical evidence allowed), Co-Scientist proposed novel single-agent candidates; of three tested (Nanvuranlat, KIRA6, Leflunomide), KIRA6 (an IRE1α inhibitor) showed selective cytotoxicity, with an 18-fold IC50 separation between the most sensitive AML line (KG-1a, 10 nM) and the non-AML control (180 nM), though two other AML lines were far less sensitive (IC50s of 1,750 nM and 870 nM). Co-Scientist-proposed drug combinations were also tested for synergy (Chou-Talalay combination-index and HSA/Bliss independence models) across seven regimens in two AML cell lines, with predominantly synergistic responses in one line and mixed synergy/antagonism in a second, more chemoresistant (TP53-mutant) line; all wet-lab work used n=3 biologically independent replicates, was not blinded (standardized automated plate-reader assays), and the authors explicitly frame these as a preliminary "biological reality check," not a substitute for pre-clinical or clinical validation. For liver fibrosis, Co-Scientist proposed epigenetic targets and drugs against them in a human hepatic-organoid model; two of three top-ranked, expert-selected candidates showed anti-fibrotic activity without toxicity, including one (Vorinostat) already FDA-approved for a different indication. For antimicrobial resistance, a research group asked Co-Scientist to hypothesize how capsid-forming phage-inducible chromosomal islands (cf-PICIs) achieve broad host range across bacterial species — a mechanism that group had already discovered experimentally but not yet published; with only minimal background information, Co-Scientist proposed, within two days, that cf-PICIs interact with diverse phage tails to expand host range, matching the group's own unpublished finding, which was published essentially simultaneously in a companion paper (co-authored by two of this paper's authors, who are domain experts from the group that made the original discovery).

The Statistics and Reproducibility section states no statistical methods were used to predetermine sample sizes (203/15/11 research goals were chosen for "robust statistical averaging"; n=3 biological replicates for in vitro assays followed standard practice for preliminary dose-response screening); the human expert preference/novelty/impact evaluation was explicitly blinded to which model produced each output, while the automated plate-reader viability assays did not require blinding. The Discussion explicitly lists limitations: literature access constrained to open-access sources (missing paywalled prior art and negative results); hypothesis quality inherits errors from mixed-quality source literature, with a stated future direction of adding provenance-tracing to specific figures/data; inherited factuality/hallucination limitations from the underlying LLM; and a general risk that AI-assisted ideation could homogenize research directions or, if used without rigorous peer review, worsen the reproducibility crisis by producing low-quality scientific artifacts at scale. The full Co-Scientist source code is not publicly released; the authors describe an experimental access program for interested scientists instead, citing proprietary infrastructure, compute cost, and safety concerns about unmonitored autonomous use.

## Learnings

Giving a critique/reflection step access to external search, rather than relying only on the model's own internal knowledge, produced a specific, quantified reduction in a checkable failure mode: on a set of already-published ideas that should be rated as non-novel, the same agent scored them 6.14/10 novel without search and 2.38/10 with it. This is a concrete demonstration that grounding self-critique in retrieval measurably reduces a particular kind of hallucination (false novelty), not just a general claim that "search helps."

A system's own internal tournament ranking (here, an Elo score computed via debate-mediated pairwise comparisons judged by the same LLM family that generates the candidates) can show a steady, unsaturating upward trend that looks exactly like genuine self-improvement, while the paper's own figure caption for this metric concedes it "is auto-evaluated and not based on independent ground truth." The honest disclosure is itself the useful thing to remember: an agent paper's self-play or tournament curve should be read as evidence of increasing self-consistency with the system's own judging criteria until cross-checked against an external or human standard, which this paper does only on much smaller subsets (15 and 11 goals) than the headline curve (203 goals).

A single, striking case of an AI system converging on the same explanation as an as-yet-unpublished experimental discovery is a qualitatively different, and weaker, form of evidence than it first appears once the roles of the people involved are made explicit: when the domain experts who hold the unpublished result also set the prompt, judge the output, and co-author the paper reporting the "recapitulation," the result is best read as evidence the system's reasoning is compatible with a known-correct answer under favorable framing, not as a blinded test of independent discovery — a distinction worth keeping in mind before citing this kind of anecdote as evidence of general discovery capability.

## Verification

Co-Scientist's evidence spans several tiers of verification strength, and it matters which tier a given headline claim rests on. The weakest tier is self-judged auto-evaluation: the central "test-time compute scaling improves hypothesis quality" claim (Fig. 2a, n=203 goals) is measured entirely by the system's own Elo tournament, adjudicated through debate prompts run on the same Gemini backbone that generates the hypotheses, with no independent ground truth (a limitation the paper's own Extended Data Fig. 1 caption states directly). A stronger but still LLM-mediated tier cross-checks Co-Scientist against four external LLM judges (Extended Data Fig. 2: OpenAI o3-mini, o1-preview, Gemini 2.0 Pro Experimental, Gemini 2.0 Flash Thinking Experimental) — two of the four judges share Co-Scientist's own model family. A stronger tier still is the blinded human expert preference/novelty/impact evaluation (Fig. 2c, n=11 goals), which is genuinely independent of the generating system, though small in scale and explicitly caveated by the authors as reflecting "subjective expert assessments, not objective ground truth." A separate, objective tier grounds some ablation numbers (Evolution- and Meta-review-agent contributions) in the GPQA-diamond benchmark, which has real correct/incorrect answers, making those specific numbers (e.g., 70.9%→75.4% precision) more solid than the auto-evaluation-only ablation numbers reported alongside them. The strongest tier by far is the real-world wet-lab validation: dose-response viability curves, IC50 estimation via non-linear regression, and drug-synergy quantification (Chou-Talalay combination index; HSA and Bliss independence models) against physical, external biological readouts, run in biological triplicate, though the authors are careful to describe this evidence as preliminary and insufficient for any clinical claim.

## Field context

This paper's system, "AI co-scientist," is not merely field-adjacent to other work in this corpus — it is a component directly cited and used by an already-reviewed paper here, [26empsw](26empsw.md) (Aygün et al., "An AI system to help scientists write expert-level empirical software," the ERA system), which used "Gemini Deep Research and AI co-scientist" as one of several idea-generation sources for its own tree-search-driven method discovery. ERA's own results give an independent, externally-scored (not self-judged) data point on how well AI-co-scientist-sourced ideas perform in practice once implemented and tested against deterministic community benchmarks: per ERA's own reporting, only 1 of 12 AI-co-scientist-derived methods for single-cell batch integration beat the OpenProblems leaderboard, and only 1 of the 14 winning COVID-19 forecasting strategies in ERA came from AI co-scientist (versus 10 from ERA's own idea-recombination mechanism). This is a genuinely useful, independently-collected data point this review can add that the Co-Scientist paper itself does not report: a separate team, using deterministic external scoring, found AI-co-scientist-sourced ideas a comparatively modest (not zero, but modest) source of winning solutions relative to other idea-generation strategies tested in the same study. Beyond this direct corpus link, the paper positions itself within test-time-compute-scaling literature (Snell et al. 2024), self-play/tournament game-playing traditions (AlphaZero, superhuman poker AI), and Elo rating methodology, explicitly citing a paper on Elo's known limitations under intransitive comparisons (Hamilton, Roughan & Kalenkova 2024) without directly addressing whether that concern applies to its own tournament. It is closely tied to two companion primary-research papers also referenced here (Guan et al. 2025 on liver fibrosis; Penadés et al./He et al. 2025 in Cell on the cf-PICI mechanism), both of which share authors with this paper.

## Critical discussion

The wet-lab validations are the paper's strongest evidence and should be weighted accordingly: real dose-response curves, IC50s consistent across the expected biological direction (lower in AML lines than the non-AML control for the most potent candidates), and drug-synergy analyses via established quantitative methods (Chou-Talalay, HSA, Bliss) are hard-to-fake, externally checkable results, even though the authors themselves correctly frame them as preliminary cell-line screens rather than clinical evidence.

The paper's central scaling claim rests on much weaker ground. Fig. 2a's "test-time compute improves hypothesis quality" curve is computed entirely from Co-Scientist's own Elo tournament, in which the same Gemini-based Ranking and Reflection agents that generate hypotheses also judge them via simulated debate — the textbook same-family-judge concern our own review framework tracks (a system's ranking function naturally favors what it already favors more, the longer it iterates against itself), and one the paper's own figure caption for a related metric explicitly concedes ("auto-evaluated and not based on independent ground truth"). The cross-validation against external LLM judges only partially mitigates this: two of the four external judges used are themselves Gemini-family models, sharing lineage with Co-Scientist's own backbone. The only genuinely independent check — blinded human expert preference — is real and positive (Co-Scientist rated best on preference, novelty, and impact), but it covers just 11 of the 203 research goals behind the headline scaling curve, so the strongest, largest-n claim in the paper is also the one with the weakest independent verification, while the smallest-n claim is the most independently verified.

The "beats frontier models" framing (Fig. 2b) compounds this concern rather than resolving it: pitting Co-Scientist's hypotheses against OpenAI o1, o3-mini-high, DeepSeek R1, and Gemini variants, then scoring the winner using Co-Scientist's own Elo tournament, is closer to a home-field advantage than a neutral bake-off — a competitor's hypothesis is judged by the debate norms and criteria Co-Scientist's own Ranking agent was built and tuned around. This does not mean Co-Scientist's hypotheses are not better; it means this specific comparison is not strong evidence of it, independent of the blinded human-preference result, which is smaller in scale but not subject to the same circularity.

The antimicrobial-resistance "recapitulation" is presented as one of the paper's most dramatic results, and the underlying scientific finding (published in a companion Cell paper) is real, but the independence of the AI demonstration itself is weaker than the framing suggests: the research group whose unpublished discovery is being "recapitulated" (Tiago R D Costa and José R Penadés, from the Fleming Initiative/Imperial College London) are co-authors on this very paper, meaning the people who set the prompt, supplied "minimal background information" of unspecified exact content, and judged whether Co-Scientist's output matched their own unpublished result are not disinterested third parties. This is disclosed implicitly through the author list and citations rather than flagged explicitly as a limitation of this specific case, and it is a single case (n=1) rather than a systematic test of how often such convergence occurs, so it should be read as a compelling existence proof under favorable conditions, not as a general capability estimate.

Two further, more minor points round out the picture: the full system's source code is not released, which is a reasonable and disclosed choice given the stated safety rationale, but it means no part of this paper's central architectural or Elo-tournament claims can be independently reproduced by outside researchers from what is provided (pseudocode and prompts, not runnable code); and one author (B.L.) is disclosed as the founder of a private therapeutics company, a conflict of interest that does not appear to have been separately walled off from the drug-repurposing and target-discovery portions of the study by any measure described in this extract.

What remains well supported after these caveats: Co-Scientist's literature-grounded, multi-agent hypothesis-generation pipeline produced genuinely testable candidates that showed real, physically verified biological activity in at least two of three validation domains (AML drug repurposing and combination therapy; liver fibrosis targets), which is a legitimate and useful result independent of how the self-improvement or model-comparison claims hold up. The specific, quantified finding that search-grounded critique reduces false novelty claims (6.14 to 2.38 on a known-non-novel test set) is a solid, narrow, well-evidenced result. The broader claims that iterative test-time compute reliably improves hypothesis quality in a way that generalizes beyond the system's own judging criteria, and that Co-Scientist demonstrably outperforms frontier reasoning models at this task, remain considerably less settled than the paper's framing suggests, pending genuinely independent, larger-scale evaluation.

## Relevance to us

This paper is close to a canonical, Nature-published instance of exactly the pattern our competitive-opening notes warn about: frontier backbone, multi-agent loop, test-time compute scaling, a human somewhere in the loop, and — specifically — judge circularity, where the same model family that generates candidates also grades them in the tournament that produces the paper's headline "beats frontier models" result. This is worth keeping as a concrete, high-profile reference point the next time we assess a similar claim elsewhere (ours or a competitor's): a same-family Elo tournament is evidence of self-consistent improvement, not of externally validated superiority, until cross-checked independently at comparable scale, and this paper's own gap between its large self-judged sample (n=203) and its small independently-judged sample (n=11) is a useful illustration of exactly how that gap tends to appear in practice.

The one clearly validated internal mechanism here — a critique agent's false-novelty rate dropping sharply once given external search — is a small but genuine data point for our verification programme's general thesis that cheap, grounded checks generalize better than a model's own unaided judgment (the "verifiers generalize where generators do not" intuition behind B12/B13). It is a generic-domain result, not a physics one, but it is evidence that this specific kind of grounding intervention works as intended for at least one narrow, well-defined failure mode (recognizing a known idea as not novel), which is the same category of claim we would want to make about a physics-native skeptic or assumption-tracking agent before trusting it more broadly.

The antimicrobial-resistance case study is a useful cautionary template for how we would want to frame (or avoid over-framing) an analogous "Theo independently reached the right answer" story in physics: insist on genuinely blind conditions, disclose explicitly if the domain experts involved in setting up and judging the test are also invested co-authors reporting the result, and treat a single striking case as an existence proof rather than a capability estimate. Finally, this paper is a real component in our own corpus's evidence chain via [26empsw](26empsw.md): a separate, external team already tested AI-co-scientist-sourced ideas against deterministic benchmarks and found them a modest, not dominant, contributor relative to that team's own idea-recombination mechanism — a useful, independently-obtained calibration point on this specific tool's practical hit rate that this paper's own self-reported results do not provide.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| Reflection agent with external search | false novelty scoring of known non-novel ideas | contradicts | 0.75 | papers/canonical/2026-05-06/26cosci.md:L1061 | Novelty auto-eval score dropped from 6.14 to 2.38 out of 10 once the agent had search access |
| Co-Scientist drug-repurposing hypotheses | AML cell-line viability | improves | 0.7 | papers/canonical/2026-05-06/26cosci.md:L317 | Binimetinib, Pacritinib, Cerivastatin, and KIRA6 showed dose-dependent inhibition in wet-lab assays |
| Co-Scientist tournament search | hypothesis Elo rating over computation time | improves | 0.5 | papers/canonical/2026-05-06/26cosci.md:L176 | Measured via the system's own self-judged Elo tournament, not independent ground truth |
| Co-Scientist AMR hypothesis | cf-PICI phage-tail host-range mechanism | implies | 0.4 | papers/canonical/2026-05-06/26cosci.md:L423 | Single case; the domain experts holding the unpublished result are co-authors of this paper |
| Co-Scientist | frontier LLMs and reasoning models in Elo rating | improves | 0.35 | papers/canonical/2026-05-06/26cosci.md:L210 | Measured using Co-Scientist's own Elo tournament as judge, a same-family-judge comparison |
