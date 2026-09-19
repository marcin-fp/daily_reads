---
schema_version: 1
paper: slug:26aisc
title: "AI in Science: Early Insights"
authors:
  - Mihai Codreanu
  - Alex Imas
  - Juan Mateos-Garcia
  - Joseph Emmens
  - Evalyne Muiruri
  - Arthur Turrell
  - Julian Jacobs
  - Atoosa Kasirzadeh
  - Ana Trišović
  - Yiyuan Chen
  - Tanya Rodchenko
  - Catherine Pollard
  - Scott Strand
  - Daniel Rock
  - Zanna Iscenko
  - Fabien Curto Millet
  - Neil Thompson
  - James Manyika
publication:
  first_public_date: "2026-09"
  first_public_date_precision: month
  venue: "Google / Google DeepMind / MIT FutureTech working paper"
  status: preprint
  reviewed_version: v1
  reviewed_version_date: ""
reviewed_at: "2026-09-18"
canonical: papers/canonical/2026-09-18/26aisc.md
raw: papers/raw/2026-09-18/26aisc-pdf.md
organizations:
  - name: Google
    sector: industry
    roles: [author_affiliation]
    authors: [Mihai Codreanu, Arthur Turrell, Yiyuan Chen, Tanya Rodchenko, Scott Strand, Daniel Rock, Zanna Iscenko, Fabien Curto Millet, James Manyika]
    grants: []
  - name: Google DeepMind
    sector: industry
    roles: [author_affiliation]
    authors: [Alex Imas, Juan Mateos-Garcia, Evalyne Muiruri, Julian Jacobs, Atoosa Kasirzadeh, Catherine Pollard]
    grants: []
  - name: University of Chicago
    sector: academia
    roles: [author_affiliation]
    authors: [Alex Imas]
    grants: []
  - name: CUNEF Universidad
    sector: academia
    roles: [author_affiliation]
    authors: [Joseph Emmens]
    grants: []
  - name: MIT FutureTech
    sector: academia
    roles: [author_affiliation]
    authors: [Joseph Emmens, Ana Trišović, Neil Thompson]
    grants: []
  - name: University of Oxford
    sector: academia
    roles: [author_affiliation]
    authors: [Julian Jacobs]
    grants: []
  - name: Carnegie Mellon University
    sector: academia
    roles: [author_affiliation]
    authors: [Atoosa Kasirzadeh]
    grants: []
  - name: University of Pennsylvania
    sector: academia
    roles: [author_affiliation]
    authors: [Daniel Rock]
    grants: []
  - name: Epoch AI
    sector: unknown
    roles: [data_provider]
    authors: []
    grants: []
  - name: More in Common
    sector: unknown
    roles: [collaborator]
    authors: []
    grants: []
artifacts: []
facets:
  domains: [economics-of-ai, science-of-science]
  paper_type: [analysis, survey]
  methods: [log-analysis, survey, bibliometrics, llm-classification]
  models: [Gemini]
  benchmarks: []
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: [missing-uncertainty]
metadata_notes: "Not an arXiv paper; no source URL is given in the extract, so source_url is omitted. Funding beyond the authors' own employers is not reported; the acknowledgments list individual names, not grants or external funders. Publication date is 'September 2026' per the title page, no exact day given."
---

Citation: Codreanu, Imas, Mateos-Garcia, Emmens, Muiruri, Turrell, Jacobs, Kasirzadeh, Trišović, Chen, Rodchenko, Pollard, Strand, Rock, Iscenko, Curto Millet, Thompson, Manyika. AI in Science: Early Insights. Google / Google DeepMind / MIT FutureTech working paper, September 2026.

## What this paper is about

A joint Google, Google DeepMind, and MIT FutureTech team asks a simple question with almost no prior real-time data behind it: how are scientists actually using AI right now, and what is that doing to the pace and shape of research? They combine three data sources, a large sample of Gemini conversation logs, a hand-built inventory of specialized science AI models (AlphaFold-like tools), and a survey of over 600 working scientists, and map all three onto a common task taxonomy so that general-purpose LLM use and specialized-model use can be compared on the same terms.

