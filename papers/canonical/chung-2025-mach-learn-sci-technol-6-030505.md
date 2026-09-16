
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX95YDdHbKUTs1Lz6tggFFp3lG6oGXnHgwtrgRTltDs3j55HfsevpMMc0ZOdrSn4WK1uTR1nraeHwxgGIZ309P_F8nT_I1J-d5-cx4YJDEqA8PUdLUvNjAgusMLywhDoUGbwpYfP=w600-h125-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8wfbZoWbycDhieoo4XqkpBeWGb2FKefOogHMvj-MHkFzXjvHgMpQC5FNNaEqzQeepjXp-E0OJNEAGG9zru55xvXdUXrVd6M5l032Z0AMv3MOmSFjJFIOYGfpQiwFGKVTfCTzN5FQ=w696-h161-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-VA38fRqzJXpvmWxjsuf-97Vyucip0nwOC6gugvpRp6zdP95SEshSFIsnEyS_aG4IEEf9cLcTQJfYHlUruiphcIy6URAP-Q9l6bC6rl4V4ce_q9F89v-vYl4FaRZlnbJhcGe1PiA=w330-h80-v0?authuser=0)

**BENCHMARK • OPEN ACCESS**
### Theoretical physics benchmark (TPBench)—a dataset and study of AI reasoning capabilities in theoretical physics
To cite this article: Daniel J H Chung et al 2025 Mach. Learn.: Sci. Technol. 6 030505
View the article online for updates and enhancements.
You may also like FeynTune: large language models for high-energy theory Paul Richmond, Constantinos Papageorgakis, Vasilis Niarchos et al.
-
Physics simulation capabilities of LLMs Mohamad Ali-Dib and Kristen Menou
-
Learning-at-Criticality in Large Language Models for Quantum Field Theory and Beyond Xiansheng Cai,  , Sihan Hu et al.
-
This content was downloaded from IP address 31.182.201.242 on 08/07/2026 at 21:36
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_0G9lHsPEC9w3NezxLo3eZ-TzC2JwEyqA9yUN8AyOgHocdiPy2DRAt9c8Cfr2IRE9lIZ_3kT5ptphqEn6TWOu9KPFUgOsmnmjHMT04t8yAk1XyvHbcxCYiIAuOk7kKiV8dhnHvdQ=w155-h57-v0?authuser=0)

*Mach. Learn.: Sci. Technol.***6**(2025) 030505 https://doi.org/10.1088/2632-2153/adfcb0
**OPEN ACCESS**
**RECEIVED**
6 April 2025
**REVISED**
7 July 2025
**ACCEPTED FOR PUBLICATION**
18 August 2025
**PUBLISHED**
2 September 2025
Original Content from this work may be used under the terms of the Creative Commons Attribution 4.0 licence.
Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
**BENCHMARK**
### Theoretical physics benchmark (TPBench)—a dataset and study of AI reasoning capabilities in theoretical physics
**Daniel J H Chung1, Zhiqi Gao2, Yurii Kvasiuk1, Tianyi Li1, Moritz****Münchmeyer1,5,∗,****Maja Rudolph3, Frederic Sala2 and Sai Chaitanya Tadepalli4**1 Department of Physics, University of Wisconsin-Madison, Madison, WI, United States of America 2 Department of Computer Science, University of Wisconsin-Madison, Madison, WI, United States of America 3 Data Science Institute (DSI), University of Wisconsin-Madison, Madison, WI, United States of America 4 Department of Physics, Indiana University, Bloomington, IN, United States of America 5 NSF-Simons AI Institute for the Sky (SkAI), Chicago, IL, United States of America*∗*Author to whom any correspondence should be addressed.
**E-mail: muenchmeyer@wisc.edu**
**Keywords:**theoretical physics, reasoning, large language models
**Abstract**We introduce a benchmark to evaluate the capability of AI to solve problems in theoretical physics (TP), focusing on high-energy theory and cosmology. The first iteration of our benchmark consists of 57 problems of varying difficulty, from undergraduate to research level. These problems are novel in the sense that they do not come from public problem collections. We evaluate our data set on various open and closed language models, including o3-mini, o1, DeepSeek-R1, GPT-4o and versions of Llama and Qwen. While we find impressive progress in model performance with the most recent models, our research-level difficulty problems are mostly unsolved. We address challenges of auto-verifiability and grading, and discuss common failure modes. While currently state-of-the art models are still of limited use for researchers, our results show that AI assisted TP research may become possible in the near future. We discuss the main obstacles towards this goal and possible strategies to overcome them. The public problems and solutions, results for various models, and updates to the data set and score distribution, are available on the website of the dataset tpbench.org.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9CKRXVWhH9COGQOor6NOLo2O6VztT9_OhkTlOp9iA-0gSmKnF1Y4-z8eOevkdYGFsARlm7Uyx_L1ww1tha_iWhHgZjCSvVKeUYxlqhBr-4QfN2Z5NR7kYrMJJ2Zs_8k6h5ZZx0=w102-h48-v0?authuser=0)

**Contents**
1. Introduction 2 2. Properties of TPBench 5 2.1. Overview 5 2.2. Problem statistics 5 2.3. Auto-verification of solutions 6 2.4. AI-based holistic grading of the entire solution 8 2.5. Novelty and difficulty of our problems 8 2.6. Public and private data set and data leakage concerns 9
3. Model performance evaluation 9 3.1. Results for auto-verified solutions 10 3.2. Results for holistic AI-based grading 10 3.3. Augmenting inference with python to reduce algebraic mistakes 13
4. Failure mode analysis 13 4.1. Background knowledge of the model 13 4.2. Algebraic mistakes 14 4.3. Logical mistakes 15 4.4. Hallucinations 16 4.5. Performance of pre-o-series models 17 4.6. Performance of o1, o3-mini, and DS reasoning models 18
5. Related work 19 5.1. Mathematical reasoning benchmarks 19 5.2. Reasoning capabilities of LLMs 20
6. Discussion 21 Data availability statement 22 Acknowledgments 23 Appendix A. Summary of problem data 23 Appendix B. Prompts 23
B.1. Prompts to query problem solutions 23 B.2. Prompts to query grading of solutions 25
Appendix C. Public problems and solutions 25 C.1. Level 5—one-pole problem 25 C.2. Level 5—bias of a sampled halo field 30 C.3. Level 4—SHO vacuum entanglement 32 C.4. Level 4—SUSY-symmetry 37 C.5. Level 3—slow-roll inflation 38 C.6. Level 3—scalar particle scattering 39 C.7. Level 2—dark matter capture as a function of time 40 C.8. Level 2—a 3-state QM problem 41 C.9. Level 1—blackbody in*d*dimensions 42 C.10. Level 1—boosted parabolic trajectory 42
References 42
**1. Introduction**
Automated mathematical reasoning at research level with AI in theoretical physics (TP) may now be within reach. Novel large language model (LLM)-based AI systems, powered by improved AI reasoning techniques at training and inference time, are potentially powerful tools for the TP community. If substantial parts of the theoretical research process could be performed by AI, this would allow to significantly accelerate progress in TP. If AI could act as a fast, reliable and skilled research assistant that can perform theoretical calculations and solve mathematical problems, human researchers could cover substantially more theoretical ground, evaluate more ideas for their promise, and thus make more theoretical discoveries. Even without super-human intelligence, an AI ‘craftsman’ would allow humans to outsource tedious calculation work and to focus more on creative aspects of the theoretical research process.
Recent advancements in LLMs have allowed models to solve progressively more difficult tasks that require abstract mathematical reasoning. While high-school level math competition benchmarks like`MATH`[1] are almost saturated by current models, the focus has recently turned to graduate level and research level mathematics. A main data set in this domain, the recently introduced`FrontierMath`[2], which contains
research level difficulty problems, is still mostly unsolved by frontier models. In TP, which also requires extensive abstract mathematical reasoning, there has been comparatively less work than in mathematics. Existing benchmarks which include physics such as`JEEBench`[3],`OlympiadBench`[4] and`PhysicsQA`[5], cover mostly high-school-level problems from college entrance exams or competitions. There is little existing work on mathematical reasoning for TP at graduate or research level. An exception is [6], where the authors evaluate the performance of LLMs for symbolic calculations in quantum many-body physics, however in the narrow context of a specific physical setting. Very recently, the`Humanity's Last Exam`dataset [7] (HLE) appeared as a multi-domain benchmark that includes problems from TP. We provide a more complete list of available data sets in section 5.1.
In the present work, we build a data set to test TP reasoning skill over a broad range of difficulty. We aim to answer the following questions:
To answer these questions, we created a new benchmark data set`TPBench`of TP problems of varying degree of difficulty, from advanced undergraduate to research level. Our problems are novel, in the sense that they do not come from public problem collections (see section 2.5 for detailed comments). For graduate level and research problems we focus in particular on problems from high-energy physics and cosmology. An important property of our data set is that it provides a*continuum*of problem difficulty, from easy to research level, which few mathematical data sets do. This allows us to compare the performance of different models over a wide spectrum of difficulty. We invite the reader to skip ahead to appendix C to get an impression of the difficulty of these problems. Before discussing our data set in detail, we begin with some general remarks about reasoning for TP and its relation to AI models.
**Differences between reasoning in math and TP.**Because TP is extremely broad and math is arguably even broader, any summary discussion of the differences between mathematical and physics reasoning is unlikely to be accurate in many examples in a generic comparison set. Nevertheless, in terms of modern graduate level and higher physics and mathematics comparisons, several aspects typically stand out.
6 Certain corners of TP such as formal general relativity and string theory come very close to the reasoning style of mathematics (e.g. [8–14]). This will not be treated here, and this in some sense is covered by the LLM literature dealing with mathematics.
These properties make TP an exciting testbed for AI reasoning models, which has not been extensively explored, perhaps because models were not powerful enough to do so, until very recently.
**Generating novel research ideas/problems in TP.**Novel research in TP, as in all fields of science, is usually incremental, and novel research ideas are combinations or further developments of prior work. For example, once a novel method has been invented, it can often be applied to many different problems. Indeed, Feynman advised to keep a list of favorite problems, and to check whether any newly learned technique could be useful for one of these problems [16]. Experienced researchers have an advantage over students at generating interesting research because their knowledge base is much larger and more interconnected. Indeed, what makes a research level question different from a classroom question is often the novelty and connection with existing knowledge and not the reasoning difficulty. It seems very plausible that machine learning models, with their ability to ingest vast amounts of knowledge during training or inference, could be particularly strong at finding promising combinations of novel results and techniques. A recent study in NLP research [17] found that LLM research ideas are rated more novel (but slightly less feasible) by human experts than human expert ideas. Experienced researchers are also able to judge whether a mathematical result is interesting or surprising and deserves further investigation. Such ‘theoretical taste’ may be beyond existing AI models. With our data set, we are not currently aiming to test these aspects of theoretical research.
**Reasoning abilities required to solve research problems in TP.**Researchers (consciously or unconsciously) have a number of techniques or heuristics to solve theoretical problems. A famous collection of problem solving techniques and advise is George Polya’s book*How to solve it*[18] which lists about 50 heuristics with suitable examples in mathematics. Techniques include decomposing the problem, finding a related problem, generalization, and many less obvious ones. Most researchers have a more limited toolkit than Polya and many novel papers are somewhat straight forward combinations of reasoning steps contained in previous works. A main difficulty in this case is to understand this prior work and be able to recall and connect it when needed. Of course, insights are also often re-discovered independently. When solving a hard problem, researchers may try many different paths or heuristics, jump back and forth in their reasoning chain, analyze examples, answer subquestions, clear up their misunderstandings, read related literature, etc. In principle, given a large enough context window for prior thoughts and unlimited inference time, LLMs may be able to perform such very long thought processes, but currently available models (with a public reasoning chain) do not show very deep thought processes in our experience.
**Technical (calculation) abilities required to solve research problems in TP.**Once a mathematical reasoning step has been proposed, it needs to be executed correctly. This step is in principle straightforward but error-prone for most humans. For example, one may decide to Taylor expand an expression to third order, perform a Gaussian integral, re-arrange terms, or even just multiply numbers. LLMs are well known to perform poorly at such tasks, but this problem can in principle be fixed by using computer algebra systems, if they can work with the required mathematical objects (which however is often not the case in TP).
**Observations from our evaluation.We**list some observations from our experiments, which we discuss in more details in the following sections.
or`Mathematica.`Such wrong intermediate results then lead to incorrect followup reasoning. It should be noted that humans tend to make similar mistakes in calculations, but are often able to spot them on revisiting. We made an initial attempt to encourage symbolic verification with python, which we describe in section 3.3, but found that it barely improved results. Better symbolic tool integration would be very beneficial for TP reasoning.
The paper is organized as follows. In section 2 we discuss the properties of our data set, including the origin of problems and our approach to verification and grading. In section 3 we benchmark popular closed source and open source models on this data set. In section 4 we analyze the output of these models in more detail, and categorize their failure modes. In section 5 we discuss related work. Finally in section 6 we discuss future directions to improve AI-based reasoning in TP.
**2. Properties of TPBench**
**2.1. Overview**We have curated a dataset of problems and associated solutions in main areas of TP. For research level problems we currently focus on high-energy theory and cosmology, the main expertise of the authors. Problems in our collection should have the following properties (similar to`FrontierMath`[2]):
It is hard to strictly enforce all these conditions in TP, as we discuss further below. Problem originality and the possibility to guess the answer can be judged differently by different researchers. For this reason we also provide metadata for each problem individually. We point out potential shortcomings in instances where we are aware of them. We include problems of varying degrees of difficulty, from undergraduate to graduate and to research problems. Naturally, research problems are more difficult to create, especially when requiring the answers to be novel and unpublished. Furthermore, more difficult problems are often more novel than easier problems (since the space of possible problems grows rapidly with their complexity). We discuss the aspect of novelty of our problems in more detail below, as well as individually in the problem metadata. We also make sure that our problems do not contain steps where a human would need a calculator to solve them (e.g. no floating point operations).
We now discuss the attributes of our data set in more detail, including their statistical distribution. We aim to enlarge and diversify the data set further in the future. We also provide ten sample problems in appendix C and we encourage the reader to browse the problems to get an impression of the whole data set.
**2.2. Problem statistics**The dataset is categorized into five difficulty levels:*1—easy undergrad, 2—undergrad, 3—easy grad, 4—grad,*and*5—research.*This classification ensures that the dataset can accommodate a wide range of use cases, from introductory studies to cutting-edge research challenges. The distribution of problems across these difficulty levels is detailed in table 1. For difficulty level 1–4 this means that the problem could appear in a homework problem or exam for students. For level 5, this problem could appear as a nontrivial step in a publication: i.e. our research level problems are sub-problems that would constitute a part of a publication, and are not by themselves large enough to constitute an entire publication. Solving level 4 and 5 problems would make models useful for theoretical research, but would not mean that models could write their own publishable papers (by a significant margin). Indeed, one of the most important steps in TP research is establishing why a particular question is important and organizing a string of level 5 type of steps to answer that question.
**Table 1.**Distribution of problems by difficulty level.
Difficulty level Number of problems Percentage
1—Easy undergrad 8 14.0% 2—Undergrad 13 22.8% 3—Easy grad 11 19.3% 4—Grad/easy research 14 24.6% 5—Research 11 19.3%
**Table 2.**Distribution of problems by domain. The ‘Other’ category includes astrophysics, electromagnetism, quantum mechanics, statistical mechanics, and classical mechanics. Many problems are in between areas. For example some Cosmology problems could also be classified as High Energy Theory.
Domain Number of problems Percentage
Cosmology 19 33.3% High energy theory 18 31.6% General relativity 4 7.0% Other 16 28.1%
Future iterations of this data set could include more open-ended research problems, more reminiscent of a research publication.
The problems in the dataset span specialized domains, including*cosmology, high energy theory,*and*general relativity.*The less difficult problems span a wide area including astrophysics, electromagnetism, quantum mechanics, statistical mechanics, and classical mechanics. This domain-specific focus ensures the dataset’s relevance to theoretical research related to the fundamental laws of nature, while the less difficult problems allow us to establish as a baseline what a successful AI performance looks like. Table 2 provides an overview of the distribution of problems by domain. In the future, we aim to include problems from other domains of TP, such as condensed matter theory.
The dataset includes problems from various sources, in particular unpublished research, private coursework, and recently published research papers. Almost half of the problems are novel (e.g. most of the level 3, 4, and 5 problems), having been created specifically for this dataset, while others draw on course-related material of the authors. A small number of problems have been taken from very recent publications (e.g. [29]).
**2.3. Auto-verification of solutions**To automate the evaluation pipeline, we developed a system inspired by how coding competitions validate their results. We introduced the requirement that the final answer to each problem be provided as a`Python`callable with the specified signature. We then developed a simple automatic (not LLM-based) grading agent that, given the model’s answer and the correct solution, extracts the code, creates, and executes a consistency-check script. This approach allows for efficient evaluation of algebraic answers and automatically ensures that equivalent correct answers are classified as such. Additionally, it is flexible enough to verify answers involving a variety of special functions or answers that involve several outputs. In some problems, the natural system of units*(c= h̄=*1) is specified in the prompt, while in other cases we pass constants of nature as function arguments to be unit agnostic. Alternatively, we could have adopted other automatic verification strategies. We could have provided numerical test cases in the prompt, but this would have led to lengthy problem statements, floating point operations, and much less flexibility. Another option is to consider multiple-choice answers, but this would make it easier to guess the answer without detailed understanding. Yet another possibility is to use another LLM as a grading agent and instruct it to compare the given solution to the true one. However we found that this approach is very error prone and LLMs are often not able to check mathematical equivalence of expressions (see below).
Our proposed scheme gives the flexibility to check the variety of classes of answers exactly. The verification process consists of three components:
1.**Code extraction:**The system extracts Python functions from both the model’s solution and the expert solution.
2.**Test case execution:**Both functions are executed with identical test inputs across multiple parameter combinations.
3.**Output comparison:**Results are compared numerically with appropriate tolerances for floating-point arithmetic.
Each problem in our dataset is accompanied by a comprehensive set of test cases, carefully designed to probe both the physical validity and mathematical correctness of solutions. These test cases span different parameter ranges (e.g. negative or complex arguments where appropriate), to ensure thorough verification.
To illustrate this approach, consider the following undergraduate-level example:
**Problemstatement:Aphotonwith**the*energyE*scatters on an electron at rest at angle*θ*in the electron’s reference frame. Find the angular frequency*ω*of the scattered photon.
**Answer requirements:**Provide the answer in the form of a`verbatim`function with the following signature:
**Model answer:**
*ω*= 1
*h̄ E*+
*h̄ mc2 (1− cosθ)*
This example demonstrates several key aspects of our auto-verification approach. First, the problem statement is clear and unambiguous, requiring a specific physical quantity*(ω)*to be calculated. Second, the answer requirements explicitly specify the expected format of the solution, including the function signature and parameter types. This standardization enables automated testing across different parameter regimes. Third, the model answer provides both the analytical expression and its implementation in Python code, allowing for direct numerical verification.
Furthermore, our verification system incorporates several safeguards to ensure reliable evaluation:
While our verification system works well for many problems, certain TP problems present challenges:
*µ +ω α µ ∧ω ν*
*α*,*L= ϵµνρθFµνFρθ,*or*∇µTµν*= 0) often have multiple equivalent representations due to symmetries. For instance, the Riemann tensor*Rµναβ*exhibits several symmetries including certain index permutations and the Bianchi identity.
´*M d(H∧B)*=
´*∂MH∧B.*For
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8kaL27WOWferRO3M_NKudKKT7yOO34LqhmihUOg78m7lvswyHoFN8kj6zbthSpBlPp2ahbgfrRvGxHYXaDht6AO-rUd2dM7cUfd-aSGF9TvLMKo7Xih4dED8T2pjSdQQ2scGI36A=w612-h173-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX89SaV-zyapsAZEgbL7NIUU1iXL54rbs0fJPU8J5F9F_5fd2VWb2mpKIY2dyXpgxbOBGZ9ClBMWvHYD6W_oIyG-0JntLk5Oej8W8TU_qIxaUPS1BdXa_zhD6hPOYk_OkvJY9YFSJg=w612-h163-v0?authuser=0)

