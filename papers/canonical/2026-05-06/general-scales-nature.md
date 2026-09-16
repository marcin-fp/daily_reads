
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9T7SkCcSwTSJQxArh5PeRo0A7O1-ElGutvI0nxvp-z20j4uSiToCHsfz_Tch-9kyKwsmuY4hBzC7Jb3CeJphablYjx2CCK-_Gztq1QIrnD3XmiB6mSrMiKuiEhEe9U_u-eSZ7QVw=w90-h79-v0?authuser=0)
**General scales unlock AI evaluation with explanatory and predictive power**
**Lexin Zhou1,2,3,4 ✉, Lorenzo Pacchiardi2, Fernando Martínez-Plumed4, Katherine M. Collins5, Yael Moros-Daval4, Seraphina Zhang2,6, Qinlin Zhao3, Yitian Huang3, Luning Sun7, Jonathan E. Prunty2, Zongqian Li8, Pablo Sánchez-García9, Kexin Jiang-Chen4, Pablo A. M. Casares4, Jiyun Zu10, John Burden2, Behzad Mehrbakhsh4, David Stillwell7, Manuel Cebrian11, Jindong Wang12, Peter Henderson1, Sherry Tongshuang Wu13, Patrick C. Kyllonen10, Lucy Cheke2,6, Xing Xie3 ✉ & José Hernández-Orallo2,4 ✉**
Ensuring safe and effective use of artificial intelligence (AI) requires understanding and anticipating its performance on new tasks, from advanced scientific challenges  to transformed workplace activities1–3. So far, benchmarking has guided progress in  AI but has offered limited explanatory and predictive power for general-purpose  AI systems4–8, attributed to limited transferability across specific tasks9–11. Here we introduce general scales for AI evaluation that elicit demand profiles explaining what capabilities common AI benchmarks truly measure, extract ability profiles quantifying the general strengths and limits of AI systems and robustly predict AI performance for new task instances. Our fully automated methodology builds on 18 rubrics, capturing a broad range of cognitive and intellectual demands, which place different task instances on the same general scales, illustrated on 15 large language models (LLMs) and 63 tasks. Both the demand and the ability profiles on these scales bring new insights such as construct validity through benchmark sensitivity and specificity and explain conflicting claims about whether AI has reasoning capabilities. Ultimately, high predictive power at the instance level becomes possible using the general scales, providing superior estimates over strong black-box baseline predictors, especially in out-of-distribution settings (new tasks and benchmarks). The scales, rubrics, battery, techniques and results presented here constitute a solid foundation for a science of  AI evaluation, underpinning the reliable deployment of AI in the years ahead.
Present general-purpose AI systems, such as LLMs, are highly unreliable and unpredictable6,12. This places a large burden on AI evaluation in terms of explanatory and predictive power: we need to understand why the AI system is failing and anticipate where it can be applied successfully. The traditional performance-oriented evaluation approach has shown limited predictive power at the instance level, inside or outside the benchmark9,10. If DeepSeek-R1 achieves 79.8% average performance13 on a popular mathematical benchmark such as the American Invitational Mathematics Examination dataset14, we cannot make informed estimates of success on individual items sampled from that benchmark. This performance score is even less informative for out-of-distribution instances from other mathematical benchmarks, let alone benchmarks from other domains. Indeed, aggregate performance scores are a function of both the benchmark and the AI system, not invariable properties of the system only—its ‘capabilities’—that delineate the limits of the system, generalizable across a wide range of scenarios.
Instead of aggregating performance, other evaluation paradigms do estimate some properties of the subject (the human or the AI system), which, jointly with some properties of the item (the specific problem instance), can predict performance; we provide a glossary for technical terms such as subject, item, ability and contamination in Supplemen-tary Information Section 1.16. Several techniques from psychometrics and other behavioural sciences have been applied to AI evaluation15, such as factor analysis16,17 and item response theory (IRT)18. However, the extracted factors or parameters are populational: they depend heavily on the population of systems and benchmarks used, which makes them quickly outdated with the fast pace of AI progress. More recently, score prediction metamodels related to uncertainty estimation and calibration methods, known as ‘assessors’19,20, have been used to anticipate performance for new tasks at the instance level, by means of latent features. Nonetheless, these features are difficult to interpret and typically extrapolate poorly out of distribution21,22. Alternatively, these features can be engineered by humans through
https://doi.org/10.1038/s41586-026-10303-2
Received: 29 March 2025
Accepted: 19 February 2026
Published online: 1 April 2026
Open access
Check for updates
1Princeton University, Princeton, NJ, USA. 2Leverhulme Centre for the Future of Intelligence, University of Cambridge, Cambridge, UK. 3Microsoft Research Asia, Beijing, China. 4Valencian Research Institute for Artificial Intelligence (VRAIN), Universitat Politècnica de València, València, Spain. 5Department of Engineering, University of Cambridge, Cambridge, UK. 6Department of Psychology, University of Cambridge, Cambridge, UK. 7The Psychometrics Centre, University of Cambridge, Cambridge, UK. 8Department of Theoretical and Applied Linguistics, University of Cambridge, Cambridge, UK. 9KU Leuven, Leuven, Belgium. 10Educational Testing Service, Princeton, NJ, USA. 11Center for Automation and Robotics (CAR), Spanish National Research Council (CSIC-UPM), Madrid, Spain. 12William & Mary, Williamsburg, VA, USA. 13Carnegie Mellon University, Pittsburgh, PA, USA. ✉e-mail: lz5066@princeton.edu; xing.xie@microsoft.com; josephorallo@ gmail.com
cognitively inspired approaches23, but the scalability of this approach is limited by the need for experts who develop the cognitive models and annotate the testing items.
These perspectives differ in what is measured and how8, but they have all grappled with explanatory depth and predictive power. Also, most of these frameworks derive features, parameters or scales that are regularly saturated by an extremely volatile space of AI systems and benchmarks, soon becoming obsolete24,25. Lack of construct valid-ity10,26–28 is also an issue in the common benchmarking paradigm8. Solving all of these issues is a prerequisite for more robust assessment in the real world9,29, such as interactive, subjective and adaptive evalu-ations30–32. Table 1 summarizes the problems and associated findings presented in this paper, the solutions it brings and its numerous new applications. Supplementary Information Section 1.1 further details related work.
We present a new methodology that can accompany, map and inform AI progress, regulation and deployment in the coming decades. This is instantiated and demonstrated for LLMs—the most popular form of general-purpose AI—but the methodology is extendable to AI systems with other architectures and affordances. The core element*is an array of 18 scales in the range (0, ∞) corresponding to general*capabilities relevant to tasks expressed in natural language—such as verbal comprehension and logical reasoning—and broad areas of knowledge—such as natural and formal sciences. The precise values on these scales (the demand levels) are obtained through 18 carefully crafted demand-level-annotation (DeLeAn) rubrics in the range 0 to 5+, which humans can interpret and apply to any testing instance, but ultimately applied by a LLM judge for scalability.
By running the rubrics through a collection of 20 benchmarks, we obtain the annotated-demand-levels (ADeLe) battery, whose 18 histograms of demand levels form a demand profile examining the sensitivity of each benchmark (measuring what they claim to measure) and specificity (not measuring other capabilities beyond what they claim to measure). For each LLM on which ADeLe is applied, we get 18 characteristic curves, delineating LLM performance as a function of the demand levels. Each curve is summarized into an ability estimate that is commensurate to each demand scale, hence composing an ability profile of 18 ability levels. Notably, the demand levels for a particular task or benchmark and the ability levels for an AI system are independent of other benchmarks and systems and any population thereof. Most notably, the demand levels can be used to build strong predictive
models for the success of AI systems on unseen in-distribution and, particularly, out-of-distribution instances (new tasks and benchmarks).
As an example, by annotating several benchmarks that claim to evaluate ‘reasoning’ (Fig. 1) and comparing the annotated demands with the measured capabilities for an AI system, we can obtain causal explanation and prediction: if an AI system such as DeepSeek-R1-Distilled-Qwen-14B has a profile with quantitative reasoning (QLq), logical reasoning (QLl) and inductive reasoning (CL) abilities of 4.5, 4.3 and 4.2, respectively, as shown in Fig. 1a, we can anticipate success in a typical instance from GSM8K with 2, 1 and 0 demands in these same dimensions (and low on the others). We can also predict a less optimistic outcome on a typical instance from OlymMATH Hard, with values around 4 and even 5 for some dimensions (Fig. 1b). We can also perform counterfactual analyses, such as arguing that, if the capability of DeepSeek-R1-Distilled-Qwen-14B in QLq were reduced to 3, its performance on GSM8K would be marginally affected. However, it would be greatly affected if its capability in QLq were reduced to 1.
Thus, with our methodology, we unlock the following possibilities, beyond the reach of previous approaches: 1. We can carve the space of capabilities into a hierarchical catalogue
of general scales. The DeLeAn rubrics v1.0 (see Supplementary Information Section 2 for the dimensions in Extended Data Table 5) are applied systematically to the 16,108 instances of the ADeLe battery v1.0 (Supplementary Table 28), yielding 289,944 annotations across 18 general scales. The clarity of the rubrics is validated by the agreement between human and LLM annotations. The existence of instances that differ on any pair of capabilities and the moderate demand correlations between the 19 dimensions (Extended Data Fig. 1) suggest that the set of scales maps potentially distinctive capabilities, not dependent on present systems, likely remaining informative for future AI systems.
2. We can explain what common benchmarks truly measure. We discover the presence of demands in extraneous dimensions such as atypicality (from common to unique), volume (from small to large) and unguessability (from multiple-choice to open-ended), indicating contamination (overestimation because similar data were seen during training33), amalgamation (underestimation because examples are made more difficult by agglomerating more things to the task34) and funnelling (underestimation or overestimation by changing the difficulty of a task by reducing or increasing options or
**Table 1 | Diagnosis of the challenges of present AI evaluation paradigms, associated new findings revealed by the methodological solutions contributed in this paper and the potential applications of the new methodology (expanded in Methods section ‘Pipeline and guidelines for applications and extensions’)**
**Challenge Finding Solution Applications**
Construct validity: common benchmarks do not measure the abilities that they claim to measure
Narrow ranges of task demand levels on targeted abilities, confounded by unwanted demands
Benchmark profiles quantifying what abilities the benchmark truly measures
Resolution of contradictory claims (for example, LLMs can and can’t reason), better benchmarks with construct validity by design
Commensurability: incomparable measurements across benchmarks and distributions
Aggregate percentages mostly reflect sufficiency of capabilities, not capability estimates
Standardized general scales fixing demand levels to infer general capability profiles of AI
Interoperability of benchmarks, instance reuse into new batteries, meaningful scaling laws through non-saturated general scales
Population independence: frequent benchmark saturation and replacement dynamics
Instances in saturated benchmarks can still be informative, owing to uneven demand profiles
Non-populational benchmark demand and model ability profiles through standardized scales
Measurements robust to changing populations (of benchmarks and AI systems), capability catalogue accommodating AI progress
Explanatory power: benchmarks do not explain why LLMs fail on particular instances and what they lack
Failures monotonically increase in a sigmoidal way as demands increase
Defining general scales and rubrics that are interpretable by humans
Capability profiles bringing explanatory power, enabling model diagnosis and counterfactual explanations of AI failures across domains
Predictive power: poor anticipation of AI performance for new tasks and new domains
Capability-based instance-level predictions are highly accurate, robust to out-of-distribution cases
Predicting performance with demand levels as features, optionally with system profiles
Routing instances to the LLM with highest predicted probability or rejecting queries, monitoring AIs, guiding red teaming
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-SwY3_83htPrc03Qw593hqygQHIAufzxArdnuxdCjIB6IWxN22MS5r455aJHkkPtFFQOXosvj_mcTGZxxooRT0AjLefEvbF2JPoQkaTMALvFhYlCMu_eMCsAtqjDFfPuDwlWctAA=w36-h337-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8rnD-q5oVJhFvRxRKUrG193uTvUrW7J4oXLqsKORpxpX5iQYHBYk8NCF7q39dkI7MBbUl8eT8y6rysoo7mKrU1FfDUXKaVQ6Zca2JEeB7vKAcyje4ksXM799UuJYtDhtJ6VcB8pg=w38-h340-v0?authuser=0)

