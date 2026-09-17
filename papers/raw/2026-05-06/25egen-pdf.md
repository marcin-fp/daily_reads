
E-Gen: Leveraging E-Graphs to Improve Continuous Representations of Symbolic Expressions
Hongbo Zheng* Suyuan Wang* Neeraj Gangwar Nickvash Kani University of Illinois at Urbana-Champaign
{hongboz2,suyuan2,gangwar2,kani}@illinois.edu
Abstract
Vector representations have been pivotal in advancing natural language processing (NLP), with prior research focusing on embedding techniques for mathematical expressions using mathematically equivalent formulations. While effective, these approaches are constrained by the size and diversity of training data. In this work, we address these limitations by introducing E-Gen, a novel e-graph-based dataset generation scheme that synthesizes large and diverse mathematical expression datasets, surpassing prior methods in size and operator variety. Leveraging this dataset, we train embedding models using two strategies: (1) generating mathematically equivalent expressions, and (2) contrastive learning to explicitly group equivalent expressions. We evaluate these embeddings on both in-distribution and out-of-distribution mathematical language processing tasks, comparing them against prior methods. Finally, we demonstrate that our embedding-based approach outperforms state-of-the-art large language models (LLMs) on several tasks, underscoring the necessity of optimizing embedding methods for the mathematical data modality. The source code and datasets are available at https://github.com/MLPgroup/ E-Gen.
1 Introduction
While large language models (LLMs) (Jiang et al., 2023; Dubey et al., 2024; Hurst et al., 2024; Jaech et al., 2024) have demonstrated effectiveness in processing natural language, these methods still perform suboptimally with math-based content which plays an important role across numerous domains (Zanibbi et al., 2024; Rohatgi et al., 2019). For instance, even a state-of-the-art LLM like GPT-4V only reaches 49% accuracy in MathVista (Lu et al., 2023), a comprehensive benchmark to evaluate the mathematical reasoning capabilities of LLMs. In
*Equal Contribution.
another instance, as tested in Frieder et al. (2024), GPT-4’s performance in computing integration is dominated by specialized embedding-based models (Lample and Charton, 2019; Lample et al., 2022). Therefore, effective approaches to process semantically rich mathematical notation are necessary.
One approach is to compute a semantic representation of mathematical content based on textual context and treat mathematical expressions as a sentence without learning mathematical semantics (Krstovski and Blei, 2018). This has been used in various mathematical language processing (MLP) tasks, such as mathematical information retrieval (Topić et al., 2013; Mansouri et al., 2022a), identifier definition extraction (Pagael and Schubotz, 2014; Hamel et al., 2022; Zou et al., 2024), mathematical reasoning (Geva et al., 2020; Nye et al., 2021) and theorem proving (Wang et al., 2020; Wu et al., 2022). But this approach has two limitations: (1) textual descriptions are lacking in some math content like textbooks or mathematical derivations in academic publications, and (2) don’t really explore relations between symbolic operators from a mathematical perspective.
To address these problems, recent studies have focused on equivalence and mathematical manipulation between expressions to derive the meaning of mathematical expressions independent of context. However, these approaches remain limited, primarily due to the quality of available data. Alla-manis et al. (2017) introduces EQNET, a TreeNN-based (Socher et al., 2013) model to group equivalent expressions together, but their datasets are limited to arithmetic and boolean expressions. SE-MEMB (Gangwar and Kani, 2023) computes vector-based semantic representations by learning to generate mathematically equivalent expressions but is significantly limited by the SymPy-generated dataset (Meurer et al., 2017). SymPy functions are designed for simplification and directly derive the most simplified expression without intermedi-
11772
ate steps, leading to a dataset that lacks enough rewrites per expression. Hence, a more efficient mathematical data generation scheme is required.
In this work, we propose E-Gen, a highly scalable and efficient corpus generation scheme based on e-graphs (Willsey et al., 2021). Leveraging a collection of mathematical transformations, E-Gen facilitates the creation of synthetic datasets with large clusters of semantically equivalent expressions. This approach significantly improves upon prior SymPy-based methods, overcoming limitations in the number of rewrites per expression while improving flexibility and scalability. In summary, we highlight the following contributions of E-Gen:
1) We introduce E-Gen, a novel scheme for generating a cluster-based mathematical expression dataset, along with a high-diversity mathematical corpus.
2) We evaluate two types of embedding models based on seq2seq and contrastive learning respectively, showing improved semantic representation performance over prior works in quantitative and qualitative tests.
3) The embedding models are evaluated on two out-of-distribution downstream tasks, to demonstrate models’ generalizability and robustness.
4) Finally, we compare our models with GPT-4o across multiple tasks, demonstrating the effectiveness of embedding-based approaches.
2 Related Work
In MLP (Meadows and Freitas, 2022), semantic representation shows strong potential across various problems. A representative application is mathematical information retrieval (MIR) (Kris-tianto et al., 2016; Zanibbi et al., 2016a; Mansouri et al., 2022c), where expressions or keywords are ranked based on their relevance to a query. Gao et al. (2017) proposes SYMBOL2VEC, a mathematical symbol representation generation scheme to group LaTeX symbols having similar contexts together. They further extend this approach to a MIR scheme (FORMULA2VEC) to prove its effectiveness. Krstovski and Blei (2018) converts symbolic layout trees (Zanibbi et al., 2016b) of mathematical expressions into token sequences and generates representation based on word2vec. Mansouri et al. (2019) further improves this approach by combining the symbol layout tree and operator tree representations of an expression. Peng et al. (2021)
proposes MathBERT, a pretrained model based on MIR and formula headline generation task (Yuan et al., 2020).
Identifier definition extraction (Kristianto et al., 2014) is another promising application, which aims to align identifiers found in scientific text with their definitions. Popovic et al. (2022) utilizes a transformer-based method to develop an end-to-end joint math entity and relation extraction approach. Jo et al. (2021) provides a mathematical understanding pretrained model by fine-tuning BERT on masked mathematical identifier prediction task. In the theorem proving field, Welleck et al. (2021b,a) generate theorem proof by retrieving relevant references to a given query theorem. However, as discussed in Section 1, MLP studies rely on semantic representation but mostly focus on establishing homomorphism between context and mathematical expressions to construct semantic representation, which is limited by the incapacity to process pure math content and can not really understand mathematical transformations. Even though some recent studies (Allamanis et al., 2017; Meidani et al., 2023) have focused on generating semantic representation based on intrinsic features of mathematical expressions to address this problem, their performance and scope of application are still limited by existing dataset, motivating this work’s demonstration of a more effective mathematical corpus generation scheme.
3 Corpus of Equivalent Expressions
3.1 Corpus Generation
To generate a diverse set of mathematical expressions, we manually design templates containing placeholders for arithmetic operators, functional operators, and numerical values. Expressions are systematically instantiated by replacing the placeholders in templates with all possible operators and values, resulting in approximately 5,000 initial expressions in prefix notation. The templates are carefully designed to cover fundamental arithmetic and functional operators in various formats while maximizing the potential for mathematical transformations. Each of the resulting initial expressions is processed by E-Gen, which applies around 800 mathematical rules to generate clusters of semantically equivalent expressions.
The core of our E-Gen is e-graph, an advanced data structure designed to efficiently manipulate collections of terms under a congruence relation.
11773
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9qO4wY8EhEzyR5AwXLN2gQIe_equNFtnisKZcTHq7vmNgJJ1oGAgh7znwH9UGs5N8SH_b-t6vPAeXETW9QfHPPNKRa2fLxYapGzDWezWt2WKvHBzmGs40bnu7eB-Ol9i-dH_iY=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_SEGE738ZCly1Gb7a3cic4QplAQAS4ahC6qjJrSRnyv9p7RcsMwNugD_5zVdE6aFD6G0kq0ikBuhDuCNGY_PIg-jU1Pip3zCkLzWooKwFbj7mD_0fZibNeQ5CDsjJmsmqMZ1ZfEA=w152-h232-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX95e0HwpLF_PFLR8ZPSp2gd35Bq-hj58L2v3K3vK60xJVHtIURX2PcYLYF6T4RamFUlq-D2a-PilnPY-kf5K4cKd0-9BkZREFiLIU3knbbawaMoEgOq2LX7Rhh78aJ3tBJOB41O=w152-h232-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8IZN-Sr_BCz7Af5Kjwoe-mOrcpxS9g4wPVnETr_YSjK4UBo9_nFPU1R6zjjyOGW_EaL5lwlKQA-kZwH3Gdw10iNs5mEUzvFojUCldtpREwtSY2LseFb5nR5BLUivboTnBpQoYeVg=w152-h260-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX98z9rfZ-rnJSFzXwJqqs1O6R5hQU5URc-D9Nq11eWZcI48btLAN5A4fV0i__nvzXCRvMqyLJGJiYAxtZx_AjK3pBbYk2UPceSlyh3ZQAWiI6465SCK_x-gWITbYtFYpmbLKX2iXw=w152-h256-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_Ee0GUMklQhrQxk1QYczxnWLFh1wkX666wvkFbPuCYhDMb6h4FNEr3WyAvrqICjmyqNGkpsxV31JsU6RLkDSzOSZqGpz-rQCrT7FHc208s7DZ59PdzbRKG1YAsGrj1c1ceRu6b=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_XbMT5nfc63K7RoVtniHL818hSWAyt51TecAKDTeYRzOpgd_wLSS-HyGdGq8uISEaz-dgzw3ZynrW5ffCwjR_xJxaA0xLzqs4vPXr-oFDBJ_MJNFhY6KLeu_YqnGYavEW6RuSQiA=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_njTAbHHRf3oj5Wn4ukDu1hc6cN0pFpBSseUR_CG5zZA-btTSxYhcKBLCUE72Vryc3a2fQLSM2wcEpvNgywsmtEgtYDwDK3bJnT5zN8zzA9yv_R8yvCO3VkjYHQMW7U0qZOiey=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-ouWPoo6xNmooKk2_T6CN8EYd4Psea18-WlhR9-Y08GC1_nEaCIQgq_gQAVdY-7BDPT0o6GoO2FI_nwRMrCM2X1Gw_WCFv60dECuFWHAYhjKhvtBI62yX-buMSFRcQhTsF4sW-=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-E4xGIEx8R5l6tOBIjkT6nEApvGKtaFTGttKVKh60hqm5jmtxrssbDQtYTCYEri6DVEtuZrk7tEAhCiu_Gte2ktOADS0TOgIYDLW4gjzkGEBGZaDWBUrn0Jvy_jmyDA6u51mU2=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_tRqyVaWgv7-DD6R4zaYnhmqSWQipIzW77G_p0sVNR9eMoBoOdbh4z1djf9Sy_97qXeGS8YJdTTSfUKV_bX_8goc5DFTgAB-rkSqlUr-loiYIO2yvo11i6tDBlLX72X6-XrjEXMw=w152-h256-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_wh3SBlgfq2ZJy5tmrMb3DWcpCc_LwIWyC7ccZ6NdXU6Yl_02c0bcbQUGze46rd7dReCeSZMgs7qUDiaeS2UkN1rM2jTEyKQUMmH9T_AdIQEbq3naE3vuqfWDGrl84cJnAaqhnYw=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9pbkUnFrckbCzUfUlruf1X-SDYJLkCwQnTDEq4o0g9aVOujqIKWaM4IzNKO45ImKbo2tw7JKYs6mNV-QPNVeUGRC3blRTc7tfeL1gK-SAN7qQM-p6UCT_K6_AP_n7GpYTiH5Ld=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9uy3kEJSH0fIoauTeO1I1TQDmthB5qCR0PYsJfwxP8b-rXTpCRrKAqJZHeeLvbjcHg3Vroe_ktj903w9t2eVtLQw_spVuz-wWVwyTECP9RG_emwLm6vyLUOgEXF_umld8rwP4=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_f1GM2Q1NWdmPExYRhneN33gDP2DLxB6j8LDnFYPwc6wVL3PHOFUp_kV7y-r9kQ7IsONl1KXm3Skx3q3WYiBsM4zHiNr-2DDjjLhfkQr6tAzWJZ6EEZYaHIYKOvuF6jW17apvr=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_U03w3JaBmwXaeQJ0x153-EmOCCiaFNfytufsC0JAD0VWkSL0OYQhIr7Wz2T1YFxkafDbroGsrDgsNE27gR45oRo7XnCLMDt9huXmgYvBOocn1rsrdMndsSh9GJqMBQmn6Pyre0A=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8NsK5D041wNvSV0izmZ7rMj-vJO1k_Yz2IxmoMOZ-n23OJyhqyjVsRsx9kY-0gH2Zw4E5dlFVo7Rzje_WYNELtd6DhZihF2HAMCy38F4jva7ypgHGemarvp0SQo890KEamTmDXnQ=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8mldt035lJHj-jW3pzhFo7PzpCFG5vPPhARcNnW7RWcAhtzMH4DMUkP8bznLKocNCw6zyy7td2BfqgwAnmdS6Ue18gHumHck_QiMijc1GXo3DzKVGLow0v_GBHGbbf0QLyu0WX5Q=w152-h256-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-0zLVR2gcZRKJyJglj6ri6Qa5Ogdbp5ghFtFWPowJ4PErsQCnRGhMuAzMLMzcAMZf83ePP7G7nuhr8DICJwp-8BcnsFv-6B7tc_BUHXJ4BGNs2HiidobZXR7fDen_pKNyNcpQGdQ=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9WfMjyDrAvyulv_tXYeunhKGlMoOY9pIiRaA_wL87p8zjWA9grQimfwx1VhiH_GyslFMNDZ61QXBeUwdVoWNQr10PLE4ZVVuQ7u4MDCPpxmP3G62HHfsdkr4ZUcnTsWwZ5wuk2kw=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8SCI5DW4M0NDxAnLh_SUzq30eYgGbyQx1AuQO4cXpwJqGxfAVpKE4xMze8gO2O3ZIN4E4_3ItmNsq9plK-l3NWqwETTIU-UHRBlgbz74snVrw7sAz-p4D8Bk6Vibl7oqUeCdjoYA=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8YWkiqqNrdacLszgnxnP4zEadt-H2rUXr8jTlrMUa6m8kLyZoEcnoTSWDpUlBVN6UewVWJbRZYunTOinvXaF-w33JUN1zDx_qrJT-nuj39XOL_RtrxzjeOHaRmL5WhoIodyBiybA=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9kMzDJu2skCES3mt2-TibB7IQ-c43CCooUE4UEhWOteVfpQ77pzco3iwORFMvm9-i3u-LBdIimqPlF1TTcK9ms4gquW8Z74tO-K11FBLAicSsP7Nf0PH6DZSLMkFz3FctbXj_07A=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8lYrXiOrGbRNHFFw4t3VdXkcXf1Li3885mvOAlkkn1qbTs9qQG3yqd14PDc7nSIYjkDE75UK025N6pjiXNf_MZzgEmMZ7zlmErejXrnYAC3ih4699Suf9sDXASYhRBXd3ofSNI=w152-h228-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-JVurPJXk3sWMMJjAlNCGvolmsb24-a6A1jEwo_sMcY0GL1dC4V3qEHwXZYmX_Tycuiyj_61fzD8yd-PEgmZX1HC_1L7PM2g4QMlOuWc42QL0QjuscLjJNxcmCDwmxNqF6ECkUUA=w56-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_AKy3zVCLJW7Z1uMkmPm7mJRXWcb7g0TkFVIpMUmiwoh4qrkW14zwXGd9Js_hab_arwfCs7Tr8ibb27d37cLQijvZQnEJWeH8oEvZfezKDZibt59TKOc6dPnLuDA3pc2RWVc-8=w56-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-pHmGyYdKhtZydeRG12E9kF-sD3lgzXM8sGhRdjD6w6lUYyzh5hyvJzU9fCDH0_Fl_W64AnqoV3jIeRM_L5NDr2r-prRqwRYmtERz3rURV1pLB4YR73ou8VCO3cEflexwSsDGWGw=w56-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9d1Ij8xfqeRqcRmXBVw-s19EfopvooFkspfc9UOU7cBML5We_54kJSzXrtCOwsArI667J-TLTGPMNhxo1c6WKmD05WqXl-VomltSS4_MxF7Lp0A_E5x9p9mEO-x6q2MRR9u9oDSw=w56-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-Y6Bm1g7g8xTMsMGC9BGgmUM8qwnn60zs7IKCXaW9hQUgcMFHNA6TMzhTIaEp4__DAelEDURurL2XVeu3e9wCFkiFCHzgerGVA87dke1Cyzz0tX2L1ZrmjbLouPqWVbiRMte5pDw=w848-h204-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-wriuPdhaFm3U51EEnvjB-G_F6vMtgNoWnv0fTFamwjSE65MguwOKpLLUBx6p8xDlzsF-Aa_tTi8T4-DIEIuXHF8-8O8nk8o6xzH9-hm_DlMU4y8DHqUcPHG1mROowvY4_4qaJzg=w252-h204-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8N1oDX9lA6PxGFtiX6GZ8uP8q56bEMgFVklHsfrgyRxCDNjZfBFwI-2e8Ygd788X-85TP4i9E2jRv-z06_lVWG_K_S504EBtYgZ-PwZcEhyOdMaxEChPmqWGwWMVHpSaV-4oMz=w460-h204-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_63zSRTCSnTPZcDOs2hM5z7iNqrIDuaK2umXPTMYq1gQEC06TxeGgtkLWeyWoYKWf6PGFYM4lwbqDrS6U_6wh_cmef59ytaSvFWbAkVzVXS33hNSUHxp3XgKK_PWWJFIDMsPjTmg=w548-h204-v0?authuser=0)

