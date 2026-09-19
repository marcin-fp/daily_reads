---
schema_version: 1
paper: slug:26empsw
title: "An AI system to help scientists write expert-level empirical software"
authors:
  - Eser Aygün
  - Anastasiya Belyaeva
  - Gheorghe Comanici
  - Marc Coram
  - Hao Cui
  - Jake Garrison
  - Renee Johnston
  - Anton Kast
  - Cory Y. McLean
  - Peter Norgaard
  - Zahra Shamsi
  - David Smalling
  - James Thompson
  - Subhashini Venugopalan
  - Brian P. Williams
  - Chujun He
  - Sarah Martinson
  - Martyna Plomecka
  - Lai Wei
  - Yuchen Zhou
  - Qian-Ze Zhu
  - Matthew Abraham
  - Erica Brand
  - Anna Bulanova
  - Jeffrey A. Cardille
  - Chris Co
  - Scott Ellsworth
  - Grace Joseph
  - Malcolm Kane
  - Ryan Krueger
  - Johan Kartiwa
  - Dan Liebling
  - Jan-Matthis Lueckmann
  - Paul Raccuglia
  - Xuefei Julie Wang
  - Katherine Chou
  - James Manyika
  - Yossi Matias
  - John C. Platt
  - Lizzie Dorfman
  - Shibl Mourad
  - Michael P. Brenner
publication:
  first_public_date: "2025-09-08"
  first_public_date_precision: day
  venue: Nature
  status: journal
  reviewed_version: "Accelerated Article Preview"
  reviewed_version_date: "2026-05-19"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/26empsw.md
raw: papers/raw/2026-05-06/26empsw-pdf.md
source_url: https://doi.org/10.1038/s41586-026-10658-6
organizations:
  - name: Google DeepMind, Montréal
    sector: industry
    roles: [author_affiliation]
    authors: [Eser Aygün, Gheorghe Comanici, David Smalling, Anna Bulanova, Shibl Mourad]
    grants: []
  - name: Google Research, Cambridge MA
    sector: industry
    roles: [author_affiliation, compute_provider]
    authors: [Anastasiya Belyaeva, Marc Coram, Hao Cui, Renee Johnston, Anton Kast, Cory Y. McLean, Peter Norgaard, Zahra Shamsi, James Thompson, Subhashini Venugopalan, Brian P. Williams, Chujun He, Sarah Martinson, Martyna Plomecka, Lai Wei, Yuchen Zhou, Qian-Ze Zhu, Matthew Abraham, Erica Brand, Jeffrey A. Cardille, Chris Co, Scott Ellsworth, Grace Joseph, Malcolm Kane, Ryan Krueger, Johan Kartiwa, Dan Liebling, Jan-Matthis Lueckmann, Paul Raccuglia, Xuefei Julie Wang, Katherine Chou, James Manyika, Yossi Matias, John C. Platt, Lizzie Dorfman, Michael P. Brenner]
    grants: []
  - name: Google Platforms and Devices, Mountain View
    sector: industry
    roles: [author_affiliation]
    authors: [Jake Garrison]
    grants: []
  - name: Massachusetts Institute of Technology
    sector: academia
    roles: [author_affiliation]
    authors: [Chujun He]
    grants: []
  - name: School of Engineering and Applied Sciences, Harvard University
    sector: academia
    roles: [author_affiliation]
    authors: [Sarah Martinson, Qian-Ze Zhu, Ryan Krueger, Michael P. Brenner]
    grants: []
  - name: Google DeepMind, New York
    sector: industry
    roles: [author_affiliation]
    authors: [Martyna Plomecka]
    grants: []
  - name: Faculty of Agricultural and Environmental Sciences, McGill University
    sector: academia
    roles: [author_affiliation]
    authors: [Yuchen Zhou, Jeffrey A. Cardille]
    grants: []
  - name: California Institute of Technology
    sector: academia
    roles: [author_affiliation]
    authors: [Xuefei Julie Wang]
    grants: []
artifacts:
  - type: code
    url: https://github.com/google-research/era
  - type: project
    url: https://google-research.github.io/era