distractors35), respectively (Fig. 2 shows the levels of these demands and Supplementary Table 2 shows how predictive these dimensions are). Beyond these effects, many benchmarks lack either sensitivity or specificity: they do not contain instances of all demand levels for the dimensions their designers claimed to measure or they include non-zero demands on other dimensions they should not be measuring (Fig. 2). Identifying what each instance really measures paves the way for interoperability of benchmarks and AI evaluation with construct validity.
3. We can explain the general strengths and limits of AI systems through commensurate scales. In our experiments with three families of LLMs, we find that the ability scores at knowledge dimensions are mostly determined by model size, whereas quantitative and logical reasoning, learning and abstraction and (perhaps surprisingly) mind modelling and social capabilities are boosted in chain- of-thought, inference-heavy models such as OpenAI’s o1 and DeepSeek- R1-Distilled (Figs. 3 and 4). Because the dependent variable is not a relative percentage on a benchmark but a level on commensurate ratio scales that do not saturate, we have been able to clarify conflicting evaluation results (Supplementary Information Section 1.12) and demonstrate diminishing returns in scaling laws (Supplementary Information Section 1.4).
4. We can robustly predict AI performance for instances from new tasks and benchmarks. High predictive power at the instance level is possible, superior to black-box assessor baselines based on embeddings or fine-tuning, especially in out-of-distribution settings (new tasks and benchmarks), supporting both internal and external validity of the
scales. These are also superior to domain-based36 or learning-levels taxonomies37 (Supplementary Information Section 1.9). This opens up a range of applications, such as better routing methods to choose what model to use38, safety operating areas in which assurance is guaran-teed7 and anticipatory reject rules when harm or cost is anticipated39,40. See Extended Data Tables 2, 3 and 4 and Supplementary Fig. 8.
These processes are fully automated through open-source pipelines that can be easily customized by AI researchers, policymakers and regulators by extending the scales to other capabilities, traits or propensities (for example, affecting safety or fairness) and to agents with affordances (see Extended Data Fig. 5 and full explanation of the collaborative platform in Methods section ‘Pipeline and guidelines for applications and extensions’). This endeavour is seminal in creating a measurement standard for AI, mimicking the measurement efforts that have been pivotal in other sciences41–43.
The key element for our overhauling of AI evaluation is the configuration of scales that are understandable, general and well-grounded in measurement theory. We work with a catalogue of 18 scales, following a hierarchical structure (Supplementary Information Section 2), chosen by following a set of criteria fully explained in Methods section ‘General scales’. We refer to the first 11 as ‘elemental’, capturing general capabilities such as verbal expression and metacognition. The second group includes five ‘knowledge’ dimensions measuring the expertise in different broad areas of science. There are also three ‘extraneous’ dimensions (two are proper scales and the third is a control variable for funnelling), AT (Atypicality), VO (Volume) and UG (Unguessability),
AS CEc
CEe
CL
MCr
MCt
MCu
MS
QLl QLq
SNs
KNa
KNc
KNf
KNn
KNs
AT
VO
2
3
4
6
7
8
vs.
1
a b
5
CEe
CL
MCr
MCt
MCu
MS QLl
AS CEc
CEe
CL
MCr
MCt
MCu
MS QLlQLq
SNs
KNa
KNc
KNf
KNn
KNs
AT VO
AS CEc
QLq SNs
KNa
KNc
KNf
KNn
KNs
AT VOAS
CEc
CEe
CL
MCr
MCt
MCu
MS QLlQLq
SNs
KNa
KNc
KNf
KNn
KNs
AT VO
AS CEc
CEe
CL
MCr
MCt
MCu
MS QLlQLq
SNs
KNa
KNc
KNf
KNn
KNs
AT VO
0 1 2 3 4
0 1 2 3 4 5+
0
20
40
60
80
100
Fr eq
ue nc
y
5+
OlymMATH Easy
Fr eq
ue nc
y
0 250 500 750 1,000 1,250
GSM8K
Fr eq
ue nc
y
GPQA
0
100
200
300
400 OlymMATH Hard
DeepSeek-R1-Distilled-Qwen-14B
0 1 2 3 4 5+
0 1 2 3 4 5+
**Fig. 1 | Commensurate LLM and benchmark profiles can be compared to explain and predict performance. Here we show LLM capability profiles  (a; DeepSeek-R1-Distilled-Qwen-14B, estimated as discussed in the section**titled ‘Explanatory power analysis: profiling LLM abilities’) and four different**‘reasoning’ benchmark demand profiles (b; GSM8K, OlymMATH Easy, GPQA**and OlymMATH Hard, for which each slice represents the frequency of demand levels for each capability, with darker colours representing higher frequency). Researchers, developers and users can intuit that performance is expected to be high for the benchmark GSM8K but worse for the other three. Moreover, these profiles explain apparently contradicting findings, such as the accuracy of DeepSeek-R1-Distilled-Qwen-14B on GSM8K, OlymMATH Easy, GPQA and
OlymMATH Hard being 90.50%, 61.80%, 59.10% and 13.30%, respectively, despite all of these benchmarks supposedly testing mathematical reasoning according to their creators. Indeed, OlymMATH Easy has lower demands for quantitative reasoning (QLq), logical reasoning (QLl) and inductive reasoning (CL) than OlymMATH Hard but similar demands for all other dimensions. Instead, GPQA yields worse performance than OlymMATH Easy, despite being easier in reasoning dimensions, because of its low specificity, with high demands for some knowledge dimensions beyond KNf (Formal Sciences), such as KNn (Natural Sciences) and KNa (Applied Sciences). Further details of these benchmarks associated with ‘reasoning’ benchmarks are discussed in Supplementary Information Section 1.12.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-slB3Eth2FvwDOPgdU3W6_mUdOjPJlWMPRiKJiqHh4ljXbb9NkB0pmtIxqqu6keS6eowf6olp2wT_1_VkvaHAVPB5PH9FEY2aDZXLdtlOL9_spUeTYmd8Fxalbb6o7Ub7beEPjpQ=w738-h391-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_6Z1_M9bi4OVrhBGAVasp19qnOqO5BCSIhWBfySEh36Iahwzkiev1kxxYW1ceEkemesod8AJ59pEe0tV4j75_6VHl01JA-_6h32TUdoT_SJM5ISxhxW1597HQmyKHm3vL2e9Al=w64-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9pmNFvpKq8fE7Df3N5JFIBw6pPxSYKoKIjtOQhSMyQzzdrLwylZSLqeLBcbTuHc4NCydCArIWklFOYl-eJKssOBfNgW9kJiU5uEQlYghpFhfYb26sDrgmENPcHsnvuy8IBC4faLQ=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-s_CXErJL4WTV65DZodV72sMqLA3I3qhgeEopV3gGCktvgREG8db5wMw2dUT097dwjZX24SG7HnkElTt8JpbokialDseVsHZALXlo-vPtw3BfhErUa0InE6lALpswuifq2RQJAfQ=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8xsvuKTR2xzjg83vJbKO6ZT4seguJZZ9wVce6IR3t7mDj73QWD7BSgjl_3Rj5QgjJSVboNyjI4HFItBd71Y-B3mf4N3XvJZhYVndG46Pxllvn8QoPd7vgbIgBIDpgiDcFm_brnVA=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_4sKypi1O5LGZixbZaiT3F2sbj8d8aC4GO1ShtzgdhhLgxWNB1ElHI9iNxm6Ax8j4TG_HaGEvI3vDChWBPXpzuYzOqiRRdt5NcrlyGLOToCvgoLQSUPI5bO4eQ8jWcASwOOJgnLA=w65-h321-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-5ei_8NgfQnBREcCQ42GZsFd6Piq6euJF6kaxGen5lX4jeNX0ujsYsJQltn0PFam_AnZ-17k7jsWXjTdOmX9GZlSxPDdOfrF8Eezwxg8jSbJNP-CMzTfneKP5EcGPzyxzwWstT3A=w65-h321-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8x3Jgp6b-nBq2oQe8dhSaBgMzpzEMs6_AfAXSmuE-kL4Mq_fj20swJDcxc--SKemylUpKsX7BG2W344MlIG_bzgTVB4dhFNW0_7Xj9oFk5pv8SAHrYEzbTDYEdn9dqW351xkPikA=w65-h321-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_RZa_KTDHQLu_oesl4uPje1x8heSS9nlKlRfbr-S6H2-kL7spguflLARxLb53FCCj2kZvecyAv3259QsFPAN0cj690Yr2sL6mauGR6Dh-cQm58B-WO_Ak9q3dAUJtefp93SwrhHQ=w65-h321-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-QzmsW8Me4_tx51apJl27l_vGS796b6Mq1wzDLHXexUkJQgy6QRJD9Z6bXeZJMkhjhn21Y1Jn08Hwa-_CsRfBCh-8q8iuIC6_Jx77erMUmmL6-qpvcLrj_YJ_DdW5GrocjuCOBMQ=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-Ax3dnasHw3bj5bFKEtDNlogWgxw6Piumhg31Gu6ZuahUTO4_wPcmYcf-J2X8stJAd2GBahkJkRUHBmusYWGAsbNsxUqmhHC-nKaVSh0X02edXQIalN39Oo2ncaExJf2sAzB57yA=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_IxIWsDp3vqUb6HvQPNhTWX1Ys7UTpo5rnkpxQ8k0aS-2OfQjodrCdGA3jCdRXZTR-xIYadMuJBRkqYO5DBEFGuCQNDH-5vZFrgavVgsW3iVBUYXlivO0IsbovF71TX6nRtN87=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9jHNXMIVC0u_QyTaG-6q8wpRRMn610cVM15DPddKwmHu8M3MgPawBF0Hd_GhXX8md0Rb0UxfZlLJU0f_TxLdTRf2QgHNFrL0L9F17juGJHwKoHbtuTvQZI0n4wHtwCSfSrzajK=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8mxRqCn8moHMgaglo_n0VB8-8xmifIM6egbiogjogj_kiv5dJcLrTzomG-s2W64zGXhSXe_qEFmOCVv0zHXkuyS9Zap2E6sdrSscZL3nOOZaBGrow7c5jMIHiXKuXv1Su73YaRyQ=w64-h321-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_pwhGFwbdWs50V3ZyMsp1ocpQm2ZyvD42tlB7Af19BWyqxpxA0vDdB3djA0pifKgdBXmHIaP9-vwJDjBKbDzkrfwkUk4I8298hXIKX4bmFMSX4rUbcD8Jll0idWytHjooayFLJ=w65-h321-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8PhdA_2sW_oA4wiGff14C4Kd-f69xV5wvwJRL8T38aJWURkw_85d_4zrz1B1jwupREWpKZX09aO4Jq7-2lBc2THjv4NsBzL2JeGrcmZSCLY_y6OuRI0Z6xbd7e-ZpZwrXS-DWsrw=w65-h321-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-pljJ0tsMgL05Njmg7-Qzp_2-ahxLs5ZO8Ff-aKeIiMAT8zAzs3BKOtDYV8f5Jksd7Gfot7Mmfqj3Y9kWt5NmpX2BOD_TbRSf5zSxSXoAdathxuJPGsfgIFYja9HuGzh_8WVfpsA=w65-h321-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-9Ku6rIgZj7gGmT8AwHcWa1xuUCrkZRcpoFbtSmTzYTIcMg7DanCxRVFCenDQdefAq04dbcVDVL1FMsx-NZlhL2ezdXBdY_BATK4bNJOhPmP-XDJPv2L5oGr4oG9FHQEIzjX3S=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-ccUFid4_Oor_DHD-K0NgHfEa1UecYQu712Z8y7ze4uCLVQ8CpO-jpehdD1Zq3Ey_l5syGQ8X5A4tU-mur-YkOUROgYHlrNt3f93G1IoP030vOlgruO7uuT0AAhfLuTByOAtcNAA=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9z9oaNXkehkvGAH39DzwPUZGVw9Vu3R9IKoZlfmjdeqaF2eI9cevaSU9Ex72R7g-1Bce594b92Phm-ykaOnN-k-D87BsMV_wyloZbrE05fAuauHDpHNn83QBBpGgCm_GaHNRQSxw=w65-h320-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_zfOPKoOo6P5-VDDwaRHj-YQxswLJCjgYGxXqNl8xGhRHnImNb8SdiuiiTX7jyoO-QHBcyJTwM0pS_l3rIxXYYrOzDrig6HER0lafEZO2nnCg4tK_iG6eZr9NSibGHkNm7Az1VaA=w65-h320-v0?authuser=0)

which do not directly capture cognitive demands but, rather, reflect those elements making items more difficult in other ways. The full scale rubrics can be found in Supplementary Information Section 2. We also explore alternative ablations with subsets of the catalogue as well as other taxonomies36,37 in Supplementary Information Sections 1.7 and 1.9, with none of them coming close to what the DeLeAn catalogue achieves in predictive or explanatory power.
In Methods sections ‘Ratio scales’ and ‘Dissecting the demand- ability space’, we explain how the scales are defined using rubrics that serve as measurement instruments for the instance demands and then build the methodology around them; this is applicable to whatever catalogue we use, be it DeLeAn v1.0, its extension or others. Our main
goal with these scales is to achieve AI evaluation with both explanatory and predictive power. We now demonstrate that this is indeed the case with four specific research questions, comparing our approach with standard practice or best baselines in AI evaluation.
**Annotation scales distinguish levels and dimensions**First we address the following research question: can humans distinguish the levels in the rubrics and the dimensions? The scales will only serve for explanatory purposes if they can be understood. In Methods section ‘LLM annotators and inter-rater analysis’, we describe how a group of five humans were selected, how the rubrics were presented and
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLq SNs
KNa
KNc
KNf
KNn
KNs AT
VO
0
400
800
1,200
1,600
ChemLLMBench
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLq SNs
KNa
KNc
KNf
KNn
KNs AT
VO
0
100
200
300
Civil Service Examination
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLq SNs
KNa
KNc
KNf
KNn
KNs AT
VO
0
10
20
30
Data Analysis
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLq SNs
KNa
KNc
KNf
KNn
KNs AT
VO
0 100 200 300 400
Date Arithmetic
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLq SNs
KNa
KNc
KNf
KNn
KNs AT
VO
0
50
100
150
200
GRE & GMAT
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLq SNs
KNa
KNc
KNf
KNn
KNs AT
VO
0
10
20
Language
0
200
400
600
800
LSAT
0
50
100
150
Math
0
50
100
150
200
MCTACO
0 100 200 300 400 500
MedCalcBench
0
200
400
600
MenatQA
0 1,000 2,000 3,000 4,000 5,000
MMLU-Pro
0
400
800
1,200
1,600
OmniMath
0 10 20 30 40 50
Reasoning
0
100
200
300
SAT
0
100
200
300
SciBench
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO
0
200
400
600
TempReason
0
100
200
300
TimeDial
0
200
400
600
TimeQA
0
250
500
750
1,000
TruthQuest
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO AS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO AS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VOAS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VOAS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VOAS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO AS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO AS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO AS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO
AS CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VOAS
CEc
CEe
CL
MCr
MCt
MCu MS
QLlQLqSNs
KNa
KNc
KNf
KNn
KNs
AT VO
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
**Fig. 2 | Distribution of level frequencies for the 18 demands (that is, demand profiles) of the 20 benchmarks in the ADeLe v1.0 battery. Supplementary**Information Section 1.12 reconciles common myths in LLM ‘reasoning’ and also describes the demand profiles for 20 so-called ‘reasoning’ benchmarks.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-AoiSbPK4_tyrYjiaKZvAAMNBmoHFQlbG0b7ZKhueQEAgqnM4TRODtVv9V4F2XCe5zTU5tqJGWqUpT3NJ94i7KXfgqwdFwnFK4pvPOqB8yR_btVUpmOPD9-3ymzCKThAty9Shp0g=w742-h734-v0?authuser=0)

*to what sample of data. The inter-rater agreement (rWG index) of these*five humans for the 18 demands ranges between 0.70 and 0.91 (with an average of 0.83). After applying the Delphi method, we have a consensus annotation, which we compare against GPT-4o, the LLM annotator,*resulting in high agreement rates (rWG scores between 0.75 and 0.94,*averaging 0.86). These agreement rates show common understanding between humans and with the automated annotations performed by
GPT-4o. Another source of necessary support for a rubric would be whether it leads to high predictive power, which we will explore in the section ‘Predictive power analysis: anticipating performance with assessors’, while still representing the construct in an understandable way.
The dimensions could be understandable by humans but conceptually redundant, in the sense that we could not conceive an instance for which one dimension level is high and the other is low. If such an
0
0.2
0.4
0.6
0.8
1.0
S uc
ce ss
p ro
b ab
ili ty
AS CEc CEe
0
0.2
0.4
0.6
0.8
1.0
S uc
ce ss
p ro
b ab
ili ty
CL MCr MCt
0
0.2
0.4
0.6
0.8
1.0
S uc
ce ss
p ro
b ab
ili ty
MCu MS QLl
0
0.2
0.4
0.6
0.8
1.0
S uc
ce ss
p ro
b ab
ili ty
QLq SNs KNa
0
0.2
0.4
0.6
0.8
1.0
S uc
ce ss
p ro
b ab
ili ty
KNc KNf KNn
0 2 4 6 8 10
Demand level
0
0.2
0.4
0.6
0.8
1.0
S uc
ce ss
p ro
b ab
ili ty
KNs
0 2 4 6 8 10
Demand level
AT
0 2 4 6 8 10
Demand level
VO
Babbage-002 Davinci-002 GPT-3.5-Turbo GPT-4o OpenAI o1-mini OpenAI o1
LLaMA-3.2-1B-Instruct LLaMA-3.2-3B-Instruct LLaMA-3.2-11B-Instruct LLaMA-3.1-405B-InstructLLaMA-3.2-90B-Instruct
DeepSeek-R1-Distilled-Qwen-7B DeepSeek-R1-Distilled-Qwen-14B DeepSeek-R1-Distilled-Qwen-32BDeepSeek-R1-Distilled-Qwen-1.5B
*n = 16 n = 317*
*n = 1,322*
*n = 322 n = 19*
*n = 84 n = 633 n = 804*
*n = 689 n = 201*
*n = 70 n = 19 n = 100*
*n = 100*
*n = 1*
*n = 1 n = 63 n = 609*
*n = 1,267 n = 129*
*n = 8 n = 44*
*n = 634 n = 762*
*n = 23*
*n = 83 n = 761 n = 1,311*
*n = 1,036*
*n = 111*
*n = 22 n = 154 n = 1,180*
*n = 1,450*
*n = 61*
*n = 53 n = 138 n = 139*
*n = 13*
*n = 80 n = 99 n = 906*
*n = 1,864*
*n = 337*
*n = 84 n = 633 n = 647*
*n = 546*
*n = 51*
*n = 8 n = 59*
*n = 321 n = 230*
*n = 4 n = 229 n = 1,260*
*n = 4,140*
*n = 1,390*
*n = 50 n = 1,018 n = 2,115*
*n = 1,462*
*n = 198*
*n = 85 n = 457 n = 1,455*
*n = 3,132*
*n = 687*
*n = 57 n = 663*
*n = 2,366*
*n = 699*
*n = 39 n = 965 n = 1,838*
*n = 108*
*n = 48 n = 505 n = 2,167*
*n = 1,749*
*n = 60*
*n = 63 n = 398 n = 235*
*n = 286*
*n = 48*
**Fig. 3 | Characteristic curves for the 18 demands and the 15 LLMs. The***x-axis shows the demand levels for that dimension and the y-axis the average*performance (probability of success) for each level. We ensure all bins are weighted the same in the fit as the largest one (except those bins with less than
100 instances, which use a proportional weight for robustness). The curve is a logistic fit with an anchor at coordinates (20, 0), accounting for 50% of the total*weight. The curves thus prolong beyond level 5 and this is why we show the x-axis*from 0 to 10, even if the present version of the scales only has levels up to 5.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-ZWieZoJuOVb2RoZMw2wmiDaYwixR8OprJ0J1yYKsAD_L3pB52BOA0naWkm8cr_Q4tUBGosflexwkXbYCi_X_fKM8P768mjJh61uXFGSodIoL3gTOP2188fsImH2f2cI7m8XTxBA=w626-h792-v0?authuser=0)

