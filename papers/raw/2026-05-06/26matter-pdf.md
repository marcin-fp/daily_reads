
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8tLJsz7mGg9dTRxPEHD21aSVyQg-zQjwc_0BXbMOjju8nE45GtpT8TNlMnrvBSDjhDr3AUJ2A6JjNuHwnFB17i5mWondd3tkIG0KlBt_PsTcxsbR5yL9PT7GJmtV2t-UettTdhLA=w46-h41-v0?authuser=0)

### **nature machine intelligence**
**Article**https://doi.org/10.1038/s42256-026-01214-y**A multimodal large language model for materials science**
**Yingheng Tang    1,8 , Wenbin Xu    2,8 , Jie Cao    3, Weilu Gao    4 , Steven Farrell2, Benjamin Erichson    5,6, Michael W. Mahoney5,6,7,  Andy Nonaka1 & Zhi Jackie Yao    1**
Understanding and predicting the properties of inorganic materials is crucial for accelerating advancements in materials science and driving applications in energy, electronics and beyond. Integrating material structure data with language-based information through multimodal large language models (LLMs) offers great potential to support these efforts by enhancing human–artificial intelligence interaction. However, a key challenge lies in integrating atomic structures at full resolution into LLMs. In this work, we introduce MatterChat, a versatile structure-aware multimodal LLM that unifies material structural data and textual inputs into a single cohesive model. MatterChat uses a bridging module to effectively align a pretrained universal machine learning interatomic potential with a pretrained LLM, reducing training costs and enhancing flexibility. Our results demonstrate that MatterChat greatly improves performance in material property prediction and human–artificial intelligence interaction, surpassing general-purpose LLMs such as GPT-4. We also demonstrate its usefulness in applications such as more advanced scientific reasoning and step-by-step material synthesis.
In silico material discovery traditionally relies on high-fidelity methods like density functional theory1 and ab initio molecular dynamics2. However, prohibitive computational costs limit their scalability for high-throughput screening. Moreover, many advanced materials lack the mechanistic understanding due to complex compositions and phase instabilities. Consequently, breakthroughs in functional materials, such as correlated oxides3,4 and quantum materials5,6, have often been serendipitous rather than driven by theory. Achieving reliable, scalable and predictive design of materials requires a paradigm shift.
With the rise of AI in materials science, there has been a surge of methods aiming to overcome these limitations, ranging from surrogate models7,8 to MLIPs9–13 and generative models14,15. These models enable
rapid predictions, accelerate large-scale simulations and facilitate the generation of novel materials. As a result, they have greatly advanced fields such as energy storage16, electronics17, catalysis18 and biomedical applications19. Among these promising ML approaches, graph-based models in materials science have become increasingly popular due to their versatile graph representation of atomistic systems in which each atom is represented as a node and chemical bonds to neighbouring atoms are represented as edges. Although these graph-based methods have shown success in accurately predicting material properties, they typically lack the capacity to handle tasks that require understanding scientific context, literature-based insights and domain-specific language20. In particular, these models do not support human–AI
Received: 4 April 2025
Accepted: 6 March 2026
Published online: 24 April 2026
Check for updates
1Applied Mathematics and Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA. 2National Energy Research Scientific Computing Center, Lawrence Berkeley National Laboratory, Berkeley, CA, USA. 3NSF National AI Institute for Student-AI Teaming, University  of Colorado at Boulder, Boulder, CO, USA. 4Department of Electrical and Computer Engineering, The University of Utah, Salt Lake City, UT, USA.  5Scientific Data Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA. 6International Computer Science Institute, Berkeley, CA, USA. 7Department of Statistics, University of California at Berkeley, Berkeley, CA, USA. 8These authors contributed equally: Yingheng Tang, Wenbin Xu.
e-mail: ytang4@lbl.gov; wenbinxu@lbl.gov; weilu.gao@utah.edu; jackie_zhiyao@lbl.gov
embeddings that are both physically meaningful and well suited for downstream tasks.
**Language processing branch. The language processing branch is**used to process the user’s text-based prompts, such as requests for property predictions, chemical formulas, space group information or other material characteristics. We use the Mistral 7B LLM23, one of the latest open-source LLMs, chosen for its exceptional performance across a wide range of scientific and non-scientific tasks. This branch processes each prompt, transforming it into dense embeddings that capture the semantic content of the enquiry. These embeddings are then combined with the query embeddings processed by the bridge model using a structured fusion approach, allowing the model to effectively incorporate both textual and material information. This integration enables the LLM to generate precise and contextually relevant responses tailored to the user’s specific material-related prompts.
**Bridge model. To facilitate the integration between atom embeddings**and the language processing branch, we developed a bridge model inspired by the BLIP2 architecture42 based on a multilayer transformer framework. This bridge model includes 32 trainable query vectors that interact with atom embeddings using an alternating attention mechanism. Cross-attention in even-numbered layers extracts key features from the atom embeddings, whereas self-attention in odd-numbered layers enhances representational depth. This approach refines the atom embeddings into query embeddings that are most connected to text (Fig. 1a). Finally, these refined representations are mapped to LLM-compatible embeddings via a linear projection layer.
Figure 1b,c provides an overview of the dataset of crystalline structures used in our training set. Figure 1b visualizes the material distribution on the periodic table, highlighting that the dataset evenly spans a diverse range of elements up to plutonium. Figure 1c depicts the distribution of crystalline structures by space group across the dataset. The dataset was curated from the Materials Project43 and contains 142,899 material structures. For each structure, we generated a corresponding text-based dataset encompassing 12 tasks: three descriptive tasks (chemical formula, space group and crystal system) and nine property prediction tasks. These property prediction tasks include metallicity, direct bandgap, stability, experimental observation, magnetic status, magnetic order, formation energy, energy above the hull and bandgap (Fig. 1a). Further details regarding the training scheme, hyperparameters and dataset curation are provided in Methods.
Figure 2 illustrates examples of a human–AI interaction with Mat-terChat across a diverse range of material property prediction and analysis tasks. It shows MatterChat’s ability to effectively address a broad spectrum of user prompts ranging from fundamental material attributes (for example, chemical formulas, space groups and crystal system) to complex material properties (for example, thermal stability, bandgaps, formation energies and energy above the hull). Figure 2a shows three interactive examples of material property prompts from randomly selected materials from the Materials Project database. The top left panel presents a human–AI query interface with MatterChat for the material with an mp-id of mp-1001021. It provides a detailed profile including the chemical formula Y2Zn4Se2, its crystalline struc-*ture denoted by the space group Fd-3m, and electronic properties such*as a bandgap of 0.23870 eV. The interface also addresses the material’s lack of thermal stability. The top middle panel shows the interaction example with the material with an mp-id of mp-1028281. It provides a comprehensive breakdown of the material’s composition attributes,*including its chemical formula (Mg14VSb) and its space group (Amm2).*The interaction further predicts that the material is both magnetic and metallic, and its formation energy is estimated at 0.07219 eV per atom. The top right panel provides an interaction example with MatterChat of the material with an mp-id of mp-10198. This panel informs the user’s query about the chemical composition Mn3PdN and its cubic crystal
interaction through user prompts or textual descriptions, making it difficult to incorporate expert domain knowledge and user-specified requests to close the feedback loop.
This bottleneck has inspired exploration into large language models (LLMs). LLMs like BERT21, GPT22, Mistral23, Llama24 and DeepSeek25 have shown promise in scientific question–answer26 and information retrieval27. Recent efforts have incorporated LLMs to solve materials problems28,29 by leveraging pretrained or multimodal architectures.
Recent benchmarks, including MatSci-NLP30, MaScQA31, Hon-eyBee32 and others33–37, provide valuable baselines for evaluating domain-specific reasoning. However, these methods primarily rely on text-based representations—such as chemical formulas28, SMILES strings29,38, and Crystallographic Information Files (CIF)39. While informative, these textual inputs often fail to explicitly capture the complex 3D spatial relationships and local environments inherent in atomic structures. Consequently, they exhibit inferior property prediction performance compared with graph-based models40. Uni-versal MLIPs11 now allow for the extraction of rich structural information from atomistic embeddings, offering a feasible pathway for multimodal integration.
In this work, we present MatterChat, a multimodal LLM for materials science. MatterChat utilizes a modular framework that bridges pretrained language and materials models. By freezing the weights of the LLM and the material encoder, our system enables plug-and-play flexibility with components like CHGNet41 or many-body atomic cluster expansion (MACE)11. This design preserves foundation model generalization and facilitates future extensions without retraining the entire architecture. MatterChat integrates structure data with textual queries, overcoming traditional LLM limitations in quantitative prediction. It maintains robust human–AI interaction and enables advanced reasoning for synthesis guidance. Embedding analysis confirms that MatterChat effectively preserves structure–property information, supporting a multimodal retrieval-augmented generation (RAG) approach to enhance inference robustness.
**Results Overview of MatterChat**Figure 1a presents the architecture of MatterChat, designed to process both material structures and user requests as inputs to generate text-based outputs for tasks such as material property prediction, structural analysis and descriptive language generation. MatterChat consists of three core components: the material processing branch, the language processing branch and the bridge model. The material processing branch extracts atomic-level embeddings from material structures represented as graphs. These embeddings are then processed by the bridge model, which uses trainable queries to produce language model-compatible embeddings. Finally, the language processing branch processes the user’s text-based prompt (for example, ‘What is the formation energy of the material?’) into language embeddings. These embeddings are then combined with the query embeddings generated by the bridge model and fed into the LLM to produce the final output in text format. Below, we provide the details of each component.
**Material processing branch. The material processing branch**encodes material structures as graphs that capture the atomic local environment. We specifically utilize the encoder modules of state-of-the-art graph-based universal MLIP models, such as CHGNet41 and MACE11, as feature extractors to process these graphs. These encoders are pretrained on a diverse dataset of materials, encompassing a wide range of symmetries, compositions and bonding types, enabling it to effectively model complex atomic interactions and structural details. By capturing essential compositional features, such as atomic types and chemical bonds, along with spatial features like bond angles, these pretrained encoders generate high-quality atom
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9xlHSK6OS3bwPKcXwnfwBmzGvibrHu-Jb-MJ6rO33LBIZuNfiYbBGrBt6Tu623mOfXw3vJwOUWqnJAh7kZPYDO-PY6aulg13hqJ0pf4lWn3M0AwR9BchmBLSsn6OPsacfoVIWlwA=w1206-h477-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-9rXRqV4ew3iubL_ADgYTkbfhkcxr6WfEljdd5YSBIephK-yR4Sg_4SYo9TlSg5TNS9eB9AiVz1gVRwhtqcVQgE0GnLKlsl9ZGgT7Qaf3iQ3GE9WNYEz3GBm-mDdMd91dbwDP15w=w1271-h499-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-N3G4uB_FwwWRdvCppJKeooUsbTFFUpQZGscK24Kw_5JL4oLaSU5_YIGRLSHLKVzSde4gtcDmXnyoUIh2qYFMvyg5Jfp98b3QxYHYWD6Cv9HRWweHyQEb4kChIiPzw6uKK1jetrg=w300-h201-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_PerKQE3wghYORXUzv8ozXVQ3pJdYHG8zAdylUboJWVquSo87ipbJlG6mGVZ1Aj2qfWeabr5nTxtMICKqbHtYz8lDIt-JYvAXRhxX1A-yROhbtjfkIznehnWVJmx0iUSTfZkie=w1280-h669-v0?authuser=0)

