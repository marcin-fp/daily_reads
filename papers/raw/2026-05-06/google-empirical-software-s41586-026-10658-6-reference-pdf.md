
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9qqIsXu_haBv2Xuxzd_UutD6wirbhyzZgja2Nz0tCe1cSQNt8b2Isvk4eFzGj5-vk6tTkIIjC5VR-nyAgQri4xTBjBs5IQIOSJorcFTIsYOBUomvDV-gRsnldrYC56tC3ceVSBcQ=w1100-h90-v0?authuser=0)
**An AI system to help scientists write expert-level empirical software**
**Eser A yg ün , A na st as iya Belyaeva, Gheorghe Comanici, Marc Coram, Hao Cui, Jake Garrison, Renee Johnston, Anton Kast, Cory Y. McLean, Peter Norgaard, Zahra Shamsi, David Smalling, James T ho mp so n , S ub ha shini Venugopalan, Brian P. Williams, Chujun He, Sarah Martinson, Martyna Plomecka, Lai Wei, Yuchen Zhou, Qian-Ze Zhu, Matthew Abraham, Erica Brand, Anna Bulanova, Jeffrey A. Cardille, Chris Co, Scott Ellsworth, Grace Joseph, Malcolm Kane, Ryan Krueger, Johan Kartiwa, Dan Liebling, Jan-Matthis Lueckmann, Paul Raccuglia, Xuefei Julie Wang, Katherine Chou, James Manyika, Yossi Matias, John C. Platt, Lizzie Dorfman, Shibl Mourad & Michael P. Brenner**
This is a PDF file of a peer-reviewed paper that has been accepted for publication. Although unedited, the content has been subjected to preliminary formatting. Nature is providing this early version of the typeset paper as a service to our authors and readers. The text and figures will undergo copyediting and a proof review before the paper is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers apply.
Received: 13 September 2025
Accepted: 13 May 2026
Accelerated Article Preview Published online xx xx xxxx
Cite this article as: Aygün, E. et al. An AI system to help scientists write expert-level*empirical software. Nature https://doi.org/*10.1038/s41586-026-10658-6 (2026)
https://doi.org/10.1038/s41586-026-10658-6
### **Accelerated Article Preview**
# ACCELE RATED
# ARTIC LE
# PREVIE W
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8Uv1AkPOHcNxhrrSc-9kxklX2XaHRHeNToMHak5A_mabKW4ZPOs4HrpDFh47Ew-HbCa7c2Ef4X6ruJre02jJpra5qRFjkvGQ2_wzNc12IA_Zi81KPL3uxtjE6h8B_aiY3dOQ7Y6Q=w839-h1115-v0?authuser=0)