instance does not exist, humans will find it hard to distinguish the dimensions. The dimensions can still be correlated in a particular benchmark (for example, because the design or selection bias always makes one increase along with the other), but if the correlation is not near-maximal, we could conclude that there must be instances with very different levels. In Extended Data Fig. 1, we show the Spearman correlations of the demand levels for all of the dimensions in the ADeLe battery, a representative sample selected mainly from AI benchmarks in 2024. The generally low or moderate correlations indicate that most dimensions seem to carve different parts of the intelligence space, still allowing for cases in which the level for one dimension is low and the level for the other dimension is high. These examples do not abound but are not impossible. Only two correlations are greater than 0.8 and they fall on CL (Conceptualisation, Learning, and Abstraction), which looks slightly central in the manifold, given its strong correlation with MC (Metacognition and Critical Thinking) and with QLl (Quantita-tive and Logical Reasoning). We also see that the correlations for the extraneous dimensions are high with other demands (except for UG). In general, these positive or negative correlations can have several interpretations, as they are contingent to our choice of benchmarks.
The overall conclusion is that the annotations by GPT-4o seem understandable for humans across all dimensions, and the dimensions can be well distinguished. This is valuable, as other rubrics in AI evaluation practice tend to be specific, rarely quantitative and only occasionally meant to be explanatory44,45, despite the recognition that this understanding is a key factor in AI adoption27. Also, the correlations between dimensions do not seem to suggest that some combinations of demand levels are impossible, but simply infrequent in the present ADeLe battery v1.0. In this paper, our choice of instances and benchmarks was meant to be representative of the landscape of AI benchmarks, rather than a cherry-picked selection to minimize correlations. This was conditioned by our interest to explore what the benchmarks measure, as we study next.
**Explanatory power through benchmark demand profiles**The research question we address in this section is: what is the sensitivity and specificity of ADeLe and its constituent benchmarks? We can first look at the demand profiles per benchmark (Fig. 2). This is
informative to understand what the benchmarks actually measure and whether they measure what their designers claim to measure.
Overall, the profiles are considerably distinct, so apparently they measure different things. Benchmarks that focus on specialized topics (for example, ChemLLMBench, OmniMath, MedCalcBench and SciBench) show high demands in their respective domains (KNa (Applied Sciences), KNn (Natural Sciences) and KNf (Formal Sci-ences)), whereas benchmarks such as TempReason and TruthQuest, which target a single domain, often peak in further dimensions. Other benchmarks—such as Date Arithmetic, GRE & GMAT, MCTACO, Time-Dial and TimeQA—have uniformly low demands. By contrast, broader assessments such as Civil Service Examination, LSAT and MMLU-Pro show mixed profiles.
To determine whether they measure what they claim to measure, we must compare Fig. 2 with the list of capabilities or domains these benchmarks are said to be measuring (Supplementary Table 28). To better illustrate the issues of construct validity, we systematize sensitivity and specificity thresholds through two criteria:
should expect to see a wide distribution of levels for the demands*related to X in that benchmark: we characterize this by having mean ≥ 2 and standard deviation (s.d.) ≥ 1.0 in dimension X.*
Table 2 quantitatively shows a list of benchmarks and whether they meet these specificity and sensitivity criteria. In a few particular cases, there is some overlap between what a benchmark claims to measure and what capabilities it is sensitive to. However, this occurs for less than half of the capabilities that the benchmark claims to measure and does not happen for most benchmarks and dimensions (that is, aggregates have little sensitivity and specificity). For instance, benchmarks such as SAT are saturated for different reasons (low atypicality, that is, high contamination), whereas MedCalcBench actually measures whether the LLM has sufficient attention and scanning capability to process the given information, rather than purely measuring medical calculation capabilities. Further, in Supplementary Information Section 1.12, we
AS CEc
CEe
CL
MCr
MCt
MCu
MS
QLl QLq
SNs
KNa
KNc
KNf
KNn
KNs
AT
VO 8
Babbage-002 Davinci-002 GPT-3.5-Turbo GPT-4o OpenAI o1-mini OpenAI o1
AS CEc
CEe
CL
MCr
MCt
MCu
MS
QLl QLq
SNs
KNa
KNc
KNf
KNn
KNs
AT
VO
5 6 7 8
LLaMA-3.2-1B-Instruct LLaMA-3.2-3B-Instruct LLaMA-3.2-11B-Instruct LLaMA-3.2-90B-Instruct LLaMA-3.1-405B-Instruct
AS CEc
CEe
CL
MCr
MCt
MCu
MS
QLl QLq
SNs
KNa
KNc
KNf
KNn
KNs
AT
VO
5 6 7 8
DeepSeek-R1-Distilled-Qwen-1.5B DeepSeek-R1-Distilled-Qwen-7B DeepSeek-R1-Distilled-Qwen-14B DeepSeek-R1-Distilled-Qwen-32B
1 2 3 4 5 6 7
1 2 3 4
1 2 3 4
**Fig. 4 | Ability profiles of the 15 LLMs. An ability of l means that there is 50%***probability of the model to succeed on questions at demand level l (that is why*some abilities go beyond 5). In contrast to radial plots usually shown for LLMs in*the literature47,48, the values shown here are actual abilities on a ratio scale (0, ∞)*
and the values (in expectation) are more robust to changes in the difficulty distribution of the benchmarks used. In Supplementary Information Section 1.4, we show clear scaling curves of model abilities as a function of number of parameters.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_faPDNeKsf5_K9lWIg21Mb4b8ymr6U_JG28n36AJwBjngIqhU71cF10EZgRAJvIWgsO2Dq3C7mR17_K5gN4fR3YmVIylvwgOkA17cTVmj4eOush_JOD26qaON9KLPHvrETMr4p_A=w743-h302-v0?authuser=0)