*structure, with the space group classified as Pm-3m. Additionally, it*estimated that the material possesses an indirect bandgap, which is an important characteristic for applications in electronics. MatterChat also accurately predicts the ferromagnetic magnetic behaviours that the material exhibits, and it mentions its energy above hull value at 0.01357 eV per atom. In the bottom panel, we present a comparative evaluation of MatterChat’s performance on formation energy evaluation tasks for newly discovered materials from GNoME44. The model was compared against commercial LLMs, like Gemini45, GPT-4o46 and DeepSeek25. The results show MatterChat’s superior accuracy in estimating formation energies, consistently delivering predictions closer
to the ground truths. For example, MatterChat’s formation energy predictions for mp-3202380 and mp-3206774 show a remarkable alignment with the ground-truth values. These results demonstrate MatterChat’s ability to integrate structural and textual data seamlessly for a wide range of material property tasks.
Figure 3 demonstrates MatterChat’s advanced reasoning capabilities, showing how it leverages the comprehensive knowledge base of LLMs to address complex materials science challenges. By using a multimodal query system, MatterChat effectively combines material structure data with textual reasoning. This integration facilitates a working memory scheme47, which enables the model to provide
Q: What is the chemical formula of this material?
Q: What is the formation energy of this material?
Q: Is this material stable or not?
A: The chemical formula of this material is Li32Ti3Cr13O48.
A: The formation energy of this material is –2.38709 eV per atom.
A: This material is not stable.
MatterChat output
User prompt
Material tasks
**a**
**b c**
Atomic structure Graph Physics model Atom embeddings
Queries
Self-attention
Cross-attention
Fully connected layer
Trainable Frozen
Bridge model
Material structure processing
Language processing
Language embeddings Query embeddings
LLM (Mistral 7B)
Elements in reduced formula: (142,899 compositions)
1 10 100 1K 10K 100K
Monoclin ic
23.4%
Orthorhom bic
22.0%
Cubic 14.1%
Tr ic
lin ic
13 .3
%
Tetragonal
11.6%
Trigonal 8.3%
Hexagonal7.3%
Other 7.5%
*P2_1/ c*
6.9%
*C2 /m*
3. 6%
*C*2/
*c*3.
4%
*C m*
2. 0%
O ther
13.3%
*Pnma4.5% Immm2.2%Amm22.0%*
*Fm-3m*6.4%
Other 5.5%
*Pm-3m*
2.2%
*P1*7.2
%
*P-*1
6. 1%
O ther
6.7%
*P4/m m*
*m*
2.6%
*I4/m m*
*m*
2.3%
Other8.3%
Other4.8%
*P6_3/mmc*2.5%
**Fig. 1 | Overview of MatterChat: a modular multimodal LLM for material-based question answering. a, MatterChat architecture: the system includes a material**encoder that generates atom embeddings and an LLM that processes language data. These components are connected by a trainable bridge model, which aligns material structure with natural language to support tasks such as material
**description and property prediction. b, Elemental distribution across 142,899 compositions, representing the dataset’s compositional diversity. c, Dataset**distribution shown by space groups (outer ring) and crystal systems (inner ring), illustrating structural variation within the dataset.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8xXmCH7VEqS4c_1i2z8lTdr8Ce7-hDBDnd6sqWETAk1LgVE6714Nfq4e0sIb29kpnxL-kABK6zUL4aS5x7SPJSmckBCTwJU6ZK8sXh51XuDZt9U4SLdKOMymfEdspGdt6zIq8N=w741-h706-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-uNjMAPFlOxPI8vTHIxSyPk8s94HAkxpmjPre_UdORPNdWCN8pZDQbFnhv-H8mf6PJtLMboxw6h8xnc7uX7WP8nFxmZbZB-g8TCGczVqm1m7FlOy0WXeg3BW87KaIrTQCf0GRNJg=w91-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-IT6jidjhLTlpqrKFh-X_259UqQjawT6JtJOGjZf0Iq_1iCV2PUJJtBFTt4uLFexjrSj1_THyLByROsOXN9R5lyOJZxuDaHqWz3ILqHebLaTp04Yx763S7kUDhKlixRVrezZF0Rg=w90-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX85CUlQMxzXvLhfhVwsSxL5ELPj7aWMJmEfUyN6q87WKpZ2ewgzwyCDIlrFBJGpvZrHVG8Xqf6OGk93t7pH3hMicGbhjy1ppIthIBo2PkIudG5m9oVsBl1IoQJ4b9mCIJt47y5E7A=w91-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-8XHtDESO9RgJCFEESwNod8UsDWTtMVBWgtx3-3ptgCPisWyP-Fo4Yp03ptzX8ebKQ--qokkAn-sh10jkpw9ujREZoogw4RB6UByIa5vQknwDuF9A7RC6W9vT4ZM-NFzE0H5ht9w=w91-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-t_L292EsWV7WMRm2SVqbzfi0T54bnSMkfTo_v5isH2o8c9yNFzCaY-QSfzouAVwH_iyXKnXNYod35HPqtvqiDnpy46HBldPOzgPgERRRsPrzn7ChjEAaPoP0KShC4e00sYIK7=w90-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_RVqqQ0zOPgO4NJrjmMzxiUEaOCf0G66ViHC204lupPUZ3Tu-cW6DZgRgLiO_wZ0wdJBtu59CrbW_5NAD5RT_BvhB7lo4rjLrov9R8p4i6R3IZRJGDE8YXDp42FOa2KiN0pa-cQg=w91-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8FGM7Gbvz4c4dX9H-AM2inC96saQnylLlqfP93TL1dp_0YQ_TLqKw16aZKel2TuMuA9WdQhQayV05Vzb0oOljoCk_ou5nqGfzj7Tyi4TOnmMEUdSRFOrPBixae4g7PnA1b5yZTzw=w90-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-W8X-8enNflNaqAdB8DVjKkMACKls5NKqfXWIQ_im-mDGIxuPcBTuVNu2G3AlYDy6KXuAQcItGl3ilf14b_weQt1UuCCkZvpcF9z9ZU38_OMfXfErLol_6qjuH3WFeNF-z3rOhYg=w90-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8Jb3wZDbcx2QexVayro3kyRJJ4VmTg1jwa_TOSUyG_TS_8j42nA3tIBsS3qitXizd-jCMFDlRhu5RNOMeDdbA-QAJRLf-6vaEozxTRGo1jmHpaCDwHhE6VDK3NE8jN4VDnooLlsQ=w91-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-AYo7MkoOQxrNgU8GQYJY9ep0TPoDCGSsNJy-TRW18m57tBe7oIqUFln7eZE9JQ6TlmYPfwk1M06B1nQ3zBgzjyBWDpR6MBPCz4RHj4yH49-9twedMAwvzKeWIIO4pjZnKaJ1QLg=w90-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX93GOG8gTzTQz4xNPRiyerrMUAs3ki3rZ2TQDSA9BnDYEz2p5mFk5Jpo5tJXhopEkXf8FRk8UgfCQDFuQ3h69gp3fjOVoZcMUS91JYs_aaeFakjOzuRPIGxfkobFZU1dazvVys=w90-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9IH6noPdzRCyniX9hO79mRY4ElFP5rphhL9WlKp8U7LWhiBnFLaCib5nAzta2tBFFuPVv1Hoxy97UeJe4DVFsYNFIXVZZll0eThU7yu4Yc4HysM7gP5BLSb_Ls5mOhIJ5n67PvOg=w90-h94-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9BeUhp83vWLpIS2M61tRKUJQlR5Z9iVfhu_fKyxO3Dz1l9mL3Q932_nqMyBiJ9T-R38TB-FJpEZSuzQ5AOwZlGrvbDUYvMoTqJnCAcw-w4JzNh1LWwxMcX2_yGnxoTQnzxRdn-mQ=w91-h94-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-mfJ1evqgaeBvnHqWq086ekghRXozA7EBkisLSm_Njl0XsXeqPGDL-4WHW9KPAQvoYisCLiYHLTMdpjk1-UGLOe-t10r9qRrrjCkY6pAUsg_BXv2XBi6K8-yJToTgfyb7L8Fra=w91-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9_bPYW3AaJ05sqOmaG1KJ2d9PHi4WMXI66ws6bk_SQ3Kc2PZEpzLxM47J8ea4Sq-8QbrsZVQ_4GTIOjSnPEjuGdsvnO2pDAMzKbq_MAlPSy--P2cz6fQN8T1ypxtWlZ9YedLiuJA=w91-h95-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-dHSDiNTLDwpdYemBay7682TAIvGJBUgyxfNvIwOP4DI8GByWDmKGmSCWbfE8yO6v0GiVix_e-1CCFJ6BMRJg7n7eVNquQd2TmhLhacdD9uGSKUWBKgpLcMWFsUvMwmpJKXci9cQ=w214-h219-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX80Ja7vADaAEsfwZqcjabjpb6H3QwTNCeOk0HnfNKpcCJlHavAjTNLmAItEYXLIQhgwlWmUHiaFhDZqtNoxjtmievqVwuYAFShap7EvHTnyvTcXaIaahVbfgFh6Y3trm2HBpLImvg=w216-h169-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8nl7vh1l-bYLlJZHjl-Db4gxgdCRuEv7dUxWgMC3YfvpzyxPgaiLJ4IicIkuasgs0vlKc0UOfUf3m7GnATD1A_I5eyUMX49eWAhh2B8fTwxSYMIvjytktj0iXj2zy9I0AXOTdVdA=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8s0fcVrtdwuMGNcUUTnas6kVOmqaheeetaI7lZqPhlLX5B7HOz9OZJ-1R0e_mHf3uDmQh-fOo3q1hqDcFItH_6r1XQB3DLBeMrSvCteTxZneLI8VgPD9rpDH9wtpwiDBQDltNG=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_Vx1JsWCMGe4tN9LSl8G_QQ8slFJBF39pSWqDct1s6Etfek33V-MchoI4Ani10li9cZNfPcufyEUVMAnE-IiWEMe6xSilBfY_a9206_Q4JfzNoRYfbkNqoGj5INjs-W5bOfz6lFQ=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-nKREQ147lvBFoFTOaRNUv740_CthaRHQAikB9AixazHFgfsv0BYDjrUKUsqfNNmEm5gWW3lL0xQyAzhzJZy4Dh4jROblUECIafE6ylzE68d0PkdlQD8U_RZljPeCQqkNKnGfr=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9mMFbrmGZPHEs-XXoPcN6vU2AcPyJcGtzVkjBjD7ighudy29DK3tv-oZgaZ-nvqxawPapCuRjr4lvUolsqTDXkfKZi9YeJ5D1aMAFvA27h_qze_kw3YSL72y99D9Z1zseq_ksgdg=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8WPDENiRnSIOyN-PFcks9qpY3qR_-8gIBGW2B_dRtgCUp47dwZFNmiyfxpBO-669IYxDE9xPO7wuozy0fXRlPRvjYzSRcXxvfHEiikP5zy46pQUCvaQSVnakB5f9rvp360ECRiCQ=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9XZhrYYZNdnF96JJVFf8Ry6b-AZ2NGXUhxtlPD4FNWekh3cn5TfTB3SsnkJQRtR76p7Lqn4qgvo199kpc_OkcoXWoRMbSzPhYbC0cj9yHzEUoRXJVivi_9NhY8ih0pLvn4OWb1Gw=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8sqGWBFL2k7dTCHs1nvCZKe7nMF0nd1Scuk-bcxIs3BlNp7fC2dVFZnnjlYvng6CGUu6i2GnIiMQ6J2puTTbIOy65MY_pCWw3KzL2Rxn6tl7lQV0Ge5FWdP0zg-X01m2Isy882=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8oJF5J15g55UOLT1vKNtc0s4twC34Tsr-PIt8Ku_a4xRz9rwzYo8YJH2NxW7sCYkhiS9qC6pfpBKCkrH8Jh7JNAZHWesKIuRoZ0F80jU8wLzlX8IYuCzpVrfOfYJ0Tnd5IVzak=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_3eh136AwOPZnBEb5CLPTftRb4H007K7tYjnU3fbRqnqOUAuwaA44l2VUR1y1KhEYMgOGuAwdEvm9mqEpaDYUuwHyv3oP22NfMtzgIl44lD0i2eJTsEI6TEj7DMBUOslhFXj4g=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-TG-aA4hTrai-PSdYVBzyTflIaUFNcTJSKqkOri64w-_Tpf79lSTwgsI6fgjtlFueTOnbUfzuo7IJD4gBX7VH63wc5IO3g3sn2IglVrsQ5NzDq3dzug19ROgaRfS9loAPvouEzAg=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8pxajmU7PA-vjP6ZEV7JHqUWDkE60LdfGxYHfz2A2CKnJ-h6Rnu22YK1JtVyZNWR0_ey49e12IUb_Cd9n7cbcAmmvpnyA5LIx2-RoNhvrGH-HMpV-t5uXmh-6mn78fn4rgDhXopQ=w65-h77-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-TrI176dZCWadN6-hWuhdQlRB_phSqkRp74QuErfJK7LFqRVc6-i6MaBCresBJ7DXWMmH7usBMidV9AhpwWY4d-iutH5WtHHODt6lWFg-13PTxe7Ge2NwGwK5_LP3eSbuCj4-9XA=w151-h155-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9Q2AbFztwlpi6HSx4S6i2SyjjdznHbuvfk5OlWGa25O0BRDPP2CI8-4HxrjMNhKSMrDm0okCx21ew_vdVE3p2f__v5N4fn5pCCBiPgyJp8rD3YLBXYJ91T90BQY59jCdvdav6sGw=w158-h131-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_2zzbXOdnFHNkZ9I39SGnBZp1sS4G0EvxxkuNkkEORSrv3eXbLE6uek6b412c-iM8zG3G8KUzEShV0Av7uQBpRsS2e6FckH1_ecX9OOwuSTNl4xuDnryi76JC6yRKM02IYTe9D=w149-h147-v0?authuser=0)