## An AI system to help scientists write expert-level1
## empirical software2
Eser Aygün1,*, Anastasiya Belyaeva2,*, Gheorghe Comanici1,*, Marc Coram2,*,3
Hao Cui2,*, Jake Garrison3,*, Renee Johnston2,*, Anton Kast2,*, Cory Y.4
McLean2,*, Peter Norgaard2,*, Zahra Shamsi2,*, David Smalling1,*, James5
Thompson2,*, Subhashini Venugopalan2,*, Brian P. Williams2,*, Chujun He2,4,**,6
Sarah Martinson2,5,**, Martyna Plomecka2,6,**, Lai Wei2, Yuchen Zhou2,7
Qian-Ze Zhu2,5,**, Matthew Abraham2, Erica Brand2, Anna Bulanova1, Jeffrey8
A. Cardille2,7, Chris Co2, Scott Ellsworth2, Grace Joseph2, Malcolm Kane2,9
Ryan Krueger2,5,**, Johan Kartiwa2, Dan Liebling2, Jan-Matthis Lueckmann2,10
Paul Raccuglia2, Xuefei (Julie) Wang2,8,**, Katherine Chou2, James Manyika2,11
Yossi Matias2, John C. Platt2, Lizzie Dorfman2, Shibl Mourad1,‡, and Michael12
P. Brenner2,5,‡ 13
1Google DeepMind, Montréal, Quebec H2Z 1W5, Canada14
2Google Research, Cambridge, MA 02142, USA15
3Google Platforms and Devices, Mountain View, CA 94043, USA16
4Massachusetts Institute of Technology, Cambridge, MA 02139, USA17
5School of Engineering and Applied Sciences, Harvard University, , Cambridge, MA 02138, USA18
6Google DeepMind, New York, New York 10011, USA19
7Faculty of Agricultural and Environmental Sciences, McGill University, Montréal, Quebec H3A20
0G4, Canada21
8California Institute of Technology, Pasadena, CA 9112522
*Equal contribution in alphabetical order.23
** Carried out as part of a student researchership at Google Research.24
‡ To whom correspondence should be addressed: shibl@google.com, mbrenner@google.com25
The cycle of scientific discovery is frequently bottlenecked by the slow, manual26
creation of software to support computational experiments1. To address this, we27
present Empirical Research Assistance (ERA), an AI system that creates expert-28
level scientific software whose goal is to maximize a quality metric. The system29
uses a Large Language Model (LLM) and Tree Search (TS)2 to systematically30
improve the quality metric and intelligently navigate the large space of possible31
solutions. ERA achieves expert-level results when it explores and integrates32
complex research ideas from external sources. The effectiveness of tree search is33
1
# ACCELE RATED ARTIC
# LE  PREVIEW
demonstrated across a diverse range of tasks. In bioinformatics, ERA discovered34
40 novel methods for single-cell data analysis that outperformed the top human-35
developed methods on a public leaderboard. In epidemiology, ERA generated 1436
models that outperformed the CDC ensemble and all other individual models for37
forecasting COVID-19 hospitalizations. ERA also produced expert-level software38
for geospatial analysis, neural activity prediction in zebrafish, and numerical39
solution of integrals, and a novel rule-based construction for time series forecasting.40
By devising and implementing novel solutions to diverse tasks, ERA represents a41
significant step towards accelerating scientific progress.42
Keywords: Tree Search, Generative AI, Scorable Scientific Tasks, Empirical Software43
### Introduction44
Empirical software, designed to maximize a measurable quality score, is ubiquitous and45
central to many scientific endeavors. Empirical software has recently enabled a number of46
Nobel Prizes in Chemistry: in 1998 for Density Functional Theory3,4, in 2013 for molecular47
dynamics simulation5 and in 2024 for protein structure prediction6,7. Empirical software48
underlies our ability to create models of complex systems, ranging from parameterizations of49
a vertical column of the earth’s atmosphere for weather modeling8, to the parameterization50
of stress response in a turbulent fluid flow9, to the prediction of social systems10,11.51
However, empirical software for science is slow and difficult to create. Domain-specific52
empirical software requires tedious work1, often over many years. When empirical software53
is used to test complex hypotheses, it becomes ever more difficult to write purely from54
first principles. There usually is no systematic search for alternative approaches. Design55
choices are often governed by intuition or expediency, rather than exhaustive experimentation.56
Creating the software is so time-consuming that it severely limits the possibilities that can57
be productively explored12.58
Here we present Empirical Research Assistance (ERA), an AI-based system that system-59
atically and automatically creates empirical software to solve scorable tasks. ERA is based60
on an LLM that rewrites software to attempt to improve its quality score. ERA creates61
multiple software candidate solutions, and uses Tree Search2 to decide which candidates62
merit further exploration (Fig. 1a). While there are many ways of designing a code mutation63
system13–16, we developed ERA by competing in Kaggle competitions (Fig. 1b), described64
below. We augment code mutation with research ideas obtained from a range of sources65
including highly-cited papers, specialized textbooks, and search engine results (Fig. 1c). In66
practice, these ideas can be injected either directly by the user or automatically using a67
search engine to access research in the literature. The LLM uses this injected guidance in68
writing code.69
We find that ERA produces software that outperforms the state-of-the-art in scorable70
tasks spanning broad scientific disciplines. This expert-level performance arises because of71
the ability to exhaustively and tirelessly carry out solution searches at unprecedented scale,72
identifying needle-in-the-haystack high quality solutions.73
2
# ACCELE RATED ARTIC
# LE  PREVIEW
### Results74
Overview of Scorable Tasks75
We develop ERA on Kaggle playground competitions, and test it by selecting scorable tasks76
based on scientific or engineering problems of high relevance in diverse fields. These scorable77
tasks are listed below, with per-node computational costs outlined in Supplementary Table S1.78
scRNA-seq batch integration:17 This task requires distinguishing subtle biological signals from79
noise in high-dimensional sparse datasets. By removing confounding factors, we can enable80
large-scale multi-lab transcriptomic data integration.81
CDC COVID Forecasting:18 This task requires predicting non-linear disease dynamics from82
lagged and noisy real-time data. By predicting COVID cases several weeks in advance, we83
can inform public health policy and resource allocations.84
Time series forecasting:19 This task requires predicting time series outcomes across a range of85
datasets and applications.86
Geospatial segmentation:20 This task requires performing dense pixel-wise multi-label se-87
mantic segmentation on complex satellite imagery. Better segmentation can lead to large88
improvements in environmental monitoring and disaster response.89
ZAPBench:21 This task requires predicting the activity of >70,000 neurons across an entire90
vertebrate brain. Performing well on this benchmark may lead to a systems-level understanding91
of brain function and behavior.92
Numerically solving difficult integrals: This task requires solving integrals that defy standard93
numerical algorithms. It is useful for modeling physical and engineering systems.94
Kaggle Playground Benchmark95
We designed ERA to score highly on a curated set of Kaggle competitions. Kaggle calibrates96
human performance with percentile rank on a leaderboard, and we score code by submitting97
directly to Kaggle. Our benchmark consists of 16 playground competitions from the 202398
season, encompassing regression and classification tasks (Supplementary Table S2). Play-99
ground competitions are an ideal benchmark because they offer fast iteration, simplicity, and100
calibration against thousands of humans. Achieving a high score requires creating complex101
code without requiring solving a sophisticated scientific task.102
Our basic strategy uses a simple prompting template (Supplementary Table S3) that103
concatenates the competition description with the previous trial. Fig. 1b evaluates the104
performance of ERA with the average public percentile rank across all 16 playground105
competitions: ERA substantially beats a single LLM call and best-of-1000 LLM calls, and106
also outperforms AIDE13, owing to its ability to maintain a diverse tree of candidates, allowing107
it to backtrack when a specific line of code mutation plateaus. During the search, the system108
discovers strategies leading to abrupt jumps in the score, with the accumulation of these109
jumps leading to the highest quality solutions.110
Problem-specific advice added to the prompt substantially improves performance. We111
illustrate this with two examples. In TS with expert advice we give ERA standard advice112
to win Kaggle competitions (Supplementary Table S4). In TS with Boosted Decision Tree113
(BDT) we tell ERA to implement a boosted decision tree library from scratch, without114
3
# ACCELE RATED ARTIC
# LE  PREVIEW
using standard packages (Supplementary Table S5). We manually verified in both cases that115
resulting codes followed the advice.116
We now evaluate ERA on six benchmarks in different scientific fields, exploring distinct117
ways to incorporate research ideas to improve system performance (Fig. 1c, Methods).118
Genomics: Batch Integration of Single-Cell RNA Sequencing Data119
Single-cell RNA sequencing (scRNA-seq) has revolutionized our ability to dissect cellular120
heterogeneity, discover novel cell types, infer gene regulatory networks and developmental121
trajectories, and improve therapeutic target prioritization22, enabling hundreds of millions122
of cells to be individually sequenced within thousands of datasets23–25. A major challenge123
required to jointly analyze many disparate scRNA-seq datasets is to computationally remove124
complex batch effects present across samples while preserving biological signals26. Nearly 300125
tools exist to perform batch integration of scRNA-seq data27, and multiple benchmarks have126
been developed for assessing metrics of batch effect removal and conservation of biological127
variability28–30.128
To assess ERA performance on this task, we used the OpenProblems v2.0.0 batch129
integration benchmark30. As of July 2025, this active benchmark evaluates 15 state-of-the-art130
methods and eight control methods on 13 different metrics that quantify both the ability131
to remove batch effects in the data and retain variability attributable to true biological132
differences in six datasets spanning human and mouse25 (Fig. 2a). To avoid overfitting to133
the benchmark, we used a separate dataset for ERA optimization (Methods, Supplementary134
Fig. S1). For each ERA run, we selected the best solution based on the performance on this135
training set, and report the performance on the holdout OpenProblems datasets (n=1,747,937136
total cells). We prompt the LLM with a description of the single cell batch integration137
problem, code for reading in the dataset, code for evaluation metrics, and optional text with138
a particular research idea.139
First, we ran ERA without guidance, and observed that its solution is conceptually140
similar to ComBat31, yet improved over the current OpenProblems leaderboard (No advice141
(TS) in Fig. 2b). We then evaluated whether ERA could improve upon existing algorithms.142
We selected nine methods from the OpenProblems benchmark, including the six highest-143
performing methods (Methods). For each method, we obtained the paper PDF and used144
Gemini 2.5 Pro to add a brief summary to the prompt (Methods). In pairwise comparisons,145
ERA outperformed the corresponding published result for eight of the nine methods in146
overall score (Fig. 2b). The top-performing method was an ERA implementation of Batch147
Balanced K-Nearest Neighbors (BBKNN (TS))32, yielding a 14% overall improvement over148
the best published method (ComBat31) and equaled or outperformed the corresponding149
published BBKNN in every dataset and across 11/13 metrics (Fig. 2b). This performance150
highlights its capacity to effectively remove batch effects without compromising biological151
signals (Supplementary Fig. S2). We observed that ERA is also able to produce performant152
implementations for an algorithm without publicly-available code (TabVI33, Extended Data153
Fig. 1). Importantly, expert manual inspection of the code solutions proposed by ERA154
confirmed that nearly all implementations adhered to the requested algorithms (Extended155
Data Table 1), with performance largely consistent across replicate runs of methods (Extended156
Data Fig. 1). Additionally, ERA demonstrated improvements even when compared to base157
4
# ACCELE RATED ARTIC
# LE  PREVIEW
methods with optimized hyperparameters, indicating that its contribution extends beyond158
hyperparameter tuning (Methods, Supplementary Fig. S3). Extended Data Fig. 2 shows the159
tree structure and evolution of the maximum score as a function of the number of nodes in160
the tree for the best performing model BBKNN (TS).161
For BBKNN (TS), part of the performance boost came from combining two existing methods,162
ComBat31 and BBKNN, rather than simply implementing BBKNN (Fig. 2c). In particular,163
while the original BBKNN method computes neighbors using PCA embeddings, BBKNN (TS)164
computes neighbors using ComBat-corrected PCA embeddings, removing global linear batch-165
associated variance. Both implementations then compute k-nearest neighbors across batches166
and construct a graph (with differences in exact implementation), thus removing local batch167
effects (Supplementary Table S6). Manual modification of BBKNN (TS) and the published168
BBKNN implementation confirmed that using Combat-corrected PCA embeddings is critical169
for improving both implementations (Extended Data Fig. 3), confirming the value in idea170
recombination.171
This motivated an exploration of systematic ways to generate more complex research172
ideas. First, similar to how scientists often combine ideas to create a novel approach, we173
programmatically generated 55 “recombinations” of all pairs of the 11 methods described above174
(No advice, nine replications, and TabVI; hereafter: “base methods”) based on summaries of175
the code for each method (Methods, Supplementary Table S7). We ran ERA, prompted with176
each of these recombinations. For each base method and recombination group, we compared177
the average scores for the top nodes over the intersection of metrics that were successfully178
computed for all three methods. Strikingly, recombination implementations of tree search179
frequently outperformed their base counterparts, with 24 of the 55 recombination solutions180
(44%) outperforming both of their base methods and 22 of the remaining 31 recombination181
solutions outperforming one of the two base methods (Extended Data Fig. 4). Second, we182
used Gemini Deep Research34 and AI co-scientist35 to generate and implement 21 additional183
ideas (Methods). After ERA was applied to each, 6/11 base methods, 29/55 recombination,184
4/9 Deep Research, and 1/12 AI co-scientist methods (40 of 87) outperform all methods185
currently published on the OpenProblems leaderboard (Fig. 2d).186
To further understand the conceptual space explored by ERA, we obtained embeddings187
for each generated code using Gemini text embedding model and computed cosine similarities188
(Supplementary Fig. S4). Visualization of the embeddings revealed distinct clusters, generally189
representing deep-learning based methods and non-deep-learning methods, suggesting that190
ERA is able to generate a variety of solutions (Supplementary Fig. S5).191
Public Health: Prediction of U.S. COVID-19 Hospitalizations192
The primary U.S. benchmark for COVID-19 forecasting is the COVID-19 Forecast Hub193
(CovidHub)18, a large, collaborative effort coordinated by the Centers for Disease Control194
and Prevention (CDC). CovidHub receives weekly forecasts from dozens of expert-led teams195
across academia, industry, and government, each using different methodologies. These196
weekly forecasts must cover new COVID-19 related hospitalizations across 52 U.S. states197
and territories for the current week and three subsequent weeks over 23 specified quantiles.198
Submissions are evaluated using the Weighted Interval Score (WIS), which rewards both199
accuracy and well-calibrated uncertainty.200
5
# ACCELE RATED ARTIC
# LE  PREVIEW
Top-performing individual models include classic autoregressive time-series approaches201
(e.g., UMASS-ar6_pooled), gradient boosting machine learning models (e.g., UMASS-gbqr),202
and epidemiological models based on renewal equations and Bayesian estimation of the203
reproductive number (e.g., CEPH-Rtrend_covid). CovidHub leverages this methodological204
diversity by integrating submissions into the CovidHub Ensemble, a robust aggregate forecast205
that has historically provided the gold standard for epidemiological prediction in the U.S.206
We designed a rigorous retrospective study to assess ERA performance in this competitive207
environment, using data available on May 1 2025. For every forecasting period, we ran ERA208
to optimize and select a model using data from the preceding six weeks, creating a rolling209
validation window throughout the 2024-2025 season (Fig. 3a), with data splits elaborated in210
Supplementary Table S8. The weekly performance of our resulting ‘Google Retrospective’211
model is detailed in the time-series leaderboard (Fig. 3b), which visualizes our model’s212
performance advantage relative to the CovidHub-ensemble and other top-performing teams.213
The temporal variation of WIS for each of the separate validation splits is shown for the214
best replicate (Extended Data Fig. 5) and across replicates (Supplementary Fig. S6). A215
direct jurisdiction-level comparison confirms our model achieved a lower (better) WIS in a216
majority of states (Fig. 3c,d). Supplementary Figs. S7 and S8 compare prediction curves for217
representative locations between different models.218
Overall, our model achieved the highest performance with an average WIS of 26, out-219
performing the official CovidHub Ensemble’s average WIS of 29. A representative tree and220
breakthrough plot is shown in Extended Data Fig. 6.221
Beyond this retrospective performance, we investigated ERA’s ability to explore the solu-222
tion space more broadly by replicating, recombining, and generating entirely new forecasting223
strategies (Fig. 3e). First, we tested its ability to replicate existing methods from other teams224
using only their brief public descriptions from the CovidHub (Supplementary Tables S9 and225
S10). Our tree-search-based implementations (‘Base Method (TS)’) not only adhered to the226
provided instructions (Supplementary Table S11) but also exceeded the performance of the227
original submissions in six of the eight cases tested; the two models that performed worse228
(replicating JHU_CSSE-CSSE_Ensemble and OHT_JHU-nbxd) did not use external data present229
for the original method implementations. Next, we explored whether solutions could be230
improved through recombination. For this experiment, we prompted an LLM to analyze the231
core principles of two different parent models and then used its synthesis to instruct ERA to232
generate a novel hybrid strategy combining their respective strengths. Of 26 generated hybrid233
models (‘Recombination (TS)’), 11 achieved a WIS score superior to both of their parent234
models (Extended Data Fig. 7). We manually verified that output code for all recombination235
experiments contained relevant aspects from both parent codes (Supplementary Table S11).236
Finally, we used Gemini Deep Research34 and AI co-scientist35 to generate novel forecast-237
ing ideas which were then implemented using ERA. In total, this systematic exploration238
yielded 14 distinct strategies that outperformed the official CovidHub-ensemble: 10 from239
recombination, two from Deep Research, one from AI co-scientist, and one of our replicated240
baselines. Cosine similarities between embeddings for each generated code show clustering241
between different methods (Supplementary Fig. S9). An extended performance plot including242
the 9 TS models and 3 other submissions that did not outperform the baseline, alongside243
their corresponding validation performance, is provided in Supplementary Figs. S10 and S11.244
Examples of prediction curves are shown in Supplementary Fig. S12.245
6
# ACCELE RATED ARTIC
# LE  PREVIEW
A deeper analysis of these 14 top-performing strategies reveals key patterns in how246
ERA achieves superior performance. The recombination models, which constitute the247
majority of the winners, highlight a clear pattern of synergistic hybridization. Two base248
models appear most frequently in these successful hybrids: the simple, climatology-based249
CMU-climate_baseline and the statistical autoregressive model UMass-ar6_pooled. This250
suggests ERA consistently discovers that the most effective strategies are built upon a251
robust foundation of historical averages and recent trends, which are then enhanced by more252
complex methods. Indeed, the most successful recombinations consistently fused different253
modeling paradigms: for instance, pairing the epidemiological CEPH-Rtrend_covid model254
with the statistical UMass-ar6_pooled model created a hybrid anchored in the theory of255
disease spread yet highly responsive to recent data trends, while pairing the powerful machine256
learning UMass-gbqr model with the stable CMU-climate_baseline provided a robust seasonal257
foundation that allowed the ML model to safely focus on learning short-term deviations.258
Finally, we verified the importance of using ERA, rather than just taking the best of 1000259
solution attempts, for both epidemiological modeling and scRNA-seq batch integration260
(Table 1).261
Time Series Forecasting: GIFT-Eval262
We next evaluated ERA using General Time Series Forecasting Model Evaluation (GIFT-263
Eval)19, a standard benchmark for time series forecasting. GIFT-Eval includes 28 datasets264
across seven diverse domains, with data frequencies ranging from seconds to years. It265
receives ∼4 new submissions per month that span diverse methodologies including black-266
box deep learning methods and foundation models. Submissions are scored on official267
train/validation/test splits using a normalized Mean Absolute Scaled Error (MASE) metric,268
calculated relative to a seasonal naive baseline.269
We applied ERA in two phases. We began with a per-dataset solution in which ERA270
discovers an independent solution for each dataset. The second unified solution created a271
single general-purpose forecasting model using only basic libraries by hill-climbing against272
the average score for the entire GIFT-Eval.273
Per-dataset solution Here we allowed ERA to use a full suite of Python libraries, including274
scikit-learn, statsmodels, and xgboost. ERA outperformed the entire May 18, 2025275
leaderboard, which included foundation models, deep learning models, and standard time series276
methods (Supplementary Table S12). The discovered solutions showed strong convergence277
towards gradient boosting and ensemble/decomposition models (Supplementary Fig. S13).278
Unified solution We wondered whether the code mutation system could create a unified,279
general-purpose forecasting library from scratch, by hill climbing with a single code on the280
average MASE on the entire GIFT-Eval dataset. To manage the benchmark’s diversity, we281
allowed the library to have an adaptive configuration system, whereby it could generate up to282
8 preset hyperparameter configurations to adapt to the diversity of datasets, with a validation283
step selecting the best performing configuration for each dataset. As the search progressed,284
date and trend-related features often led to performance breakthroughs leading to a model285
7
# ACCELE RATED ARTIC
# LE  PREVIEW
that sequentially forecasts and subtracts individual time series components, including a base286
level, trend, seasonality, datetime-based features, and a final residual correction (Extended287
Data Fig. 8). The configurations (Supplementary Table S13) include date-specific features,288
including one that featurizes holidays in a specific set of countries ([‘US’, ‘DE’, ‘CN’, ‘GB’,289
‘CA’, ‘AU’]) . The resulting unified solution was highly competitive on the May 2025290
leaderboard (Supplementary Table S12).291
Other Problems: Geospatial Analysis, Neuroscience and Numerical292
Analysis293
We also evaluated ERA on problems from three additional distinct domains: geospatial294
semantic segmentation, vertebrate neural activity forecasting, and numerical analysis (Sup-295
plementary Notes). ERA achieved expert-level performance in each case (Supplementary296
Figs. S14–S20, Supplementary Table S14).297
### Discussion298
Our work introduces ERA, an AI-based system that drives a Tree Search (TS) with a Large299
Language Model (LLM) to systematically create and improve software for scientific tasks. By300
defining the problem of creating scientific software as a search for a program whose output301
maximizes a quality score, we convert software creation into a “scorable task”, producing302
empirical software. ERA is novel in its LLM-driven rewriting approach, which allows for the303
flexible integration of domain knowledge and external research ideas. The ability of frontier304
LLMs to closely follow instructions enables efficient exploration of research ideas. ERA305
builds upon ideas from several distinct but related areas of research: Genetic Programming,306
Generative Programming, the application of LLMs to code, Automated Machine Learning307
(AutoML), Combining LLMs and Search, and agents for scientific discovery.308
Genetic Programming — Genetic Programming (GP) provides a foundation to our work.309
In GP, a population of programs is iteratively improved using evolutionary principles like310
selection, crossover, and mutation. The fitness of each program is determined by a “fitness311
function,” which is directly analogous to our “quality score” 36. While GP has been successful,312
it traditionally relies on random mutations and structured recombination of code fragments313
(e.g., swapping sub-trees in an abstract syntax tree). Prior to the widespread adoption of314
large language models, GP systems successfully incorporated human expertise by restricting315
the search space using formal grammars or leveraging structural code metrics to bias the316
evolutionary search37. A key difference in ERA is the use of an LLM to perform intelligent,317
semantic-aware "mutations" by rewriting the code, which can produce more complex and318
meaningful variations than the random changes typical in GP.319
Generative Programming — ERA can be viewed as a modern AI-driven realization of320
traditional generative programming, where, a developer creates a program generator (using321
techniques like templates, domain-specific languages38, or metaprogramming) that produces322
tailored source code for a family of related problems39. In contrast, we use an LLM guided323
by a tree search as the generative engine. This approach offers greater flexibility, allowing324
8
# ACCELE RATED ARTIC
# LE  PREVIEW
ERA to synthesize novel programs by exploring a vast solution space and integrating diverse325
domain knowledge in ways not easily achievable with more template-based methods.326
LLMs for Code Generation — The advent of large language models pre-trained on vast327
code corpora has revolutionized code generation. Systems like AlphaCode40 and OpenAI328
Codex41 have demonstrated the ability to generate correct and complex code from natural329
language descriptions. These systems are typically used for “one-shot” generation from a330
prompt. Our approach differs by using the LLM in an iterative refinement loop. Instead of331
generating code from scratch, our LLM rewrites existing software candidates, guided by a332
search algorithm (TS) that uses the quality score as a signal.333
AutoML — AutoML systems aim to automate the process of building machine learning334
pipelines by searching for optimal model architectures and hyperparameters. The goal is to335
maximize a performance metric (e.g., accuracy, F1-score) on a validation dataset42, which336
fits our definition of a scorable task. While AutoML focuses specifically on finding the best337
model within a fixed set of ML frameworks, ERA is more general. It can rewrite any software,338
including pre-processing steps, complex simulations, mathematical heuristics, and other areas339
that fall outside the typical scope of AutoML.340
Combining LLMs and Search — The most closely related work involves combining LLMs341
with search algorithms to overcome the limitations of one-shot generation. A rapidly growing342
body of literature formulates automated algorithm design as an Evolutionary Algorithm343
(EA)43,44. FunSearch uses an LLM to search for new mathematical discoveries by pairing a344
LLM suggesting code improvements with an automated evaluator15. Very recently, agentic345
frameworks like AlphaEvolve14 have expanded these evolutionary coding loops towards needle-346
in-the-haystack discovery problems, similar in spirit to the tree search algorithms explored347
here, albeit without idea exploration required for scientific problem solving.348
Agents for science problems — This sub-field has seen remarkable performance from349
highly specialized systems, with agents focusing on problems ranging from data science45 to350
computational biology46. Instead of specializing in one domain, ERA demonstrates a general351
capability for empirical software optimization, achieving expert-level performance on public352
leaderboards and in academic literature across multiple fields.353
To our knowledge, this is the first work demonstrating a system that beats human354
performance on a wide range of relevant and well-studied scientific problems. Across different355
fields, by prompting with the method description from cutting edge papers, ERA not only356
produces code that follows the methods of the paper but often has superior results.357
We would like to emphasize the critical distinction between optimizing empirical predictive358
models and performing genuine scientific discovery, the latter of which requires reasoning359
about underlying theories, causal mechanisms, and mathematical frameworks. While the360
core problems evaluated in this paper primarily emphasize advanced empirical software361
engineering to allow for rigorous, automated scoring, our underlying system goes well beyond362
this, towards scientific discovery (Supplementary Notes).363
The ability of LLM-based systems to autonomously produce expert-level empirical software364
carries broader safety risks, particularly when applied to domains that could directly impact365
human well-being. By automating complex engineering workflows, our system significantly366
lowers the technical expertise required to execute sophisticated computational tasks. While367
this democratization accelerates beneficial scientific discovery, it concurrently lowers the368
barrier to entry for deploying advanced models in sensitive or potentially dangerous domains.369
9
# ACCELE RATED ARTIC
# LE  PREVIEW
This phenomenon represents a broader, systemic risk associated with the combination of370
large-scale inference-time compute and exponentially increasing foundation model quality.371
To summarize, ERA combines a code mutation system based on Tree Search2 with372
the ability to integrate complex research ideas. Such research ideas could come from the373
published literature, from research agents (e.g.34,35) or from combining previous ideas and374
solutions that the LLM has found itself. Because ERA creates code that can follow a375
specific idea, it can search over externally-supplied research ideas. ERA created 40 methods376
that beat the best known method for scRNA-seq batch integration and 14 methods that377
outperformed the CDC ensemble for epidemiological prediction. Additionally, ERA achieved378
expert-level performance on geospatial reasoning, neural activity prediction and algorithms379
for computational mathematics and a novel rule-based strategy for time series prediction.380
Trial and error is essential to scientific progress, both for humans and for the automated381
approaches we outline here. ERA generates expert-level solutions extraordinarily quickly,382
reducing exploration of a set of ideas from weeks or months, to hours or days. Accelerating383
research in this way has profound consequences for scientific advancement. Based on this384
work, we believe that progress in scientific fields where solutions can be scored by machines385
is on the precipice of a significant acceleration.386
### References387
[1] Hannay, J. E. et al. How do scientists develop and use scientific software? In 2009388
ICSE Workshop on Software Engineering for Computational Science and Engineering,389
1–8 (IEEE, 2009).390
[2] Silver, D. et al. Mastering the game of Go with deep neural networks and tree search.391
Nature 529, 484–489 (2016).392
[3] Hohenberg, P. & Kohn, W. Inhomogeneous electron gas. Phys. Rev. 136, B864 (1964).393
[4] Kohn, W. & Sham, L. J. Self-consistent equations including exchange and correlation394
effects. Phys. Rev. 140, A1133 (1965).395
[5] Warshel, A. & Levitt, M. Theoretical studies of enzymic reactions: dielectric, electrostatic396
and steric stabilization of the carbonium ion in the reaction of lysozyme. J. Mol. Biol.397
103, 227–249 (1976).398
[6] Jumper, J. et al. Highly accurate protein structure prediction with AlphaFold. Nature399
596, 583–589 (2021).400
[7] Baek, M. et al. Accurate prediction of protein structures and interactions using a401
three-track neural network. Science 373, 871–876 (2021).402
[8] Hourdin, F. et al. The art and science of climate model tuning. Bull. Am. Meteorol.403
Soc. 98, 589–602 (2017).404
[9] Anderson Jr., J. Basic philosophy of CFD. In Computational Fluid Dynamics, 3–14405
(Springer, 2009).406
10
# ACCELE RATED ARTIC
# LE  PREVIEW
[10] Silver, N. The signal and the noise: why so many predictions fail-but some don’t (Penguin,407
2012).408
[11] Farmer, J. D. Making sense of chaos: a better economics for a better world (Yale Univ.409
Press, 2024).410
[12] Sculley, D. et al. Hidden technical debt in machine learning systems. In Advances in411
Neural Information Processing Systems, vol. 28 (2015).412
[13] Jiang, Z. et al. AIDE: AI-driven exploration in the space of code. arXiv preprint413
arXiv:2502.13138 (2025).414
[14] Novikov, A. et al. AlphaEvolve: A coding agent for scientific and algorithmic discovery.415
arXiv preprint arXiv:2506.13131 (2025).416
[15] Romera-Paredes, B. et al. Mathematical discoveries from program search with large417
language models. Nature 625, 468–475 (2024).418
[16] Hu, S., Lu, C. & Clune, J. Automated design of agentic systems. arXiv preprint419
arXiv:2408.08435 (2024).420
[17] Xu, C. et al. Automatic cell-type harmonization and integration across Human Cell421
Atlas datasets. Cell 186, 5876–5891.e20 (2023).422
[18] Centers for Disease Control and Prevention. COVID-19 forecast hub (2025). https:423
//github.com/cdcgov/covid19-forecast-hub?tab=readme-ov-file.424
[19] Aksu, T. et al. GIFT-Eval: a benchmark for general time series forecasting model425
evaluation. arXiv preprint arXiv:2410.10393 (2024). https://huggingface.co/spaces/426
Salesforce/GIFT-Eval.427
[20] Shao, Z., Yang, K. & Zhou, W. Performance evaluation of single-label and multi-label428
remote sensing image retrieval using a dense labeling dataset. Remote Sens. 10, 964429
(2018).430
[21] Lueckmann, J.-M. et al. ZAPBench: a benchmark for whole-brain activity prediction in431
zebrafish. arXiv preprint arXiv:2503.02618 (2025).432
[22] Jovic, D. et al. Single-cell RNA sequencing technologies and applications: a brief433
overview. Clin. and Transl. Med. 12, e694 (2022).434
[23] Svensson, V., Vento-Tormo, R. & Teichmann, S. A. Exponential scaling of single-cell435
RNA-seq in the past decade. Nat. Protoc. 13, 599–604 (2018).436
[24] Regev, A. et al. The Human Cell Atlas. eLife 6, e27041 (2017).437
[25] CZI Cell Science Program et al. CZ CELLxGENE Discover: a single-cell data platform438
for scalable exploration, analysis and modeling of aggregated data. Nucleic Acids Res.439
53, D886–D900 (2025).440
11
# ACCELE RATED ARTIC
# LE  PREVIEW
[26] Stuart, T. & Satija, R. Integrative single-cell analysis. Nat. Rev. Genet. 20, 257–272441
(2019).442
[27] Zappia, L., Phipson, B. & Oshlack, A. Exploring the single-cell RNA-seq analysis443
landscape with the scRNA-tools database. PLoS Comput. Biol. 14, e1006245 (2018).444
[28] Tran, H. T. N. et al. A benchmark of batch-effect correction methods for single-cell445
RNA sequencing data. Genome Biol. 21, 1–32 (2020).446
[29] Chazarra-Gil, R., van Dongen, S., Kiselev, V. Y. & Hemberg, M. Flexible comparison of447
batch correction methods for single-cell RNA-seq using BatchBench. Nucleic Acids Res.448
49, e42 (2021).449
[30] Luecken, M. D. et al. Defining and benchmarking open problems in single-cell analysis.450
Nat. Biotechnol. 43, 1035–1040 (2025).451
[31] Johnson, W. E., Li, C. & Rabinovic, A. Adjusting batch effects in microarray expression452
data using empirical Bayes methods. Biostatistics 8, 118–127 (2007).453
[32] Polański, K. et al. BBKNN: fast batch alignment of single cell transcriptomes. Bioinfor-454
matics 36, 964–965 (2019).455
[33] Chandrashekar, A. et al. TabVI: leveraging lightweight transformer architectures to456
learn biologically meaningful cellular representations. bioRxiv 2025–02 (2025).457
[34] Google. Gemini Deep Research (2025). https://gemini.google/overview/458
deep-research/?hl=en.459
[35] Gottweis, J. et al. Towards an AI co-scientist. arXiv preprint arXiv:2502.18864 (2025).460
[36] Koza, J. R. Genetic programming as a means for programming computers by natural461
selection. Stat. Comput. 4, 87–112 (1994).462
[37] Schweim, D., Hemberg, E., Sobania, D., O’Reilly, U.-M. & Rothlauf, F. Using knowledge463
of human-generated code to bias the search in program synthesis with grammatical464
evolution. In Proceedings of the Genetic and Evolutionary Computation Conference465
Companion, 331–332 (2021).466
[38] Mernik, M., Heering, J. & Sloane, A. M. When and how to develop domain-specific467
languages. ACM computing surveys (CSUR) 37, 316–344 (2005).468
[39] Czarnecki, K. Generative programming: Methods, techniques, and applications tutorial469
abstract. In International Conference on Software Reuse, 351–352 (Springer, 2002).470
[40] Li, Y. et al. Competition-level code generation with AlphaCode. Science 378, 1092–1097471
(2022).472
[41] Chen, M. et al. Evaluating large language models trained on code. arXiv preprint473
arXiv:2107.03374 (2021).474
12
# ACCELE RATED ARTIC
# LE  PREVIEW
[42] Hutter, F., Kotthoff, L. & Vanschoren, J. Automated machine learning: methods, systems,475
challenges (Springer Nature, 2019).476
[43] Wu, X., Wu, S.-h., Wu, J., Feng, L. & Tan, K. C. Evolutionary computation in the era477
of large language model: survey and roadmap. IEEE Trans. Evol. Comput. (2024).478
[44] Ma, Z., Guo, H., Gong, Y., Zhang, J. & Tan, K. Toward automated algorithm design:479
A survey and practical guide to meta-black-box-optimization. IEEE Transactions on480
Evolutionary Computation (2025).481
[45] Ifargan, T., Hafner, L., Kern, M., Alcalay, O. & Kishony, R. Autonomous LLM-driven482
research—from data to human-verifiable research papers. NEJM AI 2, AIoa2400555483
(2024).484
[46] Xiao, Y. et al. CellAgent: An LLM-driven multi-agent framework for automated485
single-cell data analysis. arXiv preprint arXiv:2407.09811 (2024).486
13
# ACCELE RATED ARTIC
# LE  PREVIEW
### Figure Legends487
Fig. 1 | Schematic and performance of ERA. a, Schematic of ERA algorithm. A scorable task, together with research ideas proposing methods to solve the task, are fed to an LLM, which produces code to evaluate the scorable task in a sandbox. This is then embedded within a tree search algorithm, whereby new nodes are chosen balancing exploitation and exploration, sampling from the LLM (Methods). b, Performance of code generation methods on Kaggle Playground benchmark. Results report the average public leaderboard percentile performance over 16 tasks. Methods based on ERA are listed in bold. TS, ERA-based tree search. BDT, boosted decision tree. Error bars indicate standard deviation of performance between different competitions in the benchmark. c, The system automates empirical software development by iteratively optimizing predictive models and computational algorithms based on research ideas and a defined quality metric. We use LLM summaries of scientific papers or AI assisted literature as part of the prompt, and also recombine successful implementations of ideas to create more powerful methods.
14
# ACCELE RATED ARTIC
# LE  PREVIEW
Fig. 2 | Performance of ERA on scRNA-seq batch integration. a, Schematic of the batch integration task, in which disparate datasets (teal and red) are processed to remove batch effects in the data while retaining biological variability. b, Performance of tree search (method names bolded and suffixed by “(TS)”) compared to the analogous published method on the OpenProblems benchmark v2.0.030. “Perfect embedding by celltype with jitter” is a positive control method that represents the best possible performance and “Shuffle integration by batch” is a negative control that does not perform any batch integration. Overall score is the mean over all datasets and metrics. Each Datasets column shows the mean of all metrics computed over that dataset. Each Metrics column shows the mean of that metric computed over all datasets. Metrics were assigned a value of 0 if they could not be computed or if their performance was worse than the lowest negative control; these are displayed as empty. c, Performance improvements annotated with code innovation for the top-performing batch balanced k-nearest neighbors (BBKNN) implementation. ComBat-based embedding generation was introduced in implementation attempt 429. d, Overall score for OpenProblems benchmark v2.0.030 non-control methods, ERA with and without recombination of ideas, Gemini Deep Research34, and ERA with AI co-scientist35. Y-axis lower bound is the overall score of the “Shuffle integration by batch” negative control method. Seven recombination, five base methods, and two AI co-scientist methods that do not match its performance are omitted. * indicates the method is a recombination, even if not explicitly prompted for recombination. TS, ERA-based tree search; fastMNN, batchelor fastMNN; mnnCorrect, batchelor mnnCorrect.
15
# ACCELE RATED ARTIC
# LE  PREVIEW
Fig. 3 | Performance of ERA on COVID-19 forecasting. a, Rolling validation window used for the forecasting experiments. Each search’s output is validated internally on a preceding block of time (blue), and the resulting model is then used to make predictions for its corresponding forecasting period (orange). Training data includes all dates on or after 2020-08-08 and prior to the validation set. b, Time-series leaderboard showing weekly forecasting performance (Average WIS) for participating teams and our ’Google Retrospective’ model, ordered by average WIS. Scores are aggregated across all 52 jurisdictions and four forecast horizons. The number within each cell is the model’s absolute Average WIS for that week. The cell’s background color visualizes the performance relative to the CovidHub-ensemble, with blue indicating a lower (better) WIS and red indicating a higher (worse) WIS. c, Direct jurisdiction-level comparison of forecasting error (Average WIS) between our model and the ’CovidHub-ensemble’, demonstrating our model’s superior performance in a majority of locations. d, Geographic distribution of our model’s forecasting error (Average WIS), aggregated over the entire 2024/25 COVID-19 season. Lower error values (lighter colors) indicate better performance. e, Comparison of aggregate forecasting performance for various modeling strategies. This includes baseline models from the CovidHub competition, our retrospective model, our replications of submitted models, novel hybrid models generated through recombination, deep research34 and AI co-scientist35. 14 strategies (10 recombination; two Deep Research; one AI co-scientist and one replicated baseline) outperform the official CovidHub-ensemble for the 3-week (3 reference dates × 4 time horizons × 52 jurisdictions) evaluation period. Models that perform worse than CovidHub-baseline are not shown.
16
# ACCELE RATED ARTIC
# LE  PREVIEW
### Tables488
Table 1 | Performance comparison of ERA and Best-of-N on the scRNA-seq batch integration and epidemiological modeling tasks. Performance is measured on the validation set for each task. Bold entries indicate better performance. BoN, best-of-N=1000.
Model Method Batch integration Epidemiology (higher better) (lower better)
Gemini 2.5 Flash BoN 0.6306 106.55 ERA 0.6552 93.07
Mistral Medium BoN 0.6129 95.73 ERA 0.6332 87.98
Claude Sonnet 4.6 BoN 0.6502 85.03 ERA 0.6575 84.56
GPT-5 BoN 0.6740 78.04 ERA 0.6671 74.55
Gemini 3.1 Pro BoN 0.6461 92.39 ERA 0.6641 72.70
17
# ACCELE RATED ARTIC
# LE  PREVIEW
### Methods489
Code mutation system490
We prompt an LLM providing a description, the evaluation metric and the relevant data.491
The LLM produces Python code, which is then executed and scored on a sandbox. Searching492
over strategies dramatically increases performance: The system uses the score together with493
output logs and other information to hill climb towards a better score. We used a tree search494
(TS) strategy with an upper confidence bound (UCB) inspired by AlphaZero47. A critical495
difference from AlphaZero is that our problems don’t allow exhaustive enumeration of all496
possible children of a node, so every node is a candidate for expansion. We therefore modify497
the UCB algorithm to count visits and compute mean values using the tree. However, when498
sampling a node to expand, we sample directly from the whole set instead of recursing from499
the root like AlphaZero. This makes our method closer to Flat UCB48 than any MCTS500
variant like AlphaZero.501
We also note that the algorithm differs from traditional TS, in that the scoring of the502
nodes do not involve random rollouts (e.g. of a game) to estimate the value of a node. Yet503
there is still randomness for scoring each node, caused by the sampling of the LLM itself,504
which produces a distribution of different codes (scores) for each fixed prompt.505
We use a PUCT tree search algorithm to explore the space of code2. The PUCT (Predictor506
+ Upper Confidence bound applied to Trees) algorithm is described in Algorithm 1. For tree507
T , and executed candidate u, we define the flat prior PT (u) = 1 |T | . To make it easier to tune508
the exploration constant cpuct across tasks, we convert task-specific scores TaskScore(u) to509
rank scores RankScoreT (u) in the PUCT formula. We define RankScoreT (u) = RankT (u)−1 |T |−1
,510
when |T | > 1, and 1 otherwise, where RankT (u) gives ascending-order ranks to the candidates.511
To select the next node for expansion, the algorithm balances exploitation of high-scoring solutions with exploration of the search space by computing a PUCT-inspired (Polynomial Upper Confidence Trees) acquisition score for each node i:
PUCTi = ri + cpuct · E(i) (1)
where cpuct is the exploration constant and E(i) is an exploration term based on the node’s512
visit count relative to the total number of visits across the entire tree. We tuned cpuct on the513
Kaggle benchmark to maximize performance, finding cpuct = 1 works well. The node with the514
globally maximum PUCTi score is selected. The language model then generates a single novel515
child solution conditioned on this parent’s code and score. The new code is executed, assigned516
an empirical score, and appended to the search tree, followed by a backpropagation of the517
visit count to its ancestors. This global, flat-tree structure allows the system to seamlessly518
backtrack and branch from any historical node if the current optimization path plateaus.519
We emphasize that in our algorithm mutations occur at the code level – ideas are part of520
prompts that produce code, that is then scored and iterated upon. With increasing nodes in521
the tree, the score saturates after 300-1000 nodes (See Breakthrough plots in Supplementary522
Figures). We search over ideas by combining different tree searches with different prompts523
together.524
Finally, the implementation we outline here was chosen for optimal performance on the525
Kaggle Benchmark. Many alternatives were explored, including different agentic configurations526
18
# ACCELE RATED ARTIC
# LE  PREVIEW
and the simple implementation outlined here had the highest overall performance across the527
benchmark. All experiments in this paper were carried out with Gemini 2.5 Flash, with the528
improvement with Gemini 2.5 Pro modest.529
Algorithm 1 UCB tree search (PUCT) Input: GenerateAndExecute(), TaskScore() to define rank scores RankScoreT (u), exploration
constant cpuct, and a root node r. 1: T ← {r} ▷ Initialize the tree with a root node. 2: V (r)← 1 3: for all iterations do 4: Ntotal ←
∑ u∈T V (u) ▷ Get total visits across all nodes
5: Select u∗ ← argmaxu∈T
( RankScoreT (u) + cpuctPT (u)
√ Ntotal
1+V (u)
) ▷ Select node with
highest PUCT score 6: uc ← GenerateAndExecute(u∗) ▷ Expand the selected node and Execute 7: T ← T ∪ {uc} 8: V (uc)← 1 9: for all ancestors ua of uc (excluding uc) do ▷ Backpropagate results
10: V (ua)← V (ua) + 1 11: end for 12: end for 13: return argmaxu∈TTaskScore(u) ▷ Best solution found
It is useful to explicitly contrast this algorithm with standard heuristic search algorithms.530
Our approach does not rely on beam search (which aggressively prunes unselected candidates531
at each depth layer) nor a (1 + λ) evolution strategy (which maintains only the most recent532
generation and discards historical states).533
Similarly, our system differs from emergent efforts to incorporate LLMs into GPs43,44,49–51.534
More recently, agentic AutoML frameworks encompass automated feature engineering,535
meta-learning, dynamic pipeline construction, and multi-objective optimization52, including536
agentic systems53,54, which have shown more impressive performance55.537
Adding research ideas to the code mutation system538
When an expert solves difficult scientific problems, they often search for prior work for ideas.539
Prior work could be sourced from highly cited papers, specialized textbooks, or search engines.540
The search for prior work can also be powered by LLMs34,35,56–60.541
We emulate the expert behavior by injecting instructions for carrying out research ideas542
into the prompt of our code mutation system (Fig. 1). We applied the research instruction543
injection for scRNA-seq batch integration, COVID prediction, segmenting remote sensing544
images, and whole-brain neural activity prediction. While the most successful outcomes545
used top methods from the literature, we also used two LLM driven search strategies: Deep546
Research from Gemini 2.5 Flash34 and AI co-scientist35.547
For running these searches, we provided the tools with background information from the548
main problem description, and instructed the models to create distinct ideas (Supplementary549
19
# ACCELE RATED ARTIC
# LE  PREVIEW
Table S15). After manually filtering proposals and removing one proposed scRNA-seq batch550
integration method, we prompted Gemini to format the ideas into a structure consistent with551
our baseline method descriptions (Supplementary Table S16). Finally, we ran ERA on these552
ideas to create empirical codes that could be scored.553
ERA versus best-of-N554
We use N = 128 ERA search nodes and compare the performance of Gemini 2.5 Flash, Mistral555
Medium, Claude Sonnet 4.6, GPT-5, and Gemini 3.1 Pro on the scRNA-seq batch integration556
task and an epidemiological flu forecasting task. This explores a range of models that were557
contemporaneous with the core model used in this paper (Gemini 2.5 Flash) while also using558
Gemini 3.1 Pro as a state-of-the-art model at the time of paper publication. The scores559
use the same scoring rules as in all other experiments: for the epidemiological forecasting560
task it is the Weighted Interval Score evaluated over a rolling evaluation window, while for561
scRNA-seq batch integration it is the average of metrics measuring preservation of biological562
information while eliminating batch effects, both measured on the validation set. Note that563
significant improvements in batch integration happen with much smaller change in validation564
scores than in epidemiological forecasting. We present here the best performance over 3565
different experiments (with both Best-of-N and ERA). Typical variation in performance is of566
order 0.01 for batch integration and O(1) for epidemiological forecasting, with some model567
dependence. For example, GPT-5 has much more experiment-to-experiment variability than568
other models.569
We note that ERA explores the solution space more efficiently than Best-of-N, and570
outperforms Best-of-N for all models and problems, with the exception of GPT-5’s performance571
on batch integration. On the batch integration problem, GPT-5’s one shot performance572
is sufficiently good that this distinction isn’t important. Indeed we expect that as frontier573
models improve, tasks that were once difficult will saturate. Tree search is useful for pushing574
model performance on difficult tasks.575
Recombination experiments576
For both scRNA-seq batch integration problem and COVID-19 forecasting, we combined577
ideas from methods already generated using tree search. For the scRNA-seq batch integration578
problem, we used the first versions of our 11 baseline methods. For the COVID-19 prediction579
problem, we used the eight replications of models submitted to CovidHub. We first took the580
top-performing node from each tree search run seeded with one of these methods, based on581
its score on the validation set (for COVID-19 prediction, this included six weeks of reference582
dates from 2025-02-22 to 2025-03-29). Then, for every pair of these methods, we prompted583
Gemini 2.5 Flash to compare the two methods and explain the core technical similarities584
and differences between the two parent models using a consistent prompt (Supplementary585
Table S7). The explanatory response was then added to the the prompt, along with a586
statement instructing tree search to recombine the ideas by combining the best parts of both587
approaches (Supplementary Table S17). Subsequently, we ran ERA to generate new hybrid588
strategies. This process yielded 55 recombined methods for the scRNA-seq batch integration589
20
# ACCELE RATED ARTIC
# LE  PREVIEW
problem, and 28 for the COVID-19 prediction problem (evaluated on the three-week holdout590
set 2025-04-05 to 2025-04-19, see Fig. 3e).591
Our method for recombination differs from previous efforts where the LLM acts as a592
mutation and crossover operator49–51,61–64. Our approach to recombining expert ideas is593
conceptually related to evolutionary methods such as RHEA, with the comparative advantage594
that our tree search recombines expert ideas directly in conceptual space via LLM prompts595
rather than solely in distilled model space65.596
Gemini embeddings597
For each tree search implementation, we input the code snippets to the Gemini text embed-598
ding model66, and the resulting 3,072-dimensional output vectors served as the semantic599
representations of their respective implementations.600
scRNA-seq batch integration601
For all scRNA-seq experiments, we ran tree search with 500 nodes. Each experiment took602
roughly seven hours to execute on our infrastructure.603
Dataset We sourced a dataset from CZ CELLxGENE Discover25 to use for hill climbing604
with tree search. To identify datasets distinct from the six OpenProblems.bio test datasets605
but that have similar characteristics, we filtered to datasets that contain only healthy hu-606
man cells, with primary cell count ≥ 2,000, at least 10 unique cell types, at least seven607
unique donor ids (i.e. number of batches), and contain at least two unique assays that are608
also present in the OpenProblems.bio datasets. This filtering process identified 22 candi-609
date datasets. After manually investigating the candidate datasets, we selected the dataset610
364bd0c7-f7fd-48ed-99c1-ae26872b1042 version ffdaa1f0-b1d1-4135-8774-9fed7bf039ba17.611
Within the selected dataset, we applied quality control metrics and data processing612
steps identical to the processing performed on the OpenProblems.bio datasets67,68, yielding613
a processed dataset with normalized expression values, highly variable genes, principal614
components, and k-nearest neighbors all computed. For computational efficiency, we randomly615
selected two disjoint subsets of N = 20, 000 cells each, attempting to match (batch, cell616
type) distributions of the entire processed dataset. The “train” dataset was used for model617
training and selection of the highest-performing node in a single tree search. The “validation”618
dataset was used to select the best tree search for methods in which we ran multiple replicates619
of the same algorithm (Supplementary Fig. S1).620
Evaluating scRNA-seq Batch Integration on the OpenProblems.bio Benchmark621
We downloaded the OpenProblems v2.0.0 input and solution data from s3://openproblems-data/622
resources/task_batch_integration/datasets/cellxgene_census/ and raw performance623
metrics from s3://openproblems-data/resources/task_batch_integration/results/run_624
2025-01-23_18-03-16/score_uns.yaml. We computed control-scaled metric results identi-625
cally to the published OpenProblems results. Briefly, for each (dataset, metric), lower626
and upper bounds on raw scores are defined as the minimum and maximum values achieved627
21
# ACCELE RATED ARTIC
# LE  PREVIEW
by the seven “control” methods. Raw values were linearly scaled between those extrema628
and clamped to be in [0, 1]. Overall score was computed as the arithmetic mean over all 78629
measurements (13 metrics computed for each of 6 datasets) with NaN values replaced by 0630
(i.e., failure to compute a metric causes it to be considered the worst possible score).631
Replication of Existing Methods for Batch Integration The OpenProblems.bio632
benchmark profiles the performance of several state-of-the-art existing methods. As of July633
11, 2025 there were 19 different methods. Three methods have implementations in both R634
and Python: LIGER and pyliger, Harmony and Harmonypy, and batchelor mnnCorrect and635
mnnpy. After grouping reimplementations of the same method, there are 16 separate research636
ideas. From this list, we excluded all six foundation model methods (UCE, SCimilarity,637
scGPT (zero shot), scGPT (fine-tuned), Geneformer, and scPRINT) because they perform638
very poorly on the benchmark and use a much larger training set. For example, only a single639
foundation model (UCE) performs better than the negative control of “No integration” which640
simply performs PCA on the dataset. We further excluded scANVI, which is a modification641
of scVI that is trained using cell type information. Since cell type information is used to642
define the metrics, this represents data leakage and consequently we consider scANVI a control643
method. This resulted in nine existing different research methods to optimize with tree644
search.645
For each of the nine existing methods, we obtained the manuscript PDF corresponding to646
the method. To obtain a short method description from the manuscript, we used Gemini 2.5647
Pro Thinking to summarize the paper (prompt in Supplementary Table S18, example output648
in Supplementary Table S19). For batchelor fastMNN, which is a faster implementation649
of batchelor mnnCorrect, there is no separate publication and thus we provided the paper650
PDF of batchelor mnnCorrect as well as the docstring corresponding to batchelor fastMNN651
from https://rdrr.io/github/LTLA/batchelor/man/fastMNN.html (Details section) with652
a slightly adjusted prompt. Finally, the method summary is added to the tree search prompt,653
and is used to come up with better code solutions given the method summary.654
For each of the nine methods, we ran three replicates of tree search. For Fig. 2, we selected655
the replicate that had the best performance based on the validation set score. We show the656
performance of all replicates in Extended Data Fig. 1. Code for the best performing method657
is in Supplementary Table S6.658
Hyperparameters To determine optimal hyperparameters for each base method, we em-659
ployed Optuna, an automated hyperparameter optimization framework69. Search spaces were660
defined across integer, float, and categorical parameter types by experts. The optimization661
process ran for a total of five times the number of parameters. In each trial, a model was662
trained using a sampled parameter set and evaluated based on a performance metric that663
Optuna’s Tree-structured Parzen Estimator (TPE) sampler aimed to maximize. All hyper-664
parameter optimization was conducted solely on the training dataset. The best identified665
hyperparameter set was then utilized to train the final base methods and evaluate them on666
the held-out OpenProblems dataset.667
22
# ACCELE RATED ARTIC
# LE  PREVIEW
COVID-19 prediction668
Dataset Our primary data source was historical confirmed COVID-19 hospital admissions,669
which corresponds to the target variable specified by CovidHub. These data are published670
weekly by the CDC within the National Healthcare Safety Network (NHSN) Hospital Res-671
piratory Data (HRD) dataset70. Preprocessing was kept minimal–missing values in the672
dataset were replaced by zeros to enable tree search to find executable code with the criterion673
score (WIS). The only additional data source used to augment the target for our model was674
static jurisdiction-specific population values from the CovidHub GitHub Repository18. For675
comparing model performance in Fig. 3c, we use all of the models submitted to Forecast Hub676
which make predictions at a state by state level and have forecasts for at least 75 percent of677
the season and time horizons. We ran tree search with 2000 nodes for each reported run. We678
note that we use available as of 2025-05-01 for the entire retrospective season, thus ignoring679
potential differences in data available at the date of forecast.680
Replication of existing COVID-19 prediction models We selected eight models for681
replication from those that had submitted to CovidHub based on the following inclusion682
criteria: (1) The method must be reproducible solely using historical COVID-19 hospitalization683
data, without reliance on external predictor variables, (2) The model submission must include684
predictions across all specified time horizons, and (3) Model submissions must be available for685
over three months (12 weeks) to enable meaningful comparison. Three models were excluded686
for failing these criteria: two were ensembles of external forecasts, and one relied entirely687
on additional data. An additional five models were excluded because they did not provide688
predictions for all forecast horizons. These five models originated from the same forecasting689
team. As all our analysis involves aggregating model performance across horizons, we have690
excluded these five models from all comparisons. Overall this gave a selection of eight models691
for replication.692
To instruct the search algorithm, we provided the method descriptions from the original693
authors’ official submission metadata. For example, the metadata for the UMASS-arc6-pooled694
model states: “AR(6) model after fourth root data transform. AR coefficients are shared695
across all locations. A separate variance parameter is estimated for each location.” We696
integrated these concise descriptions directly into the tree search prompt as part of the697
model directions, transforming them into instructions by prepending ‘Use a/an’ (see Methods,698
Supplementary Table S10).699
GIFT-Eval benchmark700
We applied our tree search methodology to the General Time Series Forecasting Model701
Evaluation (GIFT-Eval) benchmark19. The search begins from a root node defined by an702
initial code template and proceeds via hill climbing, where new candidate solutions are703
generated and evaluated against the GIFT-Eval validation folds. At the end of a tree search,704
we evaluated the solution on the held-out test set using MASE point forecast as the scoring705
metric. Our results are based on a 5/18/2025 snapshot of the dataset, official leaderboard and706
scoring, all of which have been updated since. See Supplementary Table S12 for a complete707
snapshot of the leaderboard.708
23
# ACCELE RATED ARTIC
# LE  PREVIEW
We remark that our snapshotting to a fixed date ensures stability. The GIFT-Eval709
protocols underwent significant structural changes after our experiments concluded, including710
major scoring/dataset corrections on July 24, 2025, and the introduction of an "Agentic"711
category on August 5, 2025. Later updates on August 25 redefined "Zero-shot" to account712
for widespread test data leakage in foundation models using the large pre-train dataset (Note713
that our method does not use the large pre-training data). To avoid unsound comparisons714
against baselines developed under these revised protocols, we deliberately chose not to submit715
to the live public leaderboard, restricting our comparison to the May 18th snapshot to ensure716
a valid, stable baseline. We also note that Gemini models driving our Tree Search have717
evolved significantly since our experiments.718
We adhered to the benchmark’s framework, utilizing the official dataset source from719
Hugging Face, its pre-defined training, validation, and test splits, as well as the scoring and720
evaluation code commonly used in the existing submission notebooks.721
Per-dataset Solution We conducted separate tree searches for 92 of the 97 GIFT-Eval722
datasets, excluding the five largest due to computational constraints; for these, the naive723
baseline score was used in order to produce the aggregated leaderboard score. For each dataset,724
we used a search of 300 nodes, with the system permitted to use a broad suite of machine725
learning libraries, including scikit-learn, XGBoost, and statsmodels. Supplementary726
Fig. S13 shows an analysis of the types of models used across the 92 different solutions.727
Unified Solution Here, we created a single, unified forecasting library that could generalize728
across all 97 datasets. We used a tree search of over 1,000 nodes, guided by the geometric729
mean of the normalized MASE scores across all datasets, providing a single objective function730
to optimize. To force the model to reason from first principles, its access was restricted to731
basic libraries (numpy, pandas, and holidays).732
The resulting solution consists of two components: a single forecasting library and a list of733
eight preset configurations. For each dataset, the best-performing configuration is identified734
on the validation set. This selected configuration is then used with the unified library to735
produce the final forecast on the test set, allowing the model to adapt its strategy without736
seeing test data.737
The final solution was developed iteratively. An initial search yielded a base model with738
a MASE of 0.82. A key breakthrough occurred in a subsequent run when the search space739
was expanded to ten configurations and the system was advised to use the holidays library,740
which improved the MASE to 0.77 (Extended Data Fig. 8). A final 500 node refinement run741
pruned the configurations to an optimized set of eight, achieving the final MASE of 0.734.742
The final solution sequentially models and removes fundamental components of the series,743
with the final forecast being the sum of the individual component forecasts. This approach744
allows the model to be highly configurable while systematically accounting for different745
sources of variation in the data. This process is outlined with the following steps:746
1. Preprocessing: The input series first undergoes basic cleaning, including median747
imputation for any missing values. An optional log-transform (log1p) can be applied748
to stabilize variance in series with exponential growth patterns.749
2. Base/Level Component: A base level is established using simple but robust methods750
like a seasonal naive forecast or a rolling median of recent data points. This component751
captures the basic magnitude of the series.752
24
# ACCELE RATED ARTIC
# LE  PREVIEW
3. Trend Component: The residuals from the base component are then modeled to753
capture linear or polynomial trends. This step includes a damping_factor to prevent754
unrealistic long-term extrapolation by gradually flattening the trend.755
4. Seasonality Component: The residuals from the trend component are analyzed to756
model cyclical patterns (e.g., weekly, yearly). The model identifies the cycle length757
and forecasts seasonality by averaging values at the same point in the cycle (e.g., the758
average value for all Mondays).759
5. Datetime and Holiday Features: To capture special events and non-seasonal cycles,760
features are extracted from the timestamp (e.g., dayofweek, is_holiday_flag). The761
model calculates the median effect of each feature category from the remaining residuals762
and adds it to the forecast.763
6. Residual Correction: As a final step, a correction is made by modeling the median764
of the most recent unexplained errors. This autoregressive-like step helps correct for765
short-term biases in the model. A decay_factor fades its impact over the forecast766
horizon.767
To apply the unified solution to a new dataset, one would first split the historical data768
into training and validation sets. Using the library’s adaptive configuration system, one can769
then find a suitable forecasting strategy by evaluating the eight preset configurations on the770
validation data to select the best-performing one. This provides a strong, data-driven starting771
point that can be used directly. For more specialized applications, one can also create a772
custom configuration, allowing for manual refinement of the model’s components and making773
the library both powerful out-of-the-box and flexible enough for expert tuning.774
25
# ACCELE RATED ARTIC
# LE  PREVIEW
### References775
[47] Silver, D. et al. Mastering the game of Go without human knowledge. Nature 550,776
354–359 (2017).777
[48] Coquelin, P.-A. & Munos, R. Bandit algorithms for tree search. arXiv preprint cs/0703062778
(2007).779
[49] Hemberg, E., Moskal, S. & O’Reilly, U.-M. Evolving code with a large language model.780
Genetic Programming and Evolvable Machines 25, 21 (2024).781
[50] Meyerson, E. et al. Language model crossover: Variation through few-shot prompting.782
ACM Transactions on Evolutionary Learning 4, 1–40 (2024).783
[51] Grishina, A., Liventsev, V., Härmä, A. & Moonen, L. Fully autonomous programming784
using iterative multi-agent debugging with large language models. ACM Transactions785
on Evolutionary Learning 5, 1–37 (2025).786
[52] He, X., Zhao, K. & Chu, X. Automl: A survey of the state-of-the-art. Knowledge-Based787
Systems 212, 106622 (2021).788
[53] Fang, Y. et al. MLZero: A multi-agent system for end-to-end machine learning automa-789
tion. arXiv preprint arXiv:2505.13941 (2024).790
[54] Li, Z., Zang, Q., Ma, D. et al. AutoKaggle: A multi-agent framework for autonomous791
data science competitions. arXiv preprint arXiv:2410.20424 (2024).792
[55] Grosnit, A. et al. Agent K v1.0: End-to-end autonomous data science agent. arXiv793
preprint arXiv:2410.02598 (2024).794
[56] Perplexity. Perplexity Deep Research (2025). https://www.perplexity.ai/hub/blog/795
introducing-perplexity-deep-research.796
[57] Du, M., Xu, B., Zhu, C., Wang, X. & Mao, Z. DeepResearch Bench: a comprehensive797
benchmark for deep research agents. arXiv preprint arXiv:2506.11763 (2025).798
[58] Coelho, J. et al. DeepResearchGym: A free, transparent, and reproducible evaluation799
sandbox for deep research. arXiv preprint arXiv:2505.19253 (2025).800
[59] Xu, R. & Peng, J. A comprehensive survey of deep research: Systems, methodologies,801
and applications. arXiv preprint arXiv:2506.12594 (2025).802
[60] Baek, J., Jauhar, S. K., Cucerzan, S. & Hwang, S. J. ResearchAgent: iterative research803
idea generation over scientific literature with large language models. arXiv preprint804
arXiv:2404.07738 (2024).805
[61] Lehman, J. et al. Evolution through large models. In Handbook of evolutionary machine806
learning, 331–366 (Springer, 2023).807
26
# ACCELE RATED ARTIC
# LE  PREVIEW
[62] van Stein, N. & Bäck, T. Llamea: A large language model evolutionary algorithm for au-808
tomatically generating metaheuristics. IEEE Transactions on Evolutionary Computation809
(2024).810
[63] Liu, F. et al. Evolution of heuristics: towards efficient automatic algorithm design using811
large language model. In Proceedings of the 41st International Conference on Machine812
Learning (2024).813
[64] Ye, H., Wang, J., Cao, Z., Wang, H. & Song, G. ReEvo: Large language models as814
hyper-heuristics with reflective evolution. In Advances in Neural Information Processing815
Systems, vol. 37, 43571–43608 (2024).816
[65] Meyerson, E., Francon, O., Sargent, D., Hodjat, B. & Miikkulainen, R. Unlocking the817
potential of global human expertise. Advances in Neural Information Processing Systems818
37, 119227–119259 (2024).819
[66] Lee, J. et al. Gemini Embedding: Generalizable embeddings from Gemini. arXiv preprint820
arXiv:2503.07891 (2025).821
[67] Gigante, S., Cannoodt, R. et al. openproblems (2025). https://github.com/822
openproblems-bio/openproblems.823
[68] Cannoodt, R., Zappia, L., Burkhardt, D. et al. task_batch_integration (2025). https:824
//github.com/openproblems-bio/task_batch_integration.825
[69] Akiba, T., Sano, S., Yanase, T., Ohta, T. & Koyama, M. Optuna: A next-generation826
hyperparameter optimization framework. In Proc. 25th ACM SIGKDD Int. Conf. Knowl.827
Discov. Data Min. (2019).828
[70] Centers for Disease Control and Prevention. Weekly Hospital Respiratory Data (HRD)829
Metrics by Jurisdiction (2024). https://data.cdc.gov/Public-Health-Surveillance/830
Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/mpgq-jmmr. Dataset ID:831
mpgq-jmmr. Last updated: June 14, 2024.832
### Code Availability833
A reference implementation of ERA is available at https://github.com/google-research/era.834
The best candidate solutions generated for each of the six scientific problems in this paper835
are publicly available at https://google-research.github.io/era, along with a user interface836
enabling examination of the full tree search data for a representative run for each of the six837
scientific problems. The interface allows inspecting the solution progression and breakthrough838
plot as the tree search proceeds and highlights code diffs.839
27
# ACCELE RATED ARTIC
# LE  PREVIEW
### Author Contributions Statement840
Code Mutation System (E.A., A.B., G.C., M.C., H.C., P.N., D.S., J.T., S.V., M.P., J.K., P.R.,841
J.W., L. W., S.M. and M.P.B.) Single Cell RNA-seq Batch Integration (A.Be., C.Y.M., C.H.,842
Y.Z., M.P.B.) COVID Forecasting (Z.S., S.M., M.P., M.C., M.P.B.) Geospatial Analysis (R.J.,843
Je.C., Q.Z., M.P.B.) ZAPBench (B.P.W., J-M.L, Q.Z.) GIFT-Eval (J.G., M.P.B.) Integrals844
(A.K., R.K., M.P.B.) User Interfaces (E.A., G.C., P.N., A.K., M.K., M.P.B., J-M.L., D.L.,845
J.K., C.C., S.E.) Graphical Design (G.J.) Program Management (M.A., E.B.) Leadership846
(K.C., J.M., Y.M., J.C.P., L.D., S.M., M.P.B.)847
### Acknowledgements848
We are grateful to our colleagues in Google Research and Google DeepMind for the incredible849
environment within which to do this work. We would like to specifically thank Niv Efron,850
Viren Jain, Anupam Pathak and Jamie Smith for many incisive discussions, Pablo Ruggia851
and Petkov Yotov for their help with LLM inference and scaling, and Nicholas Reich for852
comments on the manuscript.853
### Competing Interest Declaration854
The authors affiliated with Google are employees of Google Inc. and hold Alphabet stock.855
### Additional Information856
Supplementary information is available online.857
Corresponding Authors: Michael P. Brenner (mbrenner@google.com) and Shibl Mourad858
(shibl@google.com).859
28
# ACCELE RATED ARTIC
# LE  PREVIEW
Extended Data Figure Legends860
Extended Data Fig. 1 | Relative performance of base methods and ERA replicates. a, Overall scores on the holdout OpenProblems datasets for all replicates of methods evaluated in Fig. 2. For tree search implementations, three replicates of the full process were performed. Dots indicate the overall score of the replicate on the holdout OpenProblems datasets. The bar shows the performance of the replicate with highest performance in the validation dataset (identical values to those shown in Fig. 2). The lowest performing tree search replicates for BBKNN, Scanorama, and TabVI only successfully computed 30, 57, and 45 of the 78 metrics, respectively. We note that failures due to out of memory or compute time issues were not explicitly selected against in our algorithm since all optimization was performed on datasets of only 20k cells. b, Average scores for each method when restricting to only (method, dataset, metric) combinations that have non-NaN values for the base method and all three tree search replicates. No advice and TabVI are absent since they have no base method comparator.
Extended Data Fig. 2 | Breakthrough plot and solution tree for the scRNA-seq batch integration task. Top Figure Breakthrough plot for the BBKNN (TS) tree search, showing the evolution of the maximum score as a function of the number of nodes. The green dots label places where the score abruptly increases due to an improvement in the code, and the label describes the change in the code that resulted in the score increase. Bottom Figure Structure of the tree for this same search. The color range consists of orange (lower scores) to green (higher scores) with the highest score denoted by a diamond node.
29
# ACCELE RATED ARTIC
# LE  PREVIEW
Extended Data Fig. 3 | Ablation analysis of the top-performing**BBKNN (TS)**method. The BBKNN (TS) method performed standard linear expression scaling to 104 total counts followed by log1p transformation. It then applied three additional transforms: “Standardize” called sc.pp.scale to further scale the data to mean 0 and unit variance, “ComBat+PCA” called sc.pp.combat followed by sc.tl.pca to generate the expression embedding, and “BBKNN” applied an implementation of batch-balanced k-nearest neighbors writted by ERA. Bars here show the overall performance in the OpenProblems datasets for ablations that include one or more of these components. For each ablation that includes the “BBKNN” component, comparison of the written BBKNN implementation (“Tree search”) and the bbknn package implementation (“Package”) is shown. Black dots show individual performance of three replicates of each method.
Extended Data Fig. 4 | Comparison of tree search performance on base methods and their “recombination” over an intersection of successfully calculated metrics. We ran “recombination” experiments by seeding tree search with the top variants from two base method runs (see Methods). We compare the performance of two base methods and “recombination” on the OpenProblems test dataset for all 55 pairwise combinations of the 11 base methods. Since sometimes methods may fail getting a score for certain evaluation metrics due to errors like out of memory, we compare the performance on a subset of metrics that were successfully computed for all three methods. “n=X/78” on each subplot shows the number of successfully computed metrics, X, that we averaged over. For each subplot, we show the base methods on the left in light blue, and the recombination method on the right (labeled as “Recomb”), where a green bar means the recombination method outperforms both of its base methods, dark blue means the recombination method outperforms one of the base methods, and red means the recombination method does not outperform either of the base methods.
Extended Data Fig. 5 | Performance of the best retrospective COVID-19 hospitalization forecast replicates. This figure presents WIS by reference date for the single best-performing replicate of each validation window in our retrospective COVID-19 forecasting study. The best models are selected based on their performance on the validation dates. The plot shows how finding optimum models on a handful of validation dates (6 weeks) generalizes to the next two weeks of unseen reference dates.
Extended Data Fig. 6 | Breakthrough plot and solution tree for the COVID-19 prediction task. Top Figure Breakthrough plot for the retrospective COVID-19 prediction, showing the evolution of the maximum score as a function of the number of nodes. The green dots label places where the score abruptly increases due to an improvement in the code, and the label describes the change in the code that resulted in the score increase. Bottom Figure Structure of the tree for this same search. The color range consists of orange (lower scores) to green (higher scores) with the highest score denoted by a diamond node.
30
# ACCELE RATED ARTIC
# LE  PREVIEW
Extended Data Fig. 7 | Performance of recombination experiments for COVID-19 forecasting. This series of bar plots illustrates the average WIS achieved by various hybrid models (right bar, labeled "Recomb") compared to their constituent baseline models (left bars, typically light blue) from the CovidHub competition. Each subplot represents a recombination experiment, demonstrating the success of our system in synthesizing novel forecasting strategies. Green bars indicate that the recombination outperformed both parent models, dark blue indicates it outperformed one, and red indicates it outperformed neither. These results emphasize the search system’s ability to combine the strengths of existing methodologies to achieve superior predictive performance.
Extended Data Fig. 8 | Breakthrough plot and solution tree for the time series prediction task. Top Figure Breakthrough plot for the GIFT-Eval tree search, showing the evolution of the maximum score as a function of the number of nodes. The green dots label places where the score abruptly increases due to an improvement in the code, and the label describes the change in the code that resulted in the score increase. Bottom Figure Structure of the tree for this same search. The color range consists of orange (lower scores) to green (higher scores) with the highest score denoted by a diamond node.
31
# ACCELE RATED ARTIC
# LE  PREVIEW
Extended Data Tables861
Extended Data Table 1 | Expert manual inspection of adherence of ERA implementation to scRNA-seq batch integration method.
Method Replicate Judgment Notes
batchelor fastMNN 0 Follow batchelor fastMNN 1 Follow batchelor fastMNN 2 Follow batchelor mnnCorrect 0 Follow batchelor mnnCorrect 1 Follow batchelor mnnCorrect 2 Follow BBKNN 0 Follow Adds distances between batches, performs spectral clus-
tering on the graph. Does not compute connectivities. BBKNN 1 Follow + Innovative Standardize + ComBat + PCA for embedding. BBKNN
implemented on that embedding. BBKNN 2 Follow Corrects the data, computes neighbors, final embedding
is UMAP supposedly based on neighbors. ComBat 0 Follow ComBat 1 Follow ComBat 2 Follow Harmony 0 Follow Entropy-based diversity penalty. Harmony 1 Follow Linear diversity penalty. Harmony 2 Follow Linear diversity penalty. LIGER 0 Follow Uses sklearn.NMF with multiplicative update solver. LIGER 1 Follow Writes NMF function from scratch. Builds single global
KNN graph rather than by batch. LIGER 2 Does not follow Uses ComBat + SVD. No advice 0 Follow Uses batch-specific mean+std for all genes to rescale.
Then PCA. No advice 1 Follow ComBat + SVD No advice 2 Follow ComBat + PCA SCALEX 0 Follow Adds log_var clipping and weight normalization. SCALEX 1 Follow Learns batch embedding. Learns gamma and beta condi-
tioned on batch index. Batch index not supplied to first layer of decoder.
SCALEX 2 Follow Uses min_delta for robust early stopping. batch_index not supplied to the first layer of the decoder.
Scanorama 0 Follow Scanorama 1 Does not follow Implements mnnpy via sc.external.pp.mnn_correct. Scanorama 2 Follow scVI 0 Follow Applies log1p scaling with ZINB loss. Fits global disper-
sion theta rather than batch-specific. scVI 1 Follow Applies optional log1p scaling with ZINB loss. Fits global
dispersion theta rather than batch-specific. scVI 2 Follow Expression frequency exponentiated rather than soft-
maxed. Applies log1p scaling with ZINB loss. Fits global dispersion theta rather than batch-specific.
TabVI 0 Follow TabVI 1 Follow TabVI 2 Follow
32
# ACCELE RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-aHjhNjJwpFwA1k80zZlDr5arQkHdbNGNWVFokDGo7bxvA0BLD88gScwMkXYkl0I-sBx5DEn8I5GN8USJlwo9hMNxskcffqy7GOhcLmImm8p_vglQBWFVeknn7GBWJP7n6-sm2dw=w236-h204-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-4kglqbwC-eC5l3XJAIr37C-rvGw85c74gG-LcpqeJD_nxD9gYP9q0OaO4WQEwSTlGTa14kKu9dtsscIP7dSWj52M39CiZ8JPRBxub1BsOvhVPeZABaN2oLcr_rop5-EE7Gcha=w512-h512-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_JLKNRuunvFrZCoKsVm14XCwf9L_G1-qulb7gt75VhLX53QT_Zv6R6eG_sMAs7sQ6Vm_60HF-4ob97oCuqtqS6IEjEdM5a9zHsXje8XlTgzgTGpCPJ7dRx4e0mkVanssGKbQL1=w280-h280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_rsLJA5dHRijY-_7bxs2t23hsZBX04vopSFizUErAFaeQStCWzJzmphaZP_B6PfyJZys_yictxMyIJ9wBBUhxCa2RSrPk34S_f_uvc-V_QKCW6b8sPmVrEtcin9BT5rE5UGauUUw=w200-h200-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-RE5A6IBSboMk9z4zyWfSDwCmguWh1YjwTmXaVK-0-bZcUk0Gt0KDldvLLR4_loWSgEpvEReltgeocSJbMMmH2D1y5Li3rX2Lzh_gN_mcluRUr_S--TeyT9hwG91btk9Fhdj6KnQ=w200-h200-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_SmXZu_NdNfLKbybEwLyBIDbmiQM_kfVX862rjE1e6YMlMIXqR4ySX4gOa8bVbMQPJr24YC8mELKuYvdEnvgJMBh6lqQ0MnOuNMf8ZpQWq3AAyYucMtYdQPT5kQXUSPsn2HWJ4fA=w200-h200-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-NHPwYxOfXTX0KHZAUfOX0j3RWhJrRQKPlKNpf8WfpzSahbMlHpFZvDzbvFGSKyNIex_FRpdjHbaBFih18rruOgqEAWD6P1GqgPt_lTwmGNQ2sqbHTShEVLpyN79sHQgd6eVZH8Q=w200-h200-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8SDU93fm2ZuubHKvImm_wv9Qx6UNRGavslJ-rWjdISOAZNUOOez8ic5h-ZM7U9yz6Kl11U-LNjJDfC5vVeRmhKN2QkINiZJc2B2_vV7AFus58uyYpKEB2yiF_7oZJlkRNHCK0Xzw=w200-h200-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8q7SNObgJ6Y-oQy5RhFo6XD5sNv9b_2_Eq5c8QxBi-UnPPc1zTGPhsmE0iljc2S-mBmhx2LEw0gtXtuFdHS9ky3gQY6OR6uSTFTp1ibmqqDFv8_c9lsPf-mkAgrsXZOzjEYilF=w200-h200-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9Jnw_KrImptYwlk3XO3wzUk4fyx6glnSSK2Hk1HA5_suf3TY_2d8YOGyfSsmwSbftD0pot_IxGz-IpOtEqh2bGoBtXH2-K_e8KmS5G5XGZhlocp3BS4i-BB2nvzkMyglDK6QSdDA=w200-h200-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8z71dL32no9w3dwv25WaaqPNaOwFsWxn0wIekKtg4Ei0wKeAYCeragjmCWlqkncoudFOxU2vU0S1vH_NbtFVIWceuXGH_kIv6q6e9rBhsQcLCVhQCVU1XojrnKCYe3T7jPOAWn3A=w922-h633-v0?authuser=0)