(a) Initial e-graph (x+ 8)− 8
(b) After applying rule (x+y)−z → x+(y−z)
(c) After applying rule x− x→ 0
(d) After applying rule x+ 0→ x
(e) Grammar created from saturated e-graph
Figure 1: Illustration of e-graph saturation (1a to 1d) and grammar creation (1e). An e-graph consists of e-classes (dashed boxes) containing equivalent e-nodes (solid boxes). Edges connect e-nodes to their child e-classes. Applying mathematical rules to an e-graph adds new e-nodes and edges (1b and 1c), or merges e-classes (1d). Additions and modifications are emphasized in black. In 1e, the saturated e-graph is converted into a context-free grammar, where each grammar is defined using e-class id and the e-nodes with their child e-classes.
An e-graph is composed of e-classes, each containing a set of equivalent e-nodes. An e-node can be linked to one or more child e-classes, depending on the operator’s arity. From a mathematical perspective, child e-classes represent the arguments of their associated e-node, typically corresponding to a mathematical operator. Consequently, any subgraph originating from an e-node within the same e-class represents equivalent expressions.
Figures 1a to 1d show the e-graph saturation process. In the initial e-graph (Figure 1a), the e-node “+” is linked to two child e-classes “x” and “8”, respectively, and the e-node “−” is linked to a subgraph “(x + 8)” and a child e-class “8”, together forming the initial expression “(x+8)− 8”. In Figure 1b, a new e-node “+” is added to the top e-class after the associative law is introduced. The two e-nodes, “−” and “+” in the top e-class represent subgraphs for expressions “(x+ 8)− 8” and “x + (8 − 8)” which are equivalent rewrites generated by the associative law. Similarly, transformations such as “(x−x) → 0” and “x+0 → x” are embedded into the e-graph in the steps shown in Figures 1c and 1d. The e-graph is iteratively expanded by applying each applicable rule, thereby capturing all possible equivalent expressions.
A context-free grammar is created after e-graph saturation in prefix notation, based on e-classes and the connections of e-nodes in it, as shown in Figure 1e. E-classes will be represented as variable symbols denoted by "e0", "e1", "e2", "e4" in Figure 1d. Variables and numbers comprise the terminal set in the grammar. The production rules are determined by the edges and take the form:
e⟨index⟩ → [var/num]
e⟨index⟩ → [op e⟨index⟩ e⟨index⟩, . . .]
where e⟨index⟩ denotes eclass with corresponding
index, op and var/num denote enodes representing operators and variables/numbers.
Equivalent expressions are extracted from this grammar using a recursive rewrite algorithm. The process begins at a designated root e-class (e.g., “e0”) and traverses the grammar, replacing e-classes with their corresponding expansions until no e-classes remain. For instance, “e2”, in the second grammar “− e2 e1” of “e0”, can be expanded to “+ e0 e1” and generate “− + e0 e1 e1”. To avoid excessively long rewrites, a token length limit of 25 and a time limit of 600s are imposed. Eventually, clusters of semantically equivalent expressions for all initial expressions are generated by E-Gen and form a new corpus.
3.2 Corpus Analysis
Category Operators
Arithmetic +, −, ×, ÷ pow, abs, sqrt, d
dx Logarithmic/Exponential ln, exp (as pow e) Trigonometric sin, cos, tan
csc, sec, cot Inverse Trigonometric sin−1, cos−1, tan−1
csc−1, sec−1, cot−1
Hyperbolic sinh, cosh, tanh csch, sech, coth
Inverse Hyperbolic sinh−1, cosh−1, tanh−1
csch−1, sech−1, coth−1
Table 1: Operator coverage of E-Gen Corpus.
The new corpus encompasses a comprehensive set of arithmetic and functional operators as detailed in Table 1. Table 2 presents examples from three clusters of equivalent expressions generated by E-Gen. The corpus is structured into clusters, each containing numerous mathematically equivalent expressions derived through a series of flexible transformations. These transformations span
11774
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-Z9TUivgUvKRYQ0tMBjEZVdsmw3Tr8Hrt_6FQCaw-x1mH67-V4r1t9EYDpbUgLQmCPRpmX8OSdxntEWSM3qrElfKv2v5m8GwdQbYzKtiCtXMUVieQaaO7lvb-KwPpLQmjl8t4fvQ=w37-h69-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX903bCdchHrxHlrG8vA112tUCMsFbXju7i8c6vMTL-ooBbtG6CBlQR0zrnMIfAqjUUEOGRPEwXcWaRZBxESjU4TE1-WqAN4TqPkECi7xS2avBCoIRZvuQCHNjZXR0ARrQ-744NgfQ=w68-h100-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX86CAYaFSQ1XihPvOcXhIuSiYYcA3C2aXVQ5jCd024R5oab6pq0EzPMfDwlij8gTT5qAxJDQzoQvsIgRD9UiJWaW1kJg-HcwyHYeqETJ-jImh7aPfu-JdBXtxu5eQewr8C1d3JU=w80-h100-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_tQx1NvgAH0WKf3OIarsextbwHJd5uAIJXQ_YzkGA9llZ9MQEGz92OmZiM89wG6d1t-qtlSGb6n1K4nP2grMdNQmTTSxsBN9vV_M5F8FqoyjraH05rfRgVOvvwcKiJTn_J5GnnEg=w96-h112-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-oESgN95ZSmq-oUIFSkGtA6Bvjs8RBqA7b3ogT_3BZRnokij-cianU8FWY0ESHa_j5GUi3S-4IeMn3zn66k6wvGGmEnU2S0ggSbDtRINlgBfuTIL2_AtEV59v695FC0phfiP3-=w132-h80-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-6qsONf2yNJFdp-7GveX5WpEly8kovtbVyD6qACoNJ1BowhzokY2f6hwX-0p5KmgE4UB59Xy_BHJoKLXu_ysRZBdHFKqHi_ZNbe4Zn94d9JXpigWD1SRbD3miQwVFZwzpNTqg-yg=w388-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8m53AcTuDqaL1wuw6bnXfOqTr34GSB1MxU0UvMXBm6f6zovevaNSwu1e9k8tw53lOCLuGY0iePgvOse1Z25EC7KD4JLewq3QfkIN5iGRYW-PZ0uaTy35nToP-yZLZew6VCHKTiGw=w472-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8cw-bfzQbpyKUTcEDYs1NWxpWvARUcef-re-adLCyyvEEbVzKqGKD3f2He1fiYVbUsypJ-PWuiljsoKK7gMmRFHuednG5Rwfv9TlasjzRRv6_tOL8lU3GhwGpzpBQRFnyDyihi8Q=w472-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_Y81Q_IVpkdiuz47zuC4X1r-c2GN-zmT4yCz2kOKPLyDrnzLFfOj7xybGziBhK9RfESXn7Rk39d5rcviMszUg8wjXXFq6jr1QatkrVRpMswlC1CzaUkHUtNmhZY2BNeyx69Gaahw=w512-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX856bQW-5E9XYjROvpOhy5Xt7lZsbxP0jxCfFCxibdo6PXJ8dVBeCeoWJOBS0ZaSINNhujmc9eCGkN4N7cfJa4ibvsiTd0ihofMju0FQFd1xI1ZO8gnUXuXGIOZs2GGeljZHr6o7A=w312-h224-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8G1h2UfojnrYbSmiNxW0jwrOS73vhpqaIQjtcO7sxICRwkRE9-sWeBqAwrl0rCTmyZstKVTW_a9m13xIn7IwaA4Phnw7RrHATRylWxOCeQaFem1IHWTnWN73THH4RojKPwElMTxQ=w392-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX__Y_x3Nh1vwOwFPYfOaJUd0DL3cGZL_B4bsguhIIcBoRM0r2LgDxzwj7auC1VeX2HQ00-mJsLFJG0Rm4trFO4PA2iNN4uAWQRgreCX8jJdHS4D3gmshHY8JbUCRylbAahDhYK60w=w392-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8AwIU6YSEROHJLCkW1vtpBCeOZrFzze-EK9Y86lrUXvf9XbhVUr_3aM3OfhMoxLcktYT82Nijdgt6llQdYVVLECpM297Abk6O5iIel7sdtReBcH6H7BiUcKT7Yp2d1R-Mr1Z0a5A=w392-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9X42uwDRARKp1xtpYdrdBo69syHgSjGtNmBCHAOhjmpSYVaHBGfP5f0HMSz6roxnWjLd4WQgOY0z0YSX5pO7geNjCeT9XgK_VGpzuTLHHX4KPVFG_XRd-wrRcT9xCUBVddcsvE=w392-h179-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_ALQnlWrVjCyd1zlH1eu13r4XBEMKgzusCplGNcOJ0LnRAeUogbRwZgU9plTrr0MvaM_MIgfJseGJlK0LA1Z4o6P7UMRG5Y7_mY-vFJxZ3w7RCVUHucQOcJiuiWPjAiuSfVE1RJQ=w392-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8_Hl9DOt90oGKyly4goewnDaKsQlOEDDN7fgDF2aGPtPFbTirdb8YKoeV2gYbiTs0tPdZwO3g-oet5x-iBdK7ld46xMbolSH_DKfjHc2MK84eCpdRlvKGV3_kuul6kEwnwp18Tag=w392-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX807wwXAS57x52GdTaucIFH0xL5WmYwO3MQknsulQV5zwi0NzRY8kAU8Vh9pHByzS-xiztZ2QUHoGAAM3daHLg_nVZSKdA4S5C6fBu-BVDfLV0N2dfAp4NJ3zHGti41T65A0lB7UA=w312-h224-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-VvXwSdw52OAxBgk2a_HykmvXs284gUG76xkSelbTA_ftDFKTQ9v7s4zOYCUEWZKpyb5Hz0hn5crwkvupLsCeJ7uD6qQBtmqDcjZiamZY6zZILAnMLewUD9KcBWK8ssweQ1iMNVQ=w592-h171-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_vrchaP99NFlgkkUsc4fLZMsyayFbichE0i_qDLpqWuXDQjqjMFHSXHmKRRgk6mZufWhIjl1B_Sliw1XGWB9HmVEtdKq-uEPQyb6shJC8OQ92LmjpJMsrn5zP793kSOs-4S5_U-A=w392-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-khGDhZ8l0QJad3r4RS7W_-tVc4mTBj5IZXTUaTkVUcJutJdVoGxmyCydaSPP3en37lua72GaSGSRWsbARppOIeTbsLnP6bmgEBSlX8UaK-Y2YVmCNf5XdpBeueVyPc_3Kq6P0=w592-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8oiucofzQTOhU0DkXQ0f82qXMqzBDClVcDvRDHKsmYaHpgXzTyIuF1ibepcN4hfkAu-oeCZzFHf11qRO4R5y_s0A4HTlDoUDLc4rHF4gyihypnAahZHgL6x5lSVbpLkCd18v4tCA=w592-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_kLaaw2EWt_TU-kqyx5UzyI9OmQ0tNOdqGT74F1IJZB3hdQs76edYXYxdyBtncM29Qygx6DeWKnWn0XzZv-98HuJEdlSlTbjqR4J7OQ82ZsewgTdOzU2gir4IcDHeaJlxfSgNmtA=w592-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_P_GpQl6S8pR57Iq42IFRZWM5GJI-IINpAQ8ddnUn2MV7b7dv0QO1Z0Hk98qkINE1yK_mNGL_6pxelTprwbexdke7TmMWeaByq57vuAKeT2ZAFHBStpdX9eQFLFr_pBZDCXLsC3w=w592-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-4kSS_5DEOzakhHSUYB8emDC04_YTLub3cskCw9UYcddaTeReBXzG7aHdbJh-7Hg2YnS1vaHD69rF3xT135F9h2T5RNE_wtydNrbbyp5uEKccu1UhMtR31i_zNFuwpd58nPu1NXQ=w592-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9BEt64LA6zcShBLPak21dzYzPGTzx5h13xP_oulW5F71Uxek2krp3Ilj0hnrRpcF5_-H4jGPPgCc-qWeeFTLxrv2hJ2SmnSBN90bDu6HoS07DNj_FMkt-d5l367LlhlK8flwK5=w592-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8UCP5YFm9cFSIMkGDxmLd8IAHsBEnIqf8qIDERHSJ7Ycd2JPgwFhuWyoRsW8tKK1tw6UgrJL04OuUO0IwvePPPfIZmXYWmUqjrBx2Hga3TihgOjlnaCORwEZvEfhdklOvZAd7m=w592-h179-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX__iGmnqGaLcuO0wKatapo6A3mi-r35dMgoGrqO1yvC8v8VEmpeYapIm4N22F97ImDxSxBPvN-M_wPk3Vn_wlTZuzJ47l_ZOEFsjrYj9uYlCaf2_8jaVzV9wvc3010zTswo1sUI=w472-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-GfWMsAl2kWjjPwOrFYcla57BqH_KByV4XZ7P3Op8Cflp7-pk9vtmbBElKxE2kx6Ld5SbmSl9AAQsoYQFdkfqOIhiM-s_UgKuHlUM1QYBVUQa82TA3hKvmoHN4Wxp0W9kEC8F6XQ=w472-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8e4yEfLNpQ5nqYIIsRIpCASz1njyN8Zei60TZQOOzd4G0XVRbpDPdjnPIFxYP1MsGhOmLpREncrkI5vijjY5riw0gyxViEWs7n7a7hrsfJV7SbYf0lFmlE5MpkPdIga0Z9Fscd=w472-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_FRkvjh4GDMmXCFFD9nIH19qsz3g3ThwDQWWXLo0F5-UDJX0mT-PqE8JCa0GStMZ8OOHjyITnDih4CEyDaGQh1pi4eIh5EaCdYjZbKsXaSWClYUBnJUlQSYUKXiAOActZF8-I-=w472-h179-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-LI_Rd5axsGzXFIu-Acy1O5cpE1qBrSP1p9T-o-IBH87tZAleAA0-9FN4sIotYSQzpdF0Q4FRc3UXsLKnufoFmuq_U4MLSRhhQmapUWRow-NNqevt8SU46Ry6LwFQ6CGnUarpg=w472-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_r-bvl2ju-LC9oHAR00qg7ZrlnPgFYBRTu4kyN20JkyJBQ0FRaIj4VAPHHCOKouK2VtDgAHhS5G6M8RZpiFW3yCIh2BNS8vZSbrSxeidLJMi4DXbn5_t8M-DP1XuSx1PqPTjbh=w472-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9yRTqQOKSzmFbjPwCOL2Rf8boGaZ85wc142gOts3OnEfbW82MjICcfTvr8stioKbJ32E7mZX6ZeEvk_Ii6K3eobk-xZKNykwv_t5V7mMXK1sWhNudedCU4JtIoRdFflxQlsTq3qg=w472-h179-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_t_sWLosE2-8BnDc0Z9dabdgJ6EiiVGyZ9Ig7e_24GO2OBVOBrgNVeBx0dS3hfpq-2mSZVlhTKB3SxUjEFlUWgbgOZ5ViFxm0BNC4BrU9DKD0Au0QvyO9kf8-PAN3E_f--aJfLwA=w472-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-jX7P-CejQxkpdSv7MKrPs-2OMqIAUDV02164EH7shQi3c_2hE_4BK0sb3JZIn80YYeJM5uOD4sL1-lbeHddaSp30vCPw9JFvHFC84pMirkxKIaJ6Zh0tl_gpGnyNdjGti6xUG=w472-h175-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-XMH0bCd0VsltMnU4nrVGAos0-QQCBbCz0by8N1H4ZSOnsm6QgMjyiuAI6jgA0_iXnBdKA7hWT4Dg3fnc0JrWZInqXPAcYsIsS9uhfwNoMZi8c9C7J-fwrwVhzjfdDqr4eI1S61g=w472-h179-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_eGTwg3HrAwHgk-3nqz-13InFzffxnSarl9GjZ-6JGyWVvnsE8BtakFNFGSByfM6OGjLKPVHLu95aJdRcTMcFVQQiz8Yz8AoKKcnbJbQxzPl_8ev1OTs3jt18RtXlB16Q4F115=w312-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9RHjoQR-4RAp4_4dm-aFKr-dKRR9LvkFaaY7D6bMlNr9dVgj4EbjAEVx8v8WbLFhCqqfzy0vnJHstdP7des61RGUo7XejXfxDIGeNcIqWJ-LPHMRZQWM6APlbl4QwG2Ucp5brlhw=w872-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-XTY3IFN_WOuJhVn0aDlOZJXVtLlpFsGdq71To3YVkM_nMOJpVxRSNNWDyq83CI049W4rd8i6d7RYY20uZUFFUP1aazdV9hb7anvbqvbowFRxObldoXniZ1zfMU7bI7F8tx-Es=w472-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8sItJ82aX-gDiZsg0WuUAdfRLlYVsJC9j7HLIZeEVyK1dKqLkZ39-ZENtZ82q8BUzFvaJeebdAR2QmiNnySaxP3AppUn8nn3v4grVFG4C-gVmaZP-LICom3jBsjbHcrYYXEcOhnQ=w712-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX__hOekJ-wEsDdJP0b0Q5PNiZo1qDXLRekOudzrbvUgAWiuFkN9Vb518qHbvDDap_Np8eu-t9IP_Hp07kErv3aIMvhnuDj9Rc9IgLGNtuQNiNT6CxrONsn4w1O9WWtOVZWDbCbQ4A=w712-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8KYCy2MwTsJa735zkf4bh97V9rSS7VazNwc1zlXcdjbe6TrQWqyrD55Baxu5YVQ4YCPhu7OERl2X4sDlRhDV7bABZrQLwsnCDk-rvle6bf1FwSdGIC2ubsp7Sp0xP8sazDj9gC8Q=w712-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-PlKd87xsioP6j09TfrVlZRmldznOrp_dJoPhD76-9w_79Jh_qem5PUeg7z9y5W0g7DdErC4RrqcYf0nNeYoqL-4_2hr6bJYgNWXK4sST1aXVVC6_JJELLWi7p5WLrb-or-klu=w712-h179-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_HRCjSgpIEifCxAmwn42Q5nAlIW_dQrAgVPz-9y_sgplP_gLFsRCZAjB75GmNEzqAFZyyhrCa8Dxc7yOAthl7ewvMUT6Opjx4ugZmxu6a8nNqYqz_vwsPiBNoOatkMHiCxPuUpbA=w472-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-rV1kxUmAC0LVDye4b7uB17Y2pT6YMr5Im69QGrZ0kwQX-QOMakdTw91zIib8L95Fq-tUs5SoVybboCkzhy6KkuYYIkdNPc_xlqTiC3aAYm76PqeHaOBLdNtg4HX2Xz5VnCLwy4w=w712-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-YjNBmx28i7L-CviKxQxuLjRbgm7tRm7Psgki7kRRzT9df6YV60o2ZoYVl1j567DJxnp1sW1DAxtpeqqHanO20mAgtls9ufqGw1JjVzFFWHnEZIxV6-aV6rWpdqQCD37zB3ICOcw=w712-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_G7I9Ve5m01PULxSLoli0cwnUspDr_Wb26QpDnB1EipiVD8yZmttA0PizjAJ_WvHxyzVnh4YvsohOKG1Sc4L1gyawdmkqRYEJSLoCEFy310yD929JSofn7IFvJtSSrkMBEqPm5=w712-h179-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8i7SsNjtolIl0bhe_CXaT2xMKx5neASVuLucYpJ5u_H5A3TBfLTCDOyDnl7VlejtbZWe72Itul7CLVxMR8BGEHqolETkqETq9eF-tZIQPtW0rKic_cYQQVbf92GXxev1VJyB0o=w232-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-R2CRYsUMoRSIKU9hCVSMnZ6-L8SMeR6qHesxdTQAgO2Gsz_yuPG0iA4mFH2j2LjjdybLYywhiyd7ViGb72sgzugX8d65A-cTeu0xfMKCsb1eSNXnaIv15Ekx5AiqNJ6FQjKzXuQ=w552-h164-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX--iXR4kQVPuj52FU74z2pEduHil4EHvS8kXUmr5ZEeUZ6dnXMweTn5sPprL5TUXvsBpUK-SvNuV_c7Hb-9VVI48Lg5A6LdpIoVWfDIPAzPB9d6B3KVef05r-JTmPalcgGxzCmMlg=w312-h224-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_AItzWGErth7rfabSu8mqbdRMbaTBlU8pbQKvZlnCpfGOU9lNH9cVn6s6ztM4wNfDn1EIQb7ZxMw7koq9m49tq7Tz5K3kSm2h_iC-1-CNymWGhNAzbu5xdLAasKsA55LvAlZ0t=w312-h224-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8B1B420r62LPEqV02-XgdxlOeUq6HapW1vcuzJyUwpA3n0gh3_J617-nkLjXacplrs0KAlx5Gje7SEKfiDQ4lCbex9hZ4GUedhSZcgQ_AtXICYce4ojzdVDCvFFk79LhXjZmtOuA=w712-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9IIZ7w-WFAl89wH_R0HtrHK1tr09OuUKscQ2bHq_YYXqNhUbddI0I9UD2P4hmcgD_fgItwl6X0CzWHSmII2SIOsMNnYi4Gs8Xm0NH2j81Q4GJjK_PRuo7oCcDcwDB7GRhNoltZjA=w712-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8Cy4PfEc1XyrXyMnpL4zqA34qeCA_H4FpJvu3TgCwYWPxbWrcM4v6-Rf_ollYbO0FuOCBUPUq_HVJdc8pBMWy-oh2GuH8rG_a8zU_6HxUcykh1dgV-iW2EQrQPcTeMxt4E_7li=w712-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8_9M5XBls94_wWCaHUkF7h_wjPfu7xzc3B42EGObfCi5ewGNa44fEOWziPmg1LNxQBO32pJ6yZ_xqm1QvaH0w8CjpRDhnUci3VkrGckLNOE55f9zGDho95AiSelQV_AgSxTp8rtg=w72-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8n6kaOV8emRkbIAvBLRFDZM96pS0y1kX__E3i18Tcm1uB1UuoUrVtwEpVuk2BvBbykz3AFmBGg7PE9nH7Y1MLGuWSoK42FdTicOEvnCY4h9WGz8BheSP-WDDed1ggDn1070a8Kzg=w72-h155-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-9BebMGEJvo0PFBrXl3DuTfHMh-Fts4t2OlDTatFp62RHDIn3kR1jKzLbtQm0FsY7Vp8zIpnCcnIjtoEa5cVfhLorGQrCHeiX6O-qtoCrtS35URFCiAGQf_dw7zPePOQgugumGTA=w72-h155-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_dp7mL0atlvmo7l8X9HGcJOP3EPV6nhZyfNyqgyzPrDDlxWvHGQe159tCw9zFEtQRO-tPybYHsWqo-gYxNM7X0suwsAYif8bFhrj-U5aRfcfBOD6qx11Ai-sq4-Fuz2JABzbYLqw=w72-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-3DHeYIkli1p-6sRNeBc73miBTrTRt2-0WFvPYya_4lJZp2DYXMfc1ZPAdwTTM0kwN3y56HJHjHC1w4Wh3zCAIRWqJPBRa4gS_XdcvE1nwPDMr2Vmu2EvVh9AtIsDU8t3fUWtLBg=w72-h155-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX86PLblQo6Qexh7GfzVORhnCbWDMMpFGJvJ0W226Nab5F2Hy4kPOd7UI_fRBaOqFq2kY1DO-G8Qi9jSXNgw_31HUCFXTfK9wEPUTbIEHU7UyDYP44UYtmiukYZDFUNry3zMtdMd=w72-h155-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-HAWTHT-xg6w79ge3VxfSAq_US3z0DP9v2jn_SkFJZLtz1j9GSuejYN4UFDB2UAlbx7KimHKfEXEhFTqpd_Wa3s8WnDAyKsXcOXxznYijjjzikPlIoa18yosnBK9DHyymAGvRBvg=w72-h155-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_dVzM5JOaHvFGMa0jZqL0aO3r_B-iGny3lH4GFrTg3bMoiCxB3ZAwMtV2AVGU3xHYMtMBkLxHajin21x-XeGbB-SZBC_s8GUpv5_9xgypSgBGfITtsf-Jb5YjHJKvd5h753A0kfw=w72-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9v4ZGwvZBeyBSSFh7XEPvFlA4eLPH7X38lXP07ZLudYYYRmcVPKQToNUEnyBiW7r9M4b5k1yjWZn_lpOqsu9RirNCjhqDKWUDtV3OCfSp9zZXQV3LERs-8zgR_s6mHU5Yq1kOt=w592-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-vVjnKWs9pDz3jh5r5we8jFbNwV9_tsDU75_HodGzZrMUBraBqtSbepssaos9NTYed9nLknOfZw-RMwDsCiGty2OVWzZHPMw992-q0LIY9BGXAfoxlsPGdtKPRX-5c_y32niGFhQ=w152-h68-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-h60d5z3wiYT2O6tgor34OEPTzUOaeII-rE8vOcby5GeZ0UEuCRxKwPni6hfZEQqrMTysWzjrddUZAefsnt618N_hvPEYS8E-Jbq5LFXOSplkx68dBrzxChHDr_EQhFC3uLzLU=w472-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8GVhCvmUmWeCfG6ichi9vUt805hZqweflVYXw8iuGJPpBvfkFkHIoZhAFOVnEAA6yTS8E2t9n89NmHCCjLCgoQBlYxymTJZF4Tr8xw_wKOMRXLFbBkk_uOe_ZEF8WgOCUP_uGjyg=w392-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9DVJXKLYc8yZ99jmTFKptdGkUqKWbQwk8G119GV-gXjLmb-iPkL7WolXtSLlbXucyydWv_7UoL6ZabtaLceHQhgscbJoVfw-B0Y6PwhAbHqLQiVy_3SeGSybkXW-XrSw2ck15y=w392-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX91aJuO01Hfw0yO-24Y8EuMdDsnXpAvhQGjy1Yj9BlEN7nZzBzT_c2lqdduUlm8vTIntB08AjpMxfFi12WW1IEZqSWn9vF3HqlnKwQSTiP2EJT587rUqV78NNYcwo_rnwq60FIo=w392-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_WS-02MFTApdWsGN86q0mvGLkHYkbUIgvXRihx-7F4j6WqYne_-zYRptzvjEwKl-KGR3j0XMvBkeHnCy5501TEY9BQZUDQSVOaGZ4eEhIZDoyeZRLMlwfBaMoFGniXOtEaYpi9Ag=w392-h159-v0?authuser=0)