## Extended summary

Three data sources, three pipelines. (1) Gemini logs: from about 15 million anonymized interactions (Google ATLAS 1.0, April 2026 sample, excluding paid enterprise API traffic), the authors apply a three-stage filter: a work/non-work classifier (93.7% accuracy on synthetic validation), a restriction to six research-heavy SOC occupation groups (71.6% accuracy), and a custom science classifier built on OECD Frascati and UK Research and Innovation definitions (96% accuracy on held-out positives, 97% on negative controls). This yields about 360,000 "science" interactions. These are mapped, via a proprietary clustering-plus-LLM pipeline called OCTO, onto OpenAlex disciplines and a new three-level MIT FutureTech Scientific Task Taxonomy (built from 3.8 million job postings, ~210,000 representative tasks under 12 Level-1 areas, 114 Level-2, 2,433 Level-3 groups). Classification accuracy at this task/field mapping stage is much lower and drops sharply with granularity: 65% (Level-1 tasks) down to 30% (Level-3 tasks), and 83% (domains) down to 75% (217 subfields). (2) Specialized model inventory: 2,690 models (post-filtering a larger 5,501-model set to those published since 2012 with a paper and an official code repository), assembled via agentic web/GitHub search merged with Epoch AI's model database and enriched with OpenAlex metadata; OCTO extracts 4,475 downstream tasks from abstracts (what the model enables, not what its authors did to build it) and maps them to the same taxonomies. Synthetic-abstract validation: exact task count recovered in 48% of cases (mostly over-extraction, judged non-hallucinatory), exact task-label recovery 28-62% depending on the taxonomy level (versus a random baseline reported as 7x-600x worse), exact field recovery 48-74%. (3) Survey: 637 scientists (US and UK, screened for genuine research roles, unweighted, no representativeness claim, no margin of error quoted), fielded by a third party (More in Common) in July-August 2026.

Headline numbers. Science-heavy occupations show a 1.8x-2.7x Gemini-usage over-representation versus employment share (up to 5.8x in core STEM). "Analyze and model quantitative research data" is the single largest task category (about 42% of interactions). Specialized models and Gemini usage look similar in aggregate (both dominated by data analysis) but diverge sharply as task granularity increases: the log-log elasticity between specialized-model and LLM task shares falls from about 0.6 at the aggregate level to 0.2 (near zero, or slightly negative under one specification) at the most granular level, which the authors read as evidence of a division of labor rather than substitution. Citations to the specialized-model inventory total 1.3 million since 2012 (460,000 since 2020), with 49% of models in the top 1% of field-normalized citations, and over a quarter of citation links crossing scientific-domain boundaries. On the survey: 47% of scientists use AI daily, about three-quarters report net time savings averaging 6.9 hours/week, reinvested mostly into more research output (about 84% report higher lab output over the past three years). But 44% report their primary bottleneck has moved downstream (physical experimentation, validation) over the past two years, 41% report a growing backlog of untested hypotheses, 89% of time-savers spend over 10% of the saved time auditing AI outputs and 46% spend over a quarter of it, and 49% report AI pushing them toward safer, more incremental questions versus 28% reporting the opposite.

Authors' own caveats are extensive and specific: the log sample excludes enterprise API traffic and may not generalize beyond Gemini users; the model inventory is a "notability"-biased, non-exhaustive, lagging snapshot that under-counts bespoke and proprietary models; the survey is a self-selected, unweighted convenience sample likely to over-represent AI enthusiasts; the classification pipeline assigns each log/model task to a single taxonomy leaf even though real tasks often span several; and, most importantly for the headline "complementarity" finding, specialized-model "tasks" are extracted from what model authors claim their model enables in an abstract, not from observed scientist usage, which is a different kind of measurement than the Gemini usage logs. All stated results are explicitly associational, not causal.

## Learnings