domain-specific reasoning, detailed synthesis procedures and explanations that are deeply grounded in the structural properties of materials. Figure 3a presents the chat log for silicon with the space group of*cmcm. MatterChat not only retrieves the chemical formula and the*correct space group but it also provides a rationale for the structural*instability of this silicon phase. The model explains that the cmcm*space group exhibits a higher energy per unit cell compared with the thermodynamically stable cubic diamond structure of silicon, making it less likely to occur under standard conditions. Figure 3b illustrates an interaction regarding a popular semiconductor material gallium nitride (GaN). Here MatterChat accurately identifies the chemical formula and*space group (P63mc), and generates a detailed metal–organic chemi-*cal vapour deposition synthesis protocol that aligns with established experimental standards. Specifically, the model identifies trimethylgallium and ammonia as precursors within an 800–1,000 °C temperature window, directly matching landmark methods such as those reported elsewhere48,49. This demonstrates the model’s ability to leverage inherited knowledge to provide practical, grounded and experimentally
viable scientific reasoning. Figure 3c explores an interaction for a widely used ferrite material, yttrium iron garnet. MatterChat is able to take the structure and generate detailed text descriptions. Additionally, MatterChat can further generate a synthesis protocol for YIG that aligns with established experimental procedures50. By identifying the correct 3:5 mixing ratio of Y2O3 and Fe2O3 and specifying critical parameters like the 5 °C min−1 thermal rate, the model demonstrates its capability to apply domain-specific knowledge in accordance with standard practices and characterization techniques like X-ray diffraction and scanning electron microscopy50. MatterChat generates synthesis guidance via a modular two-stage process without task-specific supervision. First, structural attributes—including formula, space group and crystal system—are extracted via a frozen encoder and tokenized to form a persistent working memory. Second, the LLM generates responses conditioned on this context, aligning with a symbolic memory frame-work47 in which the inferred material facts anchor reasoning. By utilizing the LLM’s inherited knowledge with explicit structural signals, MatterChat produces physically plausible, literature-aligned synthesis
The material has the chemical formula of Y2Zn4Se2.
What is the chemical formula of this material?
The space group of this*material is Fd-3m.*
What is the space group of this material?
Is this material stable or not stable?
The material has a bandgap of 0.23870 eV.
The material is not stable.
The chemical formula of this material is described as Mg14VSb. The space group*of this material is described as Amm2.*
Can you describe this material in term of its chemical formula and space group?
This material is magnetic.
Is this material magnetic or non-magnetic?
Is this material metallic or not metallic?
The material has a formation energy of 0.07219 eV per atom.
The material is metallic.
What is the formation energy of this material?
The chemical formula of this material is*Mn3PdN. The space group is Pm-3m and*the crystal system is cubic.
Can you describe this material in terms of its chemical formula, space group and crystal system?
The material has an indirect bandgap.
Does the material have a direct or indirect bandgap?
What is the magnetic order of this material?
The energy above hull value for this material is 0.01357 eV per atom.
The magnetic order of the material is ferromagnetic.
What is the energy above hull of this material?
mp-3202380 mp-3206774
Ground truth: –0.098 eV per atom.
*Ef(Cd2Sb2Pb) ≈ –0.28 eV per atom.*
This compound is likely to have a formation energy around –0.75 eV per atom.
Ground truth: –0.563 eV per atom.
The formation energy of this material is –0.04189 eV per atom.
**a    MatterChat interaction examples on material properties**
**b    Formation energy prediction: MatterChat versus other LLMs on newly discovered materials**
What is the bandgap of this material?
mp-1001021 mp-1028281 mp-10198
The estimated formation energy is around –8.18 eV per atom.
This compound is likely to have a formation energy around –6.04 eV per atom.
The formation energy of the material is –0.52143 eV per atom.
*Estimated formation energy: ∆Hf ≈ –0.44*eV per atom.
The formation energy value is ~–1.83 eV per atom.
Gemini
GPT-4o
DeepSeek
MatterChat
Gemini
GPT-4o
DeepSeek
MatterChat
**Fig. 2 | MatterChat accurately predicts material properties and outperforms state-of-the-art LLMs. a, Illustration of multimodal material property queries**using MatterChat. The model accurately interprets user prompts to predict chemical formulas, crystallographic properties, stability, electronic bandgap, magnetic order and energy metrics of materials. The three panels demonstrate the framework’s ability to address diverse materials science enquiries, showing its alignment of graph-based and textual embeddings for precise question
**answering. b, Comparative evaluation of formation energy predictions for newly**discovered material from GNoME44. Predictions from MatterChat compared against the ground-truth values along with evaluations from commercial LLMs (Gemini45, GPT-4o46 and DeepSeek25). The results show the accuracy and stability of the MatterChat in quantitative material evaluation tasks, which closely aligns with the ground truth, demonstrating its ability to integrate material graph embeddings for precise property prediction.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8vhCew5CSN2UF8WckLHDCdfqVAt52jq55SD6tCJdCN8pAjrngmnye-8Ho4pGDlbPb8LRRAITjusuV8kZ-ZRc7ElFpSnE6opd5LmAh0JNAu8fXj2PI6iR4yz_2H00C85lsByFPL9Q=w737-h570-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9iaQs_h-FEJYbi6lBj9_lTujaEa3qjkezPWsVjyJjG8LMb6y89MdvG-kUAzAcosiEd78nz2SfXDqfKwX6si3AfJB7Wkj016sQzYb7vB2fn8hgJNiURUZLOkxPB-k7kLjJvLs6G6g=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9rW_EVlUOmfL5UmFHW1qaQWTPjX2W_dwWE0qHcoqmJnQVv5SLVBq7LidLJzM-dFJzBpOYCkvHoFc6I-elOdV4vCKlUTHOwKfcTt1hSuqbgmlmYB28WWbUJEdHi42v-W9dmFG9GRQ=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9p-EegedirRK1-CfY0gU2mJenGZGHvGGoFpx4kh_Ze3YaD12uhT58npKI_4Y1FvUXNOM69ORP_YFkzfMbF0O5EK6thBhzFldBQuxZwGCQeTwNXXYg5MjAhgURxYyXZdhOhJrOjZg=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-zoYVD1siKJCttB_pstM0QKSgTQS82eMsKyLPzm8IMfbosCa5YQDhJE3pcakz8HyCaQJEZBUY7aHAn2mQ-Ye9e59jgsAxNjCWf8Bx92KzYAAttJt43w9RfgWw9dpSZwhOczLcANA=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9iORfrQhkvjCQ-Tr2e6rkA9DOQeX1nI5WyO5sFaFqAYs1fALyn933R5cB9y2jV_PWpb2tmlaRrEHpmBVQIRt5_LDkR1-eBL9OlPUiSJtYQrnnCCfZhM4jhG1O-RQOMa9MXdsi9kQ=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX93zRDjdrLwP-Mq2zfcZi-07Yvll19UHgF62isWNXkUTyKQnGhSJz5PBbJ8PUFCK6nR6xIes2rRSsnaFp1PuF7AR4OIy7-0HZoT9ykO1KlzhvBNZOT4TG-YOCswa6_RB6ENXNcQaw=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8RJpfbW-6RUtgEk2g87QBcqvBBi0aH3x91zL1MeowORBpmpBPdvYFKwXFIbHBoVMTXvWCTaRrljAKB0by3QvHVcSJ--nRMZPkNWlPK_ot6leN9EB-dL1UVNzp15xP2iZA4ybUl9A=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8z_PebXxFonofTRoHI9LljL40yUMmEoGToaIXUlVyIoIFWXO6L6LK9zbTotqmn6cmYre7P0GMlmPnQqXskrUTfnIN_1XK8fnDfHSE64p7EMKVcwkGpHryfioj7GuI1yC41CCpn-Q=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8twxi6QkQyxJR2nZSqx7p1h_rhLAtc3LEwlIQAgJ6NQaww12awPs2EQNbPtS0IUMHWbKjFouo2rlEu0fJyuffhMbKqXSBzi57o-rGzGxDs5ddWpi9ouTeFtwVcPT_ljBCbE67Neg=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-9-uvVCCNQU5YqNgtOOYx_zIwugO5D-oTc4h5fH8f_84dSnpRWQ08SEWBrLnRMJoC9N1arKPCO8j4Rp4dPLUwDTsIlYMRqyXEEh8Zr8Asyd_AzLTghyUsfT00SPI008QrPafpT_Q=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9s9BqyQmCrP-_OGVNkG96PpgrIQBbqbs3cd_IlK03_50h1uCEWGwWr3oForR3tTXuREhk9mQJM2NiA-956C2ZRuwbfaP5oTvcBU2HeRhu-DqzOC-YQ0XASxeoOwGbdHUx1qvUnsQ=w97-h101-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8A3wL_GmBuzHiC5cElU2rgd-zPY-uwAyAVdkaSYWEC2qMOYGbQNtdh3CuW4Qq1m7LdIL1WOEQYTE0gWujq0Ap0k5JfeqwCT0G2nsbYuMtr8Tgg5T9uLESh3Iek1NDQomGzFSAnBQ=w87-h103-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_B-BmpT89ODKGqpBHzXEAKNmPsCbaYeTHYemhxtWW6Eiu-tFqRIgAjT-HSqpllKVtck-Oc-gkUrL7bEZ6G1K-PuTCHjgPJmvO8K631l4sY_Wpb8-2adc6fBF4kQ7OR8z7j4BQT-A=w87-h103-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_9OxghlheZKCidy6hyXKHEBcAnozKz8Be0iHk3mrkRhQWlQV5rtxCQ5qqZtVoSGhp97ZT8ZNUEr0UU9TBoK7Vu_HGMT0pai479rAcoU630Vpf7n3P0164QTjiAMKElYkrEJuv4ZA=w87-h103-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_cbiWQz13uFse8zksJZkVu4dWbzPsihUtutm7sry7K9dIL2ebrwMHGjXSLTd4MieRHBPj6wP-bDgt9N3hdzwq8ZcbCuXGGN6yZLagWvLKPDuFNiscdb-pabWCBIZ2Rtp2vFQrViA=w87-h103-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8If5F6HN0CVGebzcEIX-_V3AVTzTrtT6nEAreYwDKUwYgYExwMKRUEVgbKZ1eUZcNLwahA4P1rRaa2gFKZu3UgYQroea-Twdph_wd37Bdccz81bEqBLu5Boii_gD4ya8EaQLIT=w87-h103-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8sHojoKGfRG1p2692rbtgARgmoc2-_hGD85Hg55WYTLasRrlRjh_JYWjoqIy6LFXFg9zsCoXfAyarJdYNeRyOyAmjJPRvL5z5sIzbJPyr2Gf2TPNvvP1nmR4r8_nQepUju50O1YQ=w87-h103-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8QI7U37fsxcLZXXlWh6mw77MIrT7Qed7-RdtT68as6_iKzjvREqOSaubnBye3QRjsnN-NZ1o7WoMNjeOgIDLz1gaT1_xZczhGsYb0lC-9apuevCn6ga8lNuemkQu8QrA8GDd38vw=w87-h103-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9dknsTvCPYGoEpDIvs1aaC3JpLsuLJVBMy1i4TVC6nSWmCo6sE4cCuf4JLKMv2aLF2d1DJacVAEnhAhMOI4lSdeJq39Nt9p2kE2xh9Kk64G7f5TahC7rOObOg65bA5OhDUe-urIg=w87-h103-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_kDset2ZjZ1KDiUB7OVe-hGakK5isGOimMVouh1hE6JZuMaCdgOUIswBG_u7_goj9i-NOg-VD-N7tecuPerHBlMyYGEer3zLredKl0vEn7SvergsF0_bNYqy16Hww8zbvPNa15gA=w150-h155-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_GoBmGNehvQiWbqKXrwk4BPhrtzETsumpOxv8_OdrnW0qKmZ3NQhbTZNyxlc75tLTu842OPqj9ekwfDccjFGMFI0_Fj79_mwpVjSE_qMMrOe8NgNbzsr-uHJxuN6gOncxBaxs9Zw=w216-h151-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_QlwtPu_xJGKG2ojTViWe66Z-2eUXReiQpgM8se_dtqFQH7QsLsudN3wZZHsq7rXegpcAiMeTt1EuncjvuuafQB8c9z4IUYdG8QTrxWpkl_mUHFYFTHmTG2LUMObq0qpDxRU6YMg=w163-h163-v0?authuser=0)