Figure 2: Overview of E-Gen and the cluster-based training framework. Equivalent expressions of each initial expression are generated using an e-graph-based approach, forming clusters of equivalent expressions. The seq2seq model is trained on equivalent expression pairs, while the contrastive learning model is trained on triplets, with each triplet containing a reference expression x, an equivalent positive sample x+, and a non-equivalent negative sample x−. z is the latent space representation of the corresponding input x.
both simple and complex mathematical relationships, significantly enhancing expression diversity and enabling models to efficiently learn underlying mathematical rules with fewer initial expressions.
Initial expression: (x 6 + 2)9 + 3x
−(−2− x 6 )9 + (−3(−x))
3x− (−2− 1 6 x)9
(−1)(−3x− (2 + x 6 )9)
1/(x 6 + 2)−9 + 3x
(−2 + (−1)x/6)9 + 3x
Initial expression: tanh(3x− (−4))− 6
tanh(3x+ 4)− 6
1/ coth(3x+ 4)− 6
sinh(3x+ 4) sech(3x+ 4)− 6
tanh(3/ csc(sin−1(x)) + 4)− 6
sinh(3 cos(cos−1(x)) + 4)/ cosh(3x+ 4)− 6
Initial expression: d dx − 2(lnx/7)−2
4/ ( x(ln(x/7))3
)
−2/ ( x/(ln(x)− ln(7))−3
) × (−2)
−4x−1/ ln(7× x−1)3
−4/(x(ln(7)− ln(x))3)
4 cot(tan−1(x))(ln(x/7))−3
Table 2: Examples of equivalent expressions generated with E-Gen. Expressions listed below each initial expression are part of the equivalent rewrites. Additional examples are in Appendix A.1.
As detailed in Table 3, the E-Gen corpus supports a wider range of operators and achieves a significantly higher average cluster size of 102, compared to the Equivalent Expressions Dataset (EED) (Gangwar and Kani, 2023) that is generated using SymPy and limited to a cluster size of 2 (pairs). This substantial increase in cluster size enables models to develop a deeper semantic understanding of the diversity of mathematical transformations.
Statistic E-Gen EED
# Operators 34 24 Average Cluster Size 102 2 Average Sequence Length 15 16 Train Set Size (Pair) ∼ 55M ∼ 4.66M Train Set Size (Triplet) ∼ 50M -Test Set Size 8,077 5,000
Table 3: Dataset Statistics. Corpus comparison between E-Gen and EED which denotes Equivalent Expressions Dataset from prior work (Gangwar and Kani, 2023).
Training Data. The training dataset is provided in two formats: expression pairs and triplets, corresponding to the two training methodologies described in Section 4. For the seq2seq model, equivalent expression pairs are generated by permuting expressions within each cluster. For contrastive learning, expression triplets are constructed by treating expressions within the same cluster as positive pairs, while randomly sampling expressions from different clusters to serve as negative examples. This process results in a training set comprising 55 million equivalent expression pairs and 50 million expression triplets as shown in Table 3. For the validation set, a subset of clusters is randomly sampled from the corpus, yielding a total of 8,077 expressions. Following Lample and Charton (2019) and Gangwar and Kani (2023) , we use the prefix notation to encode the expressions.
4 Methodology
As illustrated in Figure 2, we employ two wellestablished approaches for learning representations of mathematical expressions: sequence-to-sequence (seq2seq) (Sutskever, 2014; Cho, 2014) equivalent expression generation and contrastive learning (CL) (Wu et al., 2018; Chen et al.,
11775
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8rRma55E2YdaDy8nw3C7qnSPtrPv_6t8gu4yFKBxko_UWHUYcnPSBBUK9EfuVoStt8wG2_ciu18FCbxD6xs6AKMOA8l66jiAGaq1wbq1tX8ofKnsoe1OadIIQcz6znaORFcqJd8Q=w209-h165-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-p_wwoBA6tsG9HhjL_hIK_AWAJRCKWtez_-ClIQfLqmXXa4ERwVU1KX9jy3oLBCyubD23fu7F_g9wVGigjrr5ob71VGgDnnE5IPRfi4XUJ5R_rWZZ5cYBjoulTGbZud3ar_evFBA=w253-h158-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX96FSLQGiykS4hYjvZYlWma1-GnRoc0cSTFFI06j-O3wPVpnWNDgiQoGiaU0623fpyxcAJ3B_UlUKfkydKrWVhfM3HXxWxKLUbBD4009ehyACizU8yeWbQtQEy2z7u9nxvkSrn9vw=w72-h166-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_OBTYE3verytcn2HIHFjueDWKAch4nSsTUMJpHIP9_tjIi1hxjZMNRqvFOPQe5gEX7qI1taEgn55NxDkAJJR9vJLErtGxs8_FLbWfLRbDMLG225GZ20o8Tjh4UsbATPp5P956n=w78-h165-v0?authuser=0)