reconcile common myths in LLM ‘reasoning’, observing the same issue of lacking either sensitivity or specificity for a batch of 20 ‘reasoning’ benchmarks.
Taking all of this into account, the specificity and sensitivity of common benchmarks are poor and variable. These results indicate that, by assigning one or more benchmarks to one ‘capability’ and aggregating their accuracy (as is the present standard practice), different demand levels and dimensions are averaged, leading to highly confounded results. If this is the baseline for common AI evaluation practice, it is simply insufficient to detect problems of specificity and sensitivity10,27. This issue becomes even more pronounced when integrating numerous benchmarks, such as BIG-bench46 and other mega-benchmarks. Even if
sensitivity may be increased by this integration (as we see for the whole of ADeLe; Extended Data Fig. 2), specificity is lost if aggregate scores are used. Instead, with our scales, we can compare mixed subsets of items from different benchmarks whose demand levels now become commensurate, create recombinations of instances to test specific capabilities and systematically select or discard benchmarks altogether based on their profile quality, before even using them.
**Explanatory power through LLM ability profiles**Another research question about explanatory power moves the focus to the AI systems: can we understand the capabilities of models and
**Table 2 | Sensitivity and specificity analysis of a subset of 20 benchmarks in ADeLe**
**Benchmark Claims to measure (their terminology) Claims to measure  (our terminology)**
**Sensitive to… Mean s.d. Accuracy**
ChemLLMBench • Generation of descriptions for molecules CEc•, CEe˚, KNf•, KNn˚ AS˚ 3.2 1.0 27.2
SNs˚ 3.2 1.3
Civil Service Examination • Logical reasoning QLI˚ KNa˚ 2.1 1.8 73.5
KNs˚ 2.0 1.8
Data Analysis • Data analysis CL˚, KNf˚, QLq˚ KNc˚ 2.2 1.0 69.7
LSAT • Analytical reasoning CEc˚, CL˚, MC˚, QLI˚ KNc˚ 2.9 1.1 81.6
MMLU-Pro • Knowledge KNa•, KNc˚, KNf˚, KNn˚, KNs˚, QL˚
KNa• 2.9 1.6 87.6
Math • Mathematics CL˚, KNf˚, QLI•, QLq˚ AT˚ 2.4 1.1 59.0
MCu˚ 2.4 1.0
QLI• 2.7 1.2
MedCalcBench • Medical calculation knowledge KNf˚, KNn˚, QLq˚ AS˚ 2.0 1.2 88.0
MenatQA • Event temporal reasoning QL˚ KNc˚ 2.8 1.0 72.8
OmniMath • Mathematical reasoning at Olympiad level CL•, KNf˚, QLI•, QLq˚ AS˚ 2.3 1.3 34.4
CL• 3.1 1.2
MCr˚ 2.6 1.1
QLI• 3.4 1.0
Reasoning • Spatial Reasoning QLI˚, SN˚ CL˚ 2.6 1.1 48.2
SAT • Critical thinking MC˚ AT˚ 2.2 1.1 98.3
SciBench • Scientific problem-solving KNa•, KNf˚, KNn•, KNs˚, MC˚ KNa• 3.0 1.6 83.7
KNn• 2.8 1.7
TempReason • Event temporal reasoning QL˚ KNc˚ 2.8 1.1 71.2
TimeQA • Event temporal reasoning QL˚ KNc˚ 2.4 1.1 89.0
Benchmarks are chosen such that at least one dimension that satisfies our two sensitivity criteria (s.d. ≥ 1 and mean ≥ 2). The second column shows what they claim to measure using their own terminology (sources are described in Supplementary Table 28). The third column shows the dimensions that the benchmarks claim to measure, expressed in our terminology. The fourth  column shows what the benchmarks are actually measuring or sensitive to. For every dimension to which the benchmark is sensitive, we provide the mean and s.d. of the levels for that dimension (fifth and sixth columns, respectively). The seventh (last) column shows the average accuracy of GPT-4o per benchmark as a reference. A superscript ∘ in the third and fourth columns indicates missed dimension (lack of sensitivity) or extra dimension (lack of specificity), respectively. A superscript • indicates the dimensions that are claimed to be measured and are actually measured (high sensitivity). The other six benchmarks from the ADeLe battery that do not follow the two aforementioned sensitivity criteria are Date Arithmetic, GRE & GMAT, Language, MCTACO, TimeDial and TruthQuest (with the accuracies of GPT-4o being 98.9, 95.6, 72.4, 95.1, 98.8 and 43.0, respectively). Takeaway: no benchmarks have high sensitivity and specificity, indicating a clear lack of construct validity.
their evolution in non-saturating plots? To answer this question, we selected 15 LLMs (Extended Data Table 1) and ran them on the ADeLe battery. As will be explained in more detail in Methods section ‘Sub-ject characteristic curves’, we use a dominant slice procedure: for*each demand level l along a dimension, we aggregate the results of*only those task instances for which the demands in all remaining*dimensions do not exceed l. We apply a logistic fit to these points,*yielding 18 per-dimension characteristic curves that capture how model success rates decline with increasing demand (Fig. 3). For example, the curves of certain dimensions are steep and with low variability across models, such as AS (Attention and Scan) and MCu (Calibrating Knowns and Unknowns). They explain success very well for instances in the low range (success for demands between 1 and 2) and the high range (failure for demand 5 or higher). By contrast, curves of other dimensions are flatter, such as KNs (Knowledge of Social Sciences), in which the discrimination (between success and failure) is the lowest. Notably, several dimensions show particularly distinct behaviours. The characteristic curves for MCr (Identifying Relevant Information) and MS (Mind Modelling and Social Cognition) clearly distinguish the performance of reasoning models (whether distilled or not) from non-reasoning ones. All subject characteristic curves, in independent plots, can be found in Supplementary Information Section 1.14.
We use the area under the subject characteristic curve to estimate ability, as explained in Methods section ‘Subject characteristic curves’. Note that an ability of 4 does not mean that the model can solve all or most of the items at level 4; it actually means that it can solve half of those at exactly level 4 in expectation. Figure 4 shows the ability profiles of the 15 LLMs, arranged into families. It is now more evident that those dimensions related to knowledge are high for larger models and reduced for small and distilled models. The reasoning models (such as OpenAI’s o1 and DeepSeek-R1-Distilled) have clear improvements on the two kinds of QL (Quantitative and Logical Reasoning) but also on MCr (Identifying Relevant Information) and MS (Mind Modelling and Social Cognition) (even down to 7B in the distilled models).
Finally, the increase of model abilities based on the number of parameters seems to be marginal for the two largest LLMs in the LLaMA or DeepSeek-R1-Distilled-Qwen families; this is further confirmed in Supplementary Information Section 1.4, in which we introduce the very first scaling laws of the actual abilities of LLMs. The use of open ratio scales commensurate to the demand levels is in opposition to the traditional scaling laws using performance, which easily saturate close to 100% accuracy and fluctuate heavily depending on the demand-level distributions of the selected benchmarks. Aggregation, even if sliced by benchmarks, domains or some tags46–48, leads to values in each dimension that are not commensurate, hard to explain and volatile to the distribution of difficulties. For instance, 70% aggregate accuracy in all logical reasoning benchmarks does not mean more capability than 50% aggregate accuracy in all metacognition benchmarks, not even more capability than 50% aggregate accuracy in another set of logical reasoning benchmarks. Reflecting to what we saw in Fig. 1, a moderate increase in demands can be associated with a big drop in performance (as seen in the two versions of OlymMATH). Making differences commensurate is one of the advantages of having demands and capabilities in the same scale. By looking at standardized scales on several dimensions, we can explain many conflicting claims made in the literature, such as LLMs being considered capable of ‘complex reasoning’49 in 2022, to claims of LLMs ‘not capable of the non-trivial reasoning’50 3 years later, which seems inconsistent with the substantial progress in chain-of-thought and reasoning models in the past few years. These contradictory statements about reasoning are explored and clarified with our scales in Supplementary Information Section 1.12.
In general, through our approach, we can investigate the capabilities of models and their evolution in a comprehensive and granular way, with characteristic curves explaining why each model succeeds
or fails in different regions, depending on the demand profile of the instance. This explanation originates from the information collected from the AI system under observation only: unlike IRT and other latent variable approaches (factor analysis or principal component analysis) derived from the results of many systems and instances, the abilities and explanations we get for one LLM with our methodology are not affected by the results or the choice of the other 14 LLMs.
**Predictive power through assessors anticipating performance**The last research question is, can we predict AI performance on unseen instances, both in distribution and out of distribution? As shown in the bottom row of Extended Data Fig. 1, most dimensions are negatively correlated with success, suggesting that, in aggregate, higher demands tend to reduce performance. This is promising about their predictive power when used in a multivariate way. To quantify this predictive power precisely, we trained three types of instance-level probabilistic classifiers, known as assessors: a random forest (RF) that maps the 19-dimensional demand annotation vector directly into a predicted probability of success, another RF model that relies on precomputed GloVe embeddings extracted from the raw text of each question and a fine-tuned LLaMA model trained end-to-end on the question text to predict success. Further details are provided in Methods section ‘Assessors and metrics’.
In-distribution results (Extended Data Table 2) show that, despite the large imbalance in some of the subject models’ own accuracies (from 0.102 for Babbage-002 to 0.843 for OpenAI o1), the demand-based RF achieves high discrimination (between success and failure), as measured by the area under the receiver operating characteristic curve (AUROC), and near-perfect calibration, as quantified by the expected calibration error (ECE). In terms of discrimination, we see that the best result is achieved for GPT-4o (0.882 in AUROC), being the most predictable LLM for the three assessors, whereas small models are less predictable. Averaged across all 15 LLMs, the demand-based RF produces an accuracy-weighted average AUROC of approximately 0.84, which is on par with the performance of the fine-tuned LLaMA assessor, whereas its average ECE (0.01) is much lower than that of the other approaches (0.03 for the GloVe-based model and 0.04 for the fine-tuned LLaMA model). Calibration plots demonstrating these results are provided in Supplementary Information Section 1.5. This strong in-distribution performance supports the internal validity of the methodology.
For the analysis of external validity, we further evaluated predictive performance under out-of-distribution conditions, by withholding entire tasks (task out of distribution) or entire benchmarks (benchmark out of distribution) from training (Extended Data Tables 3 and 4, respectively). In the task out of distribution set-up, the predictive power of the demand-based assessor remains robust (weighted AUROC = 0.81, ECE = 0.02), only slightly lower than in-distribution, and outperforms the rest of the assessors, whose performance considerably decreases (achieving weighted AUROC values of 0.79 for the LLaMA-based and 0.74 for the GloVe-based assessors). In the more challenging benchmark out of distribution, the performance of the demand-based assessor decreases a slightly more (weighted AUROC = 0.75 and ECE = 0.04). By contrast, the predictive power of the other two assessors suffers a much greater decrease. This suggests that the demand-based predictor is less prone to overfitting with spurious features compared with its counterparts. In Supplementary Information Section 1.9, we also demonstrate that the predictive power of our demand-based assessor is superior to two domain-based and learning-levels taxonomies.
Although many traditional IRT methods can explain performance on seen items, they cannot be used to predict performance for new instances (except linear logistic test models; see Supplementary
Information Section 1.1). IRT requires the item in question to be included in the pool of items that are used to extract the parameters and multidimensional IRT extracts the difficulty dimensions that matter for that pool only. In our case, any new instance, coming from any new benchmark or batch of examples, can be annotated automatically to obtain its vector of demands, which is independent of population, and from which we can predict performance.
Predictive power is paramount in a deployment setting in which the goal is to anticipate whether AI will perform well in unseen scenarios, rather than merely grading subjects in a testing environment. The natural baseline in AI evaluation practice is just average accuracy. This can extrapolate to an extent for system selection but, in the case of instance prediction, it leads to no discriminative power at all (an AUROC of 0.5) and calibration that is only good for in distribution. Uncertainty estimation from the LLM itself, on the other hand, requires running the model or, in many cases, a white-box or grey-box access, whose results are not better than external assessors20, as we have used here. Overall, the supremacy in predictive power observed for the demand-based assessors is clear. They are based on interpretable demands, in comparison with the two much larger and uninterpretable baselines. This is strongly encouraging, shedding light on a promising future for the reliable deployment of AI.
**Discussion**So far, AI evaluation is not meeting the needs of a fast-changing and increasingly diverse AI ecosystem. Understanding and anticipating performance has become an urgent requirement for many general-purpose AI systems. By building and exploiting absolute demand scales for annotating thousands of instances by means of automated rubrics, we have set a promising new direction for AI evaluation. The methodology we have presented and illustrated is comprehensive, scalable and standardizing, addressing many of the issues of conventional AI evaluation practice: a lack of explanatory and predictive power, as well as saturation and overfitting to specific populations of benchmarks and AI systems, respectively. With the pace and penetration of general-purpose AI, a rigorous, scalable and pipelined evaluation had been urgently demanded by researchers, companies, third-party evaluators, policymakers and regulators. It is paradoxical that powerful LLMs as annotators have made this new methodology possible and scalable. The explanatory value of LLM annotations has been independently validated by humans through inter-rater analysis and the Delphi method, and their predictive power stands through task diversity.
Nonetheless, our work is not without limitations. First, the DeLeAn v1.0 rubrics do not fully cover certain dimensions, such as navigation, and excludes capabilities in other modalities and paradigms in AI, such as multimodal systems and robotics, given that we limited our analysis to LLMs. We encourage other researchers to extend the set of rubrics to further dimensions (including propensities, values and other elements that are specifically conceived for safety or fairness and evaluate other kinds of AI systems with them). Second, there are very few high-quality level 5+ items in our present battery. Given the pace of progress in AI, the present scales (up to 5+) will need to be extended in a way that remains backward compatible with existing scales. Third, we could increase the predictive power in and, most importantly, out of distribution, especially if we introduce more benchmarks with ‘purer’ items only loaded on a few demands, and as LLMs improve as annotators. Fourth, we used LLM judges for grading model outputs, with excellent results compared with human graders. However, some more open-ended or agential tasks in the future may require more advanced automated grading.
Overall, the new methodology showcases the successful development of the construct-oriented paradigm in AI evaluation8, integrating perspectives from different disciplines. A streamlined collaborative platform (https://kinds-of-intelligence-cfi.github.io/ADELE/), and
associated catalogue of rubrics, will grow in the years to come, ready to explain and predict the performance and safety of AI systems. In a moment when AI evaluation is at the crux of research and regulations, and the science of evaluation had not yet digested the pace of general-purpose AI, our work takes crucial steps to make AI evaluation fit for purpose.
**Online content**Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-026-10303-2.
1. Boiko, D. A., MacKnight, R., Kline, B. & Gomes, G. Autonomous chemical research with**large language models. Nature 624, 570–578 (2023).**
2. Abramson, J. et al. Accurate structure prediction of biomolecular interactions with**AlphaFold 3. Nature 630, 493–500 (2024).**
3. Eloundou, T., Manning, S., Mishkin, P. & Rock, D. GPTs are GPTs: labor market impact**potential of LLMs. Science 384, 1306–1308 (2024).**
**4. Rahwan, I. et al. Machine behaviour. Nature 568, 477–486 (2019).***5. Shiffrin, R. & Mitchell, M. Probing the psychology of AI models. Proc. Natl Acad. Sci. USA*
**120, e2300963120 (2023).**6. Zhou, L. et al. Larger and more instructable language models become less reliable.
**Nature 634, 61–68 (2024). 7. Zhou, L. et al. Predictable artificial intelligence. Artif. Intell. 353, 104491 (2026).**8. Burden, J., Tešić, M., Pacchiardi, L. & Hernández-Orallo, J. Paradigms of AI evaluation:
*mapping goals, methodologies and culture. In Proc. Thirty-Fourth International Joint Conference on Artificial Intelligence 10381–10390 (IJCAI, 2025).*
**9. Burnell, R. et al. Rethink reporting of evaluation results in AI. Science 380, 136–138**(2023).
10. Eriksson, M. et al. Can we trust AI benchmarks? An interdisciplinary review of current*issues in AI evaluation. In Proc. Eighth AAAI/ACM Conference on AI, Ethics, and Society*850–864 (AAAI Press, 2025).
**11. Mitchell, M. The metaphors of artificial intelligence. Science 386, eadt6140 (2024).**12. Yang, Z. et al. Can large language models always solve easy problems if they can solve
*harder ones? In Proc. 2024 Conference on Empirical Methods in Natural Language Processing 1531–1555 (Association for Computational Linguistics, 2024).*
13. Guo, D. et al. DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning.**Nature 645, 633–638 (2025).**
14. Mathematical Association of America. American Invitational Mathematics Examination (AIME). https://maa.org/maa-invitational-competitions/ (2024).
15. Wang, X. et al. Evaluating general-purpose AI with psychometrics. Preprint at https:// arxiv.org/abs/2310.16379 (2023).
16. Burnell, R., Hao, H., Conway, A. R. & Orallo, J. H. Revealing the structure of language model capabilities. Preprint at https://arxiv.org/abs/2306.10062 (2023).
17. Ilić, D. & Gignac, G. E. Evidence of interrelated cognitive-like capabilities in large language**models: indications of artificial general intelligence or achievement? Intelligence 106,**101858 (2024).
18. Martínez-Plumed, F., Prudêncio, R. B., Martínez-Usó, A. & Hernández-Orallo, J. Item response theory in AI: analysing machine learning classifiers at the instance level.**Artif. Intell. 271, 18–42 (2019).**
19. Hernández-Orallo, J., Schellaert, W. & Martínez-Plumed, F. Training on the test set:*mapping the system-problem space in AI. In Proc. 36th AAAI Conference on Artificial Intelligence 12256–12261 (AAAI Press, 2022).*
*20. Schellaert, W. The Evaluation of Artificial Intelligence as a Prediction Problem. PhD thesis,*Universitat Politecnica de Valencia (2025).
21. Schellaert, W., Martínez-Plumed, F. & Hernández-Orallo, J. Analysing the predictability of**language model performance. ACM Trans. Intell. Syst. Technol. 16, 1–26 (2025).**
22. Pacchiardi, L., Cheke, L. G. & Hernández-Orallo, J. 100 instances is all you need: predicting the success of a new LLM on unseen data by testing on a few instances. Preprint at https://arxiv.org/abs/2409.03563 (2024).
23. Burden, J. et al. Inferring capabilities from task performance with Bayesian triangulation. Preprint at https://arxiv.org/abs/2309.11975 (2023).
24. Schlangen, D. Targeting the benchmark: on methodology in current natural language*processing research. In Proc. 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 2: Short Papers) 670–674 (Association for Computational Linguistics, 2021).*
25. Zellers, R., Holtzman, A., Bisk, Y., Farhadi, A. & Choi, Y. HellaSwag: can a machine really*finish your sentence? In Proc. 57th Annual Meeting of the Association for Computational Linguistics 4791–4800 (Association for Computational Linguistics, 2019).*
26. Hernandez-Orallo, J. AI evaluation: on broken yardsticks and measurement scales.*In Workshop on Evaluating Evaluation of AI Systems at AAAI (AAAI Press, 2020).*
27. Hardy, A. et al. More than marketing? On the information value of AI benchmarks for*practitioners. In Proc. 30th International Conference on Intelligent User Interfaces*1032–1047 (ACM, 2025).
28. Burden, J. Evaluating AI evaluation: perils and prospects. Preprint at https://arxiv.org/abs/ 2407.09221 (2024).
29. Stahl, B. C. et al. A systematic review of artificial intelligence impact assessments.**Artif. Intell. Rev. 56, 12799–12831 (2023).**
*30. Lee, M. et al. Evaluating human-language model interaction. Transact. Mach. Learn. Res.*https://openreview.net/forum?id=hjDYJUn9l1 (2023).
31. Collins, K. M. et al. Evaluating language models for mathematics through interactions.**Proc. Natl Acad. Sci. USA 121, e2318124121 (2024).**
32. Cohn, A. G. & Hernandez-Orallo, J. Dialectical language model evaluation: an initial appraisal of the commonsense spatial reasoning abilities of LLMs. Preprint at https://arxiv. org/abs/2304.11164 (2023).
33. Roberts, M., Thakur, H., Herlihy, C., White, C. & Dooley, S. Data contamination through the lens of time. Preprint at https://arxiv.org/abs/2310.10628 (2023).
34. Levy, M., Jacoby, A. & Goldberg, Y. Same task, more tokens: the impact of input length on*the reasoning performance of large language models. In Proc. 62nd Annual Meeting of the Association for Computational Linguistics 15339–15353 (Association for Computational*Linguistics, 2024).
35. Wang, Y. et al. MMLU-Pro: a more robust and challenging multi-task language**understanding benchmark. Adv. Neural Inf. Process. Syst. 37, 95266–95290 (2025).**
36. Miller, J. K. & Tang, W. Evaluating LLM metrics through real-world capabilities. Preprint at https://arxiv.org/abs/2505.08253 (2025).
*37. Bloom, B. S., Engelhart, M. D., Furst, E. J., Hill, W. H. & Krathwohl, D. R. Taxonomy of Educational Objectives Vol. 2 (Longmans, 1964).*
*38. Ong, I. et al. RouteLLM: learning to route LLMs from preference data. In Proc. Thirteenth International Conference on Learning Representations (ICLR, 2025).*
39. Zhou, L., Martínez-Plumed, F., Hernández-Orallo, J., Ferri, C. & Schellaert, W. Reject before*you run: small assessors anticipate big language models. In Proc. Workshop on AI Evaluation Beyond Metrics (CEUR Workshop Proceedings, 2022).*
*40. Pacchiardi, L. et al. PredictaBoard: benchmarking LLM score predictability. In Findings of the Association for Computational Linguistics: ACL 2025 (eds Che, W. et al.) 15245–15266*(Association for Computational Linguistics, 2025).
**41. Clayton, H. H. Thermometric scales for meteorological use. Nature 60, 491 (1899). 42. Davies, C. N. Measurement of particles. Nature 195, 768–770 (1962). 43. Alessandretti, L., Aslak, U. & Lehmann, S. The scales of human mobility. Nature 587,**
402–407 (2020).*44. Jin, Z. et al. CLadder: assessing causal reasoning in language models. Adv. Neural Inf.*
**Process. Syst. 36, 31038–31065 (2023).**
45. Saparov, A. & He, H. Language models are greedy reasoners: a systematic formal analysis*of chain-of-thought. In Proc. Eleventh International Conference on Learning Representations*(ICLR, 2023).
46. Srivastava, A. et al. Beyond the Imitation Game: quantifying and extrapolating the*capabilities of language models. Transact. Mach. Learn. Res. https://openreview.net/*forum?id=uyTL5Bvosj (2023).
47. Balachandran, V. et al. Eureka: evaluating and understanding large foundation models. Preprint at https://arxiv.org/abs/2409.10566 (2024).
*48. Fountas, Z. et al. Human-inspired episodic memory for infinite context LLMs. In Proc. Thirteenth International Conference on Learning Representations (ICLR, 2025).*
49. Zhou, D. et al. Least-to-most prompting enables complex reasoning in large language*models. In Proc. Eleventh International Conference on Learning Representations (ICLR,*2023).
50. Fang, M., Wan, X., Lu, F., Xing, F. & Zou, K. Mathodyssey: benchmarking mathematical**problem-solving skills in large language models using odyssey math data. Sci. Data 12,**1392 (2025).
**Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in**published maps and institutional affiliations.
**Open Access This article is licensed under a Creative Commons Attribution**4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
© The Author(s) 2026
**Methods**
**General scales**For more than a century, psychology has introduced many constructs with explanatory and predictive power about human behaviour, from conscientiousness to metacognition. On the basis of experimental data and theories of human cognition, these constructs are usually organized into hierarchical taxonomies, such as the Cattell–Horn–Carroll structure of human cognitive abilities51 or the Big Five personality traits52. In principle, we could build a similar taxonomy for artificial cognition, based on theory and experiments about machine behaviour4. However, as the base population of machines is much more arbitrary and changing than those of humans, it makes more sense to devise a taxonomy that could encompass any kind of natural and artificial intelligence, by considering capabilities that are meaningful for more general theories of cognition53. Under this paradigm and by integrating and generalizing taxonomies from human psychology, comparative cognition and AI53, a general taxonomy of 14 capabilities was designed54 and later extended with corresponding 14 rubrics by Tolan et al.55 for the study of AI and human capabilities in the workplace. These rubrics assigned the presence or absence of the need for each capability in generic tasks extracted from worker surveys, occupational databases and AI benchmarks.
This taxonomy serves as a basis to construct a catalogue of capabilities following these four criteria: (1) the capabilities are general rather than specific, enabling the characterization of a wide range of tasks usually present in human activities; (2) the capabilities represent concepts that are understandable to humans (and LLMs), enabling their levels to be expressed through rubrics in plain natural language; (3) there is no a priori assumption of correlation or orthogonality in these capabilities as observed in humans or LLMs, to accommodate various present and future AI paradigms (rather than overfitting to a specific state of the art of AI); and (4) two capabilities are considered distinct as long as many tasks could conceivably require a high level of one but not the other. Following criteria (1) and (2), we use capabilities that are familiar in human and non-human cognition and AI practice (see Supplementary Information Section 1.1 for a coverage of taxonomies in humans and AI). Despite these inspirations, we follow (3) to ensure that the catalogue does not replicate human intelligence hierarchies or taxonomies derived from populational methods. But we do not look for a middle ground either: we do not assume that humans and AI systems share a common capability structure. Finally, ensuring (4), we consider two dimensions to be different (for example, metacognition and logical reasoning) if it is possible to conceive tasks that require one but not the other, independently of whether they are correlated in human or AI populations. Indeed, we include dimensions that may not be the most discriminative ones for the population of benchmarks or LLMs we use in this paper but can be useful to detect emergent properties in the future. This population independence is especially critical in the present era in which benchmarks and models get replaced every few months: for instance, for models without chain-of-thought, dominant until 2024, the set of reasoning capabilities we use may not have been very discriminative; however, with the advent of models with reinforcement learning and integrated chain-of-thought in 2025, reasoning capabilities become more informative. If our catalogue had not included them, we would have been unable to detect this shift, and the same applies for capabilities that may not be discriminative now but can be conceived of as different from others and may be informative in the future. As we may nevertheless miss some capabilities that will become relevant, the catalogue is expected to expand to include new dimensions in the future, provided they are understandable to humans.
As mentioned, our work builds on that of Tolan et al.55. First, we extend the taxonomy by including both knowledge and extraneous dimensions. Second, we develop new scales and rubrics in a quantitative range between 0 and 5+, with 0 representing absence of demand, values 1–4
representing increasing demand levels of the capability and 5+ representing 5 or above. For instance, the famous Sally–Anne false-belief task assesses understanding of an individual’s false belief about the properties of an object if those properties change while they are not looking (Sally will look for her marble in the basket where she left it, even though Anne moved it to the box when Sally was away). This may be level 4 for dimension MS (Mind Modelling and Social Cognition) but may be level 0 for dimension QLq (Quantitative Reasoning). Similarly, the question “if all A are B, some B are C, no C are D, and all D are E, what can be inferred about the relationship between A and E?” may be level 4 for QLl (Logical Reasoning) but level 0 for MS (Mind Modelling and Social Cognition).
Extended Data Table 5 shows the set of dimensions we have included in the first version of the DeLeAn rubric set (DeLeAn v1.0). We adapt seven broad capabilities from Tolan et al.55, applicable to LLMs (for example, ‘auditory processing’ was discarded), and refine a subset of them hierarchically with subdimensions, making them a group of 11 ‘proper’ cognitive capabilities that we call ‘elemental’; by ‘elemental’, we mean that these capabilities are not derived from others, as opposed to the knowledge dimensions, which are more acquisitive. These ‘elemental’ subdimensions were included after several rounds of discussions about whether some of the original seven broad subdimensions could be carved into finer, but still general, subdimensions that are conceptually distinct. Beyond the capabilities, we also include new dimensions accounting for domain ‘knowledge’, separated into five subdimensions (KNn, KNs, KNa, KNf, KNc) covering large branches of human knowledge, and three ‘extraneous’ ones, AT (Atypicality), VO (Volume) and UG (Unguessability), to account for elements that make the task more challenging independently of elemental capabilities or knowledge demands.
In particular, Atypicality deals with contamination56,57 and other familiarization effects leading to capability overestimation because similar data were seen during training. An AI system may simply succeed because it has memorized the instance. This dimension can be used to explain and predict performance, by identifying AT as a confounder with the other demands. The second extraneous dimension, Volume, represents the use of ‘collages’ to make instances more difficult. For instance, if we put ten simple additions in an exercise and we score whether all of them are correct, then we have increased the difficulty greatly, but the quantitative reasoning demand is the same. We call this phenomenon amalgamation and it is a recurrent trick to make instances more difficult, either in benchmarks of increasing hard-ness46,58,59 or in adversarial testing60. There is a correlation between the size of the questions (and the answers) and the difficulty you can achieve with it46 (Figs. 3 and 4). In the end, amalgamation produces an underestimation of the capabilities, because the subjects fail at tasks that are incorporating many simple things. The chances of error accumulate, even if the cognitive load is not necessarily increased61,62. Finally, Unguessability captures the very usual funnelling effect to make a question more amenable for scoring but, at the same time, reducing its difficulty. The obvious case is the use of multiple-choice questions, which have become predominant in most AI benchmarks, despite its issues63. Reducing or increasing the number of options has been a common practice to change the ‘difficulty’ of a task without modifying its cognitive demands35. In general, these three extraneous dimensions will account for an important proportion of the predictability in LLM success and including them helps clarify these confounding effects.
Although we have 19 dimensions in total, only the first 18 correspond to proper capability demands (11 elemental, five knowledge and two extraneous) that may be met by the subject or not, with Unguessability being a special extraneous dimension reflecting the funnelling in the item design (for example, multiple-choice questions). Because of that, it is the only dimension expressed between 0 (the correct answer is trivially determined by the question) and 100 (unguessable, that is, a good open-ended question). Each of the other 18 demand rubrics includes
a general description of the construct to be annotated, followed by a description of each of the levels, from 0 to 5+, with three ‘anchor’ instances each. By following Supplementary Information Section 2, we can better understand the trade-offs in the construction of the rubrics.
It is important to highlight that the catalogue is not definitive and is meant to be extended in the future using the same criteria of dimensions being general and conceptually distinct. We use the term ‘catalogue’ instead of ‘taxonomy’ to better emphasize its non-definitive nature. This is also why we call the rubrics and battery DeLeAn v1.0 and ADeLe v1.0, respectively, with the vision of incorporating new capabilities and propensities in the future. This will also include considering safety, fairness and values64,65 and not only performance (correctness) as the variable to predict.
**Ratio scales**We deliberately design the demand scales as ‘ratio’ scales66, with an absolute zero(no demand) and differences that are comparable across the scale. In the social sciences, a common interest lies in understanding differences, as no human has zero capabilities, and an ‘interval’ scale with negative capabilities makes sense (as in IRT) or as percentiles of a normal distribution (as IQ scores). We argue that for AI, we should aim for the top level in Stevens’s topology of measurement67: the ratio scales. Ratio scales have all of the properties of the previous scales: intervals and differences are meaningful but so too are ratios. Given the flexibility with which we can regulate compute and time use in AI, it makes more sense to set an absolute zero (no compute) on the demands and build the scales in such a way that ratios are meaningful. We wish*to say that instance xi at level 6 doubles the demand of an instance xj*at level 3. Taking into account that we fit logistic functions, this can be understood in terms of the log odds of being correct halving when*moving 2x in the scale and doubling when moving x/2 in the scale68.*
For this first version of the scales, we decided to choose levels (0, 5)*of the full range (0, ∞) for practical reasons. With a single rubric, it is*hard for humans and LLMs to refine beyond five ordinal values—this is why Likert scales are so popular. Note that the rubrics only show cases in an ordinal scale between 0 and 5 and the annotations are discrete, never generating non-integer values. This is convenient for avoiding the need of binning for the curves and the demand histograms, but the values become fully continuous when estimating the abilities. In any case, it is usual to consider originally ordinal scales as interval or ratio scales when the number of levels is 5 or more69. Indeed, the magnitudes between 0 and 5 should not be interpreted as a mere rank. The way the scale increases depends on what the demand represents, but the pace of increase, the actual scale, is chosen in such a way that all scales are commensurate. For instance, for knowledge dimensions (applied sciences, customary everyday knowledge, formal sciences, natural sciences and social sciences and humanities) we thought of levels corresponding roughly to elementary, middle, high, undergraduate and graduate education. By looking at the attainment rates of some statistical data of education level rates (for example, Organisation for Economic Co-operation and Development (OECD) data70) and the specialization of domains as the educational level increases, we noticed*that the questions of level l were usually sufficiently advanced to have roughly one person in 10l−1 solving it correctly. Then we extend this*criterion as a rule of thumb for all scales, although future work could perform a proper calibration and see that the base of each dimension corresponds with the correct proportions. By using the same base, we achieve ratio scale consistency and commensurate scales across*dimensions. In general, an item is at level l if l is the highest number such that, in at least 95% of samples of n = 10l individuals, there is at*least one correct response. The levels we have defined are 0 (None), 1 (Very low), 2 (Low), 3 (Intermediate), 4 (High) and 5+ (Very high), with*n going from 1 to 100,000.*
We could have calibrated some dimensions using procedurally generated examples. For instance, in reasoning, we could have increased
the components of reasoning processes71 to see whether the levels increase accordingly, but each of these ‘scales’ would have been incommensurate with each other and not sufficiently general.
The 18 rubrics were crafted following the above criteria, using several iterations while testing with human and AI annotators. The final rubrics can be found in Supplementary Information Section 2. Once the rubrics were settled, we conducted the experiments, annotating tens of thousands of instances using a LLM, scalably and rapidly. Five annotation examples are illustrated in Extended Data Fig. 3.
**Dissecting the demand-ability space**Annotating instances using these general scales allows us to compare what makes them easy or hard and provides the same lens of analysis independently of where the instance comes from: human test, AI benchmark or new item design. We can discard or combine instances to build a specific test profile. Although this is not new in psychology or AI72, the scales can be applied to any task, test or collection of benchmarks; DeLeAn v1.0 is instantiated to consider only textual modality for now and to be extended in the future. By using the same scales in a standardized way, the comparison of the vast space of tests and benchmarks becomes possible for the first time.
For instance, in this paper, we applied DeLeAn to 16,108 instances from 63 tasks from 20 benchmarks, curated from the 2024 proceedings of six AI conferences and other venues, while ensuring both data quality and diversity (details in the section ‘Benchmark battery: instance selection and curation’). This is unprecedented, as all of these tasks are now represented within the same 19-dimensional space of 18 general cognitive demands (plus unguessability). After the annotation, these 16,108 instances constitute the ADeLe battery (Supplementary Table 28). We can observe the distribution of the demand levels for each dimension, the demand profile, represented as a polar histogram. Exploring this for each benchmark in ADeLe (Fig. 2) helps answer the question of whether each benchmark actually measures what their developers claimed to measure, as we explored in the main text.
Once instances are annotated, we can do more insightful analyses than just calculating one average for a whole dataset. When we run a LLM on an annotated benchmark such as the ADeLe battery, we can analyse each dimension separately using a subject characteristic curve73 to show the performance of an AI system as a function of demand levels, offering a comprehensive and robust delineation of the model’s ability on that dimension. The curve can be summarized using the area under the curve, referred to as the ability score, as described in the section ‘Subject characteristic curves’.
With this procedure on the characteristic curves, we can derive ability profiles as 18-dimensional vectors containing the estimated abilities. The usual way of representing a score profile with many dimensions is a radial plot. This is common in the behavioural sciences and more recently in AI as well. However, if we look at these plots in AI papers (for example, refs. 47,48), we see that what they represent in each dimension is the average accuracy of a selection of instances that belong to a particular domain or dataset, not an actual ability. The plots based on performance scores will change as the difficulty of the selected instances varies, whereas an ability profile is invariant to these changes. Overall, our notion of ability using the general scales is very different from the common yet inaccurate use of the term in AI as a synonym of performance. This includes the use of the term ‘capability’ in the area of safety evaluations: even if informally the concept may be associated with levels74, these levels were never defined or scaled.
By comparing the ability profile of an AI system with the demand profile of a task instance or a benchmark, we can explain the observed performance. Moreover, using the differences between abilities and demands, we can use interpretable algebraic models to anticipate performance for new instances (Supplementary Information Section 1.7.7). Notably, there is potential for other options as well. For example, the 18 values that are annotated for each single instance on the scale 0 to
**5+ and unguessability constitute a 19-dimensional vector x, which can**be used as predictor variables for a probabilistic classification model, an assessor, outputting the (estimated) performance of an AI system on that instance. Each assessor can be trained specifically for each LLM, without relying on the features of the LLM. As shown in the main text, we can compare this with many other powerful ways of predicting performance, such as assessors with embeddings and fine-tuned LLMs (there are more details on how we build distinct assessors in the section ‘Assessors and metrics’). Notably, despite the much smaller computation cost (apart from annotating the battery, which only needs to be done once), the predictive power is substantially better for the demands-based assessor than the best baseline, especially out of distribution, and evidently much better than average accuracy, which is only well-calibrated in distribution. This is because our general scales provide predictive features over a wide variety of tasks while limiting overfitting on features that become spurious when switching tasks and benchmarks. Finally, just as ability profiles are non-populational, the assessors we derive for each system are inferred exclusively from the results of that system, rather than from population-level parameters such as those used in scaling laws for aggregate performance prediction75.
**LLM annotators and inter-rater analysis**With the rubric set in hand, we annotate any new instance along each dimension using a LLM to replace human annotations, to scalably and rapidly annotate thousands of items. Although there may be some discordances between LLM and human scores, scalability is critical for widespread deployment of the new evaluation methodology. This can be seen as a trade-off but also as an opportunity to have stable and fully reproducible annotations using LLMs, which can be improved as LLMs get better or are more aligned with human interpretation. In fact, the three instance anchors per level were very instrumental for the LLMs to perform good ratings (in a few-shot inference fashion) but also for human understanding. In our case, we performed the annotations with GPT-4o, with which we found high agreement rate. The use of comprehensive rubrics in natural language that can be applied automatically is a substantial advancement in making the explanatory power of the scale a reality, especially if humans could interact with the LLM to explain their annotations.
Specifically, we prompt GPT-4o (‘gpt-4o-0513’ checkpoint)76 to annotate task demands levels (on a discrete scale from 0 to 5) instance by instance for all individual rubrics (see DeLeAn Rubric Set v1.0 in Sup-plementary Information Section 2). We use the Azure AI application programming interface (API) with chain-of-thought prompting (Sup-plementary Table 23) at temperature set to 0 with a maximum output token length of 1,000, to ensure that answers can be long enough for nearly all instances while substantially reducing the cost. The stopping condition and the rest of the parameters are left by default.
To assess the agreement rate between humans and GPT-4o, for each demand, we randomly sampled 50 instances while ensuring each level had at least a sample size of 3 to avoid minority levels getting neglected in our inter-rater analysis. This led to 900 instances to be annotated, which were distributed to five humans (authors of this paper, corresponding to Y.H., Y.M.-D., L.Z., Q.Z. and S.Z.), for which each instance was annotated by exactly three humans. The annotation process consisted of two steps. First, each annotator independently assigned a difficulty level (using the 0 to 5+ scale) to each instance using the rubrics. Next, the annotators met for a Delphi77 consensus meeting. During this meeting, instances for which the minimum and maximum ratings of the three annotators differed by two or more points were discussed in detail until a consensus was reached. For cases with differences of less than two points, a simple majority vote determined the final annota-*tion. To check the inter-rater agreement rates, we use the rWG index78,79*with the default rectangular null distribution; a score greater than 0.7 is generally considered as a good agreement rate.
The result is shown in Supplementary Table 22, in which we observe*satisfactory rWG scores (average = 0.86) between Delphi consensus and*GPT-4o, consistently greater than 0.80, except for one dimension with*a score of 0.75. However, the rWG scores between humans before the*Delphi consensus meeting were slightly lower for certain dimensions. These initial disagreements are because of several reasons, identified during our Delphi consensus meetings: occasional misinterpretations of certain words or terminologies, mainly for those humans whose primary language for daily use is not English; knowledge gaps in annotating certain particularly challenging task instances beyond the expertise of annotators; cultural variations affecting annotations, especially within some knowledge dimensions; and several inconsistent ratings for which annotators could not explain their own numerical assignments in hindsight, possibly caused by tiredness in annotating a large amount of instances; the reported time in annotating 50 instances on only one single rubric usually ranges between 30 and 60 min. The Delphi method proved useful to mitigate the individual biases and inconsistencies from human annotations caused by the miscellaneous reasons listed above, among others.
In Supplementary Information Section 1.8, we also explore two alternative LLM annotators. One is DeepSeek-V3, which is similarly powerful but open-weight: keeping all other things equal, it exhibits a similarly high agreement rate with the Delphi consensus (an average*rWG of 0.83; slightly worse than that for GPT-4o of 0.86) and it unlocks*similarly high predictive power, comparing with the section ‘Predictive power analysis: anticipating performance with assessors’. The other LLM is LLaMA-3.1-8B-Instruct, which is open-source but much smaller. We find that it achieves a reasonably good agreement rate with the Delphi*consensus (an average rWG of 0.74; noticeably worse than that for GPT-4o*of 0.86) and it exhibits moderately worse predictive power, comparing with the section ‘Predictive power analysis: anticipating performance with assessors’. This is to be expected, as older and smaller models are relatively less powerful in terms of obtaining reliable annotations.
Looking to the future, despite good agreement between humans and GPT-4o as annotator, higher agreements may be possible as the capabilities of LLMs progress, including their potential for explaining their annotations to humans.
**Benchmark battery: instance selection and curation**We constructed our benchmark battery by reviewing papers published in the 2024 proceedings from top-tier machine learning conferences (ICML, NeurIPS, ICLR) and natural language processing venues (ACL, EMNLP, NAACL). In our search, we first identified papers with ‘bench’ in the title and then supplemented the collection with further benchmark sets found at other reputable venues. Before including any benchmark (or subset thereof), we applied a rigorous quality check to ensure that the source meets the following selection criteria:
dance of trivial instances. A benchmark is discarded if state-of-the-art LLMs such as GPT-4 achieve more than 75% overall accuracy.
This eventually resulted in a total of 20 benchmarks from nine papers, comprising 63 tasks for our analysis (Supplementary Table 28). For efficiency reasons, we randomly sampled up to 500 instances per task to strike a balance between data diversity and size. This led to an original battery of 21,996 instances.
Last, we prompted GPT-4o to annotate three quality indicators: (1) the accuracy of ground-truth labels; (2) the objectivity; and (3) the unambiguity, for all instances, graded with a Likert scale from 1 to 5 (Supplementary Tables 24, 25 and 26). We inspected the annotations of 50 randomly sampled instances with a score of 1 for each quality indicator, in which a human judge (a researcher with a background in computer science) reviewed these annotations and labelled them as ‘agree’, ‘disagree’ and ‘uncertain’. For the accuracy of ground-truth labels, the agreement, disagreement and uncertainty rates were 32%, 6% and 62%, respectively. For objectivity, the agreement, disagreement and uncertainty rates were 68%, 10% and 22%, respectively. For unambiguity, the agreement, disagreement and uncertainty rates were 70%, 22% and 8%, respectively.
Given this observation, we removed those instances with a score of 1 in any of the three aforementioned indicators, which accounts for 16% of instances in the initial battery, reducing the battery at this stage to 18,462 instances. Also, we discarded 0.9% of instances in which the LLM annotator did not offer an annotation (for example, flagged by OpenAI’s moderation filters) or did not yield demand annotations in an expected and easily processable format, resulting in 18,291 instances remaining.
This is a satisfactory result, as we removed many problematic instances at the cost of eliminating a small proportion of seemingly good ones. This cleaning is critical to reduce noise when deriving the ability profiles of models and evaluating the predictive power of assessors.
**Subject LLMs and grading**The pool of analysed subjects includes 15 LLMs in total (Extended Data Table 1), six proprietary models from OpenAI, five open-weight models from Meta and four open-weight models from DeepSeek:
The four GPT models, Babbage-002, Davinci-002, GPT-3.5-Turbo (built as ‘gpt-35-turbo-0613’) and GPT-4o (built as ‘gpt-4o-0513’), are the original instruction-tuned models in the GPT family, in which the last two are also shaped up by fine-tuning with human feedback and further include a moderation post-filtering mechanism82. By contrast, OpenAI o1-mini (built as ‘o1-mini-2024-09-12’) and OpenAI o1 (built as ‘o1-2024-12-17’ with the reasoning effort parameter set to ‘low’) belong to a family of ‘reasoning’ models, designed to take extra time to generate and refine a chain-of-thought before producing a final answer. All of these models were accessed through the public API offered by Azure AI Foundry.
For inference, all subject models were queried with the temperature parameter set to 0 and no system prompt, with the exceptions of Ope-nAI’s o1 models, which can only be queried with temperature equal to 1, and the DeepSeek-R1-Distilled-Qwen models, which were queried with a temperature of 0.6 and a top-p of 0.95 as recommended by the original paper13. Similarly, we use chain-of-thought prompting for all models except for the ‘reasoning’ models (OpenAI’s o1 models and DeepSeek-R1-Distilled-Qwen models), which were already shaped up to perform chain-of-thought by default by their developers. In terms of maximum output token length, we use 2,000 tokens for all models, except for OpenAI’s o1 models and the DeepSeek-R1-Distilled models, which use 16,384 tokens instead. We used the default values for the stopping condition and the rest of the parameters.
Most grading of instances in present AI evaluation practice is performed with LLMs as a judge85, because manual grading for a large number of instances and models would be infeasible. We follow that practice but we do not want to consider instances that are wrongly graded, because that would portray a misleading account of the explanatory and predictive power of the methodology we present in this paper. We then prefer to discard those instances for which the LLMs (as a judge) are not robust. This means that we exclude some instances and this may introduce some bias selection in ADeLe. We believe instances that are hard to grade or verify do not necessarily mean that they are easier or harder to solve. In either extreme, they would increase predictability but not the separability metrics such as AUROC. Consequently, we perform the following procedure. We automatically grade the responses of these models on a discrete scale between 1 (surely incorrect) and 5 to (surely correct) using two LLMs, GPT-4o and Claude 3.5 Sonnet (‘claude-3.5-sonnet-1022’ checkpoint), prompted with temperature set to 0 while the rest follows the default configurations. The prompt contains both the input, the response of the subject and the ground truth (Supplementary Table 27) for a sample prompt template. To spot instances that are ‘hard to verify’ (for example, owing to inherent subjectivity or erroneous ground truth), which can introduce noise into the analysis, we remove approximately 12% of instances in which both LLM graders did not agree through simultaneously outputting either correctness scores ≥4 (both graders think the answer is a success with some confidence) or correctness scores ≤2 (both graders think the answer is a failure with some confidence) when verifying GPT-4o as a subject; this forms the final ADeLe battery v1.0, with 16,108 instances. We finally labelled input–output pairs graded with a mean score less than 3 as failure pairs and success otherwise (scores of 3 were filtered in the previous step anyway). We randomly sampled 100 instances from all of the gradings and manually found that 98% of input–output pairs are correctly verified.
**Assessors and metrics**An assessor is an external metamodel designed to predict the performance of a subject system (for example, a LLM) on individual task instances by taking features of those individual task instances as input19,21,22,39. These features can range from the raw representation (full text or image) to metafeatures representing cognitive demands and linguistic characteristics, as well as more structured representations such as average (word) embeddings of each task instance. When performance is defined as a binary success score (correct versus incorrect), an assessor can be built by using any standard binary classifier, including statistical models (for example, RF) and fine-tuned language models (for example, fine-tuned LLaMA-3.1-8B). Such models are trained to anticipate the success probabilities of a given subject on task instances without executing that subject and can be either tailored to predict the performance of a single AI system or designed to generalize across systems. In this work, we train and compare three types of assessor:
18 demands and the special UG (Unguessability) dimension as input to predict a subject LLM’s performance. The in-distribution data are
used to optimally select the minimum number of samples required to split an internal node, chosen as 2, 50 or 200.
For implementation, the RF models were trained using the scikit-learn library88, whereas the fine-tuned LLaMA-3.1-8B was trained on the Trans-formers library89 using the PyTorch backend running on Python 3.11. All unspecified hyperparameters were left at their default values.
In terms of computational cost, the on-demand assessor was extremely efficient. On an M3 Pro CPU, the data of each subject were processed by means of tenfold cross-validation in about 4 s. By contrast, the embedding-based assessor took about 40 times as long owing to the higher computational overhead of processing dense vector representations. The fine-tuned LLaMA assessor was by far the most expensive, taking around 300 GPU hours on a single V100 GPU to converge (that is, around six orders of magnitude longer than the demand-based approach).
To quantify the predictive quality of these assessors, we used AUROC and the ECE with ten equal-width bins, as these two metrics capture two key aspects of predictive power (discrimination and calibration) and each of them is commensurate when comparing the predictive power of distinct assessor–subject pairs.
We compute the statistical significance between the demand-based assessor and the strongest baseline. We apply the Wilcoxon signed-rank test based on the win–loss outcomes using paired comparisons of each fold between two assessors (across ten folds with ten repetitions each based on distinct seeds).
Although the use of demand annotations substantially outperforms the other baseline approaches as seen in Extended Data Tables 2, 3 and 4, two key factors explain why the discrimination power declines in out-of-distribution settings. First, because our analysis includes only 63 tasks from 20 benchmarks—many of which (for example, Chem-LLMBench) have non-overlapping demand distributions— the training data do not fully capture the multidimensional demand space. We suggest that the predictive power of the demand-based assessor for any arbitrary new tasks or new benchmarks can be boosted to the level of in-distribution by ensuring that the demand distribution of the training data efficiently covers the multivariate demand space.
Second, there is a paucity of extremely difficult instances to challenge the high-performance models (for example, OpenAI o1-mini, OpenAI o1, DeepSeek-R1-Distilled-Qwen-32B). As shown in Fig. 3, even at level 5 (for which instance coverage is low), the best models maintain success probabilities well above zero and the estimated abilities can go beyond 5, just by extrapolation. In Supplementary Information Sec-tion 1.6, we further discuss these factors and potential improvements on instance selection and automated grading.
**Subject characteristic curves**Extended Data Fig. 4 shows a subject characteristic curve for the results of Llama-3.1-405B-Instruct on 16,108 instances of the ADeLe battery, sorted and binned by the levels on the dimension KNn (Knowledge of Natural Sciences). As further elaborated in Supplementary Information*Section 1.2, for each bin b for that dimension, we exclude all points for*
which the level of any other dimension is greater. In other words, we want the represented dimension to dominate on the instances we are showing (in this case, only 3,785 out of 16,108).
On this plot, we can then fit a logistic function and look for the*x-axis value at which the probability of the subject to succeed is 0.5.*In Extended Data Fig. 4, this leads to an estimated ability of 4.3. Ability can then be interpreted as the level of demand at which the probability of the subject to succeed is 0.5, assuming all other demand levels are lower, which is in accordance with psychometric tradition (ref. 90, p. 249) and will be followed for the rest of the paper. Note that an ability of 4.3 does not necessarily mean that the subject solves all tasks instances of level 4.3 or less but that it has 50% chance of succeeding at level 4.3, higher at level 3, much higher at level 2 and so on, and evidently lower at level 5 and above, in a sigmoidal way, as we see in the figure. The exact estimation of the ability (as the usually equivalent area under the curve) is further explained in Supplementary Information Section 1.2.
The advantages of these curves and this manner of interpreting abil-*ity are reinforced by the fact that the scale on the x-axis is absolute*rather than relative. It is robust to changes of demand distribution in the data. For instance, with the 3,786 instances in Extended Data Fig. 4,*we get an average accuracy of 62%. However, if we chose the n = 699*instances of level 5 and repeated them 500 times in the dataset, the average accuracy of the LLM would decrease substantially (below 40%), as we would be adding more difficult examples. This is what adversarial testing does60, especially when benchmarks saturate. By contrast, the average accuracy for the instances at bin 5 would remain the same and the characteristic curve would not be affected at all. The ability would not alter, remaining at level 4.3. This case neatly represents the difference between performance, which is a measure of a pair subject and task distribution (so changing from 62% to 40% when the task distribution changes), and ability, which is an inferred property of a subject that is invariant to the task distribution. Although all of this is strongly inspired by IRT, and the linear logistic test model in particular91, it is important to clarify that, unlike these and other latent factors approaches—those in AI included16,17,75—we only use the information of a single LLM for the estimation of its abilities.
With the demand-based scales and the ability-estimation method introduced in this paper, the demands and abilities for tasks and AI systems get values that are completely independent of other tasks and AI systems, now or in the future. We have used the term ‘non-populational’ to refer to an indicator or measurement that does not depend on the rest of the population, only on the individual. For the first time, there is a non-populational measurement paradigm for evaluating the cognitive and intellectual capabilities of general-purpose systems. This is in contrast to common non-inferential techniques, such as benchmark aggregates, which are affected by the distribution of difficulty in the benchmark. Similarly, standard inferential techniques such as IRT, principal component analysis and factor analysis are also populational. They usually work well with human populations because samples are sufficiently stable over time but lead to different results as soon as the AI system ‘population’ is modified, whenever a new set of LLMs is added to the inferential pool. For instance, the factors that were discovered for LLMs in ref. 16 differ from those found in ref. 17, even if the two studies collected representative samples of LLMs, used the same factor analysis methodology and took place in only a few months time difference. This volatility does not happen with our approach. Our abilities are not relative to a population of subjects and the scale is absolute. Even if the evaluation battery were extended with instances of levels 7 or 8 to account for more powerful future AI systems, the logistic curve for the old systems would probably have low values on these instances, thus not affecting the original estimates. This forward-looking extensibility and backward compatibility is crucial for measurement. In sum, there is an open opportunity for the new scales, battery and procedure presented in this paper to be the genesis of a standardization initiative for the robust measurement of present and future AI capabilities.
**Pipeline and guidelines for applications and extensions**There is a consensus within the AI community that there is a need for a new science of AI evaluation92,93. However, there is also resistance to moving beyond the present benchmarking paradigm8. Although some have proposed using the potential of the behavioural sciences, such as psychology and psychometrics, for AI evaluation, this is generally understood to mean populational approaches, such as factor analysis, principal component analysis or IRT16–18, whose findings may soon lose value owing to the fast-evolving set of AI systems. Our paper demonstrates that a possible answer for a scientific approach to AI evaluation comes from behavioural inference at the instance level. These inferences are made from features that are not derived from a population of subjects. This approach was not previously possible for human evaluation because it requires tens of thousands of instance-level results for each subject—yet this scale is possible for AI evaluation. Furthermore, the annotation of this number of items with a wide range of dimensions is only unlocked now by the ability to automate good-quality annotation with LLMs. Nevertheless, to move beyond the present paradigm (based on benchmark aggregates or the use of latent factors), the methodology must be made accessible, modular and customizable.
Extended Data Fig. 5 illustrates a pipeline for our methodology, with two processes that can be followed independently. The ‘System Pro-cess’ (top) can be applied to any new AI system we want to explain or predict about and consists of running the model on the ADeLe battery, plotting characteristic curves (see, for example, Fig. 3 and Extended Data Fig. 4) and summarizing the profile of abilities with a radial plot, as in Fig. 4. The ‘Task Process’ (bottom) ensures that the methodology can be extended and kept up-to-date by using the DeLeAn rubrics to automatically obtain a demand profile for new task instances or benchmarks. This is especially useful to mitigate challenges such as data contamination and benchmark saturation while still keeping everything in the same measurement space. This can be compared with the system capability profile for any AI system that has previously gone through the ‘System Process’ to identify specific areas of strength and weakness relative to the task demands and intuitively predict performance. Moreover, we can also train powerful assessors that automatically decide whether it is sensible to use the AI system in a given situation.
In Table 1, we enumerated a series of applications. Here we extend how they are implemented using the pipelines (system or task process) in Extended Data Fig. 5.
cesses): dual profiling of tasks and systems enables us to reconcile seemingly contradictory evaluation outcomes94,95. If two benchmarks in the same domain produce different rankings or success rates for a model, the discrepancy can be explained by differences in their demand profiles. For example, several tasks labelled ‘mathematical reasoning’ can require disparate levels of reasoning versus knowledge demands, resulting in inconsistent outcomes that our method can explain. We illustrate this in Supplementary Information Section 1.12.
the capability space. In other words, complementary benchmarks can be merged or linked through their demand annotations to create composite tests that fill gaps (for example, by adding missing high-level reasoning items from one source to another).
it is conceivable that routers using these annotations will perform similarly well in such scenarios.
Other applications related to policy, such as safety auditing or regulatory review, require a comparison of LLM and task profiles, with the two processes involved.
All of these applications can use and extend the collaborative platform at https://kinds-of-intelligence-cfi.github.io/ADELE. Predicted extensions will mostly be led by future applications and the evolution of AI. Clearly, more capabilities will be added to the catalogue (for specific domains or to cover multimodal or agentic systems), more levels for some of the capabilities may be needed as AI become more powerful and more annotations of benchmarks, extending or complementing ADeLe for different purposes. This will lead to an evolution of the catalogue and, if necessary, revision of rubrics and their taxonomic relations, provided there is transparency about backward compatibility. This should be the seed of a collective consensus and standardization effort of measurement scales for AI, as has happened in other scientific disciplines.
**Inclusion and ethics**We used LLMs that are trained on very different sources of data and may have important ethical consequences, such as failing in ways users cannot understand or anticipate. This has been the main motivation for this research. The domains we use in our experiments and the examples included in the manuscript do not generate any specific ethical issue. We only use examples and prompts in the English language. The rubric is also only in English but could be adapted to other languages. We did not conduct any human study directly other than a subset of the authors applying the rubrics. More details about the costs of this research (compute), safety implications and other ethical issues can be found in Supplementary Information Section 1.15.
**Reporting summary**Further information on research design is available in the Nature Port-folio Reporting Summary linked to this article.
**Data availability**The associated data, code and instance-level results are available in an independent public platform: https://kinds-of-intelligence-cfi.github. io/ADELE. In compliance with the recommendations of ref. 9 about the reporting of evaluation results in AI, we include the results at the instance level. Source data are provided with this paper.
**Code availability**The associated data, code and instance-level results are available in an independent public platform: https://kinds-of-intelligence-cfi. github.io/ADELE. In compliance with the recommendations of ref. 9 about reporting of evaluation results in AI, we include the results at the instance level.
*51. McGrew, K. S. in Contemporary Intellectual Assessment: Theories, Tests, and Issues 2nd*edn (eds Flanagan, D. P. & Harrison, P. L.) 136–181 (Guilford Press, 2005).
*52. Rust, J., Kosinski, M. & Stillwell, D. Modern Psychometrics: The Science of Psychological Assessment 4th edn (Routledge, 2021).*
*53. Hernández-Orallo, J. The Measure of All Minds: Evaluating Natural and Artificial Intelligence*(Cambridge Univ. Press, 2017).
54. Hernández-Orallo, J. & Vold, K. AI extenders: the ethical and societal implications of*humans cognitively extended by AI. In Proc. 2019 AAAI/ACM Conference on AI, Ethics, and Society 507–513 (ACM, 2019).*
55. Tolan, S. et al. Measuring the occupational impact of AI: tasks, cognitive abilities and AI**benchmarks. J. Artif. Intell. Res. 71, 191–236 (2021).**
56. Balloccu, S., Schmidtová, P., Lango, M. & Dušek, O. Leak, cheat, repeat: data contamination*and evaluation malpractices in closed-source LLMs. In Proc. 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers) 67–93 (Association for Computational Linguistics, 2024).*
57. Jiang, M. et al. Investigating data contamination for pre-training language models. Preprint at https://arxiv.org/abs/2401.06059 (2024).
58. Suzgun, M. et al. Challenging BIG-Bench tasks and whether chain-of-thought can solve*them. In Findings of the Association for Computational Linguistics: ACL 2023 (eds Rogers, A.*et al.) 13003–13051 (Association for Computational Linguistics, 2023).
*59. Kazemi, M. S. et al. BIG-Bench Extra Hard. in Proc. 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (eds Che, W. et al.) 26473–26501*(Association for Computational Linguistics, 2025).
*60. Kiela, D. et al. Dynabench: rethinking benchmarking in NLP. In Proc. 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (eds Toutanova, K. et al.) 4110–4124 (Association for Computational*Linguistics, 2021).
*61. Sweller, J. in Psychology of Learning and Motivation Vol. 55, 37–76 (Elsevier, 2011).*62. Kalyuga, S. Cognitive load theory: how many types of load does it really need?
**Educ. Psychol. Rev. 23, 1–19 (2011).**63. Balepur, N., Rudinger, R. & Boyd-Graber, J. L. Which of these best describes multiple
*choice evaluation with LLMs? A) Forced B) Flawed C) Fixable D) All of the above. In Proc. 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (eds Che, W. et al.) 3394–3418 (Association for Computational Linguistics, 2025).*
64. Zeng, Y., Kairong, L., Dong, F. & Zheng, P. Quantifying risk propensities of large language models: ethical focus and bias detection through role-play. Preprint at https://arxiv.org/ abs/2411.08884 (2024).
65. Yao, J. et al. Value compass benchmarks: a platform for fundamental and validated evaluation of LLMs values. Preprint at https://arxiv.org/abs/2501.07071 (2025).
*66. Hand, D. J. Measurement: A Very Short Introduction (Oxford Univ. Press, 2016).***67. Stevens, S. S. On the theory of scales of measurement. Science 103, 677–680 (1946).***68. Freund, R. Rasch and Rationality: Scale Typologies as Applied to Item Response Theory.*
PhD thesis, Univ. California, Berkeley (2019). 69. Rhemtulla, M., Brosseau-Liard, P. É & Savalei, V. When can categorical variables be treated
as continuous? A comparison of robust continuous and categorical SEM estimation**methods under suboptimal conditions. Psychol. Methods 17, 354–373 (2012).**
70. OECD. Education at a glance 2024: OECD indicators. https://doi.org/10.1787/c00cad36-en (2024).
71. Mirzadeh, S. I. et al. GSM-Symbolic: understanding the limitations of mathematical*reasoning in large language models. In Proc. Thirteenth International Conference on Learning Representations (ICLR, 2024).*
*72. Zhang, J. et al. Task Me Anything. In Proc. Thirty-Eighth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (NeurIPS, 2024).*
**73. Lumsden, J. Person reliability. Appl. Psychol. Meas. 1, 477–482 (1977).**74. Phuong, M. et al. Evaluating frontier models for dangerous capabilities. Preprint at https://
arxiv.org/abs/2403.13793 (2024). 75. Ruan, Y., Maddison, C. J. & Hashimoto, T. Observational scaling laws and the predictability
*of language model performance. In Proc. 38th International Conference on Neural Information Processing Systems 15841–15892 (ACM, 2024).*
76. Hurst, A. et al. Gpt-4o system card. Preprint at https://arxiv.org/abs/2410.21276 (2024).*77. Linstone, H. A. et al. The Delphi Method Vol. 1975 (Addison-Wesley, 1975).*78. James, L. R., Demaree, R. G. & Wolf, G. Estimating within-group interrater reliability with
**and without response bias. J. Appl. Psychol. 69, 85 (1984).**79. LeBreton, J. M. & Senter, J. L. Answers to 20 questions about interrater reliability and
**interrater agreement. Organ. Res. Methods 11, 815–852 (2008).**80. Radford, A., Narasimhan, K., Salimans, T. & Sutskever, I. Improving language understanding
*by generative pre-training. OpenAI https://cdn.openai.com/research-covers/language-*unsupervised/language_understanding_paper.pdf (2018).
81. Jaech, A. et al. OpenAI o1 system card. Preprint at https://arxiv.org/abs/2412.16720 (2024). 82. Achiam, J. et al. GPT-4 technical report. Preprint at https://arxiv.org/abs/2303.08774 (2023). 83. Dubey, A. et al. The Llama 3 herd of models. Preprint at https://arxiv.org/abs/2407.21783
(2024). 84. Yang, A. et al. Qwen2.5 technical report. Preprint at https://arxiv.org/abs/2412.15115 (2025). 85. Li, D. et al. From generation to judgment: opportunities and challenges of
*LLM-as-a-judge. In Proc. 2025 Conference on Empirical Methods in Natural Language Processing 2757–2791 (Association for Computational Linguistics, 2025).*
**86. Breiman, L. Random forests. Mach. Learn. 45, 5–32 (2001).**87. Pennington, J., Socher, R. & Manning, C. D. GloVe: global vectors for word representation.
*In Proc. 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*1532–1543 (Association for Computational Linguistics, 2014).
**88. Pedregosa, F. et al. Scikit-learn: machine learning in Python. J. Mach. Learn. Res. 12,**2825–2830 (2011).
*89. Wolf, T. et al. Transformers: state-of-the-art natural language processing. In Proc. 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*38–45 (Association for Computational Linguistics, 2020).
**90. Thurstone, L. L. Ability, motivation, and speed. Psychometrika 2, 249–254 (1937).**91. Fischer, G. H. The linear logistic test model as an instrument in educational research.
**Acta Psychol. 37, 359–374 (1973).**92. Weidinger, L. et al. Toward an evaluation science for generative AI systems. Preprint at
https://arxiv.org/abs/2503.05336 (2025). 93. Yuan, J., Zhang, J., Wen, A. & Hu, X. The science of evaluating foundation models. Preprint
at https://arxiv.org/abs/2502.09670 (2025). 94. Zhang, G. & Hardt, M. Inherent trade-offs between diversity and stability in multi-task
**benchmarks. In Proc. 41st International Conference on Machine Learning 235,**58984–59002 (PMLR, 2024).
95. Zhang, G., Dominguez-Olmedo, R. & Hardt, M. Train-before-test harmonizes language model rankings. Preprint at https://arxiv.org/abs/2507.05195 (2025).
96. Leôncio, W., Wiberg, M. & Battauz, M. Evaluating equating transformations in IRT**observed-score and kernel equating methods. Appl. Psychol. Meas. 47, 123–140 (2023).**
*97. Diaz, F. & Madaio, M. Scaling laws do not scale. In Proc. AAAI/ACM Conference on AI, Ethics, and Society Vol. 7, 341–357 (ACM, 2024).*
*98. Vania, C. et al. Comparing test sets with item response theory. In Proc. 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) (eds Zong, C. et al.)*1141–1158 (Association for Computational Linguistics, 2021).
99. Lalor, J. P., Rodriguez, P., Sedoc, J. & Hernandez-Orallo, J. Item response theory for natural*language processing. In Proc. 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts 9–13 (Association for Computational*Linguistics, 2024).
100. Burden, J. et al. A framework for general-purpose AI model categorisation. Policy development KJ-01-25-459-EN-N. https://publications.jrc.ec.europa.eu/repository/ handle/JRC143256 (2025).
101. Zhou, Y. et al. Evaluating LLMs across multi-cognitive levels: From medical knowledge*mastery to scenario-based problem solving. In Proc. 42nd International Conference on***Machine Learning 267, 78984–79003 (PMLR, 2025).**
102. Qu, Y. et al. Integration of cognitive tasks into artificial general intelligence test for large**models. iScience 27, 109550 (2024).**
103. Yang, S., Yang, Q., Tang, L., Blackburn, J. & Xi, Z. On the eligibility of LLMs for counterfactual reasoning: a decompositional study. Preprint at https://arxiv.org/ abs/2505.11839 (2025).
104. Gaebe, K. & van der Woerd, B. Evaluation of large language models as a diagnostic tool**for medical learners and clinicians using advanced prompting techniques. PLoS One 20,**e0325803 (2025).
105. Hu, Q. J. et al. Routerbench: a benchmark for multi-LLM routing system. Preprint at https://arxiv.org/abs/2403.12031 (2024).
106. Hendrickx, K., Perini, L., Van der Plas, D., Meert, W. & Davis, J. Machine learning with a**reject option: a survey. Mach. Learn. 113, 3073–3110 (2024).**
107. Yu, J., Lin, X., Yu, Z. & Xing, X. GPTFUZZER: red teaming large language models with auto-generated jailbreak prompts. Preprint at https://arxiv.org/abs/2309.10253 (2023).
108. Mozes, M., He, X., Kleinberg, B. & Griffin, L. D. Use of LLMs for illicit purposes: threats, prevention measures, and vulnerabilities. Preprint at https://arxiv.org/abs/2308.12833 (2023).
109. Freenor, M. et al. Prompt optimization and evaluation for LLM automated red teaming. Preprint at https://arxiv.org/abs/2507.22133 (2025).
**Acknowledgements We thank the POLARIS Lab and the Computational Cognitive Science Lab**at Princeton University, the European AI Office, the UK AISI, the Future of Life Institute, the OECD Future of Skills team, S. Chang, M. Zilka, J. Lian, R. Burnell, W. Schellaert, Á. Gómez,  M. Tešić, C. Li and P. Romero for their valuable help and feedback at certain stages of the project. We thank OpenAI for granting us research access to several LLMs to conduct the experiments in this paper and DeepSeek and Meta for giving us access to the weights of their models.  We acknowledge support from the following institutions: Microsoft Accelerate Foundation Models Research (AFMR) grant programme, Long-Term Future Scholarship financed by Coefficient Giving (formerly Open Philanthropy) and the Spanish Government’s Knowledge Generation Projects (PID2023-150271NB-C21). This work was also supported by CIPROM/ 2022/6 (FASSLOW), IDIFEDER/2021/05 (CLUSTERIA), CIACIF/2023/276, financed by Generalitat Valenciana, the EC H2020-EU grant agreement no. 952215 (TAILOR), Spanish grants PID2021-122830OB-C42 (SFERA), PID2023-150271NB-C21 and PID2024-162030OB-100 (ROBIN) financed by MCIN/AEI/10.13039/501100011033 and ‘ERDF A way of making Europe’, Cátedra ENIA-UPV in Sustainable AI Development, TSI-100930-2023-9, INCIBE’s Chair financed by the EU’s NextGenerationEU, EUR2024-153548 (PREDAIT) ‘Towards Predictable AI’ from ‘Spanish Europe Excelencia’ 2024, Spanish National Research Council (CSIC) Special Intramural Projects programme and the Cambridge Trust. M.C. declares support from Google.org through the Silicon Valley Community Foundation by means of a grant to Fundación General CSIC. The research of J.H.-O. is supported by OpenAI’s grant to the ‘AI Progress through the Lens of Predictable AI Ecosystems’ programme, which is based at the Leverhulme Centre for the Future of Intelligence at the University of Cambridge.
**Author contributions L.Z. and J.H.-O. conceived and led the project. All authors contributed to**the collection of benchmarks, the development of rubrics, the prompts, as well as the choice of model families and experimental methodology. L.Z., Y.M.-D., S.Z., Q.Z., P.S.-G. and Y.H. ran the core experiments. L.Z. and F.M.-P. prepared the result analysis and plotting. L.Z., L.P., F.M.-P. and J.H.-O. drafted the manuscript. All authors, L.Z., L.P., F.M.-P., K.M.C., Y.M.-D., S.Z., Q.Z., Y.H., L.S., J.E.P., Z.L., P.S.-G., K.J.-C., P.A.M.C., J.Z., J.B., B.M., D.S., M.C., J.W., P.H., S.T.W., P.C.K., L.C., X.X. and J.H.-O., edited and revised the manuscript. L.Z., X.X. and J.H.-O. supervised the project.
**Competing interests We received support and free tokens from some of the providers of the**LLMs evaluated in this paper or some of their direct competitors, namely OpenAI, Microsoft Research and Google. OpenAI, Microsoft Corporation and Google Inc. had no role in the ideas and research questions, study design, data collection and analysis, decision to publish or preparation of the manuscript.
**Additional information Supplementary information The online version contains supplementary material available at**https://doi.org/10.1038/s41586-026-10303-2.**Correspondence and requests for materials should be addressed to Lexin Zhou, Xing Xie or**José Hernández-Orallo.**Peer review information Nature thanks the anonymous reviewers for their contribution to the**peer review of this work.**Reprints and permissions information is available at http://www.nature.com/reprints.**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_Xu_CemIK-8uUaiUEq5Rfv5LGsu50-ktDLHw_p_SpFvNtt7xzkVM3Gsbm4tSEUKxeC5_e_CdE60OG19HRbN8DTapx0QigO-6z3vhQiJ3sCO7ThZL6AQt39r3ZcbkfkZHPwaCUjbA=w1280-h1096-v0?authuser=0)