outputs. This modularity ensures a clear boundary between material perception and linguistic reasoning, enhancing both interpretability and structure-conditioned generation.
**MatterChat-extracted embeddings contain structural and property information**We further explore MatterChat’s ability to leverage material structural information by providing a detailed visualization/clustering analysis with the uniform manifold approximation and projection (UMAP) dimension reduction technique51. Figure 4a–e shows comprehensive visualizations of embeddings processed by the bridge model, with all material samples that contain silicon (Si), carbon (C) and their com-*posites compounds (for example, SiC and SixCy) from the Materials*Project database52. UMAP was used to reduce the embeddings from an*original 4,096 dimensions to two dimensions, with the x and y axes cor-*responding to the first and second reduced dimensions, respectively.
Figure 4a presents the visualizations containing all the selected materials; each sample is colour coded with a structure similarity score53. The clustering generally follows distinctions in chemical
compositions. Additionally, materials with the same atomic composition are grouped into separate clusters based on crystalline structural differences (for example, carbon with diamond versus graphite crystalline structure). Figure 4b,d shows the zoomed-in visualizations of clustering results for materials consisting exclusively of Si and SiC compositions. Figure 4d shows the gradient of structure similarity scores, ranging from blue (low similarity) to red (high similarity), demonstrating how closely related structural features result in spatial proximity within the embedding space. However, an interesting exception is observed with SiC (Fig. 4b): despite its identical composition and similar structural phases, two distinct clusters of SiC emerge, suggesting that factors beyond composition and structure alone influence their separation. To further explore factors that influence clustering, we labelled the samples according to their formation energy, with results displayed for SiC (Fig. 4c) and Si (Fig. 4e). These figures clearly show a trend from low to high formation energy. This analysis reveals that clusters grouped by structural similarity also align closely in terms of formation energy. Such findings indicate the model’s ability to produce embeddings that not only differentiate
The material has the chemical formula of Si.
What is the chemical formula of this material?
The space group of*this material is Cmcm.*
What is the  space group of this material?
Is this material stable or not?
The material is not stable.
The material you are referring to, Si*with the space group Cmcm, is not a*stable form of silicon. Silicon typically crystallizes in the diamond structure*(space group Fd3m) at room*temperature and pressure. The*Cmcm structure is metastable and*can be obtained under high-pressure and high-temperature conditions, but it is not thermodynamically stable under standard conditions. This means that if left alone, it would transform into the more stable diamond structure over time.
Why is it not stable?
The material has the chemical formula*of GaN. It has P63mc space group.*
Can you describe this material in terms of its chemical formula and space group?
Can you provide the detailed step-by-step synthesis for this material?
Here is a simplified version of the (metal–organic chemical vapour deposition) process: 1. Preparation of the substrate: silicon carbide (SiC) or sapphire (Al2O3) wafers are commonly used as substrates. They are cleaned ultrasonically with a detergent, rinsed with deionized water and then dried. 2. The MOCVD reactor is heated to a temperature between 800 and 1,000 °C. The substrate is placed on a heated susceptor within the reactor. 3. Gallium and nitrogen source preparation: trimethylgallium (TMG, (CH3)3Ga) and ammonia (NH3) are typically used as the gallium and nitrogen sources, respectively. 4. Gallium and nitrogen introduction: TMG and NH3 are introduced into the reactor. The gases react on the heated substrate to form GaN. 5. Carrier gas: a hydrogen (H2) or nitrogen (N2) carrier gas is used to transport the reactants into the reactor and to carry away the by-products. 6. Growth time: the reaction is allowed to proceed for a certain amount of time, depending on the desired thickness and quality of the GaN layer. 7. Cool down and in situ analysis: after growth, the reactor is cooled down. The quality of the grown GaN layer can be analysed using techniques such as X-ray diraction (XRD), scanning electron microscopy (SEM) and photoluminescence.
The material is Y3Fe5O12,*with a la3d space group.*
What is this material in terms of chemical formula and space group?
Can you provide the detailed step-by-step synthesis for this material?
Creating yttrium iron garnet (Y3Fe5O12; YIG) typically involves a solid-state reaction method. Here is a simplified step-by-step procedure: 1. Preparation of starting materials:
-Yttrium oxide (Y2O3) -Iron(III) oxide (Fe2O3)
2. Weigh the required amounts of Y2O3 and Fe2O3. A common ratio for YIG is 3:5, that is, for 10 g of YIG, you would need 6.67 g of Y2O3 and 13.33 g of Fe2O3. 3. Mix the weighed Y2O3 and Fe2O3 powders thoroughly in a ceramic crucible. 4. Heat the mixture in a mule furnace at 1,200 °C for 12 h to ensure complete reaction and formation of YIG. The heating and cooling rates should be slow (around 5 °C min–1) to prevent cracking. 5. After cooling to room temperature, grind the obtained YIG powder using a ball mill or mortar and pestle. 6. Repeat steps 4 and 5 if necessary to achieve a higher purity or smaller particle size. 7. Characterize the synthesized YIG powder using techniques such as X-ray diraction (XRD), scanning electron microscopy (SEM) and energy-dispersive X-ray spectroscopy (EDX) to confirm its composition and purity.
**a b c**
**Fig. 3 | MatterChat has the ability to solve more sophisticated tasks inherited from the pretrained LLM. a, Material property query for silicon (Si), including**its chemical formula, space group, stability, and the reasoning for why it is**not stable under standard conditions. b, Highlights a material query for GaN,**providing its chemical formula, space group, and a step-by-step synthesis
procedure using methods like hydride vapour phase epitaxy, metal–organic**chemical vapour deposition and molecular-beam epitaxy. c, Material query**interaction, yttrium iron garnet (YIG; Y3Fe5O12), detailing its chemical formula, space group and a simplified step-by-step synthesis procedure using the solidstate reaction method.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-n2smWJGy7U1k626M_xSqO3kdrqT1W8sslzHhWBvgSHcm5AK7RS5NjlQdS7UI0dT0col1UwUwrmw6tfVtnrgy6E2HDCKkOBxAQMKkXz6GvO04KqtEo50v4F-KnnCFJswz6TgdwMg=w736-h584-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-8WYOFMSR_Yq-8ADmSM4DDqm9E5Sre5g6SIq3yRYLAQJdSdE8OhE6QpSR7jdmxNSpbHF0Hftv-QQIJQC4gTTMjtNkch5wqq_VE-babqgw62kAfxOr7r2W4JtkFt4PYnWbAmyIM=w185-h118-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-BKy3vXIJewC_2iSsTaTRIp-xHMpOOJRCOteNi4kElWSJ-qEhEmzz9TzzGbB0uEOjVEwo3sZKtrO_VWqVhGolAIZHOFzbRe3IN1DQC_Pmu3qrz_DdoE73RP6rwtfU8ycw63xLyug=w175-h104-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8LcmuGaZbFgsDjt_0Yihs6t0LIW9JiMolCVgH9mkW980X0Ljrpog0l-8fjSXdrAhsP9Ttygz7Fg2TKnxRN2YzcOXa_ErfZuqq2nykwggJ3hffft2Ez_-8_mu7Hxfe6AVaBU6AOIA=w127-h125-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8xZZ-yOCLfG5CFvch-s9hzwD6P-F03TBT9UeV3Cqwi_gQyi7UsTBqAXXlj2x-lZCuxJLo9wKEihg3s0mVdWiRNXXsisBlKWsYG1J_xGr3eCpRMdP91ccwgRm-F6mtaQNZIJSQMpw=w1280-h567-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-uGFDpdIaPQGr_ps8ZIrAdrjizS1NQ84xhw5QHaDm3IVgMEtf5n6YjK6yRnSpxYY2oD9WQa1k0M_kX4eo-EAlMD29xjK2hN_KNembw-5URIHZOi5YcSVvxgyp8iuqih1mnJZFoNA=w1280-h567-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9uBwy3mFxujzYCcgc50_hVC44bb205O6D45DS-5XUSDu6J3Lq2FLtRoa6M83lCmtATDwV9DNBI2LvDf8FEx44RaGmqdLJyCqLS10kmJ15OJjmBWZ4Vmipkns1wYsOHE5_FL8d1=w217-h132-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_UQ2LR0HXYiwPm0B73IK2otsj7nYf0HR5EPEEcTnoE9P6ltBC9G6T6UGhzMBcR5iL0tAQ4Gyxi3B4OIq35ZGv0z_Emey25iZZxBop4IEvS48hNkR7DhTbT8NOJl0SxMKpOcHvL4Q=w1280-h569-v0?authuser=0)