the typical case of vanishing fields at infinity, there are also equivalences up to total derivative terms: e.g.´*[dϕ ∧∗dϕ*+*dC]*=
´*d4x*
*√−g∂µϕ∂µϕ*.
Although this list is common for TP problems in the literature, it can be extended depending on the classes of mathematical objects that need to be covered. The obvious common theme is the wealth of equivalence classes that the verification system needs to be aware of if it were to be generally applicable.
In our current data set, we only include problems where the above issues do not occur, i.e. where the final answer is an algebraic expression without tensors, derivatives, integrals, or manifolds. Of course, these objects do occur in the solution, but not in the final answer. In the future, it would be interesting to develop auto-verifiers for expressions involving these more general mathematical objects listed above. We have reserved a number of such problems for future iterations of the dataset that would be useful for testing dedicated more general verification codes.
**2.4. AI-based holistic grading of the entire solution**In addition to auto-verification, we also employ AI-based grading. In this process, the grader model has access to both the expert-labeled solution and the LLM-generated solutions from a separate model, and is tasked with assigning grades*(A–D).*This approach mirrors how a human teaching assistant grades homework, where partial credit is given for correct reasoning steps, even if the final solution is incorrect. Moreover, holistic grading can identify instances where a solution arrives at the correct answer using incorrect reasoning, which occurs in a small number of our problems. While holistic grading is conceptually preferred, we observe significant disagreement between different grader models as well as humans.
**2.5. Novelty and difficulty of our problems**Most of the problems presented here are constructed based on those given in standard courses as well as unpublished research related notes. For example, the solution to the research-level problem ‘One pole problem’ (see appendix C.1), without steps explained, is given in a footnote of [30]. Most of the research level problems would be readily doable by a good TP graduate student, and some of these are not much different from hard problems in graduate courses whose problems and solutions can be found publicly. However, we have made significant efforts to construct or modify problem statements so that the answers cannot be found by web search. Most of the research-level problems use typical or not-too-atypical notation to simulate a research setting, although this may facilitate literature recall (rather than reasoning) by the model7.
The difficulty of a problem can vary along different axes, i.e. problems may be easy or hard for different reasons. We aimed to provide a sampling of this space:
7 An interesting followup study would be to vary variable naming and other notation to evaluate this point.
well-organized set of variables (typically using group theoretic structure). Some of our problems have been designed specifically to test whether the AI can reason using a seemingly-disorganized set of variables.
**2.6. Public and private data set and data leakage concerns**We make 10 of our problems and solutions public (see appendix C and tpbench.org), two for each difficulty level, such that they can be used to understand the data set, develop inference algorithms and examine failure modes. Naturally these problems will be part of future training data. To deal with this challenge, we also keep a large part of our data set private, currently about 50 problems. If you would like to evaluate your model on our private data set, please contact the authors directly.
Guaranteeing that private data does not end up in future training data is challenging. OpenAI, which we have used extensively, adds user interface chats to its training data but does not add API calls. Correspondingly, we have generally used API calls for querying problem solutions. However, in early phases of this projects, some problems were run in the user interface. In future iterations of this project, we will emphasize data leakage control further, especially for research level problems. We note that a small number of research problems is sufficient to evaluate significant model progress, as long as for these problems data set leakage control and originality of the problem are flawless. For our current problem set, we only enforce that problems (and especially solutions) do not appear publicly accessible online. Furthermore, we took particular care that expert solutions to problems were never passed to the ChatGPT user interface, where they could be added to future training data.
**3. Model performance evaluation**
In this section, we evaluate the performance of several leading models on our dataset, TPBench, across five different difficulty levels, ranging from undergraduate to research-level problems. Closed-source models include OpenAI GPT-4o, o1, and o3-mini [19–21]. Open-source models which we were able to run locally on our hardware include small and intermediate sized Llama 3.1, Qwen 2.5, and Qwen-QwQ, which is an experimental LLM that focused on advancing reasoning developed by the Qwen Team [32–34]. We also include the recent open-source reasoning model DeepSeek (DS) R1 [35] and its base-model DS V3 [36] which we ran on`Together AI`API. Finally, we tried to solve a subset of our research problems with OpenAI’s Deep Research, including the problem in appendix C.1, primarily to spot solutions that could be found online. Deep Research was not able to solve any of these research problems. We believe our subset of models is representative of the spectrum of current LLM capabilities.
We provide the prompts for inference in the appendix B. The complete model answers from all models, for the public problems, can be found on the tpbench.org website. The evaluation considers two grading schemes:*answer-only*and*holistic.*
**Table 3.**Fraction of problems solved for each difficulty for each model.
1-Easy undergrad 2-Undergrad 3-Easy grad 4-Grad 5-Research
Model avg@5 best@5 avg@5 best@5 avg@5 best@5 avg@5 best@5 avg@5 best@5
GPT-4o 0.75 (0.12) 0.88 0.86 (0.17) 1.00 0.25 (0.16) 0.45 0.09 (0.13) 0.29 0.00 (0.00) 0.00 o1 (high) 0.85 (0.05) 0.88 0.97 (0.04) 1.00 0.76 (0.24) 1.00 0.34 (0.13) 0.50 0.18 (0.07) 0.27 o3-mini (high) 0.97 (0.05) 1.00 1.00 (0.00) 1.00 0.87 (0.13) 1.00 0.57 (0.09) 0.64 0.15 (0.12) 0.27 DeepSeek-R1 0.95 (0.06) 1.00 0.98 (0.03) 1.00 0.76 (0.23) 0.91 0.49 (0.20) 0.64 0.07 (0.08) 0.18 DeepSeek-V3 0.72 (0.15) 0.88 0.80 (0.23) 1.00 0.29 (0.29) 0.64 0.11 (0.06) 0.21 0.00 (0.00) 0.00 Llama-3.1-8B 0.30 (0.06) 0.38 0.18 (0.20) 0.46 0.02 (0.04) 0.09 0.00 (0.00) 0.00 0.00 (0.00) 0.00 Llama-3.1-70B 0.45 (0.36) 0.88 0.52 (0.22) 0.77 0.11 (0.11) 0.27 0.04 (0.06) 0.14 0.00 (0.00) 0.00 Qwen2.5-7B 0.10 (0.11) 0.25 0.40 (0.21) 0.62 0.04 (0.07) 0.18 0.00 (0.00) 0.00 0.00 (0.00) 0.00 Qwen2.5-72B 0.60 (0.11) 0.75 0.42 (0.23) 0.77 0.24 (0.16) 0.36 0.04 (0.06) 0.14 0.00 (0.00) 0.00 QwQ-32B 0.62 (0.21) 0.75 0.60 (0.27) 0.92 0.07 (0.15) 0.36 0.01 (0.03) 0.07 0.00 (0.00) 0.00
*Note:*The number in the bracket is the average of model attempts’ standard deviation per problems.
These two choices on their own are imperfect. The first one might consider a solution as correct which has two or more self-annihilating mistakes, or a solution that arrived at the correct answer with inconsistent or false reasoning. If the task is to evaluate the reasoning in challenging problem-solving, the binary grading systemmight not be representative to a satisfactory level. The second has the disadvantage of being somewhat arbitrary on assignments of grades for partial correctness. Our core results will use answer-only solutions.
**3.1. Results for auto-verified solutions**We begin by discussing the answer-only results, which are the key empirical results of this paper. Our results are obtained using zero-shot reasoning where the model is given the problem statement and expected to reason through it without any prior examples. In fact, few-shot learning can degrade general performance in reasoning models [35]. We have experimented with prompt optimization, but found no significant differences (see appendix B for our prompts).
Table 3 presents the performance of each model across various difficulty levels, ranging from easy undergraduate problems (Level 1) to research-level problems (Level 5). The table reports the percentage of problems solved by each model. The columns labeled ‘avg@5’ represent the average score across five attempts, while the ‘best@5’ columns correspond to the average score of the best attempt out of five attempts. We visualize the ‘average of five’ solution percentage in figure 1(strong models) and figure 2. Finally, for our public problems, the individual results of models are given in appendix C. For example, we include one level 5 research problem that top models can solve and one that they cannot.
For the top models, o1, o3-mini and DS R1, undergraduate problems (levels 1 and 2) are now essentially solved, with performance of 95% to 100% for the oX models. For easy graduate problems (level 3), the performance is around 80%. For our level 4 graduate problems, some of which could appear in research investigations, the best models o1 and o3-mini solve around 50%, with o3-mini slightly beating o1. Research problems are mostly unsolved at this stage with a score around 15%. o1 slightly beats o3-mini here, which may be due to it having a larger literature knowledge to draw on.
Among mid-range models, GPT-4o and DS-V3 perform similary. They are between one and two levels of difficulty less powerful than the top models. Midrange models are essentially unable to solve problems above easy graduate level. Finally, lower parameter public models, which have the advantage that researchers can run them on invididual GPUs, cannot solve problems above undergraduate level. We also provide further model evaluation statistics of the data set on the website, including a unified model score over all difficulties.
**3.2. Results for holistic AI-based grading**Table 4 presents the results for the holistic AI-based grading, which involves assigning letter grades*(A*to*D)*based on the quality of reasoning and correctness of the solution. This grading is not limited to the final answer but considers the overall approach taken by the model in solving the problem. We have used GPT-4o as a grader, as a currently mid-range model. We chose this model for cost efficiency reasons, and in the future we intend to use the most powerful model as a grader. The model was provided the grading prompt (appendix B), the expert solution, and the model solution to grade, similar to the way a human teaching assistant would work.
The models’ performances are shown across the five difficulty levels. The letter grades represent the models’ ability to produce correct solutions while demonstrating sound reasoning. An*‘A’*indicates an excellent solution with minimal to no errors, a*‘B’*suggests a good solution with minor mistakes,*‘C’*indicates a solution with significant flaws, and*‘D’*represents a fundamentally incorrect solution.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-QkzIoHy6_zw6h2vqky5wJIOa9_OAGUf4bYFEGj7BUcIVaOYiFdVZCkZMLXMa6adJhEcHnjR_TIs8V53HEhQERserblYJmqqxIO5h19BrttztCXjQKtuSbnE4sYeuEfORsw_1ltQ=w1280-h715-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8ztbb6cl3Ia400_faampQsm8fhs4Qzbu9K5q2-H1ZLcahXGQrvoGcr7JvBb6V8JFUYdOoUv8iDHGBHTXnJhCWFntTLF5SJpJNgSUYVBjPRfQm7pK5wpnGGf46sTOcpf2wqAZrzew=w1280-h708-v0?authuser=0)

**Figure 1.**Accuracy of SOTA models by difficulty level.*Note:*‘high’ in brackets indicates reasoning effort.
**Figure 2.**Accuracy of common open-source models by difficulty level.
In principle, the holistic grading system provides insights into the models’ reasoning capabilities beyond just final correctness. However, we find some difficulties with holistic grading as we now describe. This is consistent with results showing that LLM-as-a-judge approaches have considerable bias [37].
Table 5 and the corresponding bar chart in figure 3 summarize how the automatically verified results*(Correct*vs.*Incorrect)*align with the letter grades*(A, B, C, D)*assigned by the AI-based holistic grading. For*A-graded*solutions, a large fraction (80.1%) aligns with the auto-grader’s correct verification. By contrast,*B-*and*C-graded*solutions show substantially lower correctness rates (16.3% and 4.9% respectively). In the*D*category, an overwhelming 99.5% fail the auto-grader’s check, indicating that both holistic assessment and numeric verification typically reject these solutions.
Overall, there is a strong correlation between higher letter grades and positive verification outcomes, which validates that the AI-based grading system’s assessed quality generally corresponds to the auto-grader’s numeric correctness checks. At the same time, deviations exist in each category. For example, nearly 20% of
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX98vWw0nWfS4kQHFmgvI3CXONQsYLkijxsVdSy9htC_082i7LxaD0IfZWrsIiB69YSzN1g1-TAzIyNgZqmNng0P_L5ty3faSCvUYkLxvUkY4g7NmsbpQ20D8sICpE2o6M_K9YGD-w=w611-h389-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX99Rl_1lIgJzl-yhJH0ManqCz3n3x2oXmnR721xK6s7mQVnCV3-a-PSPqSw5BdiDKi8A2hZ_2eT8K1XzlV4Zl54leR2S-EQQv61nmYsek8mOl1nDBM8NiytDDTWFmnKkD85SU7h=w611-h378-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9rZRB6vRgBLxR21JYDcHEPF9Yb3FDRlInEaZeuytuMJPzLYaDKCztQm3HbtzEihxLt5sSHYs-ZqAOmQt36G5YtHQKG1tyr_7ynzouq7dYMCT4vK9WU0uIF4PJdh-aVg2NGlgKSpQ=w881-h510-v0?authuser=0)

**Table 4.**Letter grade received for different models.
1-Easy undergrad 2-Undergrad 3-Easy grad 4-Grad 5-Research
Model*A B C D A B C D A B*C*D A B C D A B C D*
GPT-4o 28 0 11 1 50 6 8 1 20 4 29 2 8 5 51 6 1 4 50 0 o1 (high) 36 0 4 0 60 5 0 0 48 3 4 0 41 4 22 3 23 9 23 0 o3-mini (high) 39 0 1 0 60 5 0 0 49 3 3 0 51 1 18 0 36 3 16 0 DeepSeek-R1 31 2 7 0 58 6 1 0 41 2 10 2 25 3 23 19 6 0 26 23 DeepSeek-V3 26 0 12 2 50 6 9 0 15 7 29 4 11 6 47 6 0 0 49 6 Llama-3.1-8B 11 1 15 13 4 7 25 29 0 1 13 41 0 0 15 55 0 0 8 47 Llama-3.1-70B 19 0 17 4 31 1 29 4 5 6 36 8 2 3 50 15 0 0 44 11 Qwen2.5-7B 3 2 24 11 22 4 25 14 3 1 22 29 0 1 34 35 0 0 32 23 Qwen2.5-72B 25 0 13 2 35 5 23 2 11 5 30 9 8 2 47 13 1 1 46 7 QwQ-32B 25 3 11 1 38 9 18 0 11 1 33 10 2 2 49 17 1 1 37 16
*Note:*the number of attempts per each level equals 5 shots times the number of problems in the level (see table 1).
**Table 5.**Grade verification results. Percentages in parentheses indicate the distribution of verification outcomes within each grade category.
Grade Correct Incorrect Total
*A*880 (82.2%) 190 (17.8%) 1070*B*61 (43.6%) 79 (56.4%) 140*C*74 (6.4%) 1075 (93.6%) 1149*D*5 (1.0%) 486 (99.0%) 491
Total 972 (34.1%) 1878 (65.9%) 2850
*Note:*The total number 2850 results from 5 attempts for each of the 57
problems in the data set across 10 models.
**Figure 3.**Stacked bar chart showing the number of solutions verified as correct (green) versus incorrect (red) across each letter grade.
*A-graded*solutions fail the numeric check, often because the AI holistic grader failed to correctly determine whether two answer expressions are equivalent. This is typically due to the expressions being overly complex. Conversely, a small fraction of lower-graded*(C*or*D)*responses may be mathematically correct in final form, yet insufficiently justified in intermediate steps, causing the holistic grader to assign a low grade despite correct numerical output.
Our findings illustrate that automatic verification and holistic AI-based grading are generally consistent: higher-quality solutions are confirmed as correct more frequently, while lower-quality solutions often fail numeric checks. Our current GPT-4o grader however has significant shortcomings. By cross-checking the grader with human grading, we find that LLM grading works reasonably well when grading solutions of low difficulty 1 to 2, but is not reliable at level 4 or 5. It seems likely that 4o is not strong enough to understand the logic of these higher difficulty problem solutions. Even when the grading model is as strong as the solver model, the success of holistic grading could be limited: LLMs are generally not very good at correcting their own results, as has been studied for example in [23]. In the present work, we thus focus on the auto-verifier results, and leave detailed exploration of holistic grading to future work.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-B5zgbF-KkW8aVlVNJTxrcSOLKWSG0f5C5cV-ufksuRZPQESJiinxOgffeMDUbvmKEwwJBYddy_jgp4MJuXbpSexljR0QASc5jfxmkxb4blp7cfVprRHfPcYeJCasJPpb_7s22ow=w611-h283-v0?authuser=0)