**Extended Data Fig. 1 | Correlations of the demand level using all of the items in the ADeLe battery for all pairs of the 18 demands and the special dimension UG (Unguessability). It also includes the success (that is, correctness at the instance level) of all of the subject LLMs considered in the experiments.**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9MYtKR0DuX3bpxbsN9s01lZ6BGzvMXRDBS7LIXcoIoyQwnazTFcfYO1SRS9rFJRwFr4QB6Rbt8tQ0YOWIlsW6Uk1REYWBoMq6J4lOv2T3OrPwMMAlkiJEoEiDOMrEtsef-V3eDQQ=w1280-h1072-v0?authuser=0)

**Extended Data Fig. 2 | Distribution of level frequencies for the 18 demands using all of the 16,108 instances in the ADeLe battery v1.0. Dimensions such**as CEe (Verbal Expression), MS (Mind Modelling and Social Cognition) and SNs (Spatial Reasoning and Navigation - Spatial) have low proportion of items of high level, but this is in accordance with the focus of LLM evaluation on factual questions with no navigation or full social interaction. Future versions of the battery for agents or multimodal scenarios can increase the number and breadth of the dimensions.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8Dx1tDr2-o-zRPorfZEdb0fP9TyGlN6_F1XfYCc01VVaXagXmh3OhMdiWDIhq9Wy18VgWJBkazw5idI7o4Ll1H9WxS7aXrYNO4u2D-QObhXMagEzJb5iL6bNZxqMOfgwjNuOt5wg=w1280-h1002-v0?authuser=0)