structural characteristics but also correlate with key material properties. To evaluate the generalization ability of MatterChat across a broader chemical space, we extended the structural embedding analysis beyond the initial silicon–carbon system to diverse material families (Supplementary Figs. 1–4). These include various iron-based compounds (oxides, sulfides, nitrides and carbides), as well as transition metal oxides containing iron, copper, cobalt and molybdenum. Similar trends are observed. The UMAP visualizations of the learned embeddings demonstrate that the model effectively captures the distinctive characteristics of different inorganic compounds. Distinct compound types form well-separated clusters in terms of both average structural similarity and formation energy similarity, whereas smooth transitions are observed within individual clusters. These findings suggest that both structural and property-related information are encoded in the learned representations, which is consistent with the property-supervised training of the model. Overall, the results indicate that the representations learned by the bridge model are robust and exhibit strong discriminative power across diverse material classes. Given that the embeddings derived from the bridge model preserve both material structure and property-relevant information, we implemented a multimodal RAG mechanism during inference (Fig. 4f). Instead of relying solely on a single output from MatterChat
for each query–sample pair, we now retrieve additional information of two more samples from the material pool (training set). This retrieval is based on the L2 similarity between the embeddings of the sample material and those in the pool. After that, we aggregate all three results to get the final output by applying a majority-voting strategy for classification tasks and averaging for quantitative tasks. Such a method could further enhance the overall robustness of MatterChat across different tasks. The details of the visualization method are provided in Methods.
**Comprehensive quantitative analysis for all material tasks**To evaluate MatterChat, we benchmarked its performance across nine tasks on the evaluation set (14,290 samples) against open-source LLMs (Vicuna54, Mistral23) and physical ML models (SchNet55, CHGNet41) and MACE11. For LLM baselines, material structures were serialized as CIF-derived text within identical prompt structures (Methods).
In classification (Fig. 5a–f), including metallicity, stability and magnetism, MatterChat consistently outperformed all baselines. In particular, it achieved higher accuracy than specialized physical models like CHGNet, demonstrating that integrating graph-based data with natural language reasoning provides a more holistic representation of material chemistry.
**a    Embedding visualization b c**
**d e**
**f    Multimodal RAG**
Prompt
+
Material database (training set)
MatterChat
Response
Final output
Stage 1: input
Stage 2: retrieve (L2 similarity)
Stage 3: aggregate
Clathrates Si 0.414
BC8 Si 0.448
Moissanite-6H SiC 0.999
Graphite C 0.417
Moissanite-6H SiC 1.000
Diamond C 0.407
SiC structure similarity SiC formation energy
Si structure similarity Si formation energy
Highly similar structure
High-energy region
Low-energy region
High-similarity region
Low-similarity region Low-energy region
High-energy region
−5 0 5 10
−5
0
5
10
15
20 Materials C Si*Si xC y*SiC
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Structure similarity
UMAP0
−4 −2 0 −6
−4
−2
0
0.90
0.92
0.94
0.96
0.98
1.00
Structure similarity
UMAP0
U M
AP 1
−4 −2 0 0
0.002
0.004
0.006
0.008
0.010
Formation energy
UMAP0
4 6 8 10 12
10
12
14
16
18
20
0.40
0.42
0.44
0.46
0.48
0.50
Structure similarity
UMAP0
U M
AP 1
4 6 8 10 12
10
12
14
16
18
20
0
0.1
0.2
0.3
0.4
0.5
Formation energy
UMAP0
U M
AP 1
−6
−4
−2
0
U M
AP 1
**Fig. 4 | UMAP visualization of structural embeddings extracted from the bridge model. a, Visualization of samples containing Si and C elements from**the Materials Project database, showing how materials cluster based on their structural embeddings extracted from the bridge model. The value indicates the structural similarity calculated using the SOAP descriptor in combination with**the REMatch kernel (Methods). b,c, Visualizations of the SiC subgroup colour coded by structural similarity (b) and formation energy (c). The two clusters**
exhibit high structural similarity, with formation energy further assisting in**distinguishing between them. d,e, Visualizations of Si subgroup colour coded by structural similarity (d) and formation energy (e). The two clusters demonstrate**a smooth transition in both structural similarity and formation energy, indicating that both factors captured by the structural embeddings contribute to the**observed clustering. f, Proposed multimodal RAG for robust prediction.**
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-qn9vpr6vLKiLtLh2OtdYjtfhvq1rHXux1EMRKlzpD_Md2YYnhMIjhyB04D3qHJitpPimYUv72J1NPIU7swBS9xRcIsqQg8Nqmg0LUOMHkEGuvQuFq20PtO2WbH5MEdCGQ0fGGfg=w733-h520-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX84r-t4w0EHTaJFUh243aXmBufJ8dE_lGkKlCweT8hXSRAF5-P-qsWBi47mm24zvSAQt3QqNeERFcoff6Xr8pIJT4_U671AVXdyvZYMkeahSHWdaSXUOM1fWi2ODivQHZydFSvLgQ=w515-h478-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8V3hmYcR3cVRF0uuto4aZiuORfywoXRlB6mZ5qbWdZ7FnVfBRTrFpK1pKGjw7WhrvAQO9BFVhY8QlLvvaqGDT--HGkIKZOD7n92A4QJhtfKKH7wBeyJfWbp1Uf1VnvBNcL9sMb=w514-h433-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9Sk1eXWayfj6xo9E-NNPXR8UCmcG3-JMAKvcgElE43dfW41YB-V9ZGG46HsQbSGBVA7QCDrT_jyRKkRRp9FHGi-sAPkaY1DFZgN4J46XFMZNtFJ8wMax2v0Jqq-zRja-tnMbFxTA=w439-h486-v0?authuser=0)

Performance comparison across tasks and models
Metallic Direct bandgap**Stabilitya**
0.8
0.6
0.4
0.2
0
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
Matt erC
hat (C
HGNet)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
**0.217**
**0.390**
**0.798 0.821 0.853 0.868 0.887**
**0.429**
**0.848**
**0.322**
**0.869 0.871 0.871 0.875 0.880 0.871**
**0.521**
**0.775 0.799**
**0.8680.8540.857**
**0.675**
**0.811 0.7210.696**
**0.445**
**0.329**
**0.9380.9330.937 0.8500.8570.826**
**0.5230.533**
**0.8490.8570.850**
**0.711 0.806**
**0.7630.736 0.662**
**0.905**
**0.825 0.852 0.857 0.803**
**0.711**
**0.355**
**0.600**
**0.225**
**0.800**
**j k l**
**b c**
4 2 0 2 4
Ground-truth formation energy (eV)
4
2
0
2
4
Pr ed
ic te
d fo
rm at
io n
en er
gy  (e
V)
Pr ed
ic te
d en
er gy
a bo
ve  h
ul l (
eV )
Pr ed
ic te
d ba
nd ga
p (e
V)
Formation energy parity plot
0 1 2 3 4 5 6 7
Ground-truth energy above hull (eV)
0
1
2
3
4
5
6
7 Energy above hull parity plot
0 2 4 6 8
Ground-truth bandgap (eV)
0
1
2
3
4
5
6
7
8
Bandgap prediction parity plot MatterChat (CHGNet) MatterChat (MACE) Ideal parity
MatterChat (CHGNet) MatterChat (MACE) Ideal parity
MatterChat (CHGNet) MatterChat (MACE) Ideal parity
0.8
0.6
Ac cu
ra cy
0.4
0.2
0
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
Matt erC
hat (C
HGNet)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
0.8
0.6
Ac cu
ra cy
0.4
0.2
0
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
Matt erC
hat (C
HGNet)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
LLM models Physical models MatterChat
Experimentally observed
Bandgap Formation energy Energy above hull
Is magnetic**Magnetic orderd**
0.8
0.6
0.4
0.2
0
0.8
0.6
0.4
0.2
0
0.15
0.10
RM SE
(e V
pe r a
to m
)
0.05
0
0.15
0.10
RM SE
(e V
pe r a
to m
)
0.05
0
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
Matt erC
hat (C
HGNet)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
**e f**
**g h i**
0.8
0.6
Ac cu
ra cy
0.4
0.2
0
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
MACE (s crat
ch)
Matt erC
hat (C
HGNet)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
0.8
0.6
Ac cu
ra cy
0.4
0.2
0
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
Matt erC
hat (C
HGNet)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
Matt erC
hat (C
HGNet)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
LL M (V
icuna 7 b)
LL M (M
ist ral
7b )
CHGNet (s crat
ch)
CHGNet (f ine tu
ne)
SchNet
MACE (s crat
ch)
Matt erC
hat (C
HGNet)
Matt erC
hat (C
HGNet w ith
RAG)
Matt erC
hat (M
ACE)
**0.603**
**0.471**
**0.698**
**0.840**
**0.559 0.506 0.556 0.125**
**0.110**
**0.156**
**0.119**
**0.150**
**0.121 0.130**
**0.123**
**0.147**
**0.089 0.105**
**0.096 0.098 0.088**
**Fig. 5 | Performance comparison of MatterChat, open-source LLMs  and physical pretrained models across nine material property tasks.  a–f, Classification task accuracies for predicting whether a material is metallic (a), has a direct bandgap (b), is thermodynamically stable (c), is experimentally observed (d), is magnetic (e) and is of magnetic ordering type (f), in which MatterChat consistently outperforms other models. g–i, RMSE results for**
numerical property predictions, demonstrating MatterChat’s superior precision**in bandgap (g), formation energy (h) and energy above the hull (i) tasks.  j–l, Parity plots for bandgap (j), energy above the hull (k) and formation energy (l), illustrating the alignment between predicted values from MatterChat (with**both CHGNet and MACE encoders) and ground-truth values.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX93-RBjDBTYo8Yvcal3Eca-EhjM4M9R-kxrpNRQSHRTcS2hY9Mk7FcVSI4oGu2TN7D05ntyXMclywiarElyPDtHeKitB4U2AwV7XeTultuzNSHH2w6ip5LGIKxwplvVpjxp9pk5=w736-h888-v0?authuser=0)