### Scorable problem
### Research ideas
## Prompt LLM
### Code sandbox
Improvement
### Finish Further exploration
### **c**
*Summarize*
Scientific papers
+*Recombine*
Prior ideas
Gemini
### code solutions
Expert*Write*
### **b**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8IOXqPhF0dVLFaGPjiKEry5eyLYU0VLv88dRppH_tLhQdsBNZdUEEwe1510sFI8eyBEbhxt1Og1C-ObK2iJFkoBhkEm7gP8G0d_aVRnV4s2lP7QLBnt_rLmcc7F_nzBebQ98K9=w1280-h640-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-CTyMzkOuF-zewESwKjgeCS9a85YhrwoVrbYW7V-C1NO8Kva-Z8P_qxBvwCOmMse6WUo1i1o1mWuaOxlKzUj6yhmD1GV0b2nhtQu1HbKZ8pDsQOUNHbgJK10EOOw3aLVlTPcuvOg=w1280-h301-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8oGKZDEdOpknKvjYwD23BmUCcc-ukbVuvbP4LnSlS8N5n91o_4Nm6Pqz3QLBSLLwB3gXwWRJISVesQiPkL2apNexvRqNyW4EHAa-HvLMbJ21fG9U4x4kbp8AjObBIq6uIqLAqj=w1280-h346-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8sAVJb5uxKbrG2r716M3UomHy9yGwP9QSv6p955__93COj6aNVs_Mrba911j8VgVB1JK4dphVoDyp7zu1857Zg-2dCLbZ3AUsMbZLcTVrCNubjzZ926iYT7_J1I90SZOKECLnVFg=w1280-h928-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9uvDb3kqkfdeX2aVaT6jjROMV-uRPFG-6H8Sk6S7Z75MsRXGqdWcQtTc2x2n-Ht8dpXP2gsqhsLkwSuV2fQBe9T85X0clPtD1grDjHy62RRTMb4WfrSRPYdPX8qvcMJIKyMZs2Zg=w1280-h928-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_W7xFYmhUnP8x-yJxANcKNcTT_z-9IpLmufoU94AMrSAsbAkewAeFTsXyJwSQb4u7eQjUkIb7XryK2LdarrX8J7k7U2CLyq9QzAaruJId3weplXUR3HPNmutjmPN1LFE5v2psj4g=w1280-h928-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_cHgwMh_r8VRpUEMBxnpk_AITk1rVfw-3WhbhxBzwCyADIhRhe8wmvHyLciLBzrfo-Skq0OL1uLluq9RNnYBpNZZDmMZankZxOa49ge5aV_mjb2q_LRhOCK_Znk0FTjAL-RLj3=w1280-h895-v0?authuser=0)