2020), both leveraging the transformer architecture (Vaswani, 2017). These methods aim to capture the underlying semantic relationships between mathematical expressions by generating meaningful embeddings in a high-dimensional latent space.
4.1 seq2seq Expressions Generation Following prior work (Gangwar and Kani, 2023), we employ the seq2seq framework to learn representations of mathematical expressions by training the model to generate mathematically equivalent expressions. Specifically, given a pair of equivalent expressions, the model takes one as input and is tasked with predicting the other as output. The encoder, during this process, learns to map the input expressions into a latent space where semantically equivalent expressions are clustered together.
4.2 Contrastive Learning The other promising approach to learning mathematical expression representations is contrastive learning, a technique that has gained significant traction in the domain of representation learning. The primary objective is to learn a latent space where semantically equivalent expressions are embedded closer together, while semantically distinct expressions are pushed apart. This is achieved using a contrastive loss function, such as InfoNCE (Oord et al., 2018) or SimCSE (Gao et al., 2021).
In this manuscript, we use a variation of the InfoNCE loss formulated as:
L(f) = E
[ − ln
ef ⊺(x)f(x+)/τ
ef⊺(x)f(x+)/τ + ef⊺(x)f(x−)/τ
] (1)
where f is a transformer encoder f : X → Z that maps an tokenized input expression x ∈ X to its latent representation z ∈ Z . The terms x+ and x−
correspond to positive (equivalent) and negative (non-equivalent) samples respectively, with τ as a temperature hyperparameter.
4.3 Representation Vector To derive the representation vector from the transformer encoder, an additional step is required to convert the output matrix from the encoder’s last layer X ∈ RS×Dmodel to a one-dimensional embedding vector x ∈ RDmodel for each expression. Here, S and Dmodel represent the sequence length of the input and the model dimension. We experiment with two common pooling strategies: average pooling and max pooling over the hidden states of the
last encoder layer. Our empirical analysis and prior work (Gangwar and Kani, 2023) indicate that max pooling consistently outperforms average pooling for the seq2seq model. In the case of contrastive learning, we train two separate models—one with average pooling (CL Mean) and one with max pooling (CL Max)—to evaluate the impact of these strategies on embedding quality. In all models, special tokens, such as the start-of-expression and end-of-expression tokens, are excluded from the pooling process.
5 Experiments
5.1 Evaluation Tasks
The models trained on the E-Gen synthetic dataset, are compared against the prior SEMEMB
model (Gangwar and Kani, 2023) trained on SymPy-generated corpus, on both in-distribution and out-of-distribution tasks, demonstrating the efficacy of the newly presented methods.
K-Means Clustering. K-Means clustering (Mac-queen, 1967) is employed to evaluate the performance of both seq2seq and CL models. The test set comprises 8,077 expressions in 279 clusters, with cluster sizes ranging from 20 to 40 expressions. The K-Means algorithm is applied to group the expressions into clusters. Clustering performance is evaluated by mapping the predicted cluster labels to the corresponding ground truth labels. Accu-racy is computed as the proportion of expressions correctly assigned to their respective clusters. A visualization of clusters is shown in Figure 3.
Model Accuracy (%)
seq2seq 96.72 CL Mean 97.61 CL Max 97.30 SEMEMB 37.70
Table 4: K-Means clustering accuracy (%) of seq2seq, CL Mean, and CL Max, compared against prior SE-MEMB model.
As shown in Table 4, both the seq2seq and CL models trained on the E-Gen cluster-based dataset exhibit strong performance in clustering semantically equivalent expressions while effectively separating non-equivalent ones. The CL models slightly outperform the seq2seq model due to their explicit training objective of grouping semantically equivalent expressions in the latent space. In contrast, SEMEMB, trained on a SymPy-generated corpus,
11776
Figure 3: Visualization of representation vectors for 17 different single-operator mathematical expressions and their equivalent forms using our method (left) and SEMEMB (right). t-SNE (Van der Maaten and Hinton, 2008) is applied to reduce the dimensionality of the embeddings from 512 to 2.
achieves only 37.70% accuracy. This significant performance gap underscores the limitation of the SymPy-generated dataset, which lacks the diversity of mathematical transformations present in the E-Gen corpus. Consequently, SEMEMB struggles to accurately capture and differentiate both subtle and substantial syntactic variations among equivalent expressions.
Semantic Understanding Beyond Syntactic Simi-larity. To assess whether models trained on the E-Gen corpus capture mathematical semantics rather than relying on syntactic similarity, we design an experiment where the model must identify the single semantically equivalent expression among syntactically similar candidates. Specifically, we sample 1,000 query expressions from the test set. For each query, one correct answer is introduced, which is semantically equivalent but structurally distinct from the query. Additionally, six distractors are generated by making minor syntactic modifications to both the query and the correct answer (e.g., altering a single operator or numerical value). These distractors are divided into two groups: three closely resembling the query and three closely resembling the correct answer. The model is tasked with selecting the correct equivalent expression from seven candidates.
As illustrated in Table 5, the correct answer (bolded) is syntactically distinct from the query. Candidate 2, 4, 7 exhibit structural similarity to the correct answer, while candidate 1, 3, 6 closely resemble the query. As shown in Table 6, models trained on the E-Gen corpus significantly outperform SEMEMB, demonstrating their ability to dif-
ferentiate semantically equivalent expressions despite structural variations, as well as to distinguish between syntactically similar yet semantically nonequivalent expressions.
Query expression: d dx
2x+ sin(x− 4)/6
1 d dx
3x+ sin(x− 4)/6
2 2 + tan(x− 4)/8
3 d dx
2x+ sin(x+ 4)/6
4 2 + cos(x/4)/6
5 2 + cos(x − 4)/6
6 d dx
2x+ cos(x− 4)/6
7 9 + cos(x− 4)/6
Table 5: Examples of semantic understanding beyond syntactic similarity. The correct answer is highlighted in bold. Six distractors are generated by introducing minor modifications to the query and the correct answer to assess the model’s ability to distinguish between syntactically similar but semantically different expressions.
Model Accuracy (%)
seq2seq 76.41 CL Mean 50.36 CL Max 48.19 SemEmb 28.62
Table 6: Semantic understanding beyond syntactic similarity accuracy (%) of seq2seq, CL Mean, and CL Max, compared against prior SEMEMB model.
Mistake Detection. Mistake detection in mathematical derivations is an out-of-distribution downstream task, with the test set generated using SymPy to assess the robustness and generalizability of the models.
11777
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8Etpruku4XH2aX2wkGYkgfYdW-ANfXAxlAFcu-lkz6Bg2gbxj-qEQ7LKD6SXAQHXiVdJ2yC69ixXpoSJofBQqZ6Tj-hFHmdFQu1t4Q39gXGl7_-7AIzp5XZKmmtX1JxUIcdfAY=w286-h186-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-_ikeyLGp1jHK-HGoLeiDtnT82dRa4YiS--AUHgPIUtJJ4hTDNDJdL-OrNzJiSY8bo5iFcSDH2pJDnZAt8HuN09e9l9S203Lz2J2PofOtrv0b7UYvpNzJA7dubylAwe8dhvnO4Mw=w286-h186-v0?authuser=0)