**3.3. Augmenting inference with python to reduce algebraic mistakes**We experimented with instructing models to break down calculations into smaller steps and verify these with python. Using a code interpreter was previously found to be beneficial in reducing algebraic mistakes in calculations (e.g. [38]) Our approach was based on the`MathChat`[39] framework and prompt tuning. We instructed the model to write python (particularly`SymPy)`code for each calculation step and verify its result using this code. In a few cases, for low difficulty problems, our approach was able to spot and correct mistakes. However, more often the approach disrupted the reasoning chain and led to worse results. For complicated problems, models struggled to identify steps that can be checked with`SymPy.`We note that our problems do not include floating point calculations, where verification would be straightforward, but require more complicated algebraic operations. Recently, the FrontierMath paper [2] included a set of prompts to encourage LLMs to verify with python, but noted that advanced models barely made use of this possibility. While human theorists do sometimes check their results with computer algebra systems, especially`Mathematica,`this process is not straightforward, and there is likely limited existing training data for this approach. We aim to experiment with few-shot inference or fine-tuning in the future, showing the model handcrafted examples of`SymPy`or`Mathematica`verification in the prompt. Since our current`MathChat-based`results are not stable we chose to defer this direction to future work8.
**4. Failure mode analysis**
We now discuss common classes of mistakes. We present a few examples highlighting the various types of errors that the LLMs make while attempting to solve problems in TP. We broadly classify these errors into four classes as shown below. Our examples mostly draw from GPT-4o and o1 model results.
**4.1. Background knowledge of the model**Background knowledge is a strength of LLMs. Problem authors were impressed by models’ ability to recall relevant mathematical definitions that were not included in the problem but are known to practicing researchers. This ability makes it much easier in principle to solve problems than with a computer algebra system like Mathematica. For example, consider the level 5 cosmology problem from appendix C.2:
**User:**In cosmology, large-scale cosmological dark-matter halo fields are biased tracers of the underlying Gaussian matter density*δm.*Assume we have a sample*δm.*We simulate a halo number density field by taking**n(x)**=*n̄max(0,1+***bδm(x)),**where bare number density*n̄*and bare bias*b*are specified con-stants.What is the bias of the sampled halo field? Derive an equation to evaluate the bias which depends on the bare bias and the variance in each pixel.
While well-defined for a cosmologist, the problem does not define the mathematical quantities in detail, and would be hard to interpret by a non-cosmologist. Advanced models correctly recalled the required definitions and generally set up the problem correctly.
However, while LLMs generally recall key definitions of various sub-fields of TP, they frequently encounter difficulties in accurately recalling more detailed mathematical information, as illustrated by the following two examples.
In one of the solutions to an undergraduate QM problem, the QwQ model incorrectly retrieves information about the Clebsch–Gordan coefficients. Specifically, it claims
From standard tables or textbooks, the Clebsch–Gordan coefficients are:
*⟨1m1 1m2|j m⟩*
For*j= 1,m=−1:*
*|1 − 1⟩=*√ 2
3*|1 −*1 1*0⟩+*
√ 1
3*|1*0 1*− 1⟩ .*
The correct value of these coefficients*are∓1/ √*2 for*|1 −*1 1*0⟩*and*|1*0 1*− 1⟩*states respectively.
8We note that in followup work, we were able to leverage symbolic verification to improve model performance by employing an agent framework and parallel test-time scaling [40], however only for a limited set of mathematical operations.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_N3zExiuIoQbVDrTSwCWUrGtnpb3fOWnDSzQwTyvTAjFFVbnyWx8jbjkVRSNoJGjoxag3pfszvk6IQAbjSVpThzl0OLEzUPH_uer2ZImZ8NVG1IF4q1c-MxPAlgG9n1HkdBw0PNA=w612-h127-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-Wqn3kBLJ08SPrCOpMYe3FYCvvVEYvDjbbL8K68ZMK4_moLSR7pOTUJD3IlTZiZvdfn1J3FnWylaLcp2pLlAP6dENU07he1mtpEsR-mIhgJf7vTShRK5Y1vN6W092il3oeXeMJ=w612-h153-v0?authuser=0)

In the following snippet, generated from a model answer, the GPT-4o model incorrectly identifies the standard eigenstates of a particle in a 1-D infinite potential well*(|x|⩽ L/2)*from existing results9
*ψn (x)*=
√ 2
*L*sin*(nπ x*
*L*
) for*n= 1,2,3, . . .*
and
*ψn (x)*=
√ 2
*L*cos*(nπ x*
*L*
) for*n= 2,4,6, . . . .*
**4.2. Algebraic mistakes**A major challenge for models is to perform correct algebraic calculations. Consider the following relatively easy math problem that appears as an individual step in one of our problem solutions.
**User:**Determine the leading real term of the expression
*F(k) =−1+*(*59a2k2*
15 +*iak+*1
)5 exp
(*−1*6*ak(85ak+ 6i)*
) for real*a,k ∈*R and*k≪*1.
**Expert solution:**The correct series expansion up to leading real and imaginary terms is
lim*k≪1*
*F(k)≈ 793a4k4*
180 +*4iak.*(1)
We attempted this problem multiple times with o1 and o3-mini. In most of its responses, the LLMs did not expand the exponential term beyond the second order in*k,*falsely assuming that the leading real term must be proportional to*k2.*In its best attempt, it expands up to quartic order in*k,*but fails to accurately combine the various terms to compute the coefficient of*k4.*This is a good example of the promise of combining with computer algebra systems. If we add the prompt ‘Write and execute`SymPy`code to evaluate the expression.’ models can generate Python code that calculates the correct expression. We have therefore tried to encourage python usage as discussed in section 3.3, however with limited initial success.
Algebraic mistakes are numerous, and often occur even in very simple calculations. Models often simply forget mathematical terms in an expression from one calculation step to the next. For example, the following is an arithmetic evaluation by GPT-4o, in which it spuriously drops a factor of the imaginary number*i:*
*∇2E⃗= iω (σ− iω) E⃗= ω (σ+ iω) E⃗.*
Similar cases of forgotten*i*factors, minus signs or constants occur frequently in many problem solution attempts.
Mathematical identities are also often applied incorrectly. For example, in the following case GPT-4o fails
to implement the vector triple product (*(⃗a× b⃗)× c⃗= (⃗a · c⃗)⃗b− (⃗b · c⃗)⃗a*
) correctly and writes
(*E⃗× ẑ*
)*× ẑ=*
[(*E⃗× ẑ*
)*· ẑ*]*ẑ−*(*E⃗× ẑ*
)*(ẑ · ẑ) .*
9 The correct set of eigenvalues are
*ψn (x)*=
√ 2
*L*sin
*(nπ x*
*L*
) for*n= 2,4,6, . . ., ψn (x)*=
√ 2
*L*cos
*(nπ x*
*L*
) for*n= 1,3,5, . . . .*
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8QTpIRgTpVVGZLmgfGROurfeIwiiXs1_IAENP6XxeW2Y2vlOZqzuhJ8us7DwiGFUkK3gV5JNlz4pLfvvUMy2g5aDHEpBpruC9qLeJJC6NXqe7uSVajtmY5sn7_ONlEBbKwPeTVPw=w612-h141-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_d2vu7M7hUzOIX8tQIoj5hUYAy9I1C0Jm2OZmOLnA8yOHdUzzEKK366UYDkS2RwrTf5Zu8Lq1nQ1IfyaInab3iQJ-5mrFKevqmeuFZNlxoTfOmnjvYgPrcGbd-qdimYGM3wK0AvA=w612-h238-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX95UT5ItmK94MvCuZf_hUfHJpIKLxCce9XDrD46QBRi9GqpTiGYy05CrRsIYNGh6AKqQfEO5O5_CEherSfzk7QbDT717Km8rqf9vx9icYUFzVDLhMJ96xAFCJSB-tGrAhwh0YkOkg=w612-h50-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-iRWrW3R-xuXZ9OR1EC3BnpQAGRyCpn7-JPDj9M4C4y8mpD5pbaza5bTgtq7gnHQ2U0pvzROLzyCYB-l5j4wQ2ZfAxH1z2Cvu2HrGhVYhjMtNY3Udn9vLz2sgd_Ejge-k24B6MPA=w612-h56-v0?authuser=0)

More powerful reasoning models tend to make less frequent ‘simple’ math mistakes such as the following:
**o3-mini:**After performing the*η−integrals*(using the standard*iϵ−prescription*so that ˆ 0
*−∞ dη eiKη*=
1
*iK ,*
ˆ 0
*−∞ dηη eiKη =−*1
*K2 ,*
where the second integral erroneously contains a negative sign. It would be interesting to compare model performance on a set of automatically generated simple calculations typical for TP.
**4.3. Logical mistakes**We frequently observed that LLMs struggle to accurately account for the validity and applicability of advanced mathematical concepts, such as incorrectly applying theorems, misinterpreting definitions, or failing to recognize the limitations of certain mathematical techniques. Consider the following mathematical problem, which we will use to discuss logical errors made by the oX series models in their attempted solution.
**User:**By Taylor expanding the integrand, find a*b*cubic polynomial approximation to the integral
*I(b)*=
ˆ 1
*b*
*√ π*
*x − π*erfc
(*1√ x*
) exp ( 1*x*
)*x3/2+ x5/2*
*dx,*that achieves a 90% or better accuracy when*b*lies in the interval*[0,1].*
**Expert solution:**First, we note that the integrand remains finite in the limit*x→*0, as the singular term proportional to*1/x*cancels out. To assess the validity of a series expansion, we estimate the radius of convergence near the boundary points*x=*0 and*x=*1. This analysis shows that the integrand is convergent within the interval*[0,1]when*expanded about*x=*1. Consequently, we perform a Taylor expansion around*x=*1 retaining terms up to*(x−*1)2:
*√ π*
*x − π*erfc
(*1√ x*
) exp ( 1*x*
)*x3/2+ x5/2*
*≈ (√*
*π−*1
2*eπ*erfc(1)
)*−*( 27*√ π*
4*−*63
8*eπ*erfc(1)
)*(x−*1)
+
( 21*√ π*
8*−*51
16*eπ*erfc(1)
)(*x2−*1
)*.*
Integrating over the interval*[b,1],*we obtain the approximate solution:
*I(b)≈*(*b3−*1
)(17 16
*eπ erfc(1)−*7*√ π*
8
) + (*b2−*1
*)(27√π*8
*−*63
16*eπ*erfc(1)
)*+(b−*1)
( 83
16*eπ erfc(1)−*41
*√ π*
8
)*.*
In the limit*b→*0, our approximate expression evaluates to
*I(0)≈ 1.54633,*
which achieves approximately*93.6%*accuracy compared to the numerical result*1.65221.We*note that this integral cannot be evaluated exactly using Mathematica or Maple software.
When the above problem was given to the o1 and o3-mini models, they demonstrated the following logical errors in their reasoning:
1. The model begins by identifying that the integrand is finite at*x=*0. However, it fails to recognize that the radius of convergence for the integrand around*x=*0 is 0. This oversight leads to an improper application
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9I7R6BUMwnPopZTAct7HCJFUfHgbamL1uQDCkm8vrxZBt_qbhhpEVsS080kjWp7YdgqiaBi86nyvuVHxOcRwFUzknxYq42O32vy3hTTuLONY_hf0yLxdLKhZaT3Z76PtKF1bCZWw=w612-h91-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX83-yR1XfJduTg7I5ZmFUO035awJQ6NfceHl6xyfIuKy4ur8iFp1MBPN5xVmN8lkFnm361YtwkQ05jaTIKsde37lOx8KuDBX7psfT6TfPZIIYq-HQjmYzxxAYSjgvW2Kdi0EQur=w612-h606-v0?authuser=0)

of approximations beyond the valid domain. Subsequently, the model factorizes the integral as
*I(b)*=
ˆ 1
*b f(x) dx=*
ˆ 1
0*f(x) dx−*
ˆ*b*
0*f(x) dx.*
Assuming*b≪*1, the model proceeds to perform a Taylor expansion of the integrand around*x=*0 and
evaluates the second integral ´*b*0*f(x)dx*up to cubic order in*b.*However, the Taylor expansion is only valid
within the radius of convergence, and this restriction is not respected, rendering the approximation potentially invalid.
2. To estimate the constant value of the first integral ´ 1 0*f(x)dx,*the model imposes the boundary condition
at*b=*1, equating
ˆ 1
0*f(x) dx=*lim
*b→1*
ˆ*b*
0*f(x) dx.*
The model substitutes the cubic-order Taylor expansion solution for ´*b*0*f(x)dx*derived in the previous
step into the right-hand side of this equation. This substitution constitutes a significant logical error in its reasoning, as the cubic-order approximation was determined only for*b≪*1, a fact that the model seemed to know but failed to implement. Extending this local approximation to*b=*1, far beyond its domain of validity, leads to an erroneous evaluation of
´ 1 0*f(x)dx.*
Interestingly, the o3-mini model demonstrates two critical flaws: it not only arrives at logically inconsistent conclusions but occasionally also confidently hallucinates the claim*I(0)*=*π/2,*failing to furnish a coherent proof despite repeated prompting.
In a different problem involving particle physics, the GPT-4o model was asked to determine the effective mass of a spin 1/2 particle with action
*S=*
ˆ*d4xψ̄*
(*iaγµ∂µ − c−*i*b√*
3*γ5*)*ψ.*
The models did not understand and failed to reason out that the parameter*c*alone does not define the physical mass. The pseudoscalar*γ5-term*must be included, corresponding to a chiral contribution to the mass.
For a much more basic example of failed logic, consider an example from QwQ. In one of our undergraduate Electrodynamics problems it produced the following expression followed by a faulty and rather incomplete reasoning:
(*E⃗× ẑ*
) =*bE⃗.*
But*E⃗× ẑ*is perpendicular to both*E⃗*and*ẑ,*which suggests that*E⃗*must be perpendicular to*ẑ*for this equation to hold.
We found that advanced reasoning models such as o3-mini generally do not make such easy mistakes on undergraduate level physics problems. However, for difficult problems, they often oversimplify the problem due to a lack of detailed understanding. For instance, while solving the Level-5 problem detailed in appendix C.1, o3-mini and other advanced reasoning models approximate scale factor*a(η)*by expanding it linearly around the transition point,*ηe,*not realizing that the pole is far from the transition point and thus one needs to apply*a(η)∼ η2.*For further details, we refer the readers to the expert solution detailed in appendix C.1.
**4.4. Hallucinations**Lastly, we present two instances where the LLM models generated new rules to obtain solutions that match with existing results in the literature. The following expression generated by GPT-4o represents an arithmetical hallucination error:
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-s6VK-e0togciVJacYQmRJjKbNSNw3b1Z-v46CIR5I6ha-uEV95jDfywETHumw7ALpmNe6Bx97Jk9mKJKhlmNHY888QmcMLoMiyHh4QWdVsgG0x1-ntmvOMD7en-XtaUf9eNt3LQ=w612-h106-v0?authuser=0)

*k= √ ωσ ≈*
*√ ωσ*
(*1√*2 + i
*1√*2
)*.*
The model performed the above arithmetic steps since it needed to determine the imaginary component of*k.*With this goal in mind, it carried out the above ‘illogical’ mathematical step inventing new arithmetic rules to justify its approach to obtaining the imaginary component from a wrong answer.
Another example, from our problems, of o1 hallucinating non-existent rules to justify its approach is the following excerpt from its solution:
We can write
*T=*Tr*[γν ̸ p1γµ ̸ p2*(1+*γ5)(1− γ5)] .*
Note that
(1+*γ5)(1− γ5)*=*0.*
Therefore, to avoid vanishing of the trace, we need to consider that the*γ5*matrices need to be kept separate. Instead, we should expand the trace without combining the projectors.
There is no such mathematical rule that an apparent zero can (must) be avoided by separating the terms and adding them later. The LLM invented this ‘rule’ since it was working with incorrect expressions to nevertheless arrive at a correct solution, which in this case it was able to guess or recall (in only one of several attempts).
**4.5. Performance of pre-o-series models**In our experience, models that are not explicitly trained for reasoning (i.e. before the oX series) can be used to assist researchers that reason through a simple problem, but with significant shortcomings. Consider the following easy mathematical subproblem that appeared in one of our recent works [29] in the context of cosmology, which we show here in simplified notation.
**User:**Assume**a, b,**and**c**are vectors, and**N**is a symmetric positive-definite matrix. Let*x*and*y*be real numbers. I want to minimize**a⊤Na**under the constraints**a⊤b=***x*and**a⊤c=***y.*Solve this for**a,**if possible.
**Expert solution:**Weminimize**a⊤Na**subject to the constraints**a⊤b=***x*and**a⊤c=***y.*The Lagrangian*L*for this optimization problem is defined as:
**L(a,λ,µ)**=**aTNa+λ**(**aTb−***x*
)*+µ*
(**aTc−***y*
)*.*
Taking the gradient of*L*with respect to**a**and setting it to zero yields:
**∇aL= 2Na+λb+µc=**0
which we can solve for**a**as:
**a=−1**2*N−1***(λb+µc)***.*(2)
The constraint equations are:
**aTb=***x*and**aTc=***y.*
Plugging the solution for**a**into the constraint equations gives[**bTN−1b bTN−1c cTN−1b cTN−1c**
][*λ µ*
] =
[*−2x −2y*
]
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9fTki7ycQfdWrZ_5y4UP2g-FxBEOIfbEqsE_dRQ4ctXR3cc6EPsi758plleKKHADaReVZMZXKtEC7jWZTjTO41qJ1L9DC89wu-jpy6RCHJ3mpDJc9Kej3HsVgGIuoO8NxAEyCp=w612-h64-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_SzGLLzu9V0qsmARIY4UZL3Pc4fgDnAb7Dwo5PknrpTvVgU-NUNw3zWnPWykORxWD6ppbNj_823gf-2BJOk_JFSf_00a40FKr17swbptOqOk7KaCmz1cbUfyT002GvO2fzy_6uSQ=w612-h184-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_9usudqdZlb0ad2Ix6-9vXko770mwaRxG10VeGafP73N-moLcYecTwCad2f__YiKCTjPCFM8pSjv3QvHw3amJfCP-C1GqGWCsQyZwnnRtol69HLgFRvHAhQAFPargJm0T1PGHkFA=w612-h480-v0?authuser=0)