facets:
  domains: [machine-learning, bioinformatics, epidemiology, time-series-forecasting, computational-science]
  paper_type: [method, experiment, system]
  methods: [tree-search, llm-code-mutation, puct, idea-recombination, retrieval-augmented-ideation]
  models: [Gemini-2.5-Flash, Gemini-2.5-Pro, Gemini-3.1-Pro, Claude-Sonnet-4.6, GPT-5, Mistral-Medium]
  benchmarks: [OpenProblems-batch-integration, CovidHub, GIFT-Eval, Kaggle-Playground, ZAPBench]
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: [missing-control, incomplete-reporting]
metadata_notes: "This exact title and system first appeared as arXiv:2509.06503 (submitted 2025-09-08); first_public_date uses that date. The Nature version reviewed here (an Accelerated Article Preview, Received 2025-09-13, Accepted 2026-05-13) is a substantially updated revision: Table 1 compares against Claude Sonnet 4.6, GPT-5, and Gemini 3.1 Pro, none of which existed at the September 2025 arXiv posting, confirming new experiments were added before Nature acceptance. Web search corroborates the Accelerated Article Preview went online 2026-05-19 and the paper appears in print as Nature 654, 909-916 (2026); the source text itself left the online-publication date as an unfilled placeholder ('Published online xx xx xxxx'), consistent with this being a preview PDF captured before typesetting was finalized. The Competing Interest Declaration states that Google-affiliated authors are Google Inc. employees holding Alphabet stock; six authors (marked '**' in the byline: Chujun He, Sarah Martinson, Martyna Plomecka, Qian-Ze Zhu, Ryan Krueger, Xuefei Julie Wang) carried out this work as a student researchership at Google Research alongside a home academic affiliation (MIT, Harvard, or Caltech), which is reflected in their listed organizations above. No external grant or funder is named in the Acknowledgements, which thank named colleagues rather than a funding body."
---

Citation: Aygün, E. et al. An AI system to help scientists write expert-level empirical software. Nature 654, 909-916 (2026). https://doi.org/10.1038/s41586-026-10658-6

## What this paper is about

A huge amount of scientific progress depends on writing "empirical software" — code whose job is to maximize some measurable score, like a forecasting model's accuracy or an algorithm's ability to separate real biological signal from technical noise. Writing this kind of software well is slow, and mostly guided by intuition rather than systematic search over alternatives. This paper presents ERA (Empirical Research Assistance), a Google system that turns "write good empirical software" into a search problem an AI can run at scale: an LLM repeatedly rewrites candidate code, a tree-search algorithm decides which candidates are worth building on, and the whole loop can be handed research ideas from papers, textbooks, or an AI literature-search tool to guide where it looks. Tested across six real scientific benchmarks (single-cell genomics, COVID-19 hospitalization forecasting, general time-series forecasting, satellite image segmentation, whole-brain neural activity prediction in zebrafish, and numerical integration), the system reportedly produced code that beat the best previously published or human-submitted solutions in most of them.

## Extended summary

ERA's core loop: an LLM is prompted with a task description, an evaluation metric, and relevant data, and produces Python code that is executed and scored in a sandbox. A tree-search algorithm then decides which existing "node" (a scored code candidate) to expand next, generating one new child solution at a time by prompting the LLM with that parent's code and score. The search algorithm is a modified PUCT (Predictor + Upper Confidence bound applied to Trees, in the spirit of AlphaZero), but because the true child-branching factor is effectively infinite (the LLM can generate arbitrarily different code), every existing node is a candidate for expansion rather than only children of the currently-explored path; the authors describe this as closer to "Flat UCB" than to standard Monte Carlo tree search. Task-specific scores are converted to rank scores within the tree to make a single exploration constant (tuned once, on the Kaggle benchmark, to c_puct = 1) transferable across very different tasks and metrics. All experiments use Gemini 2.5 Flash as the underlying LLM; the authors report the improvement from switching to Gemini 2.5 Pro was modest.