Algorithm 1 Threshold Calculation for Mistake Detection
1: input: set of derivations {Di}Ni=1, each containing a sequence of derivation steps Di = {dk}Mk=1
2: output: threshold value t 3: f : transformer encoder 4: g: cosine similarity function 5: x← [] 6: for all Di ∈ {D1, . . . ,DN} do 7: Zi ← f(Di) 8: c← g(Zi[1:],Zi[:-1], dim=-1) 9: c← c \ {cmistake}
10: cmin ← min(c) 11: x← x ∪ cmin
12: end for 13: t← 1
|x| ∑|x|
i=1 xi
14: Return t
For this task, step-by-step mathematical derivations are generated for each expression in the E-Gen corpus, and mistakes are introduced into randomly selected steps within these derivations. The goal is to ask the models to identify erroneous steps by classifying transformations between consecutive steps as either “mistake” or “no mistake”. To achieve this, a semantic similarity threshold for binary classification is calculated using only derivations generated from expressions in the training set of the E-Gen corpus, as described in Algorithm 1. Specifically, cosine similarities are computed between consecutive steps in each derivation, excluding steps with mistakes. The minimum cosine similarity among the correct steps is recorded for each derivation, and the average of these minimum values is used as the threshold. A step is flagged as a mistake if its cosine similarity with the preceding step falls below this threshold.
Derivation seq2seq GPT-4o
− 1 8 (sinh(cosh−1(7− x
−8 )))−1
− 1 8 (sinh(cosh−1(7 + x
8 )))−1
− 1 8 ( √
6 + x 8
√ 8 + x
8 )−1 ⋆
− 1 8 (6 + x
8 )−
1 2 (8 + x
8 )−
1 2
− 1 8 (6 + x
8 )−
1 2 (8 + (1− 8)x)−
1 2 ⋆ ⋆
− 1 8 (6 + x
8 )−
1 2 (8− 7x)−
1 2
5/ csc(csc−1(1/ ln( x −5
)))
5/ csc(csc−1(1/ ln( 1 −5
x)))
5/sec(csc−1((ln( 1 −5
x))−1)) ⋆ 5/(1− (ln( 1
−5 x))2)−
1 2
5 √
1− (ln( 1 −5
x))2
Table 7: Example comparison of mistake detection in mathematical derivations between seq2seq and GPT-4o. Errors in the derivations are in red. The ⋆ symbol indicates that the respective model has predicted the step to contain a mistake.
Examples of mistake detection are shown in Ta-ble 7. Some mistakes are particularly challenging to identify, as they may closely resemble the structure of the preceding step and appear deceptively correct. Conversely, steps with significant syntactic changes that are mathematically equivalent can be misclassified as errors. These challenges highlight the importance of robust semantic understanding to ensure accurate mistake detection.
Model Precision Recall F1
no mistake
seq2seq 96.40 94.69 95.54 CL Mean 97.59 92.52 94.99 CL Max 97.78 91.93 89.14 SEMEMB 92.92 83.49 87.95
mistake
seq2seq 74.68 81.61 77.99 CL Mean 69.33 88.10 77.60 CL Max 67.96 89.14 77.12 SEMEMB 44.46 67.50 53.61
Table 8: Mistake detection evaluation results precision, recall, and F1 (%) scores of seq2seq, CL Mean, and CL Max, compared against prior SEMEMB model.
The test set comprises 18,462 derivation steps, of which 2,974 steps contain mistakes, with the remainder being error-free. As shown in Table 8, precision, recall, and F1-score are used to evaluate model performance. Models trained on E-Gen corpus demonstrate strong effectiveness in identifying potential mistakes and better generalizability on this OOD task, significantly outperforming the SEMEMB approach.
Embedding Algebra. Embedding algebra is a classic task to evaluate if embeddings capture semantic information of a word/token. Techniques such as word2vec (Mikolov, 2013) and GloVe (Pen-nington et al., 2014) exhibit the ability to perform analogy-based reasoning through algebraic operations on their representation vectors, enabling solutions to analogies like “Berlin is to Germany as Paris is to France”. Extending this task to mathematical expressions allow us to assess whether models truly understand mathematical transformations or merely rely on surface-level structural similarity. For a given triplet of expressions x1, y1, and x2, we compute:
f(ŷ2) = −f(x1) + f(y1) + f(x2) (2)
where f denotes a function f : X → Z , which maps an expression x to its representation vector z in the latent space. The expression whose embedding vector has the highest cosine similarity to
11778
x1 y1 x2 ŷ2 (seq2seq) ŷ2 (SEMEMB) ŷ2 (GPT-4o) ygt
1 sin(x) − sin(−x) cos(x) cos(−x) − tan(−x) cos(−x) cos(−x) 2 cos(x) sec(x) tanh(x) coth(x) coth(x) sech(x) coth(x)
3 sinh−1(x) csch−1(1/x) tanh−1(x) coth−1(1/x) - coth−1(x) coth−1(1/x)
4 tan(x) tan(x+ π) csc(x) csc(x+ 2π) cot(x+ π) csc(x+ 2π) csc(x+ 2π)
5 sin(x) cos(x− π/2) sec(x) csc(x+ π/2) sec(x− π/2) csc(x− π/2) csc(x+ π/2)
6 x lnx coth(x) ln coth(x) coth ln(x) coth−1(x) ln coth(x)
7 x lnx cos−1(x) cos−1(lnx) cos−1(lnx) ln cos−1(x) ln cos−1(x)
8 x csc−1(x) csch(x) csc−1(csc(x)) - csch−1(x) csc−1(csc(x))
9 x x+ 1 tan−1(x) tan−1(x)× 1 tan−1(x) + 1 tan−1(x) + 1 tan−1(x) + 1
10 x x3 sinh−1(x) sinh−3(x) sinh−3(x) sinh−3(x) sinh−3(x)
Table 9: Example comparison of embedding algebra predictions between the seq2seq, SEMEMB, and GPT-4o. The model’s prediction is denoted as ŷ2, while ygt represents the ground truth. Incorrect predictions are in red. Additional experimental results are provided in Appendix C.3.
f(ŷ2) is selected as the predicted answer, excluding the original expressions x1, y1, and x2 from consideration.
For this experiment, 584 analogy examples are manually constructed. The entire E-Gen corpus serves as the search pool, with expressions equivalent to x2 and y2 removed to ensure uniqueness of the correct answer. Any necessary expressions are added to complete the analogy.
Model Accuracy (%)
seq2seq 70.38 CL Mean 64.73 CL Max 50.34 SEMEMB 54.85 GPT-4o 39.60
Table 10: Embedding algebra accuracy (%) of seq2seq, CL Mean, and CL Max, compared against prior SE-MEMB model and GPT-4o.
As shown in Table 10, the seq2seq model achieves the highest accuracy, indicating its ability to learn underlying mathematical rules and handle basic substitutions effectively. In contrast, SE-MEMB exhibit low accuracy on this task and have a tendency to imitate the transformation between x1 and y1, leading to “look-alike” predictions rather than true understanding of the mathematical rules, as seen in Test 1, 4, 5 in Table 9.
5.2 Comparison with GPT-4o
To further assess the quality of vector representations of symbolic expressions, a comparative analysis is conducted between the seq2seq model, trained on the E-Gen corpus, and the state-of-the-art large language model GPT-4o (Achiam et al., 2023) on two tasks.
Mistake Detection. For mistake detection, a small test set is randomly sampled from the mistake detection test set described earlier. This subset consists of 322 derivation steps, including 50 steps containing mistakes, while the remainder are error-free. GPT-4o is first provided with an example derivation in the prompt and asked to identify potential mistakes. If it fails to detect the mistake, explicit feedback indicating the erroneous step is provided until it correctly understands the task. Once verified, GPT-4o is tested on queries from the sampled test set.
Model Precision Recall F1
no mistake
seq2seq 96.98 94.49 95.72 CL Mean 97.64 91.18 94.30 CL Max 97.78 91.93 94.77 GPT-4o 93.58 90.84 92.19
mistake
seq2seq 73.68 84.00 78.50 CL Mean 64.71 88.00 74.58 CL Max 67.96 89.14 77.12 GPT-4o 56.90 66.00 61.11
Table 11: Mistake detection evaluation results precision, recall, and F1 (%) scores of seq2seq, CL Mean, and CL Max compared with GPT-4o.
As shown in Table 11, our approach outperforms GPT-4o across all evaluation metrics. While GPT-4o demonstrates a recall of 66%, suggesting its capability of detecting a notable portion of errors, its low precision indicates a tendency to misclassify correct transformations as mistakes, leading to a high rate of false positives.
Table 7 illustrates examples of GPT-4o’s misjudgments, which commonly occur in complex transformations, particularly those involving function operators or relatively intricate arithmetic computations. For instance, in Example 1, GPT-4o fails
11779
to recognize the equivalence between syntactically different expressions (e.g., sinh(cosh−1(x)) =√ x+ 1
√ x− 1). In Example 2, it incorrectly clas-
sifies an operator substitution in step 3 as a valid derivation, failing to detect the mistake.
Embedding Algebra. We also conduct the embedding algebra task on GPT-4o, which performs worse than both the seq2seq and CL models, achieving only 39.60% accuracy on the test set as shown in Table 10. Table 9 provides examples comparing the performance of the seq2seq model and GPT-4o on embedding algebra tests. Similar to the mistake detection test, an example query is provided to GPT-4o to verify its understanding before proceeding with the test.
While the seq2seq model consistently makes accurate predictions by adhering to mathematical rules, GPT-4o demonstrates only a partial understanding of certain mathematical properties. For instance, it correctly predicts the periodicity of “csc(x)” but often mimics the structure of “y1” rather than applying the underlying mathematical transformations. In Test 5, GPT-4o incorrectly subtracts “π/2” from “x” in “csc(x)”, imitating the structure of “y1”, while the correct answer should be “csc(x+ π/2)”, which is mathematically equivalent to “csc(x)”. A similar error occurs in Test 8, where GPT-4o predicts “y2” as “csch−1(x)” by replicating “y1 : csc−1(x)” instead of applying the correct mathematical transformation. This comparison highlights the effectiveness of E-Gen corpus in helping models to build up understanding in mathematical rules and transformations.
6 Conclusion
In this work, we enhance semantic representations of symbolic expressions by developing E-Gen, a novel mathematical corpus generation framework based on the e-graph data structure. E-Gen shows strong capability in the generation of a scalable, cluster-based corpus with high diversity in mathematical transformation. To evaluate its effectiveness, two training approaches based on seq2seq and contrastive learning respectively are implemented to capture equivalence relation between expressions. Our experimental results demonstrate the efficacy of these embedding models across a variety of downstream tasks, including clustering, semantic understanding beyond syntactic similarity, mistake detection, and mathematical analogies. No-tably, these semantic representations outperform
prior approach and GPT-4o in both quantitative and qualitative tests. This work provides an algorithmic foundation for processing symbolic mathematics, and the vector-based representations can easily integrate with vector embeddings of other data modalities.
Limitations
This work introduces and evaluates the potential of a novel mathematical corpus generation framework to augment mathematical semantic understanding. While the results are promising, there are several areas for improvement.
First, extending the dataset to include a wider range of mathematical operators used in published datasets, such as ArXMLiv (Kohlhase et al., 2024) and ARQMath (Mansouri et al., 2022b), would improve the applicability of the learned embeddings to real-world mathematical data.
Following that, more efficient grammar enumeration techniques, such as those based on the Earley algorithm (Earley, 1970), could facilitate the extension of the E-Gen corpus to support more complex operators and higher-arity expressions. In this manuscript, equivalent expressions are generated by enumerating the grammar obtained from the e-graph using a simple recursive function. Addition-ally, incorporating variable characteristics, such as dimensionality, phase, and/or bounds, into the embeddings remains an unexplored but promising direction for improving their expressiveness.
Another limitation is the scarcity of real-world datasets that focus on symbolic mathematics. While tasks like mathematical information retrieval have been explored in competitions such as NT-CIR (Zanibbi et al., 2016a) and ARQMath (Man-souri et al., 2022b), these typically involve a mixture of symbolic mathematics and natural language in queries and results. Integration of our embedding methods with natural language vectors remains an open research challenge with significant potential for advancing mathematical information retrieval and reasoning.
Acknowledgments
We would like to thank the University of Illinois for its support in facilitating this research. We would also like to extend our gratitude to the National Center for Supercomputing Applications (NCSA) for providing access to high-performance computing resources.
11780
References Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. 2023. GPT-4 technical report. arXiv preprint arXiv:2303.08774.
Miltiadis Allamanis, Pankajan Chanthirasegaran, Push-meet Kohli, and Charles Sutton. 2017. Learning continuous semantic representations of symbolic expressions. In International Conference on Machine Learning, pages 80–88. PMLR.
Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. 2020. A simple framework for contrastive learning of visual representations. In In-ternational conference on machine learning, pages 1597–1607. PMLR.
Kyunghyun Cho. 2014. Learning phrase representations using RNN encoder-decoder for statistical machine translation. arXiv preprint arXiv:1406.1078.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. 2024. The Llama 3 herd of models. arXiv preprint arXiv:2407.21783.
Jay Earley. 1970. An efficient context-free parsing algorithm. Communications of the ACM, 13(2):94–102.
Simon Frieder, Luca Pinchetti, Ryan-Rhys Griffiths, Tommaso Salvatori, Thomas Lukasiewicz, Philipp Petersen, and Julius Berner. 2024. Mathematical capabilities of ChatGPT. Advances in neural information processing systems, 36.
Neeraj Gangwar and Nickvash Kani. 2023. Seman-tic representations of mathematical expressions in a continuous vector space. Transactions on Machine Learning Research.
Liangcai Gao, Zhuoren Jiang, Yue Yin, Ke Yuan, Zuoyu Yan, and Zhi Tang. 2017. Preliminary exploration of formula embedding for mathematical information retrieval: can mathematical formulae be embedded like a natural language? arXiv preprint arXiv:1707.05154.
Tianyu Gao, Xingcheng Yao, and Danqi Chen. 2021. SimCSE: Simple contrastive learning of sentence embeddings. arXiv preprint arXiv:2104.08821.
Mor Geva, Ankit Gupta, and Jonathan Berant. 2020. Injecting numerical reasoning skills into language models. arXiv preprint arXiv:2004.04487.
Emma Hamel, Hongbo Zheng, and Nickvash Kani. 2022. An evaluation of NLP methods to extract mathematical token descriptors. In International Confer-ence on Intelligent Computer Mathematics, pages 329–343. Springer, Springer.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Os-trow, Akila Welihinda, Alan Hayes, Alec Radford, et al. 2024. GPT-4o system card. arXiv preprint arXiv:2410.21276.
Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richard-son, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. 2024. OpenAI o1 system card. arXiv preprint arXiv:2412.16720.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men-sch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guil-laume Lample, Lucile Saulnier, et al. 2023. Mistral 7b. arXiv preprint arXiv:2310.06825.
Hwiyeol Jo, Dongyeop Kang, Andrew Head, and Marti A Hearst. 2021. Modeling mathematical notation semantics in academic papers. In Findings of the Association for Computational Linguistics: EMNLP 2021, pages 3102–3115.
Michael Kohlhase et al. 2024. arxmliv project. https://kwarc.info/projects/arXMLiv/. Ac-cessed: 2024-09-17.
Giovanni Yoko Kristianto, Akiko Aizawa, et al. 2014. Extracting textual descriptions of mathematical expressions in scientific papers. D-Lib Magazine, 20(11):9.
Giovanni Yoko Kristianto, Goran Topic, and Akiko Aizawa. 2016. MCAT math retrieval system for NTCIR-12 MathIR task. In NTCIR.
Kriste Krstovski and David M Blei. 2018. Equation embeddings. arXiv preprint arXiv:1803.09123.
Guillaume Lample and François Charton. 2019. Deep learning for symbolic mathematics. arXiv preprint arXiv:1912.01412.
Guillaume Lample, Timothee Lacroix, Marie-Anne Lachaux, Aurelien Rodriguez, Amaury Hayat, Thibaut Lavril, Gabriel Ebner, and Xavier Martinet. 2022. Hypertree proof search for neural theorem proving. Advances in neural information processing systems, 35:26337–26349.
I Loshchilov. 2017. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101.
Ilya Loshchilov and Frank Hutter. 2016. SGDR: Stochastic gradient descent with warm restarts. arXiv preprint arXiv:1608.03983.
Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chun-yuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. 2023. MathVista: Evaluating mathematical reasoning of foundation models in visual contexts. arXiv preprint arXiv:2310.02255.
11781
J Macqueen. 1967. Some methods for classification and analysis of multivariate observations. In Proceed-ings of 5-th Berkeley Symposium on Mathematical Statistics and Probability/University of California Press.
Behrooz Mansouri, Anurag Agarwal, Douglas W Oard, and Richard Zanibbi. 2022a. Advancing math-aware search: the ARQMath-3 lab at CLEF 2022. In Eu-ropean Conference on Information Retrieval, pages 408–415. Springer.
Behrooz Mansouri, Vít Novotnỳ, Anurag Agarwal, Dou-glas W Oard, and Richard Zanibbi. 2022b. Overview of ARQMath-3 (2022): Third CLEF lab on answer retrieval for questions on math. In International Con-ference of the Cross-Language Evaluation Forum for European Languages, pages 286–310. Springer.
Behrooz Mansouri, Vít Novotnỳ, Anurag Agarwal, Dou-glas W Oard, and Richard Zanibbi. 2022c. Third CLEF lab on answer retrieval for questions on math (working notes version. Proc. CLEF 2022 (CEUR Working Notes).
Behrooz Mansouri, Shaurya Rohatgi, Douglas W Oard, Jian Wu, C Lee Giles, and Richard Zanibbi. 2019. Tangent-CFT: An embedding model for mathematical formulas. In Proceedings of the 2019 ACM SIGIR international conference on theory of information retrieval, pages 11–18.
Jordan Meadows and Andre Freitas. 2022. A survey in mathematical language processing. arXiv preprint arXiv:2205.15231.
Kazem Meidani, Parshin Shojaee, Chandan K Reddy, and Amir Barati Farimani. 2023. SNIP: Bridging mathematical symbolic and numeric realms with unified pre-training. arXiv preprint arXiv:2310.02227.
Aaron Meurer, Christopher P. Smith, Mateusz Pa-procki, Ondřej Čertík, Sergey B. Kirpichev, Matthew Rocklin, AMiT Kumar, Sergiu Ivanov, Jason K. Moore, Sartaj Singh, Thilina Rathnayake, Sean Vig, Brian E. Granger, Richard P. Muller, Francesco Bonazzi, Harsh Gupta, Shivam Vats, Fredrik Johans-son, Fabian Pedregosa, Matthew J. Curry, Andy R. Terrel, Štěpán Roučka, Ashutosh Saboo, Isuru Fer-nando, Sumith Kulal, Robert Cimrman, and Anthony Scopatz. 2017. SymPy: symbolic computing in python. PeerJ Computer Science, 3:e103.
Tomas Mikolov. 2013. Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781.
Maxwell Nye, Anders Johan Andreassen, Guy Gur-Ari, Henryk Michalewski, Jacob Austin, David Bieber, David Dohan, Aitor Lewkowycz, Maarten Bosma, David Luan, et al. 2021. Show your work: Scratch-pads for intermediate computation with language models. arXiv preprint arXiv:2112.00114.
Aaron van den Oord, Yazhe Li, and Oriol Vinyals. 2018. Representation learning with contrastive predictive coding. arXiv preprint arXiv:1807.03748.
Robert Pagael and Moritz Schubotz. 2014. Mathe-matical language processing project. arXiv preprint arXiv:1407.0167.
Shuai Peng, Ke Yuan, Liangcai Gao, and Zhi Tang. 2021. MathBERT: A pre-trained model for mathematical formula understanding. arXiv preprint arXiv:2105.00377.
Jeffrey Pennington, Richard Socher, and Christopher D Manning. 2014. Glove: Global vectors for word representation. In Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP), pages 1532–1543.
Nicholas Popovic, Walter Laurito, and Michael Färber. 2022. AIFB-WebScience at SemEval-2022 task 12: Relation extraction first–using relation extraction to identify entities. arXiv preprint arXiv:2203.05325.
Shaurya Rohatgi, Wei Zhong, Richard Zanibbi, Jian Wu, and C Lee Giles. 2019. Query auto completion for math formula search. arXiv preprint arXiv:1912.04115.
Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D Manning, Andrew Y Ng, and Christopher Potts. 2013. Recursive deep models for semantic compositionality over a sentiment treebank. In Proceedings of the 2013 conference on empirical methods in natural language processing, pages 1631–1642.
I Sutskever. 2014. Sequence to sequence learning with neural networks. arXiv preprint arXiv:1409.3215.
Goran Topić, Giovanni Yoko Kristianto, Minh-Quoc Nghiem, and Akiko Aizawa. 2013. The MCAT math retrieval system for NTCIR-10 math track. In Pro-ceedings of 10th NTCIR Conference, Tokyo, Japan, pages 680–685.
Laurens Van der Maaten and Geoffrey Hinton. 2008. Visualizing data using t-SNE. Journal of machine learning research, 9(11).
A Vaswani. 2017. Attention is all you need. Advances in Neural Information Processing Systems.
Qingxiang Wang, Chad Brown, Cezary Kaliszyk, and Josef Urban. 2020. Exploration of neural machine translation in autoformalization of mathematics in mizar. In Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs, pages 85–98.
Sean Welleck, Jiacheng Liu, Ronan Le Bras, Hannaneh Hajishirzi, Yejin Choi, and Kyunghyun Cho. 2021a. NaturalProofs: Mathematical theorem proving in natural language. arXiv preprint arXiv:2104.01112.
Sean Welleck, Jiacheng Liu, Jesse Michael Han, and Yejin Choi. 2021b. Towards grounded natural language proof generation. In MathAI4Ed Workshop at NeurIPS.
11782
Max Willsey, Chandrakana Nandi, Yisu Remy Wang, Oliver Flatt, Zachary Tatlock, and Pavel Panchekha. 2021. Egg: Fast and extensible equality saturation. Proceedings of the ACM on Programming Languages, 5(POPL):1–29.
Yuhuai Wu, Albert Qiaochu Jiang, Wenda Li, Markus Rabe, Charles Staats, Mateja Jamnik, and Christian Szegedy. 2022. Autoformalization with large language models. Advances in Neural Information Pro-cessing Systems, 35:32353–32368.
Zhirong Wu, Yuanjun Xiong, Stella X Yu, and Dahua Lin. 2018. Unsupervised feature learning via nonparametric instance discrimination. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 3733–3742.
Ke Yuan, Dafang He, Zhuoren Jiang, Liangcai Gao, Zhi Tang, and C Lee Giles. 2020. Automatic generation of headlines for online math questions. In Proceed-ings of the AAAI Conference on Artificial Intelligence, volume 34, pages 9490–9497.
Richard Zanibbi, Akiko Aizawa, Michael Kohlhase, Iadh Ounis, Goran Topic, and Kenny Davila. 2016a. NTCIR-12 MathIR task overview. In NTCIR.
Richard Zanibbi, Kenny Davila, Andrew Kane, and Frank Wm Tompa. 2016b. Multi-stage math formula search: Using appearance-based similarity metrics at scale. In Proceedings of the 39th International ACM SIGIR conference on Research and Development in Information Retrieval, pages 145–154.
Richard Zanibbi, Behrooz Mansouri, and Anurag Agar-wal. 2024. Mathematical information retrieval: Search and question answering. arXiv preprint arXiv:2408.11646.
Jiaru Zou, Qing Wang, Pratyush Thakur, and Nickvash Kani. 2024. STEM-PoM: Evaluating language models math-symbol reasoning in document parsing. In The 4th Workshop on Mathematical Reasoning and AI at NeurIPS’24.
11783
A Cluster-Based Corpus
A.1 Cluster Example
Initial expression: (sin(2x+ 5))−8
(sin(5− (−2) sin(sin−1(x))))−8
(csc(π + (−5− 2x)))8
(cos(π/2− 2x− 5)))−8
( cot(2x+5) cos(2x+5)
)8
(sin(2(x+ π) + 5))−8
Initial expression: sec−1(7x+ 6)/(−7)
cos−1( 1 6−(−7x)
)/(−7) (sec−1(−7x− 6)− π))× 1
7
(π 2 − csc−1(7x+ 6))/(−7)
(−1)(sec−1(7/ sec(cos−1(x)) + 6))/7
(cos−1(cot(tan−1(7x+ 6))))/(−7)
Initial expression: (csc(x/7))−3 − (−3)
1/ ( csc
( tan(tan−1 x)
7
))3
+ 3
(tan(cot−1(sin(x 7 ))))−3 + 3
3 + ( 1/ cos(sec−1(sin(x
7 )))
)3 −1(−3− (csc(x
7 ))−3)
(sin(x 7 ))3 + 3
(sin(csc−1(sin(7−1x)))−3 − (−3)
Initial expression: d dx
(−4x− 8)−4 + 7x
(−1)× (8− (−4x))−5 × 16 + 7
−16× (4x+ 8)−5 + 7
7 + (−16)× ( −1/(−4x− 8)5
)
7− (−16)× (−1)× (8− (−4x))−5
0− (−16(−4x− 8)−5 − 7)
Initial expression: d dx
(−9 sinh(−7x+ 2))
63/ sech(−7x+ 2)
−9/(−1/7 cosh(7x− 2))
63 cosh(2− 7x) 63 2 (exp(2− 7x) + exp(7x− 2))
7× 9/ sech(7x− 2)
Table 12: Additional examples of equivalent expressions clusters generated with E-Gen. Expressions listed below each initial expression are all equivalent to it.
As discussed in Section 3.2, the key distinction of the E-Gen corpus from prior datasets is its cluster-based organization of equivalent expressions, rather than equivalent expression pairs. Ta-ble 12 presents additional examples of these clusters. Each cluster consists of an initial expression along with numerous equivalent rewrites. This diverse set of transformations significantly enhances pretrained models’ ability to understand and generalize mathematical semantics, leading to improved performance in downstream tasks.
A.2 Generation Efficiency
Efficiency is a key property of any corpus generation scheme. To assess the computational performance of E-Gen, we measure the average time required for e-graph saturation and expression rewrite extraction. On an Intel Xeon E5-2666 CPU, the e-graph saturation process takes 36.83ms on average, and the extraction takes an average of 1.46s per expression. These evaluations are conducted with a 25-token length limit and a 600s timeout per initial expression.
B Training Details
Configuration Value
Transformer Architecture
Model Dimension 512 Attention Heads 6 Feedforward Dimension 2048 Encoder Layers 6 Decoder Layers 6 Dropout -
Optimizer
Optimizer AdamW Learning Rate 1× 10−4
Weight Decay 1× 10−2
Scheduler
Scheduler CosineAnnealWarmRestarts T0 10 Tmult 2 ηmin 1× 10−8
Training Parameters
Label Smoothing 0.1 Batch Size 256 Epochs 20 Gradient Clipping 4.0
Hardware Configuration
CPU AMD EPYC 7763 (64-Core) GPU NVIDIA L40S (46GB)
Table 13: Hyperparameters and hardware specifications for training the seq2seq, CL Mean, and CL Max models. The transformer-based models are optimized using AdamW with a cosine annealing warm restart scheduler. Training was conducted on an AMD EPYC 7763 CPU and a Nvidia L40S GPU.
Both the seq2seq and contrastive learning models are trained using a transformer architecture, optimized with the AdamW optimizer (Loshchilov, 2017), and scheduled with CosineAnnealingWarm-Restarts scheduler (Loshchilov and Hutter, 2016). The specific training parameters and time are detailed in Table 13 and Table 14 respectively.
11784
Model Training Time (h:min)
seq2seq 38:04 CL Mean 31:56 CL Max 29:59
Table 14: Training time of seq2seq, CL Mean, and CL Max models.
C Experiments
C.1 K-Means Clustering Accuracy Calculation. Since all expressions from the same cluster are labeled in the same class, the accuracy for K-Means clustering in Section 5.1 is calculated as follow.
acc = 1
K
K∑
i=1
acci (3)
where acci denotes the accuracy of cluster i, which is computed as follow.
acci = 1
|ci| ∑
xj∈ci 1{g(xj)=ci} (4)
where g(xj) denotes the cluster predicted by K-Means algorithm, and ci is the ground truth cluster of expression xj .
C.2 Formula Retrieval Formula retrieval is implemented as an additional task to assess the models’ semantic understanding of mathematical expressions. As discussed in Section 1, prior MIR studies heavily rely on contextual cues for semantic representation (Gao et al., 2017; Krstovski and Blei, 2018) rather than directly capturing the intrinsic mathematical property of expressions. This limitation results in suboptimal performance, particularly in scenarios with limited surrounding text, such as textbook or mathematical derivations. To evaluate the models’ performance in this scenario, we design a pure formula retrieval task using the E-Gen corpus. Given a query expression, the top-k most similar expressions are retrieved based on cosine similarity in the latent space.
We evaluate formula retrieval using the E-Gen test set, which contains 8,077 expressions. Each expression serves as a query, while the remaining expressions act as retrieval candidates. Figure 4 illustrates an example where the top-4 most similar candidates to cosx are retrieved in the latent space. As shown in Table 15, both seq2seq and CL models
trained on E-Gen corpus effectively retrieve semantically relevant expressions from the candidate pool as k increases. Conversely, SEMEMB, which is constrained by a limited number of equivalent rewrites per expression, struggles to identify semantically equivalent expressions when k exceeds 10.
Figure 4: Example of the formula retrieval with seq2seq model. The query expression is cos(x) in darker blue, and the rest are candidates. Top-4 expressions are retrieved. t-SNE is applied to reduce the dimensionality of the embeddings from 512 to 2.
Model k=5 k=10 k=15 k=20
seq2seq 99.93 99.82 99.76 99.41 CL Mean 99.85 99.73 99.50 98.94 CL Max 99.78 99.52 99.32 98.82 SemEmb 73.47 60.57 51.95 45.56
Table 15: Formula retrieval accuracy (%) of seq2seq, CL Mean, and CL Max, compared against prior SEMEMB model at different top-k values. Accuracy denotes the proportion of top-k ranked candidates that are semantically equivalent to the query expression.
C.3 Embedding Algebra Table 16 and 17 provide additional examples from embedding algebra task. The seq2seq model correctly predicts most of the answers, outperforming other models. CL Mean slightly outperforms, CL Max, SEMEMB, and GPT-4o. Notably, SEMEMB
and GPT-4o use a similar strategy to predict “y2”. For instance, Tests 6 to 11 specifically evaluate the models’ understanding of function periodicity, where the seq2seq model trained on the E-Gen corpus accurately predicts “y2” in most cases. In contrast, as discussed in Section 5.2, SEMEMB, similar to GPT-4o, tends to imitate the transformation between “x1” and “y1” rather than correctly applying the periodicity of the function. For instance, in Test
11785
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX98ErlNzu51seaHu_yN99vVdfQvZ9p1T_TfmgQGeI6HY7RjXfqQYJIGqbnBJW4eGL_vRbni4lVfflMQyoDjW21v4FSaopJSTXMLpUpZynZtdnt99ilNvJYkjJtXJXNcD4x1xxEdyA=w242-h196-v0?authuser=0)