The clearest reusable finding is a methodological one: apparent similarity between two categories of AI usage can be an artifact of coarse aggregation. At the top level of the task taxonomy, LLM and specialized-model usage look almost identical (both dominated by "analyze and model quantitative data"), but the correlation between the two collapses monotonically as task resolution increases, down to near zero at the finest grain. Any claim about which AI use cases overlap should be checked at the most granular level available before being taken as evidence of substitution or complementarity.

A second, more provisional finding: across three independent instruments (usage logs, a citation-based model inventory, and a scientist survey), the same downstream-bottleneck story recurs. As some research steps get faster, the constraint shifts to whichever step cannot be sped up the same way (usually physical experiment or validation), and a meaningful share of the time nominally saved is reallocated to checking AI output rather than to new research. This convergence across differently-biased data sources is more informative than any one of the three would be alone, even though each instrument individually has real, self-acknowledged limitations.

## Verification

The paper does not build or evaluate a verification method; it reports self-reported survey evidence on the cost of verifying AI outputs, which is directly relevant to our verification-economics interest even though "verification" is not this paper's subject. Among scientists who report time savings from AI, 89% say they now spend more than a tenth of that saved time auditing, debugging, or fact-checking the AI's output, and 46% say they spend more than a quarter of it; this "verification tax" is reported as particularly high in the Life Sciences. The authors also report a parallel and independently-elicited signal: 41% of scientists report a growing backlog of untested hypotheses, which they interpret as AI generating candidate hypotheses and computations faster than physical infrastructure (or the scientists themselves) can validate them. Both figures come from single self-report survey items on an unweighted, non-representative sample; the paper reports that the downstream-bottleneck-shift and backlog-growth results are strongly correlated with self-reported AI use in linear probability models, but that the verification-tax correlation is only marginally significant depending on specification. No coverage, precision, or judge-identity information is given because no automated checker is involved; this is entirely about the human cost of checking, not about how well any checker performs.

## Field context

The authors position this as the first large-scale, real-time telemetry study of AI use specifically in science, contrasted explicitly with two existing lines of work: scientometric studies that infer AI's footprint from finalized outputs like publications, citations, and patents (which arrive with a lag and track adoption only indirectly, e.g. Kusumegi et al. 2025 and the Renault et al. 2026 comment on it), and platform-level usage-log studies that cover the whole labor market but give science little specific attention (e.g. Chatterji et al. 2025's "How People Use ChatGPT," and Anthropic's Economic Index work by Handa et al. 2025 and Appel et al. 2025, which this paper cites as showing a similar SOC-19 over-representation ratio, about 4.5x, as a point of external corroboration for its own 2.7x-5.8x figures). It also explicitly builds on and extends a companion paper from the same data infrastructure, Iscenko et al. 2026's "Google's AI & Economy ATLAS v1.0," which supplies both the underlying log sample and the OCTO classification tooling. For specialized models, it situates itself alongside Trišović et al. 2025's foundation-model-usage inventory (similar scale, similar Epoch AI dependency) and the growing AlphaFold-impact literature (Hill and Stein 2026; Gans and Mohnen 2026; Qian 2026; Cavalli 2026) as case-study evidence for the broader claim that specialized models function as a distinct kind of scientific capital. The paper frames its own headline vision, an LLM orchestrator that plans experiments and calls specialized models for specific subtasks, as a natural extrapolation of the complementarity finding rather than something it has itself built or tested; it explicitly says "that system is still work in progress." This corpus does not yet contain another paper that measures AI-in-science adoption at this scale, so there is no directly comparable reviewed work to corroborate or contradict the headline numbers against.

## Critical discussion