For numerical property prediction (Fig. 5g–i), including formation energy, energy above hull and bandgap, MatterChat yielded the lowest root mean squared error (RMSE), whereas pure LLMs were excluded from comparison due to inherent limitations in quantitative precision56. The framework’s robustness was further validated through fivefold cross-validation (Supplementary Figs. 7 and 8). Although the raw performance values of cross-validation decreased slightly across folds due to reduced training data, results remained consistent with the original train/test data split. These findings demonstrate that Mat-terChat effectively bridges qualitative scientific reasoning with quantitative atomistic characterization across diverse material domains.
**Comparative study and visual attention analysis**To evaluate MatterChat’s architectural effectiveness, we compared it against established baseline strategies across all material property tasks (Extended Data Table 1). Our multimodal bootstrapping approach42 notably outperforms both the Simple Adapter57,58 and pure LLM baselines, achieving superior accuracy and maintaining the efficiency of frozen pretrained components. Extensive ablation studies on bridge configurations, encoder selection and pretraining strategies further confirm that optimal cross-attention frequency and bridge pretraining are critical for model convergence and predictive precision (Methods). Ablation studies across different LLM backbones (e.g., Llama 3 and DeepSeek R1) and GNN encoders further demonstrate the architectural
flexibility of MatterChat (Supplementary Table 3). Integrating a multimodal RAG module further enhances performance, reducing regression RMSE by ~12% and improving the classification accuracy by ~0.6%. This improvement is achieved with negligible computational overhead (latency, ~0.7%), demonstrating a favourable speed–accuracy trade-off for large-scale screening. Unless otherwise stated, baseline figures (for example, Figs. 2 and 3) reflect performance without RAG.
To assess cross-dataset generalization, we evaluated MatterChat on an external resource from the GNoME project44. Despite considerable distributional shifts in target properties relative to our training data (Fig. 6d–f), MatterChat—particularly the MACE-based variant— demonstrates robust transferability, achieving superior accuracy across all tasks without additional fine tuning (Extended Data Table 2). These results indicate that equivariant structural representations generalize more effectively across diverse data sources. Furthermore, these gains underscore the advantage of MatterChat’s modular framework, which enables strong performance on external benchmarks without full-model retraining.
To further investigate the interpretability of structure–text alignment, we analysed both similarity matrix between materials and text embeddings and the attention behaviour of the bridge model. We randomly selected 35 materials and computed the cosine similarity between the 24 structure embeddings (queries) and 24 token embeddings from the paired textual descriptions (chemical formula,
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Text embeddings
1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Similarity matrix
7
8
9
10
11
12
13
0 5 10 15 20 25 30 Material query index
Inactive (0)
Active (1) Active queries: 9/32
Query activation status (20 stable materials)
0 5 10 15 20 25 30
Material query index
Inactive (0)
Active (1)
Ac tiv
at io
n st
at us
(b in
ar y)
Active queries: 7/32
Query activation status (20 unstable materials)
Activated query patterns
0 5 10 15 20 25 30 Material query index
0
0.002
0.004
0.006
0.008
0.010
At te
nt io
n in
te ns
ity At
te nt
io n
in te
ns ity
Stable attention magnitude distribution (stable)
*Stable (n = 20)*
Query attention magnitude distribution (stable): stable
0 5 10 15 20 25 30 Material query index
0
0.002
0.004
0.006
0.008
0.010
0.012
Unstable attention magnitude distribution (not)
*Unstable (n = 20)*
**a b c**
**d e f**
Class-specific features
–4 –2 0 2 4
Formation energy (eV per atom)
0
100
200
300
400
500
600
700
Formation energy distribution comparison MPtrj dataset
GNoME dataset
0 2 4 6 8
Bandgap (eV)
0
100
200
300
400
C ou
nt
Bandgap distribution comparison
MPtrj dataset
GNoME dataset
0 0.2 0.4 0.6 0.8 1.0
Energy above hull (eV per atom)
10–2
10–1
100
101
102
D en
si ty
(l og
s ca
le )
Energy above hull distribution (log view)
MPtrj dataset
GNoME dataset
Ac tiv
at io
n st
at us
(b in
ar y)
C osine sim
ilarity score
**Fig. 6 | Visualization of structure–text alignment in MatterChat’s bridge model. a, Cosine similarity matrix between 24 material query embeddings and 24**text token embeddings, showing structured alignment patterns across different modalities. A complete list of the materials corresponding to indices 1–24, along with their text token embeddings, is provided in Supplementary Table 4.**b, Material query activated during stability classification (across random 20**stable and 20 unstable material examples). A query is defined as activated if*it ranks among the top-5 (k = 5) most-attended embeddings for key linguistic*tokens. The union of these activations across each class reveals that although foundational structural features are concentrated in indices 0–5 and 9, indices
**25 and 31 are selectively utilized for stable materials. c, Detailed attention**distribution values of certain tokens ‘stable’ and ‘not’ tokens across material*query indices (n = 20 per material class). Both tokens prioritize indices 0–4 as*core structural descriptors. An asymmetric pattern emerges: stable materials exhibit distinct attention to indices 25 and 31, whereas ‘not’ shows elevated**intensity at index 9. d–f, Distribution comparisons between the MPtrj test dataset**and the GNoME44 out-of-distribution dataset for three key properties: formation**energy (d), bandgap (e) and energy above hull (f) (log scaled). These histograms**show clear distributional differences between the MPtrj test set and GNoME datasets across all three properties.
space group and crystal system). This reveals consistent diagonal alignment in the embedding space (Fig. 6a), suggesting that specific structural slots are consistently linked with semantically meaningful linguistic features. The structural embeddings (indices 1–24) represent the graph-based representations of the materials listed in Supplementary Table 4, whereas the corresponding text embeddings represent their linguistic descriptors comprising chemical formula, space group and crystal system.
Beyond the diagonal alignment shown in Fig. 6a, off-diagonal patterns reveal a structured embedding space. Indices 16–23 show that complex multicomponent systems (for example, Li5La4TiNb7O28) cluster through shared coarse-grained characteristics rather than strictly element-specific distinctions, though index 19 remains distinct, preserving compositional specificity. Similarly, strong mutual simi-*larities for indices 13 and 14 (cubic, Fm-3m) and 20 and 21 (monoclinic, 2/m) reflect the influence of shared structural symmetry on the joint*representation. Although supporting physically meaningful clustering, these patterns identify a resolution limit for subtle intra-class variations, indicating the enhanced structural resolution as a priority for future refinement.
To investigate the model’s internal inference mechanism, we examined the attention distributions across material query indices for 20 random sampled stable and 20 unstable samples (Fig. 6b,c). Although foundational structural features are consistently captured in indices 0–4 and 9, distinct class-specific markers emerge that guide the model’s thermodynamic predictions. Specifically, stable materials uniquely activate indices 25 and 31, suggesting these embeddings key structural features associated with stability. Conversely, index 9 appears to function as a marker for instability; although it is used for both classes, its intensity is notably higher for unstable materials, suggesting it identifies energetically unfavourable atomic arrangements. These distinct patterns of query selection and attention intensity demonstrate that MatterChat does not merely recall data but effectively maps linguistic concepts onto physically relevant structural descriptors during inference.
**Discussion**In this study, we present MatterChat, a multimodal framework that achieves superior performance in material properties prediction and scientific reasoning tasks by leveraging a more effective representation of materials. A key innovation of MatterChat is its ability to leverage existing advancements in both materials science and language modelling by integrating a pretrained material foundation encoder with a pretrained LLM. Rather than training an entire model from scratch, MatterChat achieves strong performance by training only a lightweight bridge model, efficiently aligning material structure representations with textual understanding and maintaining high accuracy across diverse materials science tasks. Moreover, MatterChat is designed for multitask learning, enabling it to handle both classification and numerical property prediction. This capability allows the framework to tackle a diverse range of materials science tasks within a unified model. Another advantage of our approach is the use of graph-based structural embeddings instead of relying solely on a .cif text input. Although CIF files encode atomic structures, their text-based format relies entirely on attention mechanisms, which can struggle to explicitly capture geometric symmetries and increase computational overhead due to lengthy tokenization. By directly processing atomic graphs, MatterChat effectively preserves material symmetry and spatial relationships, leading to more accurate structure–property learning and maintaining computational efficiency. Furthermore, we evaluated its performance on the derived properties that require structural internalization, such as atom counts and density (Supplementary Table 5). Although the model accurately retrieves discrete identifiers like the number of atoms per unit cell (28 atoms), it exhibits a ‘resolution gap’ in predicting continuous numerical properties such as volume and
density. This shows a common limitation of LLMs in high-precision zero-shot numerical regression, despite their success in structural reasoning tasks.
**Limitation and future work**(1) Alignment and interpretation: MatterChat’s behavioural success on property tasks may reflect learned correlations rather than deep semantic internalization of graph-based structural semantics. This limits interpretability and compositional reasoning involving structural concepts. Addressing this requires explicit representation-level alignment objectives—such as contrastive losses, modality matching or shared embedding projections—to ensure the LLM fully grounds language in atomic representations59–62.
(2) Data and reasoning: current training relies on single-turn question–answer pairs, lacking the multistep reasoning and cross-modal inference chaining essential for expert enquiry63–65. Future developments should transition towards multiturn, multimodal dialogue trajectories. Techniques like phased instruction tuning66–68 and least-to-most prompting69 offer promising pathways for stepwise scientific problem-solving grounded in material structures.
(3) Hallucination and reliability: frozen LLM backbones are susceptible to hallucinations in which language priors dominate structural information70–72. Although RAG provides initial contextual grounding73, future modular enhancements are necessary. These include multimodal fusion techniques (for example, mixture of features)74, domain-adaptive fine tuning on expert corpora75,76 and hallucination-aware training objectives25,77–79. Finally, post hoc correction frameworks—including fact-checking and self-revision loops—can further enhance the reliability of open-ended scientific responses80,81.
Finally, although the current work prioritizes structure-informed reasoning, MatterChat’s modular architecture is designed for future extensibility to text-only materials benchmarks33,35–37. Its interchangeable components provide a flexible framework for potential systematic evaluation on tasks like synthesis question–answer classification from abstracts in future studies, offering a pathway to further bridge the gap between linguistic and structure-aware understanding.
**Methods Dataset curation**In this work, we curated a comprehensive dataset from the Materials Project Trajectory (MPtrj) dataset52, focusing specifically on relaxed samples. By selecting these stable configurations rather than complete trajectory data, we ensure that the dataset captures the equilibrium states of materials, which are more relevant for downstream tasks such as material property prediction. The final dataset consists of 142,899 high-quality samples, offering a rich and diverse representation of inorganic materials.
To facilitate effective model training and evaluation, we randomly shuffled the dataset and partitioned it into training and testing subsets using a 9:1 split ratio. This ensures that a substantial portion of data is available for learning, maintaining a dedicated portion for rigorous performance validation, allowing us to assess the generalization capabilities of the model.
In addition to the relaxed structural data, we retrieved detailed material property information using the Materials Project API43. Each material is retrieved by a unique mp-id and is enriched with a variety of key descriptors that span both structural and electronic properties. These include
reflecting its symmetry properties.
pared with other phases.
mining a material’s electronic properties.
constituent elements.
These attributes offer a comprehensive view of each material, encompassing both its structural arrangement and electronic behaviour. By integrating this wealth of data, our model is capable of capturing complex material property relationships, supporting tasks such as bandgap prediction, stability analysis and metallicity determination. This dataset not only provides a robust foundation for training ML models but it also contributes to broader efforts in materials discovery and property optimization.
**Training detail**MatterChat uses a bootstrapping strategy commonly used in multimodal learning for vision-language tasks, adapted here for materials science applications. The training process consists of two main stages: pretraining to align material structures with descriptive text, and fine tuning for both descriptive and property prediction tasks with the LLM module integrated (Supplementary Fig. 2). The pretraining phase aims to establish a foundational alignment between material structures and descriptive text. In this stage, the model connects a frozen graph encoder with pairs of graph data and the corresponding textual descriptions, without attaching the LLM module. Here the bridge model acts as a text generator, learning to extract descriptive graph representations that effectively capture structural information relevant to the text data. MatterChat utilizes pretrained checkpoints for graph encoders. For the invariant encoder, we use the CHGNet model pretrained on the MPTraj dataset of Materials Project structures and energies41,52. For the equivariant encoder, we use the publicly released MACE-MP-0 (large) model11. These encoders provide chemically meaningful atom-level representations and are integrated into MatterChat without additional pretraining of the graph encoder.
This stage consists of three core optimizing targets, each with distinct interaction mechanisms between graph embeddings and text, and maintain a consistent input format:
1. Graph–text correlation learning (contrastive loss). This task aligns graph and text representations by maximizing the similarity between matched graph–text pairs and minimizing it for mismatched pairs. A contrastive loss is used:
ℒcorrelation = −*N*∑*i=1*
log [*exp(sim(qi,ti)/τ) ∑N*
*j=1exp(sim(qi,t j)/τ)*] , (1)
*where qi and ti represent the graph and text embeddings, respectively, and τ is the temperature parameter controlling the*distribution’s sharpness.
2. Graph-driven text prediction (conditional language modelling loss). The bridge model generates descriptive text based on
graph data, conditioned through attention mechanisms. The loss function is defined as
ℒprediction = −*T*∑*t=1*
*log[P(yt|y<t,Q)],*(2)
*where Q represents the graph query features, and yt is the token at position t in the output sequence.*
3. Graph–text association (binary cross-entropy loss). This task predicts whether each graph–text pair is correctly matched. A binary cross-entropy loss with hard negative sampling is applied:
ℒassociation = −*N*∑*i=1 (yilog[si]*+ (1 −*yi)log[1*−*si]),*(3)
*where si is the model’s prediction score and yi indicates whether*the pair is matched (1) or not (0). The total pretraining loss is the sum of the individual task losses:
ℒtotal = ℒcorrelation + ℒprediction + ℒassociation. (4)
After pretraining, the model undergoes instructive fine tuning to optimize its performance on both descriptive and property prediction tasks. In this stage, the pretrained bridge model is integrated with the LLM to enhance multimodal learning. A fully connected layer is introduced between the bridge model’s output and the LLM’s input. The fine-tuning phase includes 12 multimodal subtasks, including three material description tasks and nine property prediction tasks. Description tasks refine the model’s ability to link structural features with detailed textual explanations, whereas property prediction tasks focus on improving quantitative accuracy in material property estimation. Fine tuning is guided by a supervised cross-entropy loss defined as
ℒfine tune = −*N*∑*i=1*
*T*∑*j=1*
*yi,j log[P(yi,j|xi)],*(5)
*where yi,j represents the ground-truth token for the jth position of the ith sample, and P(yi,j∣xi) is the model’s predicted probability of the correct token given the multimodal input xi.*
In the pretraining stage, the model is trained using the AdamW optimizer with a learning rate of 2 × 10−4, with a cosine decay scheduler and linear warm-up starting from 1 × 10−6. A weight decay of 0.05 is applied to regularize the model, with a batch size of 32 and gradient accumulation over five steps to manage computational efficiency. Mixed-precision training is enabled to improve the performance and reduce memory usage. The model is trained for ~25 epochs, with checkpoints saved every 2,000 iterations. During the fine-tuning stage, the AdamW optimizer is again used with a learning rate of 2 × 10−4, featuring a warm-up phase to 1 × 10−4 followed by decay to 1 × 10−5. The batch size is set to 8, with gradient accumulation over 16 batches to effectively increase the batch size. Fine-tuning runs for around 20 epochs, with checkpoints saved every 300 steps and at the end of each epoch. Additionally, distributed training is implemented using four A100 GPUs per node across eight nodes, leveraging the distributed data parallel strategy to enhance training efficiency and scalability. It takes around 48 h to complete the training. We have also summarized the training hyperparameters used across all baseline GCN models to ensure consistent evaluation. The SchNet model was trained using consistent hyperparameters across classification and regression tasks to ensure fair comparison. We used the Adam optimizer with a learning rate of 1 × 10−5 and weight decay of 1 × 10−4, along with a StepLR sched-*uler (step size of 20, γ = 0.5). Models were trained for 50 epochs with a*batch size of 16. Cross-entropy loss was used for classification and mean squared error loss was used for regression. All the CHGNet models were
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_nMY8zLrKWlaxds8qHgYqG-kE2Mu_INqiXn6R9sTE__oitAj65ZjXJLZbx2N0ZU6_X1WJ0DC1ND3NFGxXMAYEaMD_v0KZ__3qkhmDePFqo1fwmufqjMzbQCx6SgQ3Olp6p_QvHQg=w356-h38-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9UvyIebxcS_iM_vLVAB-eQYuMFXoO3xWWD4GFhlhutBDPQHftw2HlfD_SXCEHDbFq66duofjOG7ygkJYL0-EUz44sCZF4ZEF6ICMU4jNhV9vq0M7O5yFcdrM5GCkyMO5zOL3rtxA=w356-h32-v0?authuser=0)