6, “x1 : sin(x)” and “y1 : sin(x+ 2π)” are equivalent due to the 2π period of “sin(x)”. However, since “x2 : cot(x)” has a period of π, the correct “y2” should be “cot(x+ π)”. The SEMEMB
model just simply imitates the transformation from “x1” to “y1” by adding “2π” to “x” in “cot(x)”, and incorrectly converts “cot(. . .)” into “csc(. . .)”. This comparison highlights that the models trained with E-Gen corpus shows a better understanding of mathematical rules and transformations, rather than relying on superficial "looks-like" predictions.
11786
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_jynvSVFgxEsUxSZ_edsSe-AbZe3SkpIHauEkuqrGu8pQd-lWnW2om3JXk3BlBrtCwDz9VuC9L4XXGICEsWZLTmbBPeo_1wvV7JkLUKAJqklSey-LEcaZdjRUto4g3JfgIcIpd9w=w1252-h350-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_kIHOpgyas1OLQ8HryXSNeARPxMd-vwh_XwYftuK81f8SZrFZ9pPBp4SPmhC6xYR1BpBBLSXodus1CkJ2ePTZtvkEhu-VXreeFTpITQshpBHbHl36cOsa-T3vyRDP1rooEjhb_5A=w1280-h341-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_Sb7eXgby_WJQQr5B0pNr_3mlg_RYUZ6AiINFW4jRHTjZ47GfKzTCNJpxD7WG_qvp2-wRFnxroH1T_hf0uujNOZ5v1TSFNy4aSCufshSWqva48gOmt3NDy5HNH6V01bs6c-jg1=w1192-h350-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9HmBjnGYcMdRDW357xN9HLGECWqnuz3jwzIo0e3am-DLsX__QBzGNQZRw_yOnlrK5GxCljVBNVa18gQso-FUyARvi4tKUL5lpCWyAQ0bYCaYNzgn5IVAXqSVZSvCYL6TheuWDKYQ=w1032-h310-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9M7sNRmTVrh-iQu8pANuzUXpBQC8I4muVpRnOqiGDqHSOnAmE98J8pL61T5lcK9_laknTRWf6hd_PedB3rWIUh_T7tqMhxDnEyl73N_fOcisuIGs2cpitQ72zKRBH6ezunHOKUcA=w872-h362-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX85gicDJuzG9jQYbQvYjwZO9_fOIq1UiTKZokpTHzGvC0ZQS1mL_Re4HX-2GwSrZOT39XtXdc8vRVPS19fNKhCgWATimnain_0G0hXYf7Cj3XwVRSJEjZ94qbH3z7E61723n08b4Q=w1012-h322-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_DRoeAI-xxfaB-4jh8fSQzldvhHENfiyX2HhpRtPzYou8fOVcQ_Ib45Lvc0H6PpRpl3laMQlYWaNiOrbMrpe3vxHzs5UXHSvLS-oItnkOqkoa-hyt-ptOP__kHeoAllDh6tmxmZg=w1052-h322-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_NdLlNBEkVDYhFExQbA6s2VYqMMjfdfVMS5t8XuGj0TueuRS03djPuQb5afH8I0a42kufFfwCt_fV5LitHU34XAMt4JEgs5Uz6xEWgUPRPquae6qpZoy-qtGNS_CnYPq2Jd6JrNw=w1032-h322-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9MWfnBS3jyOHAfrUGwDFIyKwA0S8fMh_nd7Yudqjc0JR4nLm8F0JYuqIUR8OUkDKdxrVbVWkcpqsMwfgDMUslOw8xeAt31HcpIfhZxPbt08AHVSERlpIrzlfzb-YP0hDcbqqIV=w1152-h322-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9c55lo4eMCBi7TxBuE-8vuIFm3hUJ2Dk9QM8DjYl3sqQ6WsI4DsQ_CWiLNbzSqZ_2zVkDYkulhmk6knJQajyYrqGouOZ6HLv3c3g0KTyo42pYXi1tcJzHKKQfbaUP3pNQecUohgg=w972-h322-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9oIk9EyMqWa2KKwdKgl1VpXWFQgRdQZjAVZ2BtU9GNjkYWVUD5ShdSbQq_oDYJjgG28tQ5fmjeYj4jXpmDWXGXxbbVLaa9rjtfWToUqB-VKVDAbSWL28UrsPG4ZsVYDC7mR2RFSQ=w852-h322-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9i4eHsTka6NtG2y6iHDqLAboFMpxG7W1UMHFzpf6v8Fv-YL0VLBlHV_xo6GKtFOekqPHVaSK2_xFaWkXcL39jmcd8H6hA1xV2rDHtQ6ZV66byNxJILDEKQN5ujprmVQq4j4pwJEg=w1280-h107-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9KInQWOEsGX_AIGuuI6vAbq10lztjQkQSuF9L7kgXcnHq0mNW7wAbc4qBLqxghvVUfeo28c_eP6OWNK4-nJ0jI8X03FA9n2saqLOyltCv6au0B1a7T07EdgmbpzDfPMHsGrVkL4w=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9jyd2UY376tm6QNZrd2JldjOtFu2XHWsQDrqPrPZN7ftptAKgidzj-4xdW4Q6ZXuu_kEw_dvGHzi4Zjhs8D2usBlOTXOvytjoVOc1CfGg-hnsz0N7BAiUB79dN4XuvBUYiEPGZuw=w792-h108-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8mz6zDRxr1zpueHHTnoKcEd_i4RmQ8jRbPekvJNs8Sq4yGG9Laa51AWZwlK4iFQPcOwvLjM_rOQlmZ5kA3vvShXvl2DVkz_m43luWyZId5NaOSkGWSyPBqCG63s93v6UmppjAPug=w792-h135-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8JFCOfznrHecm4rQ0mCsOe-1DjjKP-0ivWwxUA_Qg3qH3JEpgaAvY1h5oqyMpnByv3b7TlCQr2oHYgGpVjtKiOrdmqP7Yuau_hbYhhB9K5m8cWdkGZ0t0eX2YETbnLBIixA7C6wg=w1280-h777-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9DYG_bdHmE6PplbTdMjhhHigkLKBzetyd3qF7MvTj73IGOrqq5lX4yVXeRQSYCGLL_EraAGJWJDoH8F-79Iotkvw4qNmiNSolPddSLR6ZFzymv2wDv0sCHpJFcecxyAgg8NjKu=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-NgrUtEuuPpVIs3pM0oUtjOXKlp2IpCZ2tdXqkshzkIzb3i3x4xkHsBCx24Xrdyr6PTEjdBQRsUxB8G-BW52coKyXc1Zy6b8rjTJLGjcUaQATcRjxppLP1WdJJRc-daNDkqofFWw=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_pKxjz6fZyTJwWrUSgkTbkNm9Yb0kXQo64tBIv_mCflEoWGDLHELuz8v_fu1RL0hS1pSv_h1zVHbiXlPLqU0gnkDJDJM4IMRKoBTZYw6g7FVNRSeQGPVN08n7y_SZ79S8lYyh9EQ=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-IzctbAn4e6hLOQ51ugQxwL13OAoZFBFbSBdSupIPgNMC1Fc10gLRhnBcLcniHm4SBvESsnnJTg02AsMo3PuwHuAeJCE78qKKhqxQmMasryOy3CaFUxJNs-FwycK7oh8OMKTDhSQ=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-hCVha4BrkFP5Zh7pLMHaKSdTmvu_Jm5SiEhtwPq6-kQXhuD330IkM7o3JUfDRi7JLZ8aFkE9AYVREsb0Pd0I10ii2XB3btvcvQLR5WdwaP0V20IKZvD76EM739WOM_w68qy9nzQ=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_1ziQJhj6gdsgKScO87V6sPhphO6EEwGoZ0jtmTv0CO-ppsU2oeLHfnLFlXyoQKfqhTCFnnwun44LRBeRXznisy13Oni3A4hSpIV0AlTWoOXyoWc435Sl1f7s-822_h3F0axnveg=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8bdlbQLzISLwGaGgrualYnP1I7WcD-ftyGEVyhOaTBTtxLxTk26yzYB0E0wlk5o0p_sFKjoEXSxaMAQRJkmKZboBu-IFfX27ynz4Pmuz-5EKX-OG6UJXnMFKeVad_cY1QNXJv3sQ=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-IA2R7D32hx9XspvFn5HnsFz944wirvJGuBW4fRWQaBd04k6Hz1ZeTMXzBAvfmK5B_NK9Twrz6yZTnHkRZiPoaYlDbjhoZPxTpQpYMRuTV-FbIlHABXYobN9UrLGO5NYWr3CivNQ=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8FktuSAY6mr2E1PSiRghOC7B7HatHF5cQGmdju-69-BGySHZVphgGPG2yrqcHNKiU_iL4EzYXTQSv0tRqCVZQAlJod4KjBkJOUFKf9z3wkxEwoKbOKTpzJ-KcjHf7zXJOZf03KoQ=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX80piSaVbWzdMwmp6Tb1j9IIub5pxc3jKIj50d5UekHT7qrNdL3Qp6tfqIzN_RPLHpWLPdyl8xkodZHANpi7z7KanjYqgzSTAHTGkrGEFcagzo7CIDpUvT_VJJtCPrLK1lvgM-g4g=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8uq5pEIXa5ZPM2VkNoSlrWNC6Q1UfmgyxnClOw5zl7tRH20n_GKxmy1DRML7ehYIXCreXaa_WJGN5XjzaVdrTP4Ot2C3jje6UF_CO65JCVzv3aq9CyDRwklF4ExgFqETxnFYo0=w592-h366-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_vJDdnEqDCji9QUPk_s0emvLUsq6VYUNN6RFM0n7GgWGEjciAMzjnA5eeeDScn9nsJYspW4ZXwTx9wbQaufYCSM3YNOtlygoWeONf9HE_797rwazh-n07PdnVk3D9KN0KLkMuOEg=w632-h374-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_aT68OGHEYgn2fqkyRg3u1dbY2lw1sCuKuFD6ZC8KW9b3Q5XdjahwxOt6JQ5K5I8ILaOykRgJyQGjeDb4R6dP-AkKqYbvpOseqyfuWy-LtWPHzE1IvAKvXHdsURiWH2o2_NcQWsw=w632-h374-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_malMBmdIYHRzwFTINGciXrxQA8PkUECB3NkEPN8dn4QSy1WZLEBBubPk-sm4cwg9WfRMTMmHlP82xEsayYULrfrqd5DNa574pK7otmIBzCCU9Mw04_5iAPa_xsxU2xN2WK9HtyQ=w792-h350-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_Ffb08r9c3h33JlUK_Yz3RWmQlWBe7kxQbJWWh6RVPnnk8t_UmFAgGOvYSg44J2mUI-e6t54uKQ-AtI3ZqMbPGjHqNyAg1y-HTWfcc9UwQPU6mtxY4AAbM5lgTkvMAGbXJu2nq4g=w672-h358-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX87PvAhrrUjkClkzY63pU2qiAQ1tTTioCMj0O2cF9w7tgYJwDO0L6hhrPfnk6mVT9OQKUlJXwCZzSiqAKSRc-W6hpCCqR7PQVJSmXMNmzBUfxh3eocPG8tQj21Rlcu2vDE-s_uINw=w632-h342-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_ltkrkrBlAZL0497Ie5PwhR21_JqAsAV0uRHhwWR0sL_loGgrhVznyrXxtILUa91Hac_xtuf4j8ZMJZB0Szbiy-e7WwqIGKYS8dOKNHXiK02jotIfriNbFRr6AZnc587Yc5jsjfQ=w1280-h107-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-fMzAjJwUssDQwUsO55ZMjEdt1lJ_ghJS0n-qq61s0HKo11JKjNV1tpGHRicKvYSmTmE-V0KGOtWJR3GBTBv4jPzZ_A7E4Zq0CqvQxWeeAUndtUKyr6oiIBQlMvy-JxSvMrnoDSg=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_dmj_M7Z9AgeJz0O9LhuTd2HOaT-WO5bGJ106nqQEU9FXqBBv1f7tHnlyl2kKnKFDbStH40SWh1q3qK8GtT2doSs47STMuyOFHAEjn1VPbq78OR5blxSZ810svvrx5AFgL13ev4Q=w792-h108-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_BRlDFjQEfCylDLecSO_rCncCDcBYaj4R6DqLfmMArulxy2Ea7f5pskZqGlq22H68bJno4lA6dwMCQQRs_q5y9QgKdNhT7pqsHet_JPsSFENc6StWVspko7IEwrRyxYB404YqvZw=w792-h135-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-l4fXKzoBipga2629mxWH85_gLQ-xAUXijQ80XJyKegnsDohw1NL9-oGM55tIC3nipIGmZ_hjCjlPVZ346rWzvAHNeIVk3dhGkg8mlOokP3wMY2ZoHx_IMzdqyeBwzPntZKEWvgw=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8ifM7owH8ABsa1dTDlK0qUFXPX35JC9ZZeEWHeZPoF5x1FBQTfuNSJ6Cp61sbajaFG5GLQZBwAQwQFNMKVFHyNJdCi7xTopYnAaB4J_fpT_rOiaoRzZY0RHMeIZwhdvpLsDtyikg=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-StjBMIHIwtysnjo-EH6blmauTSVQD5kiy6ScOntKWEUpR20aFKGb3-jrj11rGICjcFXKPdctvQt9Jdh42-WdKdK-omhw0T7g8N8w6A2Zp7s6gYPShpQiKim1qbZyPOulDDVANGw=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_ser1kTtSLl-qO0lPNzA97r_ifM2venNUwtpUsEdeKA_gkmdgf8vksuZbJlgTwjanJ4sTuyM2bu29HDX-h0ofKgIP21c9zpEozpaCvVwVrjjakqotSJk6Ycrbr8HWFASv1aT_ZcQ=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8nMgqps6kjwDApeTQuLt6WbQy7E2qfcrf3GhqYkpaac4d0ArbaopitYxQmRD5U6RHKyAQzzZGOWz9SI6hvZ07PY6yDXhS2qMA21Nwg-i4OKh5MLeIZCLSdT1rSSWBpN8dQX8uVSw=w272-h106-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9chEj9sQeb8JixVtQDtrRt2mNWjSPCgO-O2Tx3IMlIJyQp0uzTkcJ-dy7oG_bDtXfzHdATL9JAXZ8AQ-R6_YvNZv5nLgnDzdhSTwaKhlGV9Ec2_YdpokK8Ggo6glFVPBQz49TvdA=w1280-h795-v0?authuser=0)