The system was developed and its core hyperparameters were tuned on 16 "Kaggle Playground" competitions from the 2023 season (regression and classification tasks chosen for fast iteration and calibration against thousands of real human competitors via Kaggle's own leaderboard percentile). On this benchmark, ERA substantially outperformed both a single LLM call and best-of-1000 LLM sampling, and outperformed an existing code-mutation baseline (AIDE), which the authors attribute to the tree's ability to maintain a diverse set of candidates and backtrack when a line of mutation plateaus. Adding problem-specific advice to the prompt (e.g., explicit Kaggle-winning heuristics, or an instruction to implement a boosted decision tree from scratch without standard libraries) substantially improved performance further; the authors report manually verifying that the resulting code actually followed the given advice in both cases.

Six scientific benchmarks were then evaluated. (1) Single-cell RNA-seq batch integration, scored on the external OpenProblems v2.0.0 benchmark (13 metrics across 6 held-out human/mouse datasets, ~1.75 million cells total). A separate, non-benchmark dataset was used for ERA's own optimization to avoid overfitting to the eval set. Running unguided, ERA converged on a solution conceptually similar to an existing method (ComBat) but already ahead of the leaderboard. Guided by brief LLM-generated summaries of nine existing published methods' papers, ERA-produced implementations outperformed the corresponding published result in 8 of 9 cases; the best (an ERA implementation of Batch Balanced K-Nearest Neighbors, "BBKNN (TS)") improved 14% overall over the best published method and matched or beat the original BBKNN paper on 11 of 13 metrics. Manual expert review of the produced code (Extended Data Table 1) found that nearly all replications faithfully followed the specified algorithm, though a small number did not (a Scanorama replicate implemented via a different library's function; one LIGER replicate substituted ComBat+SVD for the intended NMF-based approach). A causal ablation confirmed that BBKNN (TS)'s improvement specifically came from computing k-nearest neighbors on ComBat-corrected PCA embeddings rather than raw PCA embeddings, verified by manually swapping this component in and out of both the new and the original published implementation. The system also produced a working implementation of a method (TabVI) with no publicly available code. Programmatically recombining all 55 pairs of 11 base methods (via an LLM-generated comparison of each pair's technical similarities/differences fed back into the search prompt) produced recombination solutions that beat both parent methods in 44% of cases (24/55) and beat at least one parent in a further 22 cases. Combining base methods, recombinations, and ideas sourced from Gemini Deep Research and an "AI co-scientist" tool, 40 of 87 total generated methods outperformed every method then on the OpenProblems leaderboard.

(2) COVID-19 hospitalization forecasting, evaluated retrospectively against the CDC's CovidHub Ensemble using the Weighted Interval Score (WIS, lower is better) over the 2024-25 season, with a rolling six-week validation window per forecast period, using data available as of 2025-05-01. ERA's resulting "Google Retrospective" model achieved an average WIS of 26 versus the official ensemble's 29 (lower is better). Replicating eight existing teams' models from only their brief public method descriptions, ERA's tree-search reimplementations exceeded the original submissions' performance in 6 of 8 cases (the two that did not outperform lacked access to external data the originals used). Recombining pairs of these replicated models (11 of 26 pairings beat both parents) and adding ideas from Deep Research and AI co-scientist yielded 14 total strategies beating the official ensemble, with recombinations dominant (10 of 14); the most successful recombinations paired a simple climatology or autoregressive baseline with a more complex model, and the two base methods that recurred most often in winning hybrids were the simplest ones tested (a climatology baseline and an autoregressive model).

(3) Time-series forecasting on GIFT-Eval (28 datasets, seconds-to-years frequency, scored via normalized MASE against a seasonal-naive baseline, snapshotted to a 2025-05-18 leaderboard specifically to avoid comparing against a later-revised, moving-target evaluation protocol). A per-dataset ERA solution (full Python ML library access) reportedly outperformed the entire snapshotted leaderboard, including foundation and deep-learning models. A second "unified" solution, deliberately restricted to basic libraries (numpy, pandas, holidays) and optimized by hill-climbing a single code against the average score across all 97 datasets, converged on a from-scratch decomposition model (base level, trend, seasonality, datetime/holiday effects, residual correction) with adaptive presets, reaching a final MASE of 0.734 after iterative refinement (from an initial 0.82).

(4) Three further domains — geospatial semantic segmentation, whole-brain neural activity forecasting in zebrafish (ZAPBench), and numerical integration — are each reported in a single sentence in the main text ("ERA achieved expert-level performance in each case"), with all supporting detail deferred to Supplementary Notes and figures not included in this extract.

Table 1 directly compares ERA (128 search nodes) against best-of-1000 sampling for five different underlying LLMs (Gemini 2.5 Flash, Mistral Medium, Claude Sonnet 4.6, GPT-5, Gemini 3.1 Pro) on batch integration and an epidemiological flu-forecasting task. ERA outperformed best-of-N for every model and task tested except one: GPT-5's one-shot performance on batch integration was already strong enough that tree search added little. The authors note this as an expected pattern — as frontier models improve, some tasks saturate and search adds less value, while it remains useful on harder tasks.

The Discussion section explicitly separates "optimizing empirical predictive models" from "genuine scientific discovery" (the latter requiring reasoning about theories, causal mechanisms, and mathematical frameworks), stating the evaluated tasks emphasize empirical software engineering specifically because it supports rigorous automated scoring, while claiming the underlying system "goes well beyond this" without further support in this extract. The paper also raises a general safety concern: by lowering the technical expertise needed to produce expert-level empirical software, such systems could equally lower the barrier to producing capable software in sensitive or dangerous domains, which the authors frame as a systemic risk tied to growing inference-time compute and model quality generally, without proposing a specific mitigation.

## Learnings

A tree-search-guided LLM code-mutation loop, given only a short, publicly available method description (no access to the original paper's code or the target model's training data), reproduced or exceeded the described method's own published performance in the large majority of replication attempts tested here (8/9 single-cell batch-integration methods, 6/8 COVID-forecasting models). This suggests that for many published empirical methods, most of the algorithm's value is recoverable from a natural-language description plus enough automated search, which has implications both for how reproducible empirical methods really are and for how cheaply a "replicate this paper's method" step can be automated.

Explicitly prompting an LLM to compare two existing solutions' technical similarities and differences, then instructing search to synthesize a hybrid, produced a strong and specific effect: 44% of 55 pairwise recombinations of single-cell methods beat both parent methods on held-out data, and the paper's own analysis of the 14 best COVID-forecasting strategies found the most successful hybrids consistently paired a simple, robust baseline (climatology, basic autoregression) with a more complex model, rather than combining two complex models. Structured recombination of known ideas, not just refinement of one idea or brute-force sampling, was the dominant source of the best results in the epidemiology task.

A single, cheap, causal ablation — manually swapping one specific component (ComBat-corrected versus raw PCA embeddings) in and out of both a newly discovered implementation and the original published implementation it was compared against — was used to establish that this one component, not the reimplementation as a whole, was responsible for the performance gain. This is a meaningfully stronger form of evidence than the correlational embedding/attention analyses common in adjacent multimodal-LLM papers, and it is cheap enough (a manual code edit and rerun) that it is worth treating as a standard, not exceptional, bar for "we found what's actually driving this" claims.

## Verification

Verification here is unusually strong for an agentic-AI paper, for a specific structural reason: correctness is checked against external, deterministic, already-existing scoring pipelines (Kaggle's leaderboard percentile, the OpenProblems benchmark's 13 metrics against real single-cell ground truth, the CDC's own WIS scoring for actual hospitalization counts, GIFT-Eval's official MASE on held-out test splits) rather than by an LLM judge, so there is no same-family-judge concern for the headline numbers. On top of this external scoring, the paper adds two further checks worth naming specifically because they go beyond what most comparable papers do: expert manual inspection of whether generated code actually implements the algorithm it claims to (Extended Data Table 1), which explicitly reports the coverage of that check (all replicates for most methods, with disclosed exceptions where a replicate used a different technique than the one it was compared against, and a note that the lowest-performing tree-search replicates for three methods only successfully computed 30, 57, and 45 of 78 possible metrics); and a causal ablation isolating which specific code component drives an observed performance gain (the ComBat-embedding test described above), rather than resting on a correlational or purely behavioral argument. Neither check is exhaustive — the manual code-adherence review covers the batch-integration replications only, not the COVID, time-series, or "other problems" results, and only one component-level ablation of this kind is reported — but both are disclosed with enough specificity (exact counts, exact failure cases) to be evaluated rather than taken on faith.

## Field context

The paper positions ERA explicitly against several adjacent lines of work in its own Discussion section: Genetic Programming (crossover/mutation on program syntax trees, which ERA replaces with LLM-driven semantic rewriting), Generative Programming (template/DSL-based code generators, which ERA replaces with an LLM-plus-search generative engine), one-shot LLM code generation (AlphaCode, Codex), AutoML (which ERA generalizes beyond fixed ML pipelines to arbitrary rewritable software), and, most closely, other work combining LLMs with search — FunSearch (LLM plus automated evaluator for mathematical discovery) and the more recent AlphaEvolve, which the authors describe as similar in algorithmic spirit but lacking ERA's literature-grounded "idea exploration." ERA's search algorithm is a direct, disclosed modification of AlphaZero/PUCT-style tree search, adapted because the branching factor here (arbitrary LLM-rewritten code) cannot be exhaustively enumerated the way board-game moves can. On the Kaggle benchmark specifically, ERA is compared directly against an existing code-mutation baseline, AIDE. None of these specific precedents (FunSearch, AlphaEvolve, AIDE, AI co-scientist) are yet reviewed in this corpus, so this positioning reflects the authors' own detailed related-work framing, which is unusually thorough and explicit for a paper of this kind, rather than an independent check against another review here.

## Critical discussion

The overall evidentiary bar this paper clears is genuinely high for an agentic-AI-for-science paper: headline claims are checked against external, deterministic scoring on real, pre-existing community benchmarks rather than an LLM judge, several ablations are causal rather than merely correlational, and the authors report negative or complicating results alongside positive ones (GPT-5 already saturating one task; specific replicate implementations that did not faithfully follow the target algorithm; the honest acknowledgment that "genuine scientific discovery" is a higher bar than what is demonstrated here). This transparency should be weighed positively against the specific gaps below.

The COVID-19 retrospective comparison has a disclosed but consequential asymmetry: the authors state they used data "available as of 2025-05-01... for the entire retrospective season, thus ignoring potential differences in data available at the date of forecast." The original CovidHub teams had to forecast using real-time, not-yet-revised hospitalization data as it existed on each historical forecast date; ERA's retrospective model was optimized and evaluated using later, more complete/revised data for the whole season. Hospitalization reporting is well known to be revised upward over time as delayed reports arrive, so this is not a hypothetical concern; it means the reported WIS advantage (26 versus 29) reflects both any genuine algorithmic advantage and an unknown, undisclosed-in-magnitude advantage from working with better-quality retrospective data than the original forecasters had. The paper's own framing ("rigorous retrospective study") does not fully signal how much this matters, even though the underlying caveat is honestly stated. This is a missing-control issue specific to the epidemiology result; it does not extend to the batch-integration or GIFT-Eval comparisons, where held-out data and fixed benchmark snapshots were used more symmetrically.

The proportion of evidence across the six claimed domains is very uneven. Single-cell batch integration and COVID-19 forecasting together receive several pages of detailed methodology, quantitative comparisons, ablations, and manual verification. Geospatial segmentation, zebrafish neural-activity forecasting, and numerical integration — the tasks with the least existing community-leaderboard infrastructure, and the one (numerical integration) closest to a physics/mathematics setting — receive one sentence in the main text each, with all detail deferred to Supplementary Notes not present in this extract. Nothing here suggests those results are wrong, but as reported in the material available, "expert-level performance" for these three domains is an assertion rather than something this review can independently assess; the claim should be treated as reported, not supported, until the Supplementary Notes are examined.

The Table 1 model-comparison ablation, while a genuinely useful check on whether search adds value beyond one-shot generation across vendors, is run at a much smaller budget (128 search nodes) than the headline results elsewhere in the paper (500 nodes for batch integration, 2,000 for COVID forecasting, up to 1,000+ for the unified GIFT-Eval solution). This is a reasonable practical choice for a five-model, two-task ablation, but it means the "search helps across model vendors" finding is established at a materially smaller compute budget than the specific numbers used for the paper's central "outperforms the state of the art" claims, and the paper does not report whether the relative ordering (ERA beats best-of-N) holds at the larger budgets used elsewhere.

What remains well supported after these caveats: on the two most thoroughly documented benchmarks (single-cell batch integration and, with the stated data-availability caveat in mind, COVID-19 forecasting), ERA's tree-search-plus-LLM approach outperforms one-shot and best-of-N baselines, a prior code-mutation agent (AIDE) on Kaggle, and most tested published methods, with at least one specific mechanistic driver of an improvement (the ComBat-embedding component) verified causally rather than assumed. Idea recombination, specifically, is a well-quantified and reproducible source of the strongest results in both of these domains. The claims for the remaining three domains, and the precise size of the COVID-19 advantage net of the data-availability asymmetry, are less independently verifiable from what is reported here.

## Relevance to us

This is a clean, well-documented, real-world instance of the "typical giant recipe" our competitive-opening notes describe (frontier backbone, agentic search loop, large inference-time compute), and it is unusually good at doing the thing that recipe often skips: the paper's own ablations identify specific mechanisms behind the gains (idea recombination, a particular embedding component, search versus best-of-N at matched-ish budgets) rather than crediting an undifferentiated "agentic capability," which is the standard our own competitive analysis should hold other agent papers to, and a positive counter-example when we want to cite one. The idea-recombination result in particular — structured combination of two known methods reliably beating single-method refinement or brute-force sampling — is a concretely measured instance of a mechanism relevant to B07 (heterogeneous specialist federation) and to our interest in diversity-preserving generation (B16): recombination, not just more samples, is what found the strongest solutions here.

The uneven depth of evidence across domains is a close-to-literal confirmation of our own observation that "physics demonstrations in general agent papers are often the weakest domain": even a very well-resourced team, given six candidate domains to demonstrate on, gave its most rigorous, most heavily ablated treatment to the two domains with mature, pre-existing, deterministic community benchmarks (bioinformatics, epidemiology) and its thinnest treatment (one sentence, no main-text detail) to numerical integration, the one task here closest to physics or applied mathematics. This is worth remembering not as a criticism of this specific paper's honesty (the gap is disclosed, not hidden) but as a data point for why a physics-native benchmark and verification infrastructure (B12) needs to exist on purpose — mature checking infrastructure appears to be what determines where an otherwise-general system gets its evidence built out, not the other way around.

The COVID-19 data-availability caveat is a concrete, transferable lesson for our own eventual prediction- or forecasting-style evaluations: a "retrospective" comparison against real-time forecasters is not apples-to-apples unless the evaluated system is restricted to genuinely point-in-time data, and this paper is a specific, citable example of how easy it is to disclose this caveat honestly while still reporting a headline number that doesn't fully account for it.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| ERA tree search | single-cell batch-integration published methods | improves | 0.8 | papers/canonical/2026-05-06/26empsw.md:L171 | Outperformed the published result for 8 of 9 methods on the external OpenProblems benchmark |
| ERA idea recombination | single-parent method performance | improves | 0.75 | papers/canonical/2026-05-06/26empsw.md:L179 | 44% of 55 pairwise recombinations beat both parent methods on held-out data |
| ERA retrospective model | CDC CovidHub ensemble forecast | improves | 0.5 | papers/canonical/2026-05-06/26empsw.md:L250 | WIS 26 vs 29, but retrospective evaluation used later-revised data unavailable to original real-time forecasters |
| ERA tree search | single LLM call and best-of-1000 sampling | improves | 0.8 | papers/canonical/2026-05-06/26empsw.md:L128 | Outperforms both baselines averaged across 16 Kaggle Playground competitions |
| ComBat-corrected PCA embeddings | BBKNN batch-integration performance | improves | 0.9 | papers/canonical/2026-05-06/26empsw.md:L196 | Causally verified by manually swapping the embedding step in both the new and original published implementation |