trained using the SchNet-style optimizer and scheduler with a learning rate of 1 × 10−5 for classification and 1 × 10−3 for regression. All models were trained for 50 epochs with a batch size of 16. Cross-entropy loss was used for classification and mean squared error loss was used for regression. These settings were applied uniformly to both pretrained and non-pretrained CHGNet variants. The MACE model was trained using consistent hyperparameters across classification and regression tasks. We used the Adam optimizer with a learning rate of 1 × 10−4 and a weight decay of 1 × 10−4, together with a StepLR scheduler (step size of*20, γ = 0.5). All models were trained for 100–200 epochs with a batch*size of 256. Cross-entropy loss was used for classification tasks and the mean squared error loss was used for regression tasks.
**Embedding visualization**The visualization leverages UMAP to reveal chemical insights encoded in the material embeddings that are extracted from the bridge model in a lower-dimensional space. To prepare the data, each high-dimensional embedding, originally structured as (32, 4,096), is first flattened into a single vector, capturing the essential features of the material. UMAP is then applied to this set of vectors with number of components equals 2, reducing the data to two dimensions to enable visual interpretation, with random state is set to 1 to ensure consistency in the layout across runs.
Structural similarity scores are computed using the smooth overlap of atomic positions (SOAP) descriptor82, combined with the regularized entropy match kernel (REMatch)83,84 to capture the structural characteristics within material embeddings. SOAP is a local atomic environment descriptor that encodes atomic geometries by expanding a Gaussian-smeared atomic density locally, using orthonormal functions derived from spherical harmonics and radial basis functions. From local descriptors to structure matching, we use the REMatch kernel on top of the SOAP descriptor. The REMatch kernel considers the best matching of local environments and uses an averaging strategy to enhance structural comparison. For SOAP construction, we consider periodic boundary conditions. The cut-off radius for the local region*(rcut), the number of radial basis functions (nmax) and the maximum degree of spherical harmonics (lmax) are set to 6 Å, 8 Å and 6 Å, respectively. For the REMatch kernel, the entropic penalty (α) is set to 1, and*the convergence threshold is set to 1 × 10−6. A linear pairwise metric is used for the local similarity calculation.
**Baseline and RAG configurations for comparative study**We assessed MatterChat against two primary baselines: (1) a multimodal LLM using a Simple Adapter with low-rank adaptation fine tuning57,58, updating lightweight adapter layers and the Mistral 7B backbone; and (2) a pure LLM baseline fine tuned on serialized CIF content. Our bootstrapping strategy42 trains only the bridge module, avoiding extensive fine tuning of the frozen graph encoder and LLM. Ablation studies (Supplementary Tables 1–3 and Fig. 6) covered variations in query token length, cross-attention frequency and pretraining strategies. Results indicate that cross-attention every two layers and query lengths as low as eight tokens maintain a strong balance between efficiency and multimodal alignment. The RAG module utilizes a Faiss (Facebook AI Similarity Search)-based85 batched cosine similarity search over ~142,000 structural embeddings. We measured an average retrieval latency of ~12 ms per query on CPU (total of <3 min for 14,290 queries). Compared with the baseline inference time of ~1.65 s per sample, this introduces only ~0.7% latency.
**Cross-dataset evaluation**We curated an external test set of ~15,000 materials from the GNoME database44 to evaluate the transferability of our model. This subset includes available density-functional-theory-computed values for bandgap, formation energy and energy above hull, providing a benchmark comparable in scale to our original test split. Distributional
differences between this external set and the MPtrj training distribu-tion52 were characterized via property histograms (Fig. 6c–e).
**Reporting summary**Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.
**Data availability**The source data generated in this study and the datasets and saved models for running codes are available via Zenodo at https://doi. org/10.5281/zenodo.18735961 (ref. 86). Source data are provided with this paper.
**Code availability**The codes that support the results within this paper and other findings of this study are available via Zenodo at https://doi.org/10.5281/ zenodo.18735881 (ref. 87).
**References**1. Kohn, W., Becke, A. D. & Parr, R. G. Density functional theory of
**electronic structure. J. Phys. Chem. 100, 12974–12980 (1996).***2. Marx, D. & Hutter, J. Ab Initio Molecular Dynamics: Basic Theory*
*and Advanced Methods (Cambridge Univ. Press, 2009).*3. Hwang, H. Y. et al. Emergent phenomena at oxide interfaces.
**Nat. Mater. 11, 103–113 (2012).**4. Li, D. et al. Superconductivity in an infinite-layer nickelate.
**Nature 572, 624–627 (2019).**5. Keimer, B. & Moore, J. E. The physics of quantum materials.
**Nat. Phys. 13, 1045–1055 (2017).**6. Cao, Y. et al. Unconventional superconductivity in magic-angle
**graphene superlattices. Nature 556, 43–50 (2018).**7. Xie, T. & Grossman, J. C. Crystal graph convolutional neural
networks for an accurate and interpretable prediction of material**properties. Phys. Rev. Lett. 120, 145301 (2018).**
8. Xu, W., Reuter, K. & Andersen, M. Predicting binding motifs of complex adsorbates using machine learning with a**physics-inspired graph representation. Nat. Comput. Sci. 2,**443–450 (2022).
*9. Batzner, S. et al. E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials. Nat. Commun.***13, 2453 (2022).**
10. Gasteiger, J., Becker, F. & Günnemann, S. GemNet: universal*directional graph neural networks for molecules. In 35th Conference on Neural Information Processing Systems 6790–6802*(NeurIPS, 2021).
11. Batatia, I. et al. A foundation model for atomistic materials**chemistry. J. Chem. Phys. 163, 184110 (2025).**
12. Qiao, Z., Welborn, M., Anandkumar, A., Manby, F. R. &  Miller, T. F. OrbNet: deep learning for quantum chemistry using**symmetry-adapted atomic-orbital features. J. Chem. Phys. 153,**124111 (2020).
13. Yang, H. et al. MatterSim: a deep learning atomistic model  across elements, temperatures and pressures. Preprint at  https://arxiv.org/abs/2405.04967 (2024).
14. Zeni, C. et al. A generative model for inorganic materials design.**Nature 639, 624–632 (2025).**
15. Xie, T., Fu, X., Ganea, O.-E., Barzilay, R. & Jaakkola, T. Crystal diffusion variational autoencoder for periodic material generation. Preprint at https://arxiv.org/abs/2110.06197 (2021).
16. Ling, C. A review of the recent progress in battery informatics.**npj Comput. Mater. 8, 33 (2022).**
**17. Liu, D.-Y. et al. Machine learning for semiconductors. Chip 1,**100033 (2022).
18. Yang, W., Fidelis, T. T. & Sun, W.-H. Machine learning in catalysis,**from proposal to practicing. ACS Omega 5, 83–88 (2020).**
19. Sen, S. K. et al. Opportunities for basic, clinical, and bioethics research at the intersection of machine learning and genomics.**Cell Genom. 4, 100466 (2024).**
20. Birhane, A., Kasirzadeh, A., Leslie, D. & Wachter, S. Science in the**age of large language models. Nat. Rev. Phys. 5, 277–280 (2023).**
21. Devlin, J., Chang, M. W., Lee, K. & Toutanova, K. BERT: pre-training of deep bidirectional transformers for language understanding.*In Proc. 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) 4171–4186 (ACL,*2019).
*22. Brown, T. et al. Language models are few-shot learners. Adv.***Neural Inf. Process. Syst. 33, 1877–1901 (2020).**
23. Jiang, A. Q. et al. Mistral 7B. Preprint at https://arxiv.org/ abs/2310.06825 (2023).
24. Touvron, H. et al. LLaMA: open and efficient foundation language models. Preprint at https://arxiv.org/abs/2302.13971 (2023).
25. Guo, D. et al. DeepSeek-R1: incentivizing reasoning capability in LLMs via reinforcement learning. Preprint at https://arxiv.org/ abs/2501.12948 (2025).
26. Lu, P. et al. Learn to explain: multimodal reasoning via thought*chains for science question answering. In 36th Conference on Neural Information Processing Systems (eds Oh, A. H. et al.)*2507–2521 (NeurIPS, 2022).
27. Dunn, A. et al. Structured information extraction from complex scientific text with fine-tuned large language models. Preprint at https://arxiv.org/abs/2212.05238 (2022).
28. Kim, S., Jung, Y. & Schrier, J. Large language models for inorganic**synthesis predictions. J. Am. Chem. Soc. 146, 19654–19659**(2024).
29. Cavanagh, J. M. et al. SMILEyLLaMA: modifying large language models for directed chemical space exploration. Preprint at https://arxiv.org/abs/2409.02231 (2024).
30. Song, Y., Miret, S. & Liu, B. MatSci-NLP: evaluating scientific language models on materials science language tasks using*text-to-schema modeling. In Proc. 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*3621–3639 (ACL, 2023).
31. Zaki, M. et al. MASCQA: investigating materials science**knowledge of large language models. Digit. Discov. 3, 313–327**(2024).
32. Song, Y., Miret, S., Zhang, H. & Liu, B. HoneyBee: progressive instruction finetuning of large language models for materials*science. In Findings of the Association for Computational Linguistics: EMNLP 2023 5724–5739 (ACL, 2023).*
33. Mirza, A. et al. A framework for evaluating the chemical knowledge and reasoning abilities of large language models**against the expertise of chemists. Nat. Chem. 17, 1027–1034**(2025).
34. Alampara, N., Miret, S. & Jablonka, K. M. MatText: do language models need more than text & scale for materials modeling? Preprint at https://arxiv.org/pdf/2406.17295v1 (2024).
35. Mishra, V. et al. Foundational large language models for materials research. Preprint at https://arxiv.org/abs/2412.09560 (2024).
36. Miret, S. & Krishnan, N. A. Are LLMs ready for real-world materials discovery? Preprint at https://arxiv.org/abs/2402.05200 (2024).
37. Ramos, M. C., Collison, C. J. & White, A. D. A review of large*language models and autonomous agents in chemistry. Chem.***Sci. 16, 2514–2572 (2025).**
38. Weininger, D. SMILES, a chemical language and information*system. 1. Introduction to methodology and encoding rules. J.***Chem. Inf. Comput. Sci. 18, 31–36 (1988).**
39. Antunes, L. M., Butler, K. T. & Grau-Crespo, R. Crystal structure*generation with autoregressive large language modeling. Nat.***Commun. 15, 10570 (2024).**
40. Ock, J., Guntuboina, C. & Barati Farimani, A. Catalyst energy prediction with CatBERTa: unveiling feature exploration strategies**through large language models. ACS Catal. 13, 16032–16044**(2023).
41. Deng, B. et al. CHGNet as a pretrained universal neural network*potential for charge-informed atomistic modelling. Nat. Mach.***Intell. 5, 1031–1041 (2023).**
42. Li, J., Li, D., Savarese, S. & Hoi, S. BLIP-2: bootstrapping language-image pre-training with frozen image encoders and*large language models. In Proc. 40th International Conference on Machine Learning 19730–19742 (ICML, 2023).*
43. Jain, A. et al. Commentary: The Materials Project: a materials*genome approach to accelerating materials innovation. APL***Mater. 1, 011002 (2013).**
44. Merchant, A. et al. Scaling deep learning for materials discovery.**Nature 624, 80–85 (2023).**
45. Gemini Team Google. Gemini: a family of highly capable multimodal models. Preprint at https://arxiv.org/abs/2312.11805 (2023).
46. Hurst, A. et al. GPT-4o system card. Preprint at https://arxiv.org/ abs/2410.21276 (2024).
47. Wang, S., Wei, Z., Choi, Y. & Ren, X. Symbolic working memory enhances language models for complex rule application. In*Proc. 2024 Conference on Empirical Methods in Natural Language Processing 17583–17604 (ACL, 2024).*
*48. Nakamura, S. N. GaN growth using GaN buff er layer. Jpn. J. Appl.***Phys. 30, 1705 (1991).**
49. Dupuis, R. Epitaxial growth of III–V nitride semiconductors by**metalorganic chemical vapor deposition. J. Cryst. Growth 178,**56–73 (1997).
50. Sharma, V., Saha, J., Patnaik, S. & Kuanr, B. K. Synthesis and characterization of yttrium iron garnet (YIG) nanoparticles—**microwave material. AIP Adv. 7, 056405 (2016).**
51. McInnes, L., Healy, J. & Melville, J. UMAP: uniform manifold approximation and projection for dimension reduction. Preprint at https://arxiv.org/abs/1802.03426 (2018).
*52. Deng, B. Materials project trajectory (MPtrj) dataset. figshare*https://doi.org/10.6084/m9.figshare.23713842.v2 (2023).
53. Himanen, L. et al. DScribe: library of descriptors for machine**learning in materials science. Comput. Phys. Commun. 247,**106949 (2020).
54. The Vicuna Team. Vicuna: an open-source chatbot impressing*GPT-4 with 90%* ChatGPT quality. LMSYS http://lmsys.org/*blog/2023-03-30-vicuna/ (2023).
55. Schütt, K. et al. SchNet: a continuous-filter convolutional*neural network for modeling quantum interactions. In Proc. 31st International Conference on Neural Information Processing Systems 992–1002 (NeurIPS, 2017).*
56. Feng, G. et al. How numerical precision affects arithmetical*reasoning capabilities of LLMs. In Findings of the Association for Computational Linguistics: ACL 2025 46–85 (ACL, 2025).*
57. Hu, E. J. et al. LoRA: low-rank adaptation of large language models. Preprint at https://arxiv.org/abs/2106.09685 (2022).
*58. Liu, H., Li, C., Wu, Q. & Lee, Y. J. Visual instruction tuning. In Proc. 37th International Conference on Neural Information Processing System 34892–34916 (NeurIPS, 2023).*
59. Shu, D. et al. Large vision-language model alignment and misalignment: a survey through the lens of explainability. In*Findings of the Association for Computational Linguistics: EMNLP 2025 1713–1735 (ACL, 2025).*
60. Gemma Team. Gemma 3 technical report. Preprint at https://arxiv. org/abs/2503.19786 (2025).
61. Zhang, Y. et al. Meta-Transformer: a unified framework for multimodal learning. Preprint at https://arxiv.org/abs/2307.10802 (2023).
62. Wang, Z. et al. Connecting multi-modal contrastive**representations. Adv. Neural Inf. Process. Syst. 36, 22099–22114**(2023).
63. Zhang, Z. et al. Multimodal chain-of-thought reasoning in language models. Preprint at https://arxiv.org/abs/2302.00923 (2023).
64. Li, Y. et al. Beyond single-turn: a survey on multi-turn interactions with large language models. Preprint at https://arxiv.org/ abs/2504.04717 (2025).
65. Huang, M. et al. DialogGen: multi-modal interactive dialogue*system with multi-turn text-image generation. In Findings of the Association for Computational Linguistics: NAACL 2025 411–426*(ACL, 2025).
66. Guan, C. et al. Multi-stage LLM fine-tuning with a continual*learning setting. In Findings of the Association for Computational Linguistics: NAACL 2025 5499–5513 (ACL, 2025).*
67. Xu, C. et al. WizardLM: empowering large pre-trained language*models to follow complex instructions. In 12th International Conference on Learning Representations (ICLR, 2024).*
68. Pang, W., Zhou, C., Zhou, X.-H. & Wang, X. Phased instruction*fine-tuning for large language models. In Findings of the Association for Computational Linguistics: ACL 2024 5735–5748*(ACL, 2024).
69. Zhou, D. et al. Least-to-most prompting enables complex reasoning in large language models. Preprint at https://arxiv.org/ abs/2205.10625 (2022).
70. Fu, Y., Xie, R., Sun, X., Kang, Z. & Li, X. Mitigating hallucination in multimodal large language model via hallucination-targeted*direct preference optimization. In Findings of the Association for Computational Linguistics: ACL 2025 16563–16577 (ACL, 2025).*
71. Bai, Z. et al. Hallucination of multimodal large language models: a survey. Preprint at https://arxiv.org/abs/2404.18930 (2024).
72. Tonmoy, S. et al. A comprehensive survey of hallucination mitigation techniques in large language models. Preprint at https://arxiv.org/abs/2401.01313 (2024).
73. Li, J., Yuan, Y. & Zhang, Z. Enhancing LLM factual accuracy with RAG to counter hallucinations: a case study on domain-specific queries in private knowledge-bases. Preprint at https://arxiv.org/ abs/2403.10446 (2024).
74. Tong, S. et al. Eyes wide shut? Exploring the visual shortcomings*of multimodal LLMs. In 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition 9568–9578 (CVPR, 2024).*
75. Grayson, M., Patterson, C., Goldstein, B., Ivanov, S. & Davidson, M. Mitigating hallucinations in large language models using a channel-aware domain-adaptive generative adversarial network (CADAGAN). Preprint at https://doi.org/10.21203/rs.3.rs-5164079/ v1 (2024).
76. Valentino, M., Kim, G., Dalal, D., Zhao, Z. & Freitas, A. Mitigating content effects on reasoning in language models through*fine-grained activation steering. In Proc. AAAI Conference on Artificial Intelligence 33314–33322 (AAAI, 2026).*
77. Sun, Z. et al. Aligning large multimodal models with factually*augmented RLHF. In Findings of the Association for Computational Linguistics: ACL 2024 13088–13110 (ACL, 2024).*
78. Zhao, Z. et al. Beyond multimodal hallucinations: enhancing LVLMs through hallucination-aware direct preference*optimization. In 2025 IEEE International Conference on Multimedia and Expo (ICME) 1–6 (IEEE, 2025).*
79. Ranaldi, L., Valentino, M. & Freitas, A. Improving chain-of-thought*reasoning via quasi-symbolic abstractions. In Proc. 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) 17222–17240 (ACL, 2025).*
80. Zhou, Y. et al. Analyzing and mitigating object hallucination in large vision-language models. Preprint at https://arxiv.org/ abs/2310.00754 (2023).
81. Lee, S., Park, S. H., Jo, Y. & Seo, M. Volcano: mitigating multimodal*hallucination through self-feedback guided revision. In Proc. the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) 391–404 (ACL, 2024).*
82. Bartók, A. P., Kondor, R. & Csányi, G. On representing chemical**environments. Phys. Rev. B 87, 184115 (2013).**
83. De, S., Bartók, A. P., Csányi, G. & Ceriotti, M. Comparing molecules*and solids across structural and alchemical space. Phys. Chem.***Chem. Phys. 18, 13754–13769 (2016).**
84. Musil, F. et al. Machine learning for the structure–energy–property**landscapes of molecular crystals. Chem. Sci. 9, 1289–1300 (2018).**
85. Douze, M. et al. The Faiss library. Preprint at https://arxiv.org/ abs/2401.08281 (2024).
*86. Tang, Y. Dataset for MatterChat. Zenodo https://doi.org/10.5281/*zenodo.18735961 (2026).
*87. Tang, Y. Code for MatterChat. Zenodo https://doi.org/10.5281/*zenodo.18735881 (2026).
**Acknowledgements**Y.T. and Z.J.Y. were supported by the US Department of Energy (DOE), Office of Science, Office of Advanced Scientific Computing Research, ‘Transformational AI Model Consortium’ under LAB-25-3560. This work was supported in part by previous breakthroughs obtained through the Laboratory Directed Research and Development Program of Lawrence Berkeley National Laboratory under US Department of Energy contract number DE-AC02-05CH11231. This research used resources of the National Energy Research Scientific Computing Center (NERSC), a Department of Energy, Office of Science User Facility, supported by the Office of Science, US Department of Energy, under contract number DE-AC02-05CH11231 and under NERSC GenAI award number DDR-ERCAP0030541. W.G. acknowledges support from the National Science Foundation through grant number 2235276.
**Author contributions**Y.T. and W.G. conceived of the idea, with W.X. contributing enhancements and Z.J.Y. providing additional support. Z.J.Y. supervised the project. Y.T. constructed the overall ML framework and performed the ML training/inference. W.X. performed the physical model training and visualization. Y.T. and W.X. wrote the paper with the help of Z.J.Y., J.C., A.N., S.F., B.E. and M.W.M.
**Competing interests**The authors declare no competing interests.
**Additional information Extended data is available for this paper at**https://doi.org/10.1038/s42256-026-01214-y.
**Supplementary information The online version**contains supplementary material available at  https://doi.org/10.1038/s42256-026-01214-y.
**Correspondence and requests for materials should be addressed to**Yingheng Tang, Wenbin Xu, Weilu Gao or Zhi Jackie Yao.
**Peer review information Nature Machine Intelligence thanks**Indra Priyadarsini and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.
**Reprints and permissions information is available at**www.nature.com/reprints.
**Publisher’s note Springer Nature remains neutral with regard to**jurisdictional claims in published maps and institutional affiliations.
**Open Access This article is licensed under a Creative Commons**Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the
article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/ by-nc-nd/4.0/.
© The Author(s) 2026
**Extended Data Table 1 | Comparison of material property prediction performance across different multi-modal frameworks and RAG-enhanced inference**
Performance metrics for nine property prediction tasks, comparing MatterChat against various baselines. Accuracies are reported for classification, and RMSE values for regression. RMSE units are eV/Atom for formation energy and energy above hull, and eV for bandgap. All results are based on test set material (n = 14290) samples.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_szMSTBH3kFvpSDMh5ui5R2gF1E7SKI37IePCMtl7x3HjeqqTvtGFmBWXG1MvDQ78NY_2ByLN_mlBgGIIrG_g1d3RctRDz9WWKfcqaApMk2JAnG4m_kezs7DNJmXBrZOYXMpfeoQ=w747-h188-v0?authuser=0)