Figure 5: Two examples of mistake detection conversations in the GPT-4o prompt. Errors in the derivation are highlighted in red. In the left example, GPT-4o correctly identifies the erroneous step but also incorrectly flags a false positive. In the right example, GPT-4o fails to detect the mistake entirely.
11787
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX91ukYIjdaicz0ffvMlb4BdQf2ZJSVFKOrjUX8Wf5fhI7U5bmMW9WpFXir6Ilyxjo9irD15z0q8qZpwQpzRgd5WAiFk7XQcfeOOLIdSCrlOIrzqR-U-Q6G6YRhuvcjayXyxF63Utw=w311-h338-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8cozYRfcEn3EhEN3CZmJqQGUEVfOqFZcehBDMkgrfG5B72tEIt9QTVFV4m89S_Hj0t40bveO9K3dHfnVpndFlwMpq3cWNzR6TiP3KUPeJQlR5TYGFuVGS7ocDWhqFWGu5U6IIQ=w311-h204-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9N-X8GRtgNpdp6LnBpv7tSfpnhoXEbHtGAeRdlIJwkxNtGbNpkO3EVWxj1hwLKcKTXHEoYIbyted5lhLEMh2wWNJYV_5rHMIadxaR1cH1P2Y2_wzfLHnaTwO4LqBWTaPKOGHImzQ=w311-h334-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-Dytex7KYWsc7gAd5vFxryX8R7ueTBK6_28ZWCiTRPqt1ybOzlM0LXDEPRLXV75WiyVOUOmVGismKjOcIZzTUGkVI06_F5HVskr9B4PLndU3BdC3DRR6VLFpdo7YP2z_vIb2zp=w311-h204-v0?authuser=0)