which is of form
**M**
[*λ µ*
]*=−2*
[*x y*
]*.*
The above linear system is solved by (assuming the inverse exists, e.g. the two bias vectors are not colinear): [
*λ µ*
] =
1
*det(M)*
[**cTN−1c −bTN−1c −cTN−1b bTN−1b**
][*−2x −2y*
]*.*
We then substitute the solution for*λ*and*µ*back into**a**using equation (2).
That is a typical problem that GPT-4o and Llama-3 generally solve correctly, with correct mathematical derivation, although sometimes with a wrong numerical factor. It seems certain that this problem was in the training data of the model. Nevertheless, it is already time-saving for researchers to get answers to similar problems without manual labor. In particular for matrix algebra problems, existing computer algebra systems are not very strong or user friendly in our experience. However, the fact that models are very error prone limits their usefulness significantly. If every step needs to be checked in detail, the time saving can be minimal, or a wrong result can even confuse the user. Of course, human solutions can also have this property, depending on the skill and carefulness of the researcher.
**4.6. Performance of o1, o3-mini, and DS reasoning models**From evaluating the output solutions generated by advanced LLM models such as o1, o3-mini and DS, we observe that these models exhibit significantly stronger reasoning capabilities compared to other LLMs tested in our study. Notably, these models can perform more difficult algebraic manipulations, identify different components of a problem, and connect them with established concepts in the literature. This ability allows them to make meaningful progress in research-level problems, including those from topics such as QFT and String theory, by pinpointing key aspects of the question and recalling relevant background knowledge.
However, these models still struggle with detailed and systematic logical reasoning. When tasked with solving our Level-4 and Level-5 problems, these models often perform well in the initial phase of problem solving, demonstrating promising insights. Yet, for problems requiring extensive calculations combined with step-by-step logical rigor (e.g. loop integrals in QFT, tensor manipulations in general relativity) and systematic justfication of the assumptions, their performance deteriorates significantly. Our analysis of multiple solutions suggests that when intermediate steps become too complex, the models (including DS) often resort to literature memory from pre-training rather than performing detailed calculations. Rather than explicitly detailing intermediate steps, the models often present only their final answer, recalling related literature knowledge without references or resorting to vague assertions such as ‘after a lengthy (but straightforward) calculation’ or ‘a short calculation shows’. While the full CoT of the o-series models is not public, we have no evidence that the models genuinely perform relevant calculations internally in these cases.
As an illustrative example, when asked to compute the one loop anomalous magnetic moment of a fermion (e.g. [41]) including a contribution from a heavy scalar coupling, the model resorted to recalling existing solutions seen during pre-training rather than explicitly solving. However, it failed to recognize that the Yukawa interaction Lagrangian provided in our problem statement contained an additional factor of*1/ √*2, which may deviate from the conventions in the literature. Consequently, its final answer overlooked
this crucial modification. In a similar manner, when presented with the task of solving the Level-4 problem in appendix C.4, all advanced models (oX, DS-R1) initiate their response by articulating their interpretation of the problem statement and correctly identifying its connection to the standard supersymmetric transformations within the free Wess–Zumino model, as extensively documented in the literature. Subsequently, these models produce their final solution from memory. However, a consistent error emerges across all responses: the absence of the critical ‘negative sign’ as seen in the solution given in equation (108).
**o3-mini:**The well-known and consistent choice is
*δηϕ*=*√ 2ηα ξα,*
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-4zcsHNGg1szpN3akd5xTh7Oe4W63gZXoJPbpTUh0o2G65pRBEgvH5atvDL48UZqxkI9Qd_hiOxT2QqzaLEGiWZulSpQ4N6-L1G3cDe8h_6M-x5wi5slfYFMZBj5M-cY2DP2PWfA=w612-h214-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX81DF4fyh2ibuyaBSxwamz7BdHxgV80xf3Oso7bJP0NBUnRHKmj_Zz_IyQ_-nCxwoWNauLiW02VWjYhjR0ff2sl2TQ0Y2_2cYYt9lxgd7S1ZrCI3YyNLr_HcUn_auvq1a78kkX0wg=w612-h72-v0?authuser=0)

with the Hermitian conjugate
*(δηϕ) †*=*√*2*η̄α̇ ξ̄*
*α̇.*
This is verified by checking that the variations of all terms in*L*under the full set of SUSY transformations (including the ones for*ξ*and*F)*cancel (up to a total derivative).
While this might appear to be a minor discrepancy, it originates from a fundamental aspect of the problem. Specifically, the sign convention utilized in our given problem statement likely differed from the convention commonly adopted in the literature (for instance refer to section 5.2 in [42]) used within the models’ training samples, thereby necessitating a corresponding modification in the final transformation rule. This seemingly subtle yet conceptually significant detail indicates a potential cognitive limitation in these AI models, reflecting an over-reliance on memorized patterns rather than a systematic, first-principles approach, as well as a failure to validate the appropriateness of the retrieved solution within the context of the specific problem statement.
As another example of literature memory, one of the problems in TPBench involves solving a nonlinear differential equation in a manner similar to how Chandrasekhar presents the Kerr solution in [43]. The number of steps to reach the answer is long and complicated. Such (complicated) recall problems are expected to be solvable by an AI due to its vast knowledge of the literature. Indeed, on one of the attempts, the AI can recognize the literature and write an answer to this problem, but even in that instance, it does not reason through the problem but just states:
**o3-mini:**In fact, after a (lengthy) calculation one finds that the only solution (consistent with the field equations and the asymptotic condition) is
*eX*=*r2+C2µ2√*
*∆(r) .*
These inconsistencies suggest that models’ solutions often fluctuate based on how their internal sampling mechanism recalls (pre-)training data, rather than adhering to a logically coherent problem-solving strategy. This underscores a fundamental issue: unlike a proficient researcher who would maintain logical consistency across different attempts, these models exhibit uncertainty in their outputs, lacking a clear measure of confidence in their solutions. Such limitations and the opaque structure of the training and inference process (especially of closed-source models) present obstacles to their applicability in research settings. It appears that successfully solved high-difficulty problems often benefit from the very deep and interconnected literature memory of these models, in addition with their ability to translate this knowledge to the problem setting. While this ability is useful for research, it may not be sufficient to create novel TP results without human assistance. In summary, current model performance perhaps resembles a student with superhuman literature knowledge but low intellectual rigor and technical expertise.
**5. Related work**
Despite significant advances in the mathematical reasoning capabilities of LLMs, accurately solving reasoning problems in specialized domains, such as TP remains a persistent challenge. In math reasoning, the landscape of existing benchmarks has been instrumental for the evaluation of LLM reasoning capabilities and the development of more robust and interpretable reasoning strategies. We review related benchmarks in section 5.1 as well as common strategies for eliciting more accurate reasoning from LLMs in section 5.2.
**5.1. Mathematical reasoning benchmarks**Recent progress in LLMs has enabled these models to tackle increasingly complex tasks that demand high-level abstract mathematical reasoning. A significant body of work has focused on datasets for mathematical reasoning at the middle-school (e.g. [44]), high-school (e.g. [1]), or undergraduate level (e.g. [45]), which often cover arithmetic, geometry, or math word problems. Other benchmarks are focused on theorem proving [46–48]. For example, the recently introduced`PutnamBench`[46] provides a collection of formalized theorems from the Putnam competition, while`MiniF2F`[47] and`FIMO`[48] offer datasets of formalized proof problems drawn from competitions like the IMO, AIME, and AMC. In addition,`ProofNet`[49] comprises both natural language and formalized theorem statements and proofs at the undergraduate
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8TpIRNuSKk63QzBR8dIq9BRFJuYs8Eb3N1CRfKPgeIfHsK_tkwmWQQvi-Chue0yohgKbcVoRxYaIacZ3uU1NzTXQqaPPKwyLLCt-9mJM8-oGLT--JCqP-HdloMKRTZPmFIT-5V=w612-h128-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8DLGBeF37J0_6yoBaBXXjFVEj0NK1pVkweA6RyQ-_Bf3xw-cURdbEZ8mI2GJ4Bvw4_oS0L-mLAsnCQod6BZkFUTRy6QMJPTemUHTF2LlAKU_9Dx_VIHPxvE8hw57Pzdv0-1GKRRg=w612-h110-v0?authuser=0)

level. Complementary to these are natural language datasets that feature problems of varying difficulty [1, 44], as well as benchmarks like GPQA diamond [50], which are designed to be hard. Even more recently, the`HLE`dataset [7] is an industry-curated, multi-domain benchmark that includes very challenging problems, among them some from TP. However, problems in HLE are constrained to numerical answers or multiple choice formats, there is no spectrum of difficulty, and it is not specifically designed to probe reasoning capabilities in TP.
While lower difficulty math benchmarks such as`MATH`[1] have nearly been mastered by current LLMs, the`FrontierMath`[2] dataset, which includes research-level problems curated by working mathematicians, remain largely unsolved.`FrontierMath`spans a range of difficulties from high-school to research level and features properties like auto-verifiability and rich metadata, design principles we have also incorporated into TPBench. However, Glazer*et al*[2] provide limited information about the difficulty distribution and the specifics of the problems that have been solved by advanced models.
In the realm of physics, which also demands extensive abstract mathematical reasoning, the focus has been predominantly on high-school level challenges as seen in datasets such as`JEEBench`[3],`OlympiadBench`[4], and`PhysicsQA`[5]. Beyond undergraduate-level problems, very little work has addressed mathematical reasoning for TP. One notable exception is [6], which examines symbolic calculations, albeit within the narrow context of a specific class of quantum many-body physics problems.
Our new dataset, TPBench addresses the gap in TP reasoning benchmarks beyond the undergraduate level. TPBench encompasses problems ranging from undergraduate to research level, with research problems reflecting challenges typical of those found in TP publications (rather than representing entire publications in themselves). Importantly, TPBench is designed to be independent of industry control, ensuring that the TP research community has access to a reasoning benchmark that is not susceptible to data leakage from future training data. We look forward to sharing this dataset with collaborators under appropriate data leakage controls.
**5.2. Reasoning capabilities of LLMs**Despite the remarkable fluency of LLMs in generating human-like text, their capacity to perform reliable multi-step reasoning remains a challenge [51]. Many LLMs still struggle with complex arithmetic and logical inference tasks. In this section, we review state-of-the-art methods, spanning both training-time and inference-time techniques that have been developed to boost the reasoning capabilities of LLMs.
**Training-timemethods for improved reasoning.**Training-time methods encompass all strategies where pre-trained language models are fine-tuned or otherwise modified to improve their reasoning capabilities. The most popular approaches in this category rely on either supervised fine tuning [52–54], or reinforcement learning [35, 52] (or both [35]). In supervised fine-tuning [55–58], high-quality reasoning chains are curated and used to fine-tune models to display more accurate reasoning behavior. Chen*et al*[59] demonstrate that self-play fine-tuning can improve model reasoning.
**Inference-timemethods for improved reasoning.**Test-time methods aim at improving reasoning capabilities by either designing prompts that elicit good reasoning behavior or by building reasoning systems which prompt the LLM over and over to arrive at a solution in a systematic way. The most popular strategy for prompting LLMs to reason is chain-of-thought [60], where the prompt includes instructions to ‘think step-by-step’. This is a type of test-time approach [61–63], as it typically leads to longer token sequences generated by the LLM. The default prompt (see appendix B) we use to evaluate various LLMs on TPBench is a customized variation of chain-of-though—it includes the tips from Polya’s famous manual ‘How to solve it’ [18] which was originally intended to teach students how to solve mathematical problems. Related advances include prompting the model to break down the problem into simpler subproblems [64–66], or seeking abstractions [67]. Other prompting strategies encourage models to self-verify [68, 69], self-improve [59, 70], or iteratively refine their answer [71, 72].
Other strategies to elicit reasoning behavior involve the generation of multiple reasoning chains which can then be sampled from (as in*best-of-n*[73]) or combined via majority voting or by ensuring self-consistency [74]. Methods that improve reasoning through planning [66, 75–78] roll out multiple reasoning chains hierarchically and explore the space with Monte-Carlo Tree Search [79]. The success of these methods depends on how the different reasoning chains are evaluated and can be achieved either through other language models [76] or through external tools, e.g. [77]. Tool usage in reasoning is explored next.
**Verifiers and tool usage.**Another avenue for boosting the performance of LLMs is by allowing tool usage [80, 81] either during the reasoning phase [82], or to verify intermediate reasoning steps [77] and solutions [22]. Verifiers and tools are compatible both with training-time and test-time methods. Since each of the
problems in TPBench has an auto-verifier, one could consider giving the LLM under evaluation access to the auto-verifier to test if, by using it, it can achieve better results.
**6. Discussion**
We developed the dataset TPBench to test TP reasoning capabilities of AI models. The core of our work is a set of novel uncontaminated problems, to detect true reasoning rather than memorization. However, as we discussed, scientific reasoning is always based on existing works and methods, and there is no sharp transition between true reasoning and memorization (for example of logically equivalent problems, or logically similar problems with minor modifications). It is clear from our benchmark results that reasoning models vastly outperform non-reasoning models, and that these models are capable of some degree of reasoning. We note that our problems were not constructed to match a particular target error rate (o3-mini and DS R1 appeared after most problems were finalized), but rather to reflect real problems encountered by theoretical physicists at each career level. Our TP reasoning results are consistent with studies from more general benchmarks, and illustrate the speed of progress in AI. The most advanced models are able to solve some problems at graduate level, but are not yet capable of solving most research level problems. While advanced models demonstrate remarkable proficiency in algebraic and conceptual problem-solving, they struggle with structured logical reasoning and transparent step-by-step calculations, particularly in complex, research-level problems. Their reliance on literature recall without verification or referencing and their lack of consistency in detailed reasoning remain key limitations in their problem-solving capabilities. We discussed these shortcomings and summarized common failure modes.
Progress has been rapid, even during the creation of this data set. If models could solve level 5 research problems consistently, their impact on TP would be substantial. However, even then, AI models could not perform independent research without further developments. We now discuss some future directions related to our work, that could make LLMs more powerful for TP research.
**Updates to the TPBench data set and score board.We**will update the score board for novel SOTA models. Results will be published on the website of the data set tpbench.org. The website also contains additional model evaluation metrics, which assign a unified model score over all difficulties. We aim to add more problems to the data set in the future, both public and private problems. It would be particularly interesting to design more research problems which are clearly outside of the training data. This could be achieved by curating research problems specifically from the newest arxiv publications, before the current knowledge cutoff. We invite interested researchers to contribute new problems and collaborate on future TPBench updates (see website for details).
**Automatic problem scraping from publication archives.**To improve inference methods specifically for TP, for example by reinforcement learning of reasoning chains (e.g. Deepeek R1 [35]), it would be important to have a large collection of verifiable problems. If problems could be extracted automatically from publications, perhaps after a training data cutoff, this would allow generation of training data without human labor at industrial scale. An initial exploration of LLM-based problem extraction from papers has revealed that this is difficult in TP because calculations are often spread over the paper and it is not clear to the model what information is needed to state the problem and what the answer is. This is more obvious in mathematical papers that clearly mark theorems and proofs (e.g. with latex tags), however those are more difficult to auto-verify. Nevertheless, this is an exciting direction for future work, especially since large industry labs keep their training data for reasoning models private.
**Automatic verification for non-algebraic expressions.We**were somewhat constrained in our choice of problems by the criteria of auto-verifiability. Many TP results can be written in inequivalent ways, and models are not currently good at judging equivalence of expressions. Large collections of verifiable problems are also important for reinforcement learning-based training of reasoning models, see e.g. the recent DS R1 [35]. Generating stronger verifiers that work for a wider class of problems is a very interesting direction for future work, where theoretical and computational physics domain expertise is valuable. Some challenges were listed in section 2.3. We note that results in TP are often symbolic expressions, which are more suited for auto-verification than mathematical proofs (which need to be checked by proof assistants).
**Improving reasoning methods for TP.We**have reviewed methods to improve reasoning capabilities of LLMs in section 5.2. It is clear from our experiments that a significant gain could be obtained if tools such as`SymPy`or`Mathematica`would be used consistently to check symbolic calculations where this is possible. Few shot learning or fine-tuning could be used to improve models ability to call symbolic software packages.
However, many TP calculations require specific packages and do not come with a lot of training data. Further, the human TP research process involves reading publications, and looking up results or methods when needed. References are also used to spot mistakes in calculations by comparing to known published results where possible. While LLMs can parse literature with techniques such as RAG [83], to our knowledge this has not been demonstrated to lead to performance gains in mathematical reasoning. The fact that models cannot point to a specific source for mathematical statements lowers their trustworthiness. Finally, inference methods that provide more information about uncertainty in individual steps would be particularly beneficial for difficult TP problems. This would pave the way for trustworthy, automated TP research assistants that reliably solve some aspects of a problem, but then ask for help for the parts they are uncertain about.
**Diagrammatic and spatial reasoning.**Theoretical physicists like to reason using spatial diagrams such as Feynman diagrams or drawing integration contours. In principle, such diagrams can be encoded in some formal language and multi-modality for spatial reasoning may not be necessary. For example, some of our problem solutions include Feynman diagrams or integration contours encoded with the`TikZ`LaTeX library (e.g. figure 4). For some of our problems humans would have trouble reasoning through them without the ability to draw on some scratchpad. It would be interesting to see whether multi-modal language and spatial reasoning models could make models stronger. Visualizing the problem (e.g. ‘running an example in your head’) is a common strategy and could be particularly powerful for models to develop truly novel ideas.
**Training reasoning models on TPBench.While**we designed TPBench for the evaluation of the reasoning capabilities of LLMs, it would also be very interesting to curate a dataset for supervised fine-tuning or for reinforcement learning purposes. While we expect fine-tuning to increase the TP specific reasoning capabilities of LLMs, it is equally important to avoid data leakage to avoid problems that are later used for evaluation to seep into the training data. For this reason we choose not to publish all of our problems in TPBench at this time. Instead we encourage researchers who wish to have their models evaluated on TPBench to reach out to us.
**Open-ended research problems.**If models could solve well-posed problems such as the research problems in our collection reliably, this would speed up TP research projects considerably. However, a large part of research consists of arriving at well-posed problems, which are interesting to answer and can be answered. It could be possible to design more open-ended tasks, where the goal is to ‘derive interesting results’ based on some set of initial constraints or observations. The AI model could suggest assumptions to include or drop, design its own problem statements, and attempt to judge the importance of its results (develop ‘theoretical taste’). It would be exciting and challenging to set up such a more open-ended benchmark.
**Community efforts by the TP community.With**reasoning models being developed primarily by industry, usually with proprietary and closed data sets, it is important to consider how the open research community can contribute to AI driven TP reasoning. It now seems possible that AI models will be able to do significant theoretical research within a few years. The TP community should work towards the goal that such research remains open and accessible, rather than being performed exclusively at a few select industry labs. While pre-training may be financially inaccessible to publicly funded research, supervised fine-tuning, reinforcement learning, and algorithm development require more moderate resources. As an example, the community could build data sets for both TP reasoning training and benchmarking that are available to both the community and AI labs (with some data leakage control). These could also include examples of tool usage such as Mathematica. A large community-curated data set of verifiable TP problems would in particular allow supervised fine-tuning and Reinforcement Learning specifically for TP. Our data set is a first step in that direction. We hope that this work will contribute to engaging theoretical physicists in this exciting research direction.
**Data availability statement**
Some of the data we use is available here: https://tpbench.org/. The private data set needs to stay private to avoid leakage into pre-training data of future reasoning models. The data that support the findings of this study are available upon reasonable request from the authors.
**Acknowledgments**
We thank Kendrick Smith and Matthew Johnson for discussions. M M and D J H C acknowledge the support by the U.S. Department of Energy, Office of Science, Office of High Energy Physics under Award Number DE-SC0017647. MM also acknowledges the support by the National Science Foundation (NSF) under Grant Number 2307109 and the Wisconsin Alumni Research Foundation (WARF). F S is grateful for the support of the NSF under CCF2106707 and the Wisconsin Alumni Research Foundation (WARF).
**Appendix A. Summary of problem data**
For each problem we collect the following data.
**Appendix B. Prompts**
**B.1. Prompts to query problem solutions**We used two different system prompts to initialize the LLMs, as well as a unique user prompt to query individual solutions.
*Simple system prompt*Our simple system prompt only specifies the required output format and encourages complete calculations.
**System:**You are a mathematical problem-solving assistant specializing in TP. Input problems will be provided in LaTeX format, and you must provide your solutions in LaTeX format as well. Please provide detailed step-by-step solutions and clearly mark your final answer with ‘Final answer:’ at the end. When writing equations, ensure proper LaTeX formatting including appropriate equation environments and mathematical notation.
*Extended system prompt with CoT advise*Our extended system prompt includes additional problem solving advice inspired by Polya’s book ‘How to Solve It’. [18]. We have used this system prompt as our default. However, we did not find a systematic difference between these prompts as illustrated in table 6 for a subset of problems.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8s5TW_apdIMtVwsjOna-xh_yI5m4mfz435zN51SgmfEqWrqhAgX9aIPJl2-qNTNQxc55QCMTAM-KJQbXkorAM4ATlZC6YYXdj25qz-gW0Sdh3_ikqkACtb16FOgutK99rCW1GUVg=w612-h142-v0?authuser=0)