**Extended Data Fig. 3 | Level annotations of five items (from benchmarks OmniMath, TimeQA, MedCalcBench, MMLU-Pro and TruthQuest) using the DeLeAn rubric set by GPT-4o. The listed demands in the table (from left**
to right) follow the same order shown in Extended Data Table 5 (from top to bottom): 11 being elemental, five knowledge and three extraneous.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-HpqWl6t-NRxaWPal-j4lzcA4AngxB4SLHAS-Hh5Ljhs4hikIEI06CYy_vYOWIfWwLPwi2dJ79QXXhwcHUTnzp2su4HPZMTrazHKWKUirxmIOQl9WsvsuMsxCL8GkB2HNsKshbSA=w1280-h894-v0?authuser=0)

**Extended Data Fig. 4 | The characteristic curve of Llama-3.1-405B-Instruct for dimension KNn (Knowledge of Natural Sciences) on the ADeLe battery.***The x-axis shows the demand levels from 0 to 5 for KNn and the y-axis is the*average performance for that level (probability of success). As usual, level 0 has no points left (0 never dominates), but in this case, we see a situation with no point for 1 either. The curve is a logistic fit in the output range (0, 1).
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9WeIS0Tn26XEDJGssFtm6bQikNmAIncVduKRfM3Zw3mfcsxTojrJS7o6ojtiOeqFDRNeF8Py8zA_r1Ho_-m1mHN9R4Ge1VOBr-my2MKXx_GclwRO5rFeUXSc7Mk0awTUL23vYooA=w1280-h940-v0?authuser=0)