### **d**
### **c**
Overall score                         Score per dataset (mean over metrics)            Score per metric (mean over datasets)
0   0.5         1 0       0.4     0.6         0.8              1 0       0.4     0.6         0.8              1
Combine
# *Poor Good✗*✓
PC1
PC1
PC 2
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-SHY1I1FHQ76wiLeQFB0XCCNlpEhKa9yiQhLmVsTgWOLT_30j71Wb1AsLNaxs2734d0Fp5GaqzH_lOP9ga3v85wl-_FxFLAForXw1FvhA1iZJnHb_-Y4IdOFDMdEbV7R_WJCnG=w1280-h1108-v0?authuser=0)

# ACCELE RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8MguSBzC1ZP8QWFxUKZwFF0WXryBOglKAfudTI2fObLFjLaHois366vFb4aYVdrmRqKt4pJ7eCLUNprT-XYEwZmJidgbcxd5C-hjYY6Ft1kHhECB600QlnOOATTKVi6P68rij39g=w1280-h768-v0?authuser=0)

**Extended Data Fig. 1**
# ACCELE RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9Q3WoM1H70jZFi9-T7Mu3KMHEKYiRYsWAWv0kH3lIwArDqyLE1adn_Seo5wR_EvmEELoRrKhHZiv2noZRIjd9q8Eud_nQavGo1u_oNITb0LKPOKpAntKmGiG3qEBjN7r9V01j00Q=w1280-h720-v0?authuser=0)