**Table 6.**Performance comparison for different system prompts, using the GPT-4o model, on a subset of problems.
*A B C D*avg@5 best@5
Difficulty level Ext Std Ext Std Ext Std Ext Std Ext Std Ext Std
1-Easy undergrad 20 23 3 1 2 1 0 0 0.72 0.76 0.8 0.8 2-Undergrad 22 17 1 0 2 8 0 0 0.88 0.68 1.0 1.0 3-Easy grad 8 10 3 3 14 12 0 0 0.16 0.24 0.4 0.6
**System:**You are a mathematical problem-solving assistant specializing in TP. Input problems will be provided in LaTeX format, and you must provide your solutions in LaTeX format as well. Please provide detailed step-by-step solutions and clearly mark your final answer with ‘Final answer:’ at the end. When writing equations, ensure proper LaTeX formatting including appropriate equation environments and mathematical notation. Please follow a structured and logical approach. Here are your key steps for solving any problem: 1. Understand the problem: - Identify the unknown, the given data, and the conditions. - Evaluate if the conditions are sufficient, redundant, or contradictory. - Break down and analyze the different parts of the condition. 2. Devise a plan: - Explore connections between the data and the unknown. - If necessary, consider auxiliary problems to bridge gaps. - Reflect on whether you have encountered similar problems or solutions before. - Look for related problems, theorems, or methods that might apply. - Consider simplifying or reformulating the problem to make it more accessible. - Use definitions and explore analogous, general, or special cases. 3. Carry out the plan: - Execute your solution step by step, ensuring each step is clear and logically valid. - Confirm the correctness of each step and justify your reasoning. For each problem, ensure clarity, logical rigor, and consistency. You may iterate to refine and improve your solution.
*User prompt*
**User:**Problem: problem[“problem_details”][“Problem Statement”]
IMPORTANT SOLUTION REQUIREMENTS: 1. You MUST FIRST solve this problem using mathematical reasoning and symbolic calculations: - Use proper mathematical notation and symbols - Arrive at a final symbolic mathematical expression
2. ONLY AFTER completing the mathematical solution: - Convert your final mathematical expression into Python code - The code must satisfy these requirements: problem[“problem_details”][“Answer Requirements”]
Code Format Requirements: 1. Your solution MUST include the final executable Python code as required by the ‘Answer Requirements’ 2. You MUST wrap the final Python code between````python`and`````tags 3. Ensure the code is complete and can run independently 4. The code should NOT contain ANY externally defined variables, including physical constants.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-8JkgTGsJccZPuNeVQ7Wb2y6ExTFhEfDCO8dCvHhuhBcJzw3_1Kqa2wnwrzHhQQK7Fvx9_Y5Fp3CkD8xU2TDWmcWtAESrhNtjHBUKwIes14YmPZQkP1UX4DEXjp-f1iZh2YwpjfQ=w612-h445-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_8Xk6JDgVD9cV-Mrycj870256cKKapgPiCvkIjeAsDAdfwfcrAV7EP69_R45UI7_eSKkTvGumIaN0gkddzzShuEGosIKy2x3jGUlt77xQIiN3v8eruepglNoCq9yKqa1992HsE=w612-h355-v0?authuser=0)

**B.2. Prompts to query grading of solutions***System prompt*
**System:**You are a grader for machine learningmodel solutions of TP problems. I will provide you with a correct expert solution to the problem for your reference, and a model solution for you to grade. Grade solutions using*A/B/C/D*grades where:*A*= Excellent: The solution is mathematically equivalent to the expert solution, even if the symbolic expression differs (e.g. terms are arranged differently). The solution includes all necessary steps and the reasoning in each step is correct. Different but valid solution methods are acceptable.*B*= Good with minor issues: Generally correct solution with small errors such as: arithmetic mistakes that do not affect the main approach, missing intermediate steps, or minor notation issues. The problem was correctly understood and the reasoning of the solution is generally correct.*C*= Significant issues but partially correct: Shows basic understanding but has major flaws such as: incorrect application of formulas, missing crucial steps, or computational errors that lead to wrong final answer. The approach has some merit despite errors.*D*= Incorrect or major issues: Fundamentally flawed approach, completely incorrect calculations, or missing essential components. Shows little to no understanding of themathematical concepts involved. When comparing final answers, verify that the equations or expressions are mathematically equivalent (e.g.*2x+*2 is equivalent to*2(x+*1)). Always format your notes using LaTeXnotation formathematical expressions. Provide evaluation in compact JSON format with only ‘grade’ and ‘notes’ fields. Format all mathematical expressions in your notes using LaTeX notation (e.g. $x`̂2$,`$*\frac{1}{2}$, $\sqrt{x}$).*
*User prompt*
**User:**Compare the following model solution detailed steps with the expert solution, along with the code verification result which check the equivalence of 2 expression numerically, and evaluate its correctness. Expert Solution:*{expert_solution}*Model Solution*{model_solution}*Code Verification result:*{code_verification_result}*Format your response as JSON with the following structure:*{*“grade”:*“A/B/C/D”,*“notes”: “your notes here with LaTeX math notation”*}*
**Appendix C. Public problems and solutions**
We list ten public sample problems along with their solutions. AI model results for these problems are available on the dataset website tpbench.org. Table 7 summarizes the performance of different AI models on these problems, covering a range of topics and difficulty levels from Level 1 (L1) to Level 5 (L5). The scores indicate the average accuracy of the 5 attempts of each model.
**C.1. Level 5—one-pole problem***Problem statement*Consider the conformally coupled scalar field*ϕ*
*L=*1
2
[*gµν∂µϕ∂νϕ−*
(*m2−*1
6*R*
)*ϕ2*]
(3)
in curved spacetime
*ds2*=*a2 (η)*(*dη2− |d⃗x|2*
) where the Ricci scalar is
*R=−6a ′ ′ (η)*
*a(η)*(4)
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8X-wsgaw04fglyfsAaJUPMgVTQPI6Z0CC8MUdTYFZpGeronpo-pkNk5wq-c2FBtQrTkuKFK7havz113lxU-K5HEULT8cPYJhT7f7WSXQCJUrwQns8wjIA54G40icq9-ISOhx6Tjw=w612-h340-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8lDEM8_O_qbgq_i3WouPWG0lz8bO5bUwAZtmZW5GqX39x-1KRK-8FQvGyuu78nuGHX8tgdiXhX3okL2SNWVOGbwioL01Jp94fjujxPm4LrhDgIXR_pps9zFSEUlS5q7oaFG-qdlQ=w612-h216-v0?authuser=0)

**Table 7.Model**average scores by problem.
Problem ID Llama-70B GPT-4o R1 o1 o3-mini
Boosted parabolic trajectory (L1) 0.60 1.00 1.00 1.00 1.00 Blackbody in*d*dimensions (L1) 0.20 0.40 1.00 1.00 1.00 A 3-State QM Problem (L2) 0.40 0.80 1.00 1.00 1.00 Dark matter capture as a function of time (L2) 0.60 1.00 1.00 1.00 1.00 Slow-roll inflation (L3) 0.00 0.00 1.00 1.00 1.00 Scalar particle scattering (L3) 0.00 0.40 0.80 0.40 0.40 SHO vacuum entanglement (L4) 0.00 0.00 0.80 0.00 1.00 SUSY-symmetry (L4) 0.00 0.00 0.00 0.00 0.00 Bias of a sampled halo field (L5) 0.00 0.00 0.60 1.00 0.80 One-pole problem (L5) 0.00 0.00 0.00 0.00 0.00
and*a*satisfies the differential equation
d
*dt lna=Θ(te − t)HI +Θ(t− te)*
*HI*
1+ 3*2HI (t− te)*
(5)
with*te*a finite positive number, theΘ function having the steplike behavior
*Θ(t− te)≡*
{ 1*t⩾ te*
0 otherwise*,*(6)
and*t*being the comoving proper time related to*η*through
*t= te*+
ˆ*η*
*ηe*
*a(y)dy.*(7)
The boundary condition for the differential equation (in comoving proper time) is*a|t=te*=*ae.*In the limit that*k/(aeHI)→∞,*using the steepest descent approximation starting from the dominant
pole*η̃*(with*ℜη̃ >*0) of the integrand factor*ω ′ k(η)/(2ωk(η)),*compute the Bogoliubov coefficient
magnitude*|β(k)|*approximated as
*|β (k) | ≈*∣∣∣∣ˆ*∞*
*−∞ dη*
*ω ′ k (η)*
*2ωk (η) e−2i*
´*η ηe*
*dη ′ωk(η ′)*∣∣∣∣ (8)
for particle production where the dispersion relationship given by
*ω2k (η)*=*k2+m2a2 (η)*(9)
with*0<m≲HI.*Use a one pole approximation which dominates in this limit.
*Answer requirements*Provide the answer in the form of the`verbatim`code. Implement the following function.
`def abs_beta(k:float, a_e:float, m:float, H_I:float)``->``float: pass`
*Comments about the problem This is an example of a difficult problem from QFT in curved spacetime, dealing with gravitational particle production, that appears out of reach of current models. This is part of a published research work and the solution, without steps explained, is given in a footnote of [30], but would be difficult to locate (in fact we tried, without success, with OpenAI’s Deep Research).*
*Solution*To find the pole of*ω ′*
*k(η)/ωk(η),*we need*a(η)*from the given differential equation
*dlna*
*dt =Θ(te − t)HI +Θ(t− te)*
*HI*
1+ 3*2HI (t− te)*
*.*(10)
Integrating from time*t= te,*we find
ln*a*
*ae*=
ˆ*t*
*te*
*dT HI*
1+ 3*2HI (T− te)*
(11)
= 2
3 ln
[ 1+
3
2*HI (T− te)*
*]t te*
(12)
= 2
3 ln
[ 1+
3
2*HI (t− te)*
] (13)
for*t⩾ te.*In other words, this scale factor
*a*
*ae*=
[ 1+
3
2*HI (t− te)*
*]2/3*(14)
behaves as a typical coherent oscillations spacetime minus the oscillatory effects. Hence, note that for*t≫ te,*the scale factor can be approximated as
*a(η)≈ c1η*2 (15)
for*η≫ ηe*(where*ηe*is the corresponding conformal time for*te)*where we see by matching
ˆ*η*
*ηi*
*a(η)dη*=*t− ti*(16)
with*ηi ≫ ηe*and*ti ≫ te,*we can write
1
3*c1η*
3*≈ t*(17)
for times much larger than*ηi.*This means that at time*ηi ≫ ηe,*we have
*c1 ≈*2
*H(ηi)η*3*i*
(18)
(where the Hubble expansion rate is*H(η)*=*a ′(η)/a2(η))*which gives
*a(η)≈ 2η2*
*H(ηi)η*3*i*
(19)
for*η > ηi*where the choice of*ηi*controls the approximation error proportional to positive power of*ηe/ηi.*Since*ηi ≫ ηe >*0, we can approximate*η=*0 to be equivalent to*η− ηi →−∞.*In other words, when we analytically continue and consider the poles of the integrand, we will consider only the region with*ℜη >*0.
Next, note the pole of
*ω ′*
*2ω*=
*m2∂ηa2*
*4(k2+m2a2)*(20)
is at*η̃*defined by
*k2 =−m2a2 (η̃)*(21)
which means
*η̃*=
√*H(ηi)η*
3*i*
2
(*−k2*
*m2*
*)1/4*=*ηi*
√ 1
*a(ηi)*
(*−k2*
*m2*
*)1/4*=*ηie*
*i(2l+1)π/4*
√*k/a(ηi)√*
*m*(22)
where*l*is an integer. We see that*ℜη̃≫ ηi*for*k/a(ηe)≫ k/a(ηi)≫m.*We also see that*l ∈ {1,2}*have negative*ℜη̃*which are in the region that we excised with the*η− ηi →−∞*discussed above. That means we can consider either*l ∈ {3,4}.*We will see below that one of these poles is irrelevant.
**Figure 4.**The original contour in blue is deformed into the orange contour in the lower half complex plane of*η.*The large radius arcs have vanishing contributions, and one-pole approximation has been taken. The upper green and purple boundaries correspond to where integrations over any arcs extended beyond this boundary would not converge. The dashed horizontal curve is parallel to the real axis. The red squiggly line is the branch cut*at−5π/12.*
Equation (8) tells us that
*|β (η)|=*∣∣∣∣ˆ*∞*
*−∞ dη*
*ω ′ k (η)*
*2ωk (η) e−2i*
´*η ηe dη ′ωk(η ′)*
∣∣∣∣ =
∣∣∣∣ˆ*∞*
*−∞ dη*
*ω ′ k (η)*
*2ωk (η)*e*−2i*´*η ηi dη ′ωk(η ′)e−2i*
´*ηi ηe dη ′ωk(η ′)*
∣∣∣∣ =
∣∣∣∣ˆ*∞*
*−∞ dη*
*ω ′ k (η)*
*2ωk (η)*e*−2i*´*η ηi dη ′ωk(η ′)*
∣∣∣∣*.*(23)
With the steepest descent technique starting from the pole of*ω ′ k/ωk,*we write after analytically continuing*η*
*|β|=*∣∣∣∣ˆ*∞*
*−∞ dη*
*ω ′ k (η)*
*2ωk (η)*e*−2i*
[´*η̃ ηi dη ′ωk(η ′)+*
´*η η̃ dη ′ωk(η ′)*
]∣∣∣∣ =*∣∣∣e−2i´ η̃ηi dη ′ωk(η ′)v*
∣∣∣ (24)
where*η̃*is the pole of*ω ′ k(η)/ωk(η)*and*v*is the part obtained from the steepest descent. The factor in the
integrand of equation (8) is therefore
*ω ′*
*2ω ≈*1
*4(η− η̃)*(25)
which implies*v*in equation (24) is
*v=*
ˆ*∞*
*−∞*
*dη*
*4(η− η̃) e−*
4 3*im*
*√ C ′(η̃)(η−η̃)3/2*(26)
where
*C(η)≡ a2 (η) .*(27)
Deforming the integration contour as shown in figure 4 allows us to rewrite this as
*v=*
ˆ*C*
*dη*
*4(η− η̃) e−*
4 3*im*
*√ C ′(η̃)(η−η̃)3/2*(28)
where the*C*is the orange part of the contour in the lower half plane. To define the contour, one must understand the complex values of*C ′(η̃).*To this end, let
*−*i √
*C ′ (η̃)*=*U+ iW*(29)
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9RUEIFFwWL0BFOtZvSBX-xyWgBXouCOOeqDJkYAV9o21k1rYQEXhiTTfxprdESUksTISGf0jfeeGvA2PrtoTgzmtXnMtbqwP1-vqFpizXvEC80oMwlp9dZ0EjANiHPUbZy5iO5=w611-h343-v0?authuser=0)