**Extended Data Fig. 5 | Pipelines to explain and predict performance for new systems and benchmarks. Top, ‘System Process’ – steps for each new AI**system: (1) run the new system on the ADeLe battery; (2) plot characteristic curves for all dimensions and extract the ability profile for the system; and, optionally, (3) train a simple assessor using the annotated levels as inputs  and the score as output. Bottom, ‘Task Process’ – steps for each new task or benchmark: (A) apply the DeLeAn rubrics to the new tasks using a standard
LLM; (B) get demand histograms and demand profiles that explain what demands the tasks require; and, optionally, (C) predict performance for the new tasks  for any system that has built an assessor after the ‘System Process’. Assessors based on the demand profile have especially higher predictive power in out-of- distribution settings than other baseline assessors, anticipating validity in new situations.
**Extended Data Table 1 | Characteristics of the 15 language models evaluated in this paper**
SFT, supervised fine-tuning; RLHF, reinforcement learning from human feedback; CoT, chain-of-thought.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9L0TE6M4lUDd_a1HucdrZPRqnWd6DwZXmLWQRtPqmpCustFnfz3JQwCC8VjWklRID9EUFOr4gD8VphtMqckbZpc8ecv83GIhNWiHPsdxEN5xwhmamL_S7vHZ7NKLyBDwCQP4RTjg=w86-h149-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9RMtpksKnjoWiKAvCU_rpx7fmo9BioKgBhg0bxm0W7dkAz6PRqARpS-oiBcxjhKkWmf6YgwDtWAUJeW264iqVu7QhxW4N2jYC5D2DStNz1DhUt9tfMJgZPBReI2TyN9VRUtd0uzQ=w86-h125-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9mkUT540yopn8QBOzva-S0LhI52pUhlr0p3p6lPPdEs30aMAlYv2DYHw6pLPKTyCa-89qrkDUTAJKxrGIGZGL8DA1p4xgvRvM0Lv9xEn8EOKuQm4ZUTNU0cnZROpE3orMnkQzbhw=w86-h50-v0?authuser=0)

**Extended Data Table 2 | In-distribution predictability results of 15 LLMs for the ADeLe battery using tenfold cross-validation, averaged across ten seeds**
The first two columns show names of subject LLMs and the overall accuracy of subject LLMs on the ADeLe battery. The remaining three pairs of columns show the AUROC and ECE of three different assessors (RF using demands, RF using average GloVe embeddings and fine-tuning LLaMA-3.1-8B). For a single LLM subject, the training time is 4 s and 160 s for the demand-based and embeddings-based assessors, respectively, on a M3 Pro CPU, whereas the fine-tuned LLAMA assessor costs 300 h on a single V100 GPU. The weighted average is only indicative for easy comparison, and uses the normalized LLM accuracy as a weight in the mean, giving more relevance to more powerful models, which are more representative now and in the near future. The*asterisks indicate statistical difference (α = 0.05) between the demand-based assessor and the strongest baseline (fine-tuned LLAMA), using the Wilcoxon signed-rank. The RF assessor’s s.d.*across the ten seeds range between 0.0004 and 0.001 for AUROC and between 0.0006 and 0.002 for ECE among subject LLMs. Given these low s.d. scores, we do not show confidence intervals (which are very narrow) for the sake of clarity.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9xWQe0ZhCXFpcRtuXgIVqomU_LWzqud0ZdOoaHf761jKZ6DVkelOoSCMuN1IMZH1mloWUR_9HOQ5kCzDQDGJUArcaGxGdgwB0zSUnPZrpSrSFTNNro9ylV8uNwMOw5c13KZDfU=w156-h38-v0?authuser=0)

**Extended Data Table 3 | Task out-of-distribution predictability results**
15 LLMs for the ADeLe battery using tenfold cross-validation, averaged across ten seeds (all other things equal to Extended Data Table 2 except for the RF assessor’s s.d. across the ten seeds ranging between 0.001 and 0.007 for AUROC and between 0.001 and 0.005 for ECE among subject LLMs).
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8N5-ZgPUBap7HSVp7KyISok7-YtGBkJoEKuKjpUSRS20p2Kyd4-Bd5Qm_GdxIZ-LILXfqzxqN8bh74EAaLsu2JL8W8dPdKZOf7ETqorvNYVxkYTl9Syyhg6x_hr90JzJT0vZOd=w156-h38-v0?authuser=0)

**Extended Data Table 4 | Benchmark out-of-distribution predictability results**
15 LLMs for the ADeLe battery using tenfold cross-validation, averaged across ten seeds (all other things equal to Extended Data Table 2 except for the RF assessor’s s.d. across the ten seeds are now ranging between 0.004 and 0.02 for AUROC and between 0.003 and 0.03 for ECE among subject LLMs).
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_9fJzIRmLmtZnRvNsgys403Y0JfMyuzOeOtXVPv5LyWpHI4hb_aw-lS5DtCU9dZ-gsbWOQKP8FWBSpdv2faFsCUDAMfMLwdi8qP1TnOun_WJiF1QAGRYjt-BzYLbCIPLMK5Z7w=w156-h38-v0?authuser=0)