The paper is unusually careful about its own limitations, which makes it easier to state exactly how far the evidence goes. Two structural issues, both flagged by the authors themselves, deserve emphasis because they bear directly on the two most quotable numbers in the abstract. First, the "complementarity" claim (LLMs and specialized models diverge at fine task granularity) compares two measurement types that are not equivalent: Gemini usage is observed behavior, while specialized-model "tasks" are extracted from what a model's authors claim it enables in a publication abstract, explicitly not what scientists actually do with it. A model paper's abstract can claim broad applicability that never translates into comparable observed use, so the low-overlap finding could partly reflect a mismatch between claimed and realized capability rather than a genuine division of labor in practice. This does not make the finding wrong, but it means the "acts as complements" framing in the abstract is a stronger claim than the underlying comparison directly supports. Second, the headline productivity and adoption figures (47% daily use, 6.9 hours/week saved, 84% higher output) come from a self-selected, unweighted, non-representative, no-margin-of-error survey that the authors themselves say likely over-samples AI enthusiasts; these numbers should be read as plausible upper bounds on typical scientist experience rather than population estimates, exactly as the paper itself cautions in Appendix 3.

A third point that the authors mention but slightly underplay: fine-grained task and field classification accuracy is quite low in absolute terms, 28% to 65% depending on the taxonomy level for logs, and 28% to 62% for the model inventory. This is framed relative to a random baseline (where it looks very strong, 7x to over 600x better), but the random-baseline comparison is not the relevant bar for reading Table 1's claims about which specific tasks are over- or under-represented by scientific domain; a substantial share of the fine-grained task assignments underlying that table are wrong, which the paper's own footnotes acknowledge (misclassification concentrated in semantically adjacent or interdisciplinary categories) without quite carrying that caveat through to how confidently the domain-level task table should be read.

What remains solidly supported after these caveats: the broad qualitative pattern, widespread and intensifying AI adoption in science, a real division of labor between general and specialized models that sharpens at finer task grain, and a self-reported downstream shift in bottlenecks toward validation and verification work, is triangulated across three differently-biased instruments and is unlikely to be a pure artifact of any single one. The precise magnitudes (2.7x over-representation, 6.9 hours/week, 46% spending a quarter of saved time verifying) are considerably less trustworthy than the paper's confident tone in the abstract suggests, and should be treated as directional rather than precise.

## Relevance to us

The verification-tax and hypothesis-backlog findings are an independent, larger-sample echo of exactly what our own interviews said: the gap scientists report is not raw capability but calibration and trust, and a meaningful share of any time AI saves gets reinvested into checking its output rather than into new work. That this shows up again here, in a very different population and instrument (a cross-disciplinary survey rather than physicist interviews), is worth treating as corroborating evidence for the premise behind our verification programme (B12) and for prioritizing cheap, well-characterized partial checks over broader coverage.

The "safer, incremental questions" tilt (49% vs. 28%) is a new empirical instance of something like the Streetlight Effect operating at the level of research-topic choice rather than model-generation diversity. We currently frame diversity concerns (B16) mainly around generation-time mode collapse; this paper suggests the same dynamic, AI lowering the cost of tractable, benchmarkable work relative to higher-risk, harder-to-validate work, may also operate at the sociological level of which questions scientists choose to pursue at all. That is a broader and messier version of the tension than our current framing captures, and it is worth tracking as a candidate mechanism rather than folding it silently into B16.

The paper's closing vision, an LLM that orchestrates calls to specialized domain models and interprets their outputs, is a market-level statement of something close to our own heterogeneous-specialist-federation bet (B07), arrived at independently from adoption data rather than from an architecture proposal. It is useful as external validation that the shape of the problem (general orchestrator plus domain specialists) is being read the same way from the demand side, though the paper itself has not built or evaluated such a system.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| LLM and specialized-model task usage | task specialization (division of labor) | implies | 0.55 | papers/canonical/2026-09-18/26aisc.md:L167 | Log-log elasticity between LLM and specialized-model task shares falls from ~0.6 (aggregate) to ~0.2 (finest grain), read as division of labor rather than substitution |
| AI-driven time savings | time spent verifying AI outputs | implies | 0.5 | papers/canonical/2026-09-18/26aisc.md:L220 | 89% of scientists who save time report spending >10% of it auditing/verifying AI output, 46% spend >25% |
| AI adoption | tilt toward safer, incremental research questions | implies | 0.45 | papers/canonical/2026-09-18/26aisc.md:L227 | 49% of surveyed scientists report AI pushing them toward safer, established questions versus 28% reporting a push toward riskier, higher-ambition questions |