where the imaginary part generically is nonvanishing. The branch points are given by equations (22) which gives
*C ′ (η̃)*=*4a2 (ηi)*
*ηi*e 3 4*i(2l+1)π*
(*k/a(ηi)*
*m*
*)3/2*(30)
which says
*U+ iW= 2a(ηi)√*
*ηi*e 1 8*i(6l−1)π*
(*k/a(ηi)*
*m*
*)3/4*=*a3/2 (ηi)*
√*2H(ηi)e*
1 8*i(6l−1)π*
(*k/a(ηi)*
*m*
*)3/4 .*(31)
To deform the contour, we need regions where the arcs with large radius does not contribute to the integral. Note that if we define*δ ≡ η− η̃*=*Reiθ,*we have
*δ3/2*=*R3/2ei3θ/2*=*R3/2*( cos
*3θ*
2 + i sin
*3θ*
2
) (32)
making the exponent in*v*
*−*4
3*im*√
*C ′ (η̃)(η− η̃) 3/2*
= 4
3*mR3/2 (U+ iW)*
( cos
*3θ*
2 + i sin
*3θ*
2
) (33)
which is damped only if
*Ucos(3θ/2)−W sin(3θ/2)< 0.*(34)
For the case of equation (21), we need
cos*[π*8*(6l−*1)
]*cos(3θ/2)−*sin
*[π*8*(6l−*1)
]*sin(3θ/2)<*0 (35)
for one choice of*l.*For the choice of*l=*3, we can choose the arc regions to be*θ ∈ [−5π12 , π*4 ] and another arc
region to be*θ ∈*[*11π12 , 19π*12 ] with a branch cut*at−5π/12.*
Choosing*l=*3, we find the steepest descent contour shown in orange in figure 4. The left contour is*5π/4*and the right contour is*at−π/12,*along which
*−4*3*im*√
*C ′ (η̃)(η− η̃) 3/2*
*=−4*3*mR3/2a3/2 (ηi)*
√*2H(ηi)*
(*k/a(ηi)*
*m*
*)3/4*gives a damped exponential in equation (26). Hence, the integral is
*v=*1
4
ˆ*ϵ*
*∞*
*dR*
*R*e*−*4*3mR3/2a3/2(ηi)*
*√ 2He*
(*k/a(ηi)*
*m*
*)3/4*
+ 1
4
ˆ*∞*
*ϵ*
*dR*
*R*e*−*4*3mR3/2a3/2(ηi)*
*√ 2He*
(*k/a(ηi)*
*m*
*)3/4*
+ 1
4
ˆ*−π/12*
*5π/4 idθ*exp
[*−4*3*im*√
*C ′ (η̃)*(*ϵeiθ )3/2]*
=*i*
4
[*−π*12
*− 15π*
12
] =
*−iπ*
3 (36)
where in the first line we have introduced a regulator*ϵ→*0. The final piece in equation (24) is
*I=*e*−2i*´*η̃ ηi dη ′ωk(η ′).*(37)
Use the expansion
*I=*e*−2i*´*η̃ ηi dη ′ωk(η ′)*
=*exp(−2i*[Φ+*J])*(38)
where Φ is real and*J*is purely imaginary. We take the path to be along the real axis until*η*=*ℜη̃*and then integrate in the imaginary*η*direction:
*J= iℑ*ˆ*ℜη̃+iℑη̃*
*ℜη̃*
*dη ′ωk (η ′) .*(39)
This gives
*J≈−i*2
3
*√ 2π*
*Γ(5/4)*
*Γ(3/4)*
*(k/a(ηi)) 3/2*
*H(ηi) √ m*
*.*(40)
Now, note from equation (14), we can compute
1
*a3/2e*
= 1
*a3/2 (ηi)*
[ 1+
3
2*HI (ti − te)*
]*≈*1
*a3/2 (ηi)*
3
2*HIti*
*≈*1
*a3/2 (ηi)*
*HI*
*H(ηi)*(41)
where we used equation (10). Equation (24) then becomes
*|β| ≈ π*
3 exp
(*−4*3
*√ 2π*
*Γ(5/4)*
*Γ(3/4)*
*(k/ae) 3/2*
*HI √ m*
)*.*(42)
**C.2. Level 5—bias of a sampled halo field***Problem statement*In cosmology, large-scale cosmological dark-matter halo fields are biased tracers of the underlying Gaussian matter density*δm.*Assume we have a sample*δm.*We simulate a halo number density field by taking**n(x)**=*n̄max(0,1+***bδm(x)),**where bare number density*n̄*and bare bias*b*are specified constants. What is the bias of the sampled halo field? Derive an equation to evaluate the bias which depends on the bare bias and the variance in each pixel.
*Answer requirements*Provide the answer in the form of the`verbatim`code. Implement the following function.
*Comments about the problem This is an example of a cosmology research problem that is being solved correctly by advanced reasoning models. This may be because the calculation is similar to existing calculations in the literature. However, this is a genuine research problem, which we solved independently, for an upcoming cosmology publication. The problem requires to retrieve some background knowledge, such as the definition of the matter power spectrum in cosmology.*
*Solution*The solution to this question involves some domain knowledge, parts of which were given in the problem’s statement, some approximations sourced by the domain knowledge, and some mathematical calculations. The domain knowledge is very basic and should be known to anyone in the field. Approximations are intuitive and also, mostly, inspired by the domain knowledge. Following Polya, we can organize it as follows:
**Understand the problem.**The number density of halos**nh(x)**is defined as
*Nh*=
ˆ*V nh***(x)dx.**(43)
The overdensity is defined as
*δh***(x)**=*nh***(x)−⟨nh (x)⟩**
*⟨nh***(x)⟩***.*(44)
Linear bias is defined in terms of Fourier-transformed quantities:
*δh***(k)**=*bδm***(k)***.*(45)
This is an approximation that holds on sufficiently large scales (small*k).***δm(k)**and**δh(k)**are Gaussian random fields with zero mean and their variance depends only on the magnitude of the wave-vector*k=***|k|:**
*δm ∼N (0,Pmm (k)) , δh ∼N (0,Phh (k)) .*(46)
The quantity*P(k)*is called the power spectrum and is defined as
*⟨δ***(k)δ****(k****′)⟩=***(2π)3 δD***(k+ k****′)P(k)***.*(47)
It immediately follows that
*Phh (k)*=*b2Pmm (k) .*(48)
We are given the expression in real space. In real space, the quantity**δm(x)**is also a Gaussian random field:
*δm***(x)∼N***(0, ξm) , δh***(x)∼N***(0, ξh) .*(49)
Quantity*ξ*is called a two-point (real-space) correlation function and is defined as
*⟨δ***(x)δ****(x****′)⟩=***ξ***(|x−****x****′|)***.*(50)
This quantity is sufficiently small when**|x−****x****′|***≫*1. We are asked to find what is the expression for*b*in the equation*δh(k)*=**bδm(k),**given the real-space expression for the number density**nh(x)**in terms of real-space sample of**δm(x).**
**Devise a plan.**The key point to solve this problem should be that real-space correlation function for halos*ξh*should also be equal to*b2ξm.*We want to calculate that correlation function. It should be expressed in terms of**⟨n(x)⟩**and**⟨nh(x)nh(x ′)⟩.**We expect to be able to calculate these expectations since they are the expectations of functions of the Gaussian random variables. We are given the pixel variance*σ.*How does it connect to the other quantities we know? In principle, that’s also the part of domain knowledge but it also can be deducted from the definitions already given. A discretized version of the correlation function is
*ξij*=**⟨δxiδxj⟩.**(51)
When*i= j,*it becomes the pixel variance*σ. Aside, we could have given instead of σ, the quantity Pmm(k), that is a common description of a cosmological dark-matter field. In that case, from the definitions of ξ(r)*and*Pmm(k), we could have deduced that σ*= 1
*V*
∑*kPmm(k).*Then we pick the ensemble of all the pixels at given
fixed large distance*r=***|xi− xj|.**The key is to recognize that it is fully described by a correlated bivariate Gaussian distribution. (
*δmi , δ m j*
)*∼N (0,Σ)*(52)
with a covariance
Σ=
(*σ2 ξmr ξmr σ2*
)*.*(53)
In general, the integrals from the expectation values are cumbersome, but we should expect some simplifications from the fact that*ξ*is small and we can Taylor-expand the pdf.
**Carry out the plan.**It’s more convenient to define*δ̂i*=*δmi /σ*and*ξ̂*=*ξmr /σ*2, and*ϕ2—a*correlated bivariate
Gaussian pdf—then
(*δ̂i, δ̂j*
)*∼*e
*−*1*2(1−ξ̂2) [δ̂*
2*i +δ̂2j −2ξ̂δ̂iδ̂j]*
*2π*√*1− ξ̂2*
*≡ ϕ2*
(*δ̂i, δ̂j|ξ̂*
)*.*(54)
We note that
*ξnr*=*⟨ninj⟩ ⟨n⟩2*
*− 1.*(55)
The quantity*⟨n⟩*is the actual mean number density:
*n̄ ′*=*⟨n⟩= ⟨ni ⟩=*
ˆ*nloc (δi,b, n̄)ϕ2*
(*δ̂i, δ̂j|ξ̂*
)*dδ̂idδ̂j*=
ˆ*nloci ϕ1*
(*δ̂i*
)*dδ̂i.*
Here,*ϕ1—is*a standard normal pdf. It is expected that it is not dependent on the correlation*ξ̂,*but only on*b*and*σ,*just as the marginal of 2D correlated Gaussian distribution is 1D Gaussian that’s not dependent on the cross-correlation. To the linear order in*ξ̂,*
*ϕ2*
(*x,y|ξ̂*
)*≈ ϕ1 (x)ϕ1 (y)*
( 1+*ξ̂xy*
)*.*(56)
So that the two-point function neatly factorizes:
*⟨ninj⟩=*ˆ
*nloc (δi,b, n̄)n*loc (*δj,b, n̄*
)*ϕ2*
(*δ̂i, δ̂j|ξ̂*
)*dδ̂idδ̂j*
*≈*ˆ
*nloci ϕ1*
(*δ̂i*
)*dδ̂i*
ˆ*nlocj ϕ1*
(*δ̂j*
)*dδ̂j*+*ξ̂*
ˆ*nloci ϕ1*
(*δ̂i*
)*δ̂idδ̂i*
ˆ*nlocj ϕ1*
(*δ̂j*
)*δ̂jdδ̂j*
*≡ ⟨n⟩2+ ξ̂⟨nδ̂⟩2.*(57)
Substituting the results for*⟨n⟩*and*⟨ninj⟩*in the equation for*ξnr*, we can read off the bias:
*b ′2*=
*ξnr*
*σ2ξ̂*=
*⟨nδ̂⟩2*
*σ2⟨n⟩2 .*(58)
All that is left is to calculate the expectations. One can evaluate for*b⩾*0
*⟨n⟩=*ˆ
*nloci ϕ1*
(*δ̂i*
)*dδ̂i*=
ˆ*n̄max(0,1+ bσx)ϕ1 (x)dx*
=*n̄*
ˆ*+∞*
*−*1*bσ*
(1+*bσx)ϕ1 (x)dx= n̄*
[ Φ1
( 1
*bσ*
) +*bσϕ1*
( 1
*bσ*
)]*.*(59)
For*b<*0 it is, however,
*⟨n⟩= n̄*
ˆ + 1*|b|σ*
*−∞ (1− |b|σx)ϕ1 (x)dx*
=*n̄*
[ Φ1
( 1
*|b|σ*
) +*|b|σϕ1*
( 1
*|b|σ*
)]*.*(60)
So we conclude that the latter expression is valid for all*b.*Similarly, one can show that
*⟨nδ̂⟩= n̄*
ˆ*max(0,1+ bσx)xϕ1 (x)dx= n̄bσΦ1*
( 1
*|b|σ*
) (61)
where*Φ1(x)*= ´*x −∞ϕ1(x)dx—normal*cdf. Finally, one can get
*b ′*=
*bΦ1*(
1*|b|σ*
) Φ1
( 1
*|b|σ*
) +*|b|σϕ1*
( 1
*|b|σ*
)*.*(62)
Note: We also accept solutions as correct if they omit the*| |*around the bias, since halo bias is usually positive.
**C.3. Level 4—SHO vacuum entanglement***Problem statement*Consider a coupled simple harmonic oscillator governed by the Hamiltonian
*H=*2∑
*i=1*
1
2
(*p2i m*
+*kx2i*
) +*g*
*(x1− x2)*2
2*.*(63)
If the ground state is*|Ω⟩*and the operator*ρ̂*is the vacuum density matrix partially traced over the*|w⟩x2*components (satisfying*x̂2|w⟩x2*=*w|w⟩x2),*i.e.
*ρ̂≡*ˆ*dx ′ ′1*
ˆ*dx ′1*
ˆ*dw(|x ′ ′1 ⟩x1 x1⟨x ′ ′1 | ⊗ x2⟨w|)(|Ω⟩⟨Ω|)(|x ′1⟩x1 ⊗ |w⟩x2 x1⟨x ′1|)*(64)
which is an operator acting on a reduced Hilbert space, compute
*S≡−Trx1 [ρ̂*ln*ρ̂]*(65)
which involves the trace over*x1*states.
*Answer requirements*Provide the answer in the form of the`verbatim`code. Implement the following function
`def entropy(k:float,g:float,m:float)->float: pass`
*Comments about the problem This problem, whose solution can be found in [84] (with less detailed reasoning steps), has been rephrased in a pedagogical manner for graduate-level physics courses. It is a well-known question in quantum entanglement research, and the best performing LLMs are capable of solving it accurately, perhaps at least partially due to memorization.*
*Solution*Diagonalize the original Hamiltonian
*H= (x1 x2 p1 p2)*
*k+g*2*− g*
2
*− g*2
*k+g*2
1*2m*
1*2m*
 
*x1 x2 p1 p2*
*.*(66)
One easily finds
*x1*=*y1+ y2√*
2 (67)
*x2*=*y1− y2√*
2 (68)
diagonalizes the Hamiltonian such that in the*(y1,y2,q1 ≡mẏ1,q2 ≡mẏ2)*basis, it is
*H= (y1 y2 q1 q2)*
*k*2 0 0*k*
2 +*g*1*2m*
1*2m*
 
*y1 y2 q1 q2*
*.*(69)
The ladder operators are
*aj*=*1√*2
(*√ mωjyj*+
*i √ mωj*
*qj*
) (70)
*ω21*=*k*
*m ω22*=
*k+ 2g*
*m*(71)
which allows one to rewrite the Hamiltonian as
*H=*2∑
*j=1*
*a†j ajωj*+*ω1+ω2*2
*.*(72)
In this basis, we denote the ground state as
*a1|00⟩⃗ny*= 0=*a2|00⟩⃗ny .*(73)
Hence we have found*|Ω⟩= |00⟩⃗ny*. We know that the wave function in the*y⃗*coordinates is the product of well known simple harmonic oscillator solutions:
*⟨y ′1,y ′2|00⟩⃗ny*= 1
*(π b21) 1/4*exp
[*−(y ′1)*
2
*2b21*
] 1
*(π b22) 1/4*exp
[*−(y ′2)*
2
*2b22*
] (74)
where
*bn ≡*1
*√ mωn*
(75)
making this a convenient basis to work with. Note
*ŷ1*(*|a⟩x1 ⊗ |b⟩x2*
) =
ˆ*dy ′1dy*
*′ 2ŷ1|y ′1y ′2⟩⟨y ′1y ′2|*
(*|a⟩x1 ⊗ |b⟩x2*
) =
ˆ*dy ′1dy*
*′ 2y*
*′ 1|y ′1y ′2⟩⟨y ′1y ′2|*
(*|a⟩x1 ⊗ |b⟩x2*
) =
ˆ*dx ′1dx*
*′ 2y*
*′*1
(*|x ′1⟩x1 ⊗ |x ′2⟩x2*
) (*x1⟨x ′1| ⊗ x2⟨x ′2|)*
(*|a⟩x1 ⊗ |b⟩x2*
) =
*a+ b√*2
(*|a⟩x1 ⊗ |b⟩x2*
) (76)
where we used the completeness of the basis, equations (67) and (68), and the usual delta function normalization of the position basis. This and a similar relation for*ŷ2*imply
*|a⟩x1 ⊗ |b⟩x2*=*∣∣∣∣a+ b√*
2*, a− b√*2
〉*.*(77)
This means
*n⃗y⟨00|(|x ′ 1⟩x1 ⊗ |w⟩x2)*=*n⃗y*
〈 00
*∣∣∣∣x ′1+w√*2*, x ′1−w√*2
〉
= 1
*(π b21) 1/4*exp
*−*(
*x ′ 1+w√*2
)2*2b21*
 1
*(π b22) 1/4*exp
*−*(
*x ′ 1−w√*2
)2*2b22*
*.*(78)
The partial trace is defined through the following contraction of (2, 2) tensor to a (1, 1) tensor:
*ρ̂=*
ˆ*dx ′ ′1*
ˆ*dx ′1*
ˆ*dw(|x ′ ′1 ⟩x1 x1⟨x ′ ′1 | ⊗ x2⟨w|)*
(*|00⟩⃗ny n⃗y⟨00|*
)*(|x ′1⟩x1 ⊗ |w⟩x2 x1⟨x ′1|)*
=
ˆ*dx ′ ′1*
ˆ*dx ′1*
ˆ*dw|x ′ ′1 ⟩x1 x1⟨x ′1|*
1
*(π b21) 1/4*exp
*−*(
*x ′ ′*1*+w√*2
)2*2b21*
 1
*(π b22) 1/4*exp
*−*(
*x ′ ′*1*−w√*2
)2*2b22*
*×*1
*(π b21) 1/4*exp
*−*(
*x ′ 1+w√*2
)2*2b21*
 1