**Extended Data Table 5 | Dimensions and subdimensions in the DeLeAn rubric set v1.0**
The first 18 (grouped into 11 ‘elemental’, five ‘knowledge’ and two ‘extraneous’ in a sequential order) are demand scales in the range (0, 5), whereas UG (Unguessability) is not a demand: it is another extraneous dimension representing the (1 minus the) probability of success by random guess or a naive method. For instance, a multiple-choice question with four options would have value 75%. Full rubrics are in Supplementary Information Section 2.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9PT7RLkHxXDKwssLo97ALp31OAalqEkltuS75qnDC218-R5FnrWXH9IB84Qvd3qOtvERsWDpVxGa3Jb4-fwfPc27t_XeljQ1iyrP4r8BOlMt1amGIGvWhdTpPAnCPn2AIznSAjYQ=w36-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8kRNHwjwAFghK69QhMdIhkRNsLdudVJGe_fU1UlFEn1Z8zRaAbw3z04lNFixObqRKZZGgiBqvs8yfEiCJzPflgJLZRrVogjPJ87kykZX8PLSgEQ1rPJ6DyEI_qVzaE23sFbVaiSQ=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-EFRBQoIR5PO1z-v7rMcflbXtmJ2MYGysmT_qgO_vj-JmlXs2L6U47mQadsAPyM1-MGzokUfjqNKYapF0ACGrh0GIFNxYMdwL2YdU8an0jf3OcX6ws5vrUdZywNFrw3mnnYZ5Ltg=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_5rm64QtTxtFYmoVIKeJJxjv7e7ddXcE832CmcItazR1ndE1erEd-hbTOY8QiBwXa7TZA8a2EQiccJj4tyOUtfSdP-foeBsjrHRkJ4FOb-kX2JWlR61ry4CR6zru7Y1IRO_DF3=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_Ra-zwrDB0WemXnA_8wCNScYjtp3PyXWpzXDHsMY1NKaPjw2b9F2noPmC2YUZQGieAe_a8ukbahMbYBqLTV00XLg1naR_dpTzxrmy1rJZhaDBPj7EnmDyvfieG3bcWOtObbmhcSw=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX91LXfwq8VPbpDt6HgniJeOOSVJj-djKhbmJRA0eFG0HfZyYii_6O18M4-3chtr_xVEYC_XHLjhja-SWsCMbsXfWvNGDNW-GFL3GiHLlBNM_IANSow9hwpgFQ1_pUkbOv0jkv-5=w36-h53-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9vFO2fcSuy4p4lGIfqS9uC2nu21Av70PtbCp9XyLUc12170q8mfFjxmQXDX4_v5Cs7Qe78F9pNnZh87pmNGDQwiLoLwQBxl0SxvT2wjc2cp98gOb399R3BxY7KZg-Kc33mNkP-Iw=w127-h53-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9lnVkepSmnvBq0tNtdj4-6iIE79FURL7dBTziET1Pjwts92d6YsDA_93NKGaeZ2OAJcEDb55IiihrOm7-2jxJ7dcZ0rfKXaB_oPdjYOeliy1uGHhoVFzPMtAAfWBXHzuZiNIMQ=w36-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9Z84BRXR1L0LtuW0z5QPRTWJsDkBbmpWFM7I2-4yuTweFbl78kOxcUQcX0dpIO-OaEeIpwzjtv7-Mfb5EhuHCDjKyELzhXHyKEiSzSOuWlnXZsqIF2KXwID43CQ1jqMHFk36Qb8g=w127-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9JT8iOhK9VXSRY7tiIoV7owzM0aErXy9SESRRhS9X-tgDiN7ABzEDL9FOVXe5xAFaDdW0N_QSOvJM6MMO-Q9c4_OkjgEiQJU39IcLzpfvlXJNGo_hop-2xaBEFxgvkCwOsGUSOlw=w39-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-vsCCWyYDU7Bf4x6fGKCdnkbh9Bsty4qsoNn_FOtdRjSP8x4rQjcPOWQPSyvEyZrV6Gtr-TTsBM9nyzMMn-6Myuqzt25kN2zbh1lvHbeUBICf3g3G7fAlz8524aaBGPa0_em0G6A=w127-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-M1HcW6SDIXeSn4LYSfHrAEgNk__j8g2vzgC1iG6tecwjQTFsNH2frCl-z0dKqqQZdQOslKEgLsGlGtgiUkhy_pt3IPfEzOzwq_dgWG7kf0L5VrKREkxV8NJHzqPp73eMfLUNkMg=w307-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-426kRRK_DWuBpBHQEIC4ab29FYiaE8-dPxPK-gY8B0MsGbK1RtnRyKc2TTM_CocWbcKq6CALY5FbHKjLh3GsIH8mvSarU-KGy3TEKXeykIcr6wszLBZzdNhsa6xhU8QEB2QNs=w36-h119-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_EopgAT0A4k9JlnMXkvbbCLZgtIMiuQ9ZGEsXCdkVccN9H0EbfC5UzC7mRhS_Vjcjy8Y2VDZPElHYKMn8mNzLCfpO7YkYWEXEglLD-jH-_gushyoK5cmnYbnW234TpFNlCu8gsMw=w127-h119-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_tVX_KNubWlQjwq1RxBNRWT1o5yNc-MfFvTQXlGc-kQiI8zkzqUWJWDoPuk9V3C7yQ66QaAonEyBr_6MwmeXgxz3dUyHA356kyH1ddqIuAiMod9oji9UHbFTxutiYBbgIQuZs1kQ=w39-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_NTfqGGYyT7nB962TPsS95RIC_5Eoqy4KqX_8FdPUKtaw6VAizhFwBuyRxqUjQASwh6cwOUcwDEK8t0HrhAV3cTHF_VjVJBOzcS8r6ryJi_AnZQCYj25kYitVu_wGoMH1bD-2BUA=w127-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX98QQmHsHAcmYqUgwc7SgPefhT-LzQcAm7fhjgBTGZIK2gKkujTFUcIY5Ba-RmmVdK8kf6OLsk0WYBceTH7emqj0KIm-ZGOdtjPgS8_n5pRRRg_Yi5RRxT4MOVnc1DgTQV7I5tDzA=w307-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9CySW4KTvB9ST-ETmtITxwMVll3zFHSrORNRE7GqKYPz6lYqIHgPAjloe5x77NOj16skaJ5i5b-h8ZTnwLtbkT_xa1w1JY6fIxrx29pzEY64mbnH1OaQ_R9iuAhd0N3pL8cDWG=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9YyuDWdtofNnKKJzKr2qTSZxsicJIO5jakkiNAOuvR5x0Ws-_pLVkOt3d98yF2culUG9AA7kUtcUqRniV2bU1-CCgLwDrvv46GKVTjL1Dy-X9blMf1dW0-8QBlofFIlqQy0HoNOw=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-OvsPxLlZqnMoT9VVvyQ0_u6PA0LC5kC8x_AsPZrzyp35gDP6wpav_WXl2RzvHAHFMn4cMTDJGVw2FoXmsQ14qPjzrtQFW4RS9MB_YDI9amX-dPtv9TZUVxo7298gZ3izcySky=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8FSYxp7OnjCVUo_rjDtlyspSbkXhohjqzKMby1T8qr9wnm15FJVFXiD_-nbdf59-cJpQ7OMfPfM6xg6GVfR2ofL1UvCABGFlrvxGTxYhEk15wck03_mWCSYsaPolkwQyzgKZQUow=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9vU6xQVCXRW5nhz_eiIIwKXZmAQP-_WCt5SdS_o1gJl1xkGfKv8pRqAN07YXRbWMdj2YlawO4vJtQnKt_mXV7ZEWM3-tmg97HSjJz3cDzHzL2BaFJDRykLUVFsMqhH4XDcngqUGA=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-K4R4LV7odDsrSXdL7S4NCP8YQosJG3jYCklWn_aQuNxti-fNE_qDjxBKu0f5dreKtJl6WLUcKY5XsgGKvSrwEqc7EuuHqIwkvwNZOCfMd7OEqvzWCx7H51mRNCCYdEQWLym1KrA=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9l4KwR1yI3xtwzXI-2uS6nyl4nAQNWJernFYwA15aANpYFh68wGDdHI28B2LzWCaf6PybwQ5hOiT7iFfCXM223Y1UWrhhKMcj9OJWkOyLdJrcGwAxb48RAfhIU-HWr7R1aCUv0qw=w36-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-LO_tIxZs_n70krS9NMrtMlepXi5I-Enrr-WNd_1-G8BGXHMK2mSaFhuoGOKnmYuvDiMqqJNSppGnTx3nwATVl6gnnU7aR3aXmv3az0udQb7iwNSUKfyyXQIPfhuO1WOxr3geYAQ=w127-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-W8we2We2JRnvz1xsL3YHmGuHqDdQxkiwwTQD840Wjk-txeN1wcHG8QuCkFt4IMHTaafimkTnC60Jk5RIdvYlFnVoNXVJ6Yn7LiGdkr8j7AYDIGOAS0KF470ajT_ZwIwkdQKfoeA=w39-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9dngXiHuWbe8cz4RYWXoM5FCASwZ_gK2A2s4fs7IvRWMEB5TkJt1crWSw3ODWHINMcRJ0vhD6syAzc4SYEuQZ0WAIX5lUEio_YoyjiolVOZHhx4cj8eqqlllqajQTCC5C2WzDA=w127-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_F1168jFMQMp8SPIwI3EaIzbHZexmy0Qr0aAij1n_b_loAgye3nZOkNUH00nEWAv49X3_rtCG7G6PIj2cot5eCLKLZZWoyktSTGIGO83HEB6VhCPxmv_tahIy8nNIdB0HVf6M=w307-h40-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_HCGzKBWskg1CJgJUTrrkbOnpiuJXuxLLodvkpGgJFpZgej7XyaensLL0ZpY4uPNUuO5fS6e9_w_0S8i9v7z6SQGfHTCcOm96igQtGW-JqQ9yPocW5A5Wzv7gOcuz9y7N0eFv6=w36-h66-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-uIRV-c0-17LxrGAWHas5iQFc42C6P2URrq1Roq5gJq2d84Jzlp2taxxHg-6Vc_R6WjYoHy5kiMllWjtBX6Le5UxOj-8u0cmdsC20f4hP94uZIoncj2hJL48MqyjR9Tow34r3feA=w127-h66-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_uZmWihnEStvgV1MJIR4e5jV8p81ijrigQsWjobaxMgVlOr1cdaTf-SKthBZquR0LV5y-DFr-GA6Qj_cEt4KyUBnbdWfzlEG8PNrjCs-1Q_QDxoxXfg7G6-GiwxjPyRSvazzbH3g=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_wEsOgJY8M6q5ADEXpOVdMu1Sclrzys-Ww6UafCbBWypI9CMlMfqQeP3Pe3PesqRHhcL5E61IFkAbZA9YaTWWqwdQ7VcWsyhX3LnS0jewGXE1u0RxWru6ynlXd8f4vZH55namPRA=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_ODZ6IdtVT07sPeZvnKKX0V4manIQpMcGB3P3ez0spyAvZlBAuUpHFUHh_jlyhIb94dBMTFYgHyb_FiOyTlDJDEHBYPDbWcjTGJnH3J3lFV6C-nllbcl4fl3nYh5ECZVDYPl_uFg=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8Wp9uV0wytsB9NQb-gZT_jbLZF_-w9Zs2uhnsOzhxTc7asgMUtPNlgRhBJQyqCVeIc0bzrQA1LPwf0c3CdFQNOnTWVtA_Cs0zzNLmHyqDhykhW2rP2XR3y71vfV2Q05yJpWV4bUQ=w127-h185-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9fF7Z6KYKyDmY7iUWKjsM8tOoMtuf9sdLtkqVVqIThp99UMcET-1n1fOpFqMQD9O268VidQ4sGw8dC8IDjw3HIh38bdmJqHaD6OJQYFhAGEz87M-HjEyDKWdbEaHEfHKH7-CCDBA=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9GRp8nbMt2t4s2pc6LALNAo3r-_X8L8ma6fTBhsxM2LrfQl1f92doP5vha6StQdLcxs-04scgVAFY0DT1EJVesJqvUAoVYuGGehmdi-yjFMNQAWdOLo5FLpbb2aQz1rkNexMFT=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8wf08J5wFdgPqGgo3ypfpGiDsffkzdduOCMHEhrQMgz8XvnZmw_x4VJf7zqrkRLtflrwXlGISnI6a3ZnGuuJQYoE9dkt5rd6JoCCGKL844hOIVftnCD6NSIWgWO6T7guIID0mI=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8DJahfLyA6NdDE5Gels_vSuMh4PCnHs9tV1Z6I07UZT3dBbHcfbAw_qRHUOEdDPcKbRUaufe5lSowEsNB5VUD4lT_e2GjtvuGYbe-C60NK00QSrjqf_542I-rZuNmyocroTdXwCw=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9UOZynB6V4R5qIB7qaX7xiUPQqRkGjziKPcqKYhHNzhVtF0g73yH0bBKGla0xYM04lttym0PIdIERSYWY5-ODG5AVq5ssxzZxoY3Nkj7vUniNdhi46BkxVYqYhfRIoiyb8G4qC4g=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-l3fmVW2HjSzpBnso2-XZnwFA3pFxC3_HJ7UjkPvdTerpzd1sLISoCo1RzJDWRfprzCLznCVyrMuhLiiU_NNIhZVFn7GJL9wSDb5NMzNYGkUwx-ydxmjfjlvYWcGeoKnuc8UMmCQ=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8wbchtc4HQE0pG0pAJfaAwrR1TgSEfqVanP-jGcPh1WYLyr9Thkj_sx34tmDjN20ocKlAPAyndAC3Soe66rDXM1nVvjyrjw7RLmwUWuq-D30dV9KZt-aLoHLa-_ct2yVFX2xpBxA=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9UhewjgDJPOrw48E2jecQeBkKxVyU5gGJD_BWUh7_Tk8Q9Y9O5Q6IBpWMHNe3BQtPlRlKtWEmnTdGkbiZEKX_bvlrrMWGWpe1IMy5tqGUgfIn0NShYBjHjxA4YcyxJEuokngpVCA=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_9Bt6zrcKVPN5iv4_OEqRPJxKw53_bp0shAmrAFJHBhOOA-3VKRVSdAs_6CZicp7Sgc1Zzh4sFe4lTnrKJunr46tWQpLXxyfveXaekS-tSOSmgzmhLad4PeQAn4uDf48-h99r0Ug=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_pXq1sV1BRgNRX1zerzvrded6M1UJ29WEBocv0v_IJ62e0J--bF1Mh5NsuxExYWHS9fB1C9hX1uqBTnUmQKjRDlVh2rMI-O36GP8JB0D93CV9LmewLi6-EXah-evYhcdbVKLLMOg=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_YhvaAUkSgdgrTaVL2O4LGLYd7fbl6sf3Px16S4vnhXe5-0s8-fWJM7QZXByU6Lfm1tUfiWagNoraYiuqAKv43g5DD155Ffv8DtRt07bTQrT3-DXKSNJH6S_k--xo2k07_i0-V=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-xocUKV5uyP2HTrnZb4skqXd4YAD4UAvNmmTI8qWUo2PeYge2tw9-5n8LnB6eG1eEwvV7UIBa4XhidjUKGzn6fNKvOU0yy6rRvXwrKC6bgjd7j6pdyut6v68ogxf40kZSlQDIo6g=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8Nz12A2z-X2N7IToDLpeHdVOebHeGHvNT3daZc-9cuh8rwx10SunbzRsZ12VjTM4GvMkxZXS0BUnmKFc_NAMMPdiHUggsGhA4frV8xQD9Hv90NYemTjrq7dpeNJmDkyTTa0fu02Q=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_kdc5sJV0wezH4xW65ssNospGEIBgoJp01cu4BlXmk1dVVw81SqWKe5viNDTKxn3oxFkpbzcjGEKHKPPANnJG3ZX3h96OOc6_Lk73DPPSJxftOd95Po44LqKFMkheq1NFsrA74=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_4Gf7BVcKIFMuUtAFFTKrBOnRttBwrg3bqY0B4tpH2KZFkFeG7Ix932TjjiGbZt1nLtfqZOoQLbf1axyWfwCQ7CDVhPVhuldLbh6eLF6jOFkPkCBNeYXvj8WhEJdAUqO4HFPUc=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_auavNvzf9-4wq9gdAqfkVxfPUlBIb4ajSsxXHVj-uZCzf2OzBSUqyxfofRqU6bmQ4u2aeyMO6YfZXHMlNPVqkYuMWSv1WOuP1zek7dNuom3gwEgVE20azqXbYXpkexCyJRm-1ig=w36-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9PkGuLqqDT-8WLboj5rasfR0vOUGnDc-T2hzOuLKH3jZxTtTIRrzH7aIpuhTzSRK0Q6Z4roTz4FvJxUbyHjmSoyLcHLSLWBxnSvNEXAyBWORzKpmicdCsywn9uJBxX-Hf-AWbD4w=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9MnfNuxHt91Nk6SidRBVAsx3MCi96HGC39IhWdMYQxv34R73UPfb2SfPkQnVrIsqoCzAZBe7tTAKfsAJkNl2NZ5kVtCF-MvRTJE2v6ky-xm3n67M8ew_Fn3suty743-S4n8NE6Vw=w39-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_HtQs06AhBaKSg5qSqUcfi-oMYbycN245d-LHelKGkV4Wfs7NY2nHQNpI9iAhjM0v4jx-rWjR-MZRNYfQPqdLm30_L035-kgvtAbySfW-xxO84upDGP8PshO-m2lSSdj4XOeQE=w127-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_r8CjSAWaR7keH07QhIuYuRVqctnILlnSi4LsURkS2gKA2sZPkAC9tQiE6KpoHX7LPLIvVgXrCqE3wiJJIeyzN2BaLAT2KeomeTXycehmRQSFalmnh1lMoEaPxIdmcNWa-KU75vA=w307-h39-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-m-TAEUdTEz3qYVxal_WFMufrS9n8vvHmSrQLeaGUny9hx1wn0qujvvFZyBRdcHmBLPLyhybrlV4cRA-PcX9E8ZDvs-F9wa0BBdJnWTzzl6t0bzcGDe3cca8MjxSDDWCh5rZLXjA=w943-h148-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_PbRDKWv5TOdZP8c0ziQtkIalkXgpLCp0AqdufvnX5_AB12yeN9iCABrhXtLJpQJ49EJkgVLf5Q-Q_XPcIdHVjksNrkBeDp4j5RGM0EbxhXS8m-diJY40-8RMnbpK5CPtCy-2qFg=w840-h1116-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-6WbSvsRBinB_T8NKFRCbvgE3GNd1697Z6E7gkm_5Nv5gZN_Omf8NelSHThh1AKViln7eZC43ovjp-9-9fFLKOJt2AE7uq8CVktoU8O2RaX7_zx6-P4BfT6_6HSBYC0tYXPU0tfA=w840-h1116-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9ZZumyXMlPbiFHgvWzDVtlSaGs7nSjIo0B9Z5-RPa4Yirde71ImHyRYcFDUhAUUoPvrwWA7DBCu6P_sQdr1vfXpH6VMV91OHo017yYp9aWmK6WxdF_yt3uSGKXOKHQ63unp92Vtw=w840-h1116-v0?authuser=0)