x1 y1 x2 ŷ2 (seq2seq) ŷ2 (CL Mean) ygt
1 sin(x) − sin(−x) cos(x) cos(−x) cos(−x) cos(−x) 2 sin(x) − sin(−x) tan(x) − tan(−x) − tan(−x) − tan(−x) 3 cos(x) sec(x) tanh(x) coth(x) coth(x) coth(x)
4 sin−1(x) csc−1(1/x) cos−1(x) sec−1(1/x) sec−1(1/x) sec−1(1/x)
5 sinh−1(x) csch−1(1/x) tanh−1(x) coth−1(1/x) coth−1(1/x) coth−1(1/x)
6 sin(x) sin(x+ 2π) cot(x) cot(x+ π) cot(x+ π) cot(x+ π)
7 tan(x) tan(x+ π) csc(x) csc(x+ 2π) csc(x+ 2π) csc(x+ 2π)
8 − cos(x) cos(x+ π) − cot(x) cot(x)× 1 cos(x)(1/ sin(x)) tan(x+ π/2)
9 sin(x) cos(x− π/2) sec(x) csc(x+ π/2) csc(x+ π/2) csc(x+ π/2)
10 − csc(x) csc(x+ π) − sec(x) sec(x+ π) cot(x) csc(π/2 + x) sec(x+ π)
11 − cos(x) cos(x+ π) − tan(x) tan(π + x) sin(− csc−1(cot(x)) + π) cot(x+ π/2)
12 x lnx sin(x) ln sin(x) sin(ln(x)) ln sin(x)
13 x lnx coth(x) ln coth(x) ln coth(x) ln coth(x)
14 x lnx cos−1(x) cos−1(lnx) ln sec−1(x) ln cos−1(x)
15 x sin−1(x) cos(x) sin−1(cos(x)) sin−1(cos(x)) sin−1(cos(x))
16 x csc−1(x) csch(x) csc−1(csc(x)) csc−1(sinh(x)) csc−1(csc(x))
17 x x+ 1 tan−1(x) tan−1(x)× 1 tan−1(x) + 1 tan−1(x) + 1
18 x x− 1 sin(x) sin(x)− 1 sin(x)− 1 sin(x)− 1
19 x x/1 tan(x) tan(x)/1 ( d dx
ln(x))1 tan(x)/1
20 x x3 csch(x) csch3(x) csch3(x) csch3(x)
21 x x3 sinh−1(x) sinh−3(x) 5 + (1/ tan(cot−1(x)))3 sinh−3(x)
Table 16: Additional examples from the embedding algebra evaluation comparing the seq2seq and CL Mean models, both trained on the E-Gen corpus. ŷ2 represents model’s prediction, while ygt denotes the ground truth. Incorrect predictions are highlighted in red. The seq2seq model offers superior performance over the CL Mean model.
x1 y1 x2 ŷ2 (CL Max) ŷ2 (SEMEMB) ŷ2 (GPT-4o) ygt
1 sin(x) − sin(−x) cos(x) cos(−x) − tan(−x) cos(−x) cos(−x) 2 sin(x) − sin(−x) tan(x) − tan(−x) − tan(−x) − tan(−x) − tan(−x) 3 cos(x) sec(x) tanh(x) coth(x) coth(x) sech(x) coth(x)
4 sin−1(x) csc−1(1/x) cos−1(x) sec−1(1/x) - sec−1(1/x) sec−1(1/x)
5 sinh−1(x) csch−1(1/x) tanh−1(x) coth−1(1/x) - coth−1(x) coth−1(1/x)
6 sin(x) sin(x+ 2π) cot(x) cot(x+ π) csc(x+ 2π) cot(x+ π) cot(x+ π)
7 tan(x) tan(x+ π) csc(x) csc(x+ 2π) cot(x+ π) csc(x+ 2π) csc(x+ 2π)
8 − cos(x) cos(x+ π) − cot(x) sec(cos−1(cot(x))) sec(x+ π) cot(x+ π) tan(x+π/2)
9 sin(x) cos(x−π/2) sec(x) cos(x) sec(x− π/2) csc(x− π/2) csc(x+ π/2)
10 − csc(x) csc(x+ π) − sec(x) csc(π/2 + x) sec(x+ π) sec(x+ π) sec(x+ π)
11 − cos(x) cos(x+ π) − tan(x) sin(csc−1(cot(x))) tan(x+ π) tan(x+ π) cot(x+π/2)
12 x lnx sin(x) ln(csc(x)) ln sin(x) sin−1(x) ln sin(x)
13 x lnx coth(x) ln coth(x) coth ln(x) coth−1(x) ln coth(x)
14 x lnx cos−1(x) sec−1(lnx) cos−1(ln(x)) ln cos−1(x) ln cos−1(x)
15 x sin−1(x) cos(x) sin−1(cos(x)) cos(sin−1(x)) cos−1(x) sin−1(cos(x))
16 x csc−1(x) csch(x) sin−1(csch(x)) - csch−1(x) csc−1(csc(x))
17 x x+ 1 tan−1(x) tan−1(x)/1 tan−1(x) + 1 tan−1(x)+1 tan−1(x)+1
18 x x− 1 sin(x) sin(x)− 1 sin(x) + 1 sin(x− 1) sin(x)− 1
19 x x/1 tan(x) d dx
lnx tan(x)/1 tan(x)/1 tan(x)/1
20 x x3 csch(x) csch3(x) - csch3(x) csch3(x)
21 x x3 sinh−1(x) csch−1(x) sinh−3(x) sinh−3(x) sinh−3(x)
Table 17: Additional examples from the embedding algebra evaluation comparing the CL Max model trained on the E-Gen corpus with prior work SEMEMB and GPT-4o. ŷ2 represents model’s prediction, while ygt denotes the ground truth. Incorrect predictions are highlighted in red. All three models have comparable performance.
11788