*(π b22) 1/4*exp
*−*(
*x ′ 1−w√*2
)2*2b22*
*.*(79)
Integrate over*w,*we find
*ρ̂=*
ˆ*dx ′ ′1*
ˆ*dx ′1|x ′ ′1 ⟩x1 x1⟨x ′1|*
1
*(π b21) 1/2*
1
*(π b22) 1/2*exp [*−m*
4*(ω1+ω2)*
(*[x ′1]*
2 +*[x ′ ′1*]
2 )]
*× √ 2π√*
*m [ω1+ω2]*exp
*(√*
*ω2√ ω1*
*− √ ω1√ ω2*
)2*(x ′1+ x ′ ′1*)
2
8*1m*
( 1*ω1*
+ 1*ω2*
) 
=
ˆ*dx ′ ′1*
ˆ*dx ′1|x ′ ′1 ⟩x1 x1⟨x ′1|*
1
*(π b21) 1/2*
1
*(π b22) 1/2*
*× √ 2π√*
*m [ω1+ω2]*exp
*m(ω2−ω1)*2*2x ′1x*
*′ ′*1*−m*
[*8ω1ω2+(ω1−ω2)*
2 ](
*[x ′1]*2 +*[x ′ ′1*]
2 )
*8(ω1+ω2)*
*.*(80)
Next, to identify the matrix, use
*m(ω2−ω1)*2*2x ′1x*
*′ ′*1*−m*
[*8ω1ω2+(ω1−ω2)*
2 ](
*[x ′1]*2 +*[x ′ ′1*]
2 )
*8(ω1+ω2)*
*=−*1
*2b2*
[(*[x ′1]*
2 +*[x ′ ′1*]
2 )*−*2*(ω2−ω1)*
2
*γ x ′1x*
*′ ′*1
] (81)
*γ ≡ 8ω1ω2+(ω1−ω2)*2 (82)
1
*2b2 ≡ mγ*
*8(ω1+ω2)*(83)
*b=*2
√√√√*ω1+ω2*
*m*[*8ω1ω2+(ω1−ω2)*
2 ] (84)
to write
*ρ̂=*
ˆ*dx ′ ′1*
ˆ*dx ′1|x ′ ′1 ⟩x1 x1⟨x ′1|*
1
*(π b21) 1/2*
1
*(π b22) 1/2*
*× √ 2π√*
*m [ω1+ω2]*exp
[*−*1
*2b2*
(*[x ′1]*
2 +*[x ′ ′1*]
2 )] exp
(*(ω2−ω1)*
2
*γb2 x ′1x*
*′ ′*1
)*.*(85)
Change basis to energy with a new effective frequency
*b3*= 1
*√ mω3*
(86)
*ρ̂=*∑*nv*
*|v⟩⟨v|ρ̂|n⟩⟨n|*(87)
*⟨v|ρ̂|n⟩=*ˆ*dx ′ ′1*
ˆ*dx ′1⟨v|x ′ ′1 ⟩x1 x1⟨x ′1|n⟩*
1
*(π b21) 1/2*
1
*(π b22) 1/2*
*× √ 2π√*
*m [ω1+ω2]*exp
[*−*1
*2b2*
(*[x ′1]*
2 +*[x ′ ′1*]
2 )] exp
(*(ω2−ω1)*
2
*γb2 x ′1x*
*′ ′*1
) (88)
where
*⟨x ′1|n⟩=*1√
*n!b3 √ π2n*
e*−(x ′1*)
2
*2b23 Hn*
(*x ′1 b3*
) (89)
are the well known oscillator wave functions and*b3*still has to be chosen. One can show by carrying out the integrals that the matrix is diagonalized if
*b3*=*b(*
*1− b4*[*(ω2−ω1)*
2
*γb2*
*]2)1/4*=
1*√ mω1/41 ω*
*1/4*2
*.*(90)
This gives
*⟨v|ρ̂|n⟩= λnδvn*
where
*λn*=
*√ 2π√*
*m [ω1+ω2]*
1
*(π b21) 1/2*
1
*(π b22) 1/2*
*m11*
*b2 (ω2−ω1)*2
*γb2*
1+
√*1− b4*
[*(ω2−ω1)*
2
*γb2*
]2 
*n−1*
=*π √ m*
2*[ω1+ω2] 3/2*
1
*(π b21) 1/2*
1
*(π b22) 1/2*
*(ω2−ω1) 2(√*
*mω1/41 ω 1/4*2
)3(*b23 b2*+ 1
*)3/2**(ω2−ω1)*
2
*8ω1ω2+(ω1−ω2)*2
1+*b2*
*b23*
*n−1*
(91)
where we used
*m11*=*b3 (ω2−ω1)*
2
*γb2*
*√ 2π(*
1+
√*1− b4*
(*(ω2−ω1)*
2
*γb2*
*)2)3/2*
=*m(ω2−ω1)*
*2√2π*
*4(ω1+ω2)*( 1*b2*+
1*b23*
*)3/2*(92)
(*b3 b*
)2 =
1
*mω1/21 ω 1/2*2
1
4*ω1+ω2 m[8ω1ω2+(ω1−ω2)*
2]
= 1
*ω 1/2*1*ω*
*1/2*2
*8ω1ω2+(ω1−ω2)*2
*4(ω1+ω2) .*(93)
Simplify:
*λn*= 4*√ ω1ω2√*
*8ω1ω2+(ω1−ω2)*2 +*4ω1/21 ω*
*1/2*2*(ω1+ω2)*
(*(ω2−ω1)*
2
*8ω1ω2+(ω1−ω2)*2*+ω*
*1/2*1*ω*
*1/2*2*4(ω1+ω2)*
*)n*
= 4*√ ω1ω2(√*
*ω1+ √ ω2*)2 [
*(ω1−ω2) 2(√*
*ω1+ √ ω2*)4*]n .*(94)
Since we want to evaluate
*−Tr [ρ̂*ln*ρ̂] =−∂n*ln*trρ̂n|n=1*(95)
we compute
*lntrρn*= ln
*∞∑ j=0*
*λnj*
 = ln
∑*j*
 4*√ ω1ω2(√*
*ω1+ √ ω2*)2 [
*(ω1−ω2) 2(√*
*ω1+ √ ω2*)4*]jn*
=*n*ln
[ 4*√ ω1ω2(√*
*ω1+ √ ω2*)2 ] + ln
∑*j*
[*(ω1−ω2)*
*2(√ ω1+*
*√ ω2*)4*]nj*
=*n*ln
[ 4*√ ω1ω2(√*
*ω1+ √ ω2*)2 ]*−*ln
(*1−*
[*(ω1−ω2)*
*2(√ ω1+*
*√ ω2*)4*]n)*
*.*(96)
Hence, we arrive at
*S=−*
ln [
4*√ ω1ω2(√*
*ω1+ √ ω2*)2 ]*−*
[*(ω1−ω2)*
2
(*√ ω1+*
*√ ω2)*
4
] ln [
*(ω1−ω2)*2
(*√ ω1+*
*√ ω2)*
4
] (*1−*
[*(ω1−ω2)*
2
(*√ ω1+*
*√ ω2)*
4
]) 
=*−*ln
( 4*√ ω1ω2(√*
*ω1+ √ ω2*)2 )*−*
(*(ω2−ω1)*
2
4*√ ω1ω2*
*(√ ω1+*
*√ ω2*)2 ) ln
(*(ω2−ω1)*
*2(√ ω1+*
*√ ω2*)4 )
(97)
where
*ω1*=
√*k*
*m ω2*=
√*k+ 2g*
*m .*(98)
**C.4. Level 4—SUSY-symmetry***Problem statement*Consider the theory
*L= iξ̄σ̄µ∂µξ+ |∂ϕ|2− |F|2*(99)
where*ξ*is a 2-component Weyl spinor while*ϕ*and*F*are complex scalar fields. Suppose you want to make the following infinitesimal transformation a symmetry of this theory:
*δηξα*= i*√ 2σµ*
*αα̇η̄ α̇∂µϕ+*
*√ 2ηαF*(100)
*δη ξ̄β̇*= [ i*√ 2σµ*
*βα̇η̄ α̇∂µϕ+*
*√ 2ηβF*
*]† =−i*
*√*2 (*η̄α̇σµ∗*
*α̇β*
*)∗ ∂µϕ̄+*
*√ 2η̄β̇ F̄*
*=−i √ 2ηασµ*
*αβ̇ ∂µϕ̄+*
*√ 2η̄β̇ F̄*(101)
*δηF=*i*√ 2η̄α̇σ̄*
*µα̇α∂µξα*= i*√ 2η̄σ̄µ∂µξ*(102)
*δηF̄=−i √ 2(η̄σ̄µ∂µξ)*
*†*
*=−i √ 2(∂µξ)*
*† (σ̄µ)*
*† (η̄)*
*†*
*=−i √ 2∂µξ̄σ̄*
*µη*(103)
along with*δηϕ*and*(δηϕ) †*where*η*is a spacetime-independent infinitesimal fermionic parameter inducing
the transformation. Find the transformation rule*δηϕ*and*(δηϕ) †*for the action associated with*L*to remain
invariant.
*Answer requirements*Provide the answer in the form of the`verbatim`code. Implement the following function
*Comments about the problem This problem is situated in advanced QFT within the framework of supersymmetry (SUSY). It involves analyzing how bosonic and fermionic fields transform under an infinitesimal SUSY transformation and requires knowledge and careful application of Grassmann variables and the associated algebra. Such topics are typically encountered in advanced graduate-level physics courses. Note that the Hermiticity of σµ matrix convention as well as the metric convention of (1,−1,−1,−1) is implicit in the statement of the problem (the latter inherent in the kinetic minus the potential form of the Lagrangian).*
*Solution*Denoting the variation*(δηϕ)*
*†*as*δηϕ̄,*we write
*δηL= iδη ξ̄σ̄ µ∂µξ+ iξ̄σ̄*
*µ∂µδηξ+ ∂µδηϕ̄∂ µϕ+ ∂µϕ̄∂*
*µδηϕ− δηF̄F− F̄δηF*
= i [*−i*
*√ 2ησβ∂βϕ̄+*
*√ 2η̄F̄*]*σ̄µ∂µξ+ iξ̄σ̄*
*µ∂µ*
[ i*√ 2σβ η̄∂βϕ+*
*√ 2ηF*]
+*∂µδηϕ̄∂ µϕ+ ∂µϕ̄∂*
*µδηϕ−*[*−i*
*√ 2∂µξ̄σ̄*
*µη*]*F−*
*F̄*[ i*√ 2η̄σ̄µ∂µξ*
]*.*(104)
Integrating by parts, we find (denoting with equality an equivalence up to total derivative terms)
*δηL= √ 2ησβ∂βϕ̄σ̄*
*µ∂µξ+ ∂µξ̄σ̄ µ [√ 2σβ η̄∂βϕ−*
i*√ 2ηF*]
+*∂µδηϕ̄∂ µϕ+ ∂µϕ̄∂*
*µδηϕ+*i*√ 2∂µξ̄σ̄*
*µηF .*(105)
Integrate by parts the first two terms to eliminate the the*σ*matrices using the identity*σ̄µσν*+*σ̄νσµ*=*2gµν*:
*δηL= √*2 (*η∂µϕ̄∂*
*µξ+ ∂µξ̄η̄∂µϕ*) +*∂µδηϕ̄∂*
*µϕ+ ∂µϕ̄∂ µδηϕ*(106)
again denoting with equality an equivalence up to total derivative terms, and we are using the standard notation*ηξ ≡ ηαξα*and*ξ̄α̇η̄α̇ ≡ ξ̄η̄.*To make the remainder cancel, we solve
*√ 2η∂µϕ̄∂*
*µξ+ ∂µϕ̄∂ µδηϕ*= 0 (107)
yielding
*δηϕ =− √ 2ηξ, (δηϕ)*
*† =−*
*√ 2ξ̄η̄ .*(108)
**C.5. Level 3—slow-roll inflation***Problem statement*For the action
*S=*
ˆ*dta3 (t)*
{ 1
2*ϕ̇2−V0*exp
[*−*
√ 2
*q*
(*ϕ*
*MP*
)]} (109)
where*q*and*V0*are constants, derive and solve (integrate) the equation of motion for the field*ϕ*assuming slow-roll inflation and initial condition*ϕ(t=*0) =*ϕ0.*
*Answer requirements*Provide the answer in the form of the`verbatim`code. Implement the following function
*Comments about the problem This problem lies in the field of cosmology, particularly in inflationary cosmology, and involves studying the dynamics of a scalar field (inflaton) driving the accelerated expansion of the early Universe, before the ‘hot Big Bang’. It is typically encountered in specialized graduate-level courses in cosmology and requires familiarity with field theory in an expanding spacetime.*
*Solution*The equation of motion is
*ϕ̈+ 3Hϕ̇−*
√ 2
*q*
( 1
*MP*
)*V0*exp
[*−*
√ 2
*q*
(*ϕ*
*MP*
)] =*0.*(110)
For the slow-roll inflation, the following must hold:
*ϕ̈≪ 3Hϕ̇ .*(111)
Hence, we have
*3Hϕ̇=*
√ 2
*q*
( 1
*MP*
)*V0*exp
[*−*
√ 2
*q*
(*ϕ*
*MP*
)]*.*(112)
Slow-roll approximation also implies
*H2 ≈ V(ϕ)*
*3M2 P*
(113)
so we need to solve the following ODE:
3
*√√√√V0*exp [*−*√
2*q*
(*ϕ MP*
)]*3M2*
*P*
*dϕ*
*dt*=
√ 2
*q*
( 1
*MP*
)*V0*exp
[*−*
√ 2
*q*
(*ϕ*
*MP*
)] (114)
ˆ*dϕ√ V0*exp
[√ 1
*2q*
(*ϕ*
*MP*
)] =
√ 2
*3q t .*(115)
Performing the integration and solving for*ϕ(t)*we get
*1√ V0*
*MP*
√*2q*
( exp
[√ 1
*2q*
(*ϕ*
*MP*
)]*−*exp
[√ 1
*2q*
(*ϕ0 MP*
)]) =
√ 2
*3q t*(116)
*ϕ*= √*2qMP*ln
{ exp
[√ 1
*2q*
(*ϕ0 MP*
)] +
1
*MPq*
√*V0*3*t*
}*.*(117)
**C.6. Level 3—scalar particle scattering***Problem statement*Consider
*L=*
{ 2∑
*i=1*
[ 1
2*(∂µϕi)(∂*
*µϕi)− m2*
*i*
2*ϕiϕi*
]*− λ*
4*ϕ21ϕ*
2 2
} (118)
What is the differential cross section*dσ*dΩ for*ϕ1(⃗k1)ϕ1(−k⃗1)→ ϕ2(⃗k ′1)ϕ2(−k⃗ ′1)*in the CM frame accurate to
*O(λ2)?*Express your final answer in terms of Mandelstam variables.
*Answer requirements*Provide the answer in the form of the`verbatim`code. Implement the following function.
*Comments about the problem This is a question from QFT. It involves calculating the differential cross section for a process where two ϕ1 particles annihilate into two ϕ2 particles. Such problems are typically encountered in graduate-level particle physics courses and require familiarity with perturbative field theory and the use of Mandelstam variables to express scattering amplitudes.*
*Solution*The amplitude for this process is
*iM=−4iλ*4*=−iλ*(119)
In the CM frame, energy conservation gives
2 √*|⃗k1|2+m2*
1 = 2 √
*|⃗k ′1|2+m2*2 (120)
A standard formula for differential cross section gives
(*dσ*
dΩ
) CM
= 1
*64π2s*
*k ′1 k1 |M|2*
=*λ2*
*64π2s*
√*|⃗k1|2+(m2*
*1−m2*2)
*k1*(121)
Since in the CM frame, we know
*k1*= 1
2*√ s*
√*s2− 4m2*
*1s*(122)
(*dσ*
dΩ
) CM
= 2*√ s*
*64π2s*
√ 1
*4s [s2− 4m2*
*1s]*+*(m2 1−m2*
2)*λ2√*
*s2− 4m2 1s*
=*λ2*
*64π2s*
√*s2− 4m2*
*1s+ 4s(m*2*1−m2*
2)√*s2− 4m2*
*1s .*(123)
The final result is
(*dσ*
dΩ
) CM
=*λ2*
*64π2s*
√*s− 4m2*
2√*s− 4m2*
1
*.*(124)
**C.7. Level 2—dark matter capture as a function of time***Problem statement*Suppose*C*is the capture rate of dark matter in an astrophysical body. Let*CA*be the dark matter annihilation rate per effective volume. Then an approximate Boltzmann equation governing the number*N*of dark matter particles in the astrophysical body is
*dN*
*dt*=*C−CAN*
*2.*
If initially,*N(0)*= 0, what is*N(t)*as a function of time?
*Answer requirements*Provide the answer in the form of the`verbatim`code. Implement the following function.
`def``answer(C:``float,``C_A:``float,``t:``float)``->``float: pass`
*Comments about the problem This problem mainly belongs to astrophysics, specifically involving dark matter dynamics in celestial bodies. It is typically encountered in advanced undergraduate or graduate-level courses and requires knowledge of differential equations and kinetic theory. This type of analysis is also important for understanding dark matter detection and its astrophysical implications.*
*Solution*We can integrate by quadrature.
ˆ*dN*
*C−CAN2*=*t.*(125)
We can express the integrand as a sum of two fractions:
1
*C−CAN2*=
*1√ C−*
*√ CAN*
*1√ C+*
*√ CAN*
= 1
2*√ C*
[*1√*
*C− √ CAN*
+*1√*
*C+ √ CAN*
]*.*(126)
Integrating, we find
*t+K=*1
2*√ C*
[*−1√ CA*ln*(√*
*C−*√
*CAN*) +
*1√ CA*ln*(√*
*C+*√
*CAN*)]
= 1
2*√ CAC*
ln
*(√ C+*
*√ CAN√*
*C− √ CAN*
) (127)
where*K*is an integration constant. Setting the boundary condition*N*= 0 at*t=*0, we find
*K= 0.*
We find the solution
*N=*
*√ C√ CA*
( e2
*√ CCAt −*1
) ( e2
*√ CCAt*+ 1
)*.*(128)
Note that it is easy to check that it reaches the obvious steady state in the limit*t→∞.*
**C.8. Level 2—a 3-state QM problem***Problem statement*
The Hamiltonian of a three-level system is given as*H=*
*Ea*0*A*0*Eb*0*A*0*Ea*
 where*A*is real. The state of the system at time*t=*0 is (in this basis)*ψ(t=*0) =*1√*