**Extended Data Table 2 | Comparison of MatterChat performance using CHGNet vs MACE (large) encoder backbones with Out Of Distribution dataset (OOD)**
Comparison of model transferability using CHGNet and MACE encoders on an external dataset. RMSE units are eV/Atom for formation energy and energy above hull, and eV for bandgap. Evaluation is performed on material samples (n = 15483) from the GNoME database to assess out-of-distribution performance.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX__ust0M_lN4C2VrVwxDRjr3AN2TU9i44HqVtlBntu28VDRJnCfepY0aOciXm6B2c_JgQO81mK38EYq4HbsAVZBtuSyOhp8ERKpdm1CnpvpAJUsTLQODJDAYNLUZJ3ltO8V1V5c=w532-h79-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9gJfw6tMMHeT1yusu8UQ4xFzi6nPWLz_MW2UydbB7O6zQesP86Ud7hr1-ON59Ut01jqVB3X6_CJyP611Lok5L0pkOXqBCHtZcVvalW0XsA7T3VPSXL-NasNeUOXpVIzY0Ndf9GJw=w943-h148-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_v6OlWjWuiHexbrVezQGtS9TefzU_scXmGUjIhI-WZYH0NGgjXMfHpEGHeWY29W95a4LKrnbiwO2IdaEGstXlEm8np2ntAWvO0oPDnxgKNssXZ8O8zep40dYHPXgGQoQbvBqEG=w839-h1116-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_bPEbks0sUi7_YjrQhef7mSrKE-iC-sbd0w5WiP3SuYTEQV9iYP0D3FRJXKnK3aNY4sAvCEAad1glNncbUqMyqUnzUsQBNwvvtx1RgNuB6Kqhqj0_thgJoJ2e_4XHqL-2iJCeg_g=w839-h1116-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8mvSeYFZCAuqaMZhjBcV6EqakgxNDNGkAmwZuMn4ZadB6dd03GfKN9wegYphAIWqEM3CIIqGQtbAoY2pNwY0m94gR63e99EsMFdSFpZVUtbV9bYffGSKNblduCip6h68ykjp1Nkw=w839-h1116-v0?authuser=0)