**Extended Data Fig. 2**
# ACCELE RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9QCi4xdhp_dpu3OX25HVT8qI-3icQG9fP1ESvLH8h0vUGVyF0lJcNquLV57HKwJebR-LOSurtzbG4i91Wx56X4cSh9Eh2g32LB4mQt5tMHIs8bYADqSobzs8mQ3EwbwWMeYL6FDQ=w720-h576-v0?authuser=0)

**Extended Data Fig. 3**
# ACCELE RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX82ruWnjOkjMK98GQbcpcqBEBJI6jsCykxdsd9y1zRmCPjyHRsviJXdthbnoETTm1YV5abFOvcKoNI1S1Q2t0E-ySQeqCeS5v98BuaWH3C-2W6vizU7p9UsT-Vf3WTMH41GaSlDnA=w905-h1280-v0?authuser=0)

**Extended Data Fig. 4**
# ACCELE RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8QpK9ahA0fchScSPiz7DBxzGUstbrvy5ZXpIid-wqaoSjnEvZHjWS1-7smB__1cc_rAHbK_epR6qyUpbTnsx3GOiNtxx4enBmc8kTnuGhdTdFEGf2u28qUM8sxS2mP1dt_JmFohg=w1280-h507-v0?authuser=0)

**Extended Data Fig. 5**
# ACCELE RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9RNert7B4CtX39QD1c0xOInQ5Ml3kn1IOREYTDy_YxpGqq6lSRSTtEMbs9XorA1HOnjk2AWOGlbiJtdiFfQFNAWCoSqeEHBJ1iBzKzEpwMd7dtnE8KSDt8OpFrs4bm1Q8Vl_oMhg=w706-h280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-xp8jEaFbOTZq4GKD7N0JwaZ-C_5pf_S_NVsMRBOHrrKa1VWAZX68_XWyMXXUOjgwEYuovg3RVl4pzlmwDJRFU6RLXD6lbhWOzH1b1tyeM3TrT533xCa3B0J1rAyEZ3QZ36McZUw=w1280-h719-v0?authuser=0)

**Extended Data Fig. 6**
# ACCELE RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9YKkq5jcCwSzEn4N9DDsbqke5iz3-F_CQIDwby4j1OuXLzqVhYmd1QpQZ__4MhzTGM8nnYMTW6e0TJ1ayni0L6ywrpvcKwQaJ-Wr_UYA5ovWt28Zu-QLwTYuZD1zFfvfvNtF2K2g=w1066-h1280-v0?authuser=0)

# **Extended Data Fig. 7ACCELE**RATED ARTIC
# LE  PREVIEW
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_xKSEdt7BgU620rsi_jbWAvAqpPSgbMsXYWd4aZ1Eq8FJoelJnS845CvFUZO8lGOsmlHjNQug8rZIccjpvZxxKmBPlrIeVrISrPa9T2-qHIlZ2SpoNGDW8SjFS8nVlfnlMInmpSQ=w1280-h719-v0?authuser=0)

**Extended Data Fig. 8**
# ACCELE RATED ARTIC
# LE  PREVIEW