2
11 0
What is the expectation value of the energy at time*t?*
*Answer requirements*Provide the answer in the form of`verbatim`code. Implement the following function
`def``expectation_value(A:``float, E_a:float, E_b:float, t:float)``->``float: pass`
*Comments about the problem This problem belongs to quantum mechanics, focusing on multi-level quantum systems found in areas like quantum optics or molecular physics. It is typically encountered in advanced undergraduate or early graduate-level courses and requires knowledge of linear algebra, time evolution, and the calculation of expectation values in quantum mechanics.*
*Solution*The eigenstates are easily found to be*1√*
2*(1,0,±1)T*and*(0,1,0)T*with corresponding energies*Ea ±A, Eb.*Let
us denote them as*|1⟩, |2⟩*and*|3⟩.*Given state*ψ*is decomposed as 12*(|1⟩+ |2⟩)+ 1√*2*|3⟩,*the expectation of
energy stays constant:
*⟨E⟩=*1
4*((Ea +A)+ (Ea −A))+*
1
2*Eb*=
1
2*(Ea*+*Eb) .*(129)
**C.9. Level 1—blackbody in****d****dimensions***Problem statement*Assume we live in a 4+1 dimensional spacetime. How does the total energy density of a black body scale with temperature*T.*Find the exponent*n*in the expression*u∝ Tn.*
*Answer requirements*Provide the answer in the form of`verbatim`code. Implement the following function
`def``answer() ->``float: pass`
*Comments about the problem This problem lies in the realm of statistical mechanics and thermodynamics applied to higher-dimensional spacetimes, a topic typically encountered at the undergraduate level in TP.*
*Solution*The density of states scales as*kD−1dk*in D spatial dimensions giving*TD+1*scaling for the total energy density. Hence,*n=*5*.*
**C.10. Level 1—boosted parabolic trajectory***Problem statement*Consider a situation where a space-probe very briefly fires its rockets while passing a planet of*massM*at periapsis, its nearest point to the planet. Suppose that the probe is on a parabolic trajectory and at periapsis, when travelling at velocity*ve,*it results in a boost of*δv.*What will be its speed once it escapes the planet’s gravitational field only in terms of*ve*and*δv?*
*Answer requirements*Provide the answer in the form of`verbatim`code. Implement the following function
`def``speed(v_e:``float, delta_v:float)``->``float: pass`
*Comments about the problem This problem is part of orbital mechanics, typically covered at the undergraduate or advanced high school level in physics. It involves principle of energy conservation in Newtonian gravity.*
*Solution*Conservation of energy gives*12m(ve+ δv)2− mMG*
*rp*= 1
*2mv2∞.*We also know that 1*2m(ve)2− mMG*
*rp*=*E=*0 for
the parabolic trajectory. We can solve for*ve: ve*= √
*2MG rp*. Then we can substitute it in the first equation
and get:
*v∞*=*δv*
√ 1+
*2ve δv*
*.*(130)
**ORCID iDs**
Zhiqi Gao 0009-0006-4989-3753 Yurii Kvasiuk 0009-0002-4720-1320 Tianyi Li 0000-0001-9545-8556 Moritz Münchmeyer 0000-0002-3777-7791 Sai Chaitanya Tadepalli 0000-0001-9947-4748
**References**
[1] Hendrycks D, Burns C, Kadavath S, Arora A, Basart S, Tang E, Song D and Steinhardt J 2021 Measuring mathematical problem solving with the math dataset (arXiv:2103.03874)
[2] Glazer E*et al*2024 FrontierMath: a benchmark for evaluating advanced mathematical reasoning in AI (arXiv:2411.04872) [3] Arora D, Singh H G and Mausam 2023 Have LLMs advanced enough? A challenging problem solving benchmark for large
language models (arXiv:2305.15074)
[4] He C*et al*2024 OlympiadBench: a challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems (arXiv:2402.14008)
[5] Jaiswal R, Jain D, Popat H P, Anand A, Dharmadhikari A, Marathe A and Shah R R 2024 Improving physics reasoning in large language models using mixture of refinement agents (arXiv:2412.00821)
[6] Pan H, Mudur N, Taranto W, Tikhanovskaya M, Venugopalan S, Bahri Y, Brenner M P and Kim E-A 2024 Quantum many-body physics calculations with large language models (arXiv:2403.03154)
[7] Phan L*et al*2025 Humanity’s last exam (arXiv:2501.14249) [8] Iyer V and Wald R M 1994 Some properties of Noether charge and a proposal for dynamical black hole entropy*Phys. Rev. D*
**50**846–64 [9] Geroch R P 1968 Spinor structure of space-times in general relativity. I*J. Math. Phys.***9**1739–44 [10] Kontsevich M 1992 Intersection theory on the moduli space of curves and the matrix Airy function*Commun. Math. Phys.***147**1–23 [11] Schon R and Yau S-T 1981 Proof of the positive mass theorem. 2*Commun. Math. Phys.***79**231–60 [12] Aganagic M, Danilenko I, Li Y, Shende V and Zhou P 2024 Quiver Hecke algebras from Floer homology in Couloumb branches
(arXiv:2406.04258) [13] Parker T and Taubes C H 1982 On Witten’s proof of the positive energy theorem*Commun. Math. Phys.***84**223 [14] Hausel T and Thaddeus M 2003 Mirror symmetry, Langlands duality and the Hitchin system*Invent. Math.***153**197 [15] Hardy G H 1940*A Mathematician’s Apology*(Cambridge University Press) (available at: www.cambridge.org/core/books/
mathematicians-apology/A344F9D097F5AFF45BDA21B57B54BDCA) (Foreword by C P Snow) [16] Rota G-C 1997 Ten lessons i wish i had been taught*Not. Am. Math. Soc.***44**22–25 (available at: www.ams.org/notices/199701/
comm-rota.pdf) [17] Si C, Yang D and Hashimoto T 2024 Can LLMs generate novel research ideas? A large-scale human study with 100+ NLP
researchers (arXiv:2409.04109) [18] Pólya G 1945*How to Solve It: A New Aspect of Mathematical Method*(Princeton University Press) [19] OpenAI 2024 GPT-4o (available at: https://openai.com/index/hello-gpt-4o/) [20] OpenAI 2024 Introducing OpenAI o1-preview (available at: https://openai.com/index/introducing-openai-o1-preview/) [21] OpenAI 2025 o3-mini (available at: https://openai.com/index/openai-o3-mini/) [22] Imani S, Du L and Shrivastava H 2023 Mathprompter: mathematical reasoning using large language models (arXiv:2303.05398) [23] Huang J, Chen X, Mishra S, Zheng H S, Yu A W, Song X and Zhou D 2023 Large language models cannot self-correct reasoning yet
(arXiv:2310.01798) [24] Yin Z, Sun Q, Guo Q, Wu J, Qiu X and Huang X 2023 Do large language models know what they don’t know? (arXiv:2305.18153) [25] Kamoi R, Zhang Y, Zhang N, Han J and Zhang R 2024 When can LLMs actually correct their own mistakes? A critical survey of
self-correction of LLMs (arXiv:2406.01297) [26] Dhuliawala S, Komeili M, Xu J, Raileanu R, Li X, Celikyilmaz A and Weston J 2023 Chain-of-verification reduces hallucination in
large language models (arXiv:2309.11495) [27] Zhang J, Li Z, Das K, Malin B and Kumar S 2023 SAC3: reliable hallucination detection in black-box language models via
semantic-aware cross-check consistency (arXiv:2311.01740) [28] Jiang Z, Peng H, Feng S, Li F and Li D 2024 Llms can find mathematical reasoning mistakes by pedagogical chain-of-thought
(arXiv:2405.06705) [29] Kvasiuk Y, Münchmeyer M and Smith K 2024 A tale of two fields: neural network-enhanced non-gaussianity search with halos
(arXiv:2410.01007) [30] Basso E, Chung D J H, Kolb E W and Long A J 2022 Quantum interference in gravitational particle production*J. High Energy Phys.*
JHEP12(2022)108 [31] Ellis J 2017 TikZ-Feynman: Feynman diagrams with TikZ*Comput. Phys. Commun.***210**103–23 [32] Meta AI 2024 Meta Llama 3.1 (available at: https://ai.meta.com/blog/meta-llama-3-1/) [33] Qwen Team 2024 Qwen2.5 (available at: https://qwenlm.github.io/blog/qwen2.5/) [34] Qwen Team 2024 Qwen QwQ 32B preview (available at: https://qwenlm.github.io/blog/qwq-32b-preview/) [35] Guo D*et al*2025 DeepSeek-R1: incentivizing reasoning capability in LLMs via reinforcement learning (arXiv:2501.12948) [36] Bi X*et al*2024 DeepSeek LLM: scaling open-source language models with longtermism (arXiv:2401.02954) [37] Chen G H, Chen S, Liu Z, Jiang F andWang B 2024 Humans or LLMs as the judge? A study on judgement biases (arXiv:2402.10669) [38] Kumar T and Kats M A 2023 ChatGPT-4 with code interpreter can be used to solve introductory college-level vector calculus and
electromagnetism problems (arXiv:2309.08881) [39] Wu Y, Jia F, Zhang S, Li H, Zhu E, Wang Y, Lee Y T, Peng R, Wu Q andWang C 2023 MathChat: converse to tackle challenging math
problems with LLM agents (arXiv:2306.01337) [40] Gao Z, Li T, Kvasiuk Y, Tadepalli S C, Rudolph M, Chung D J H, Sala F and Münchmeyer M 2025 Test-time scaling techniques in
theoretical physics—a comparison of methods on the TPBench dataset (arXiv:2506.20729) [41] Peskin M E and Schroeder D V 1995*An Introduction to Quantum Field Theory*(Addison-Wesley) (https://doi.org/
10.1201/9780429503559) [42] Bailin D and Love A 1994*Supersymmetric Gauge Field Theory and String Theory*(CRC Press) (https://doi.org/
10.1201/9780367805807) [43] Chandrasekhar S 1985 The mathematical theory of black holes*General Relativity and Gravitation*(Springer) [44] Cobbe K*et al*2021 Training verifiers to solve math word problems (arXiv:2110.14168) [45] Ling W, Yogatama D, Dyer C and Blunsom P 2017 Program induction by rationale generation: learning to solve and explain
algebraic word problems*Proc. 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*pp 158–67
[46] Tsoukalas G, Lee J, Jennings J, Xin J, Ding M, Jennings M, Thakur A and Chaudhuri S 2024 PutnamBench: evaluating neural theorem-provers on the Putnam mathematical competition (arXiv:2407.11214)
[47] Zheng K, Han J M and Polu S 2022 MiniF2F: a cross-system benchmark for formal olympiad-level mathematics (arXiv:2109.00110) [48] Liu C*et al*2023 FIMO: a challenge formal dataset for automated theorem proving (arXiv:2309.04295) [49] Azerbayev Z, Piotrowski B, Schoelkopf H, Ayers E W, Radev D and Avigad J 2023 ProofNet: autoformalizing and formally proving
undergraduate-level mathematics (arXiv:2302.12433) [50] Rein D, Hou B Li, Stickland A C, Petty J, Pang R Y, Dirani J, Michael J and Bowman S R 2023 GPQA: a graduate-level Google-proof
Q&A benchmark (arXiv:2311.12022)
[51] Mirzadeh I, Alizadeh K, Shahrokhi H, Tuzel O, Bengio S and Farajtabar M 2024 GSM-symbolic: understanding the limitations of mathematical reasoning in large language models (arXiv:2410.05229)
[52] Team K*et al*2025 Kimi k1. 5: scaling reinforcement learning with LLMs (arXiv:2501.12599) [53] Xu H*et al*2025 RedStar: does scaling long-CoT data unlock better slow-reasoning systems? (arXiv:2501.11284) [54] Bespoke Labs 2025 Bespoke-Stratos: the unreasonable effectiveness of reasoning distillation (available at: https://hf.co/bespokelabs/
Bespoke-Stratos-32B) (Accessed 22 January 2025) [55] Yu L, Jiang W, Shi H, Yu J, Liu Z, Zhang Y, Kwok J T, Li Z, Weller A and Liu W 2024 MetaMath: bootstrap your own mathematical
questions for large language models (arXiv:2309.12284) [56] Zelikman E, Wu Y, Mu J and Goodman N 2022 STaR: bootstrapping reasoning with reasoning*Advances in Neural Information*
*Processing Systems*vol 35 pp 15476–88 [57] Zelikman E, Harik G, Shao Y, Jayasiri V, Haber N and Goodman N D 2024 Quiet-STaR: language models can teach themselves to
think before speaking (arXiv:2403.09629) [58] Shao Z, Wang P, Zhu Q, Xu R, Song J, Bi X, Zhang H, Zhang M, Li Y K, Wu Y and Guo D 2024 DeepSeekMath: pushing the limits
of mathematical reasoning in open language models (arXiv:2402.03300) [59] Chen Z, Deng Y, Yuan H, Ji K and Gu. Q 2024 Self-play fine-tuning converts weak language models to strong language models
(arXiv:2401.01335) [60] Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, Chi E, Le Q and Zhou D 2023 Chain-of-thought prompting elicits
reasoning in large language models (arXiv:2201.11903) [61] Snell C, Lee J, Xu K and Kumar A 2024 Scaling LLM test-time compute optimally can be more effective than scaling model
parameters (arXiv:2408.03314) [62] Welleck S, Bertsch A, Finlayson M, Schoelkopf H, Xie A, Neubig G, Kulikov I and Harchaoui Z 2024 From decoding to
meta-generation: inference-time algorithms for large language models (arXiv:2406.16838) [63] Muennighoff N, Yang Z, Shi W, Li X L, Fei-Fei L, Hajishirzi H, Zettlemoyer L, Liang P, Candès E and Hashimoto T 2025 s1: simple
test-time scaling (arXiv:2501.19393) [64] Khot T, Trivedi H, Finlayson M, Fu Y, Richardson K, Clark P and Sabharwal A 2022 Decomposed prompting: a modular approach
for solving complex tasks (arXiv:2210.02406) [65] Zhou D, Schärli N, Hou L, Wei J, Scales N, Wang X, Schuurmans D, Bousquet O, Le Q and Chi E 2022 Least-to-most prompting
enables complex reasoning in large language models (arXiv:2205.10625) [66] Hao S, Gu Y, Ma H, Hong J J, Wang Z, Wang D Z and Hu Z 2023 Reasoning with language model is planning with world model
(arXiv:2305.14992) [67] Zheng H S, Mishra S, Chen X, Cheng H-T, Chi H, Le Q V and Zhou D 2023 Take a step back: evoking reasoning via abstraction in
large language models (arXiv:2310.06117) [68] Lightman H, Kosaraju V, Burda Y, Edwards H, Baker B, Lee T, Leike J, Schulman J, Sutskever I and Cobbe K 2023 Let’s verify step by
step (arXiv:2305.20050) [69] Ren J, Zhao Y, Vu T, Liu P J and Lakshminarayanan B 2023 Self-evaluation improves selective generation in large language models
(arXiv:2312.09300) [70] Chen S, Li B and Niu D 2024 Boosting of thoughts: trial-and-error problem solving with large language models (arXiv:2402.11140) [71] Madaan A*et al*2024 Self-refine: iterative refinement with self-feedback*Advances in Neural Information Processing Systems*vol 36 [72] Forsman A 2024 Analyzing the performance of self-refine on different large language models (available at: https://github.com/
anforsm/self-refine/blob/main/report.pdf) [73] Beirami A, Agarwal A, Berant J, D’Amour A, Eisenstein J, Nagpal C and Suresh A T 2025 Theoretical guarantees on the best-of-n
alignment policy (arXiv:2401.01879) [74] Wang X, Wei J, Schuurmans D, Le Q V, Chi E H, Narang S, Chowdhery A and Zhou D 2023 Self-consistency improves chain of
thought reasoning in language models*11th Int. Conf. on Learning Representations*(available at: https://openreview.net/ forum?id=1PL1NIMMrw)
[75] Yao S, Yu D, Zhao J, Shafran I, Griffiths T, Cao Y and Narasimhan K 2023 Tree of thoughts: deliberate problem solving with large language models*Advances in Neural Information Processing Systems*vol 36 pp 11809–22
[76] Qi Z, Ma M, Xu J, Zhang Li L, Yang F and Yang M 2024 Mutual reasoning makes smaller LLMs stronger problem-solvers (arXiv:2408.06195)
[77] Zhang D*et al*2024 LLaMA-Berry: pairwise optimization for O1-like olympiad-level mathematical reasoning (arXiv:2410.02884) [78] Kang J*et al*2024 MindStar: enhancing math reasoning in pre-trained LLMs at inference time (arXiv:2405.16265) [79] Kocsis L and Szepesvári C 2006 Bandit based monte-carlo planning*European Conf. on Machine Learning*(Springer) pp 282–93 [80] Schick T, Dwivedi-Yu J, Dess̀ı) R, Raileanu R, Lomeli M, Hambro E, Zettlemoyer L, Cancedda N and Scialom T 2024 Toolformer:
language models can teach themselves to use tools*Advances in Neural Information Processing Systems*vol 36 [81] Saad-Falcon J*et al*2024 Archon: an architecture search framework for inference-time techniques (arXiv:2409.15254) [82] Chen W, Ma X, Wang X and Cohen WW 2022 Program of thoughts prompting: disentangling computation from reasoning for
numerical reasoning tasks (arXiv:2211.12588) [83] Gao Y, Xiong Y, Gao X, Jia K, Pan J, Bi Y, Dai Y, Sun J and Wang H 2023 Retrieval-augmented generation for large language models:
a survey (arXiv:2312.10997) [84] Srednicki M 1993 Entropy and area*Phys. Rev. Lett.***71**666–9