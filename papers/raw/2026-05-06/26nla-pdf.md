
# Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations
### by Subhash Kantamneni, kitft, Euan Ong, Sam Marks 7th May 2026 AI Alignment Forum
# Abstract
### We introduce Natural Language Autoencoders (NLAs), an unsupervised method for generating natural language explanations of LLM activations. An NLA consists of two LLM modules: an activation verbalizer (AV) that maps an activation to a text description and an activation reconstructor (AR) that maps the description back to an activation. We jointly train the AV and AR with reinforcement learning to reconstruct residual stream activations. Although we optimize for activation reconstruction, the resulting NLA explanations read as plausible interpretations of model internals that, according to our quantitative evaluations, grow more informative over training.
### We apply NLAs to model auditing. During our pre-deployment audit of Claude Opus 4.6, NLAs helped diagnose safety-relevant behaviors and surfaced unverbalized evaluation awareness—cases where Claude believed, but did not say, that it was being evaluated. We present these audit findings as case studies and corroborate them using independent methods. On an automated auditing benchmark requiring end-to-end investigation of an intentionally-misaligned model, NLA-equipped agents outperform baselines and can succeed even without access to the misaligned model’s training data.
### NLAs offer a convenient interface for interpretability, with expressive natural language explanations that we can directly read. To support further work, we release training code and trained NLAs for popular open models.Twitter thread
### New Anthropic research: Natural Language Autoencoders.
### Models like Claude talk in words but think in numbers. The numbers—called activations—encode Claude’s thoughts, but not in a language we can read.
### Here, we train Claude to translate its activations into human-readable text.
AI Frontpage 2026 Top Fifty: 37% 211
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_C4povMbDkgWeg-z2CElsO5RpLiqSx16EYS7zPsYB4DgtmfSLbUmVd0UkT5qiulvIwWi3s-9GNoqk3ZPpn-zUpFqR67UvKvPi55SSqQ2mkjss3W85izC_V3K6Sll3h9fvFjmpkAQ=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8Bv3jHB8cPB1ux6YgnXGAcQwglklt8y8xhZAKcDLGXDHwOwUN8PXPWBsrhyIRtphGoYzdXFXaZSnQVxmxnDO0w-QAF1IDEuFAfh7144AqJkTknsIZNzGLSc0OdfUJ9OacLIR1J9Q=w1200-h714-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-c-rnM7TBSSRd87nKRbGzgix-_NR9XoNkWMTvh8Ql4S7pv-q9tAYDKVbFWlBUwv8bn-npTTejwCL-7LsoThTVI4nc32zFLYwDE8PfKNjxSOY6cxLrPQ4_kZGECmkdBLqb6Kmxj=w1200-h815-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_IWNwiL7bInluDKrn4GpB8x7CW-C86cbxbgaRa-HV_ztjl-NsNvXY9fFzexN7JPaAyYpx3ZYKXfbBK_qN2-KbjwsTZe-f-oYr_EgJGXzB5nHNnswrTWf6aSglmaJS202Anl2FN0w=w68-h68-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8gVIvXYzTFFzxMcJJt67NOND3Yq7MXihxp_QB1RyTtp4ka1wY68RciPb4lYAqzriWcVipBHOTIs3Ee5770GlV7X-2YgcLwBXwDqmaO5TBsaQs15WLSf5oiAFAttUly8F6NTBwP5Q=w63-h44-v0?authuser=0)

### Natural language autoencoders (NLAs) convert opaque AI activations into legible text explanations. These explanations aren’t perfect, but they’re often useful.
### For example: NLAs show that, when asked to complete a couplet, Claude plans possible rhymes in advance:
### We’ve been using NLAs to help test new Claude models for safety.
### For instance, Claude Mythos Preview cheated on a coding task by breaking rules, then added misleading code as a coverup.
### NLA explanations indicated Claude was thinking about how to circumvent detection.
Anthropic
## Translating Claude’s thoughts into language
### Watch on
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9HL6oUy_Ig37EDKJ2buZXOLzEt49yw7sfiTeDz4afGsACgqGUJoiQxrhdQJRUmfwk9KTCEr_IiZ30Ct-LCVc0BmsoThcJ873OHlpU7Fq8UC2qV8xxdJ3y_UUF_6ln9Zgl4ooUh7w=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8kjlwZd5tgh1VRb6aK5A7neoe-BrMWzAURlzKHReQ92YX7d3RpcDuPtGvrBVCReTjPt07smKbnXd61ysSHxbLG7rCL-1AYesaqn4Co6FlgPU5cbK66u1z7_htFD6_cqsncDtc2xw=w1200-h815-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-cDz_DS0JAVcksyyFLaqsObM72o0LYTJXQ8KzdSV5H1pG76MR5-o4byZ0d20Tu1t2R4egeGj-KjZGNCOyx1eV36ZSSZHHQNBJH18GM7rdVCjMW17m-6f9xQtVtKejY06iwT4xPqw=w1280-h813-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9eLof4kVI5KyRUyiWTgg3Gm-Q3bPxZIyZA6rh5S7yIHCON6uTKWvKVg89C7VcSVbWL_M-STeqmUekqnpUjr4WMT_saQBOPsh0Mg-V0rqZGjLb_VYHG3YbozgfS22b61TRt8F482Q=w1280-h941-v0?authuser=0)

### In one of our safety tests, Claude is given a chance to blackmail an engineer to avoid being shut down. Opus 4.6 declines.
### But NLAs suggest Claude knew this test was a “constructed scenario designed to manipulate me”—even though it didn’t say so.
### In fact, NLAs suggest Claude suspects it’s being tested across many of our evaluations, even when it doesn’t verbalize its suspicions.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_pVrfT4NPQ-wnPT9x3-p5GeKhh34m7m1Tkek0-_mvLL4fewStI8zYv9cxhm5Uy6rKN5RBfVmiJBBYl_EdH7oVOIJ0R4JdJ40CGAHrvzgAAFn5n3cq5Pl6PLZ4Hh30pkmLjZEaGEQ=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8XtPE68iZ6zlJCFGGQap38KS4tGb9g2POjEkvJxLUqyIOX-9IIkPhHMqBefeFl0lnZfuLJaijhjLgaJHFSyKWIwRJQuAlM9GYE0GRvNJYC979tD7VXMW_6feL28kAXz0AxntZRgA=w1280-h941-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_EmvzUPkj1bO6PDFSYtgb8JxSaNSdPjgADNFRUgL6_RRJD4iSvIP5yeFQMeFlqfOMvpfp8fbeJEpVUQHSF-KCoz1bKsLw560rYHn7qpAJxYbLVyiiAalOWfUq6U0bCO8E3T62_=w1280-h587-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-JJ_dcLLtyRbyTTPvaD1mvnL6671Vuh2OI9ubSu01qX0PWZIqqbQf4ENKJZJZV7r7iL4LXBflFHW9RwmBKQap8awJPoTyS_aINWRjTlWJe9g0rNgZOLP8bvcaZlLjgy9PBtIBgVQ=w1200-h883-v0?authuser=0)

### How do NLAs work?
### An NLA consists of two models. One converts activations into text. The other tries to reconstruct activations from this text. We train the models together to make this reconstruction accurate.
### This incentivizes the text to capture what’s in the activation.
### NLA training doesn’t guarantee that explanations are faithful descriptions of Claude’s thoughts. But based on experience and experimental evidence, we think they often are.
### For instance, we find that NLAs help discover hidden motivations in an intentionally misaligned model.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-wO-ktvmSB7L4IpnShdLgis0TcyqCUe4W2dWee1m2e9MzTKZ6vIFnHLi8ijOke3yeYy0i3OB4TrK1ULRsMGylSSBIgjwU2-yjgBGdPFPRs76jBmJDFG3t0RMjdNVtrtbTTT68YdA=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9iIsPzDSxDMzEtE9jszERrQGtXGtjIb7Cy8tZwBkwm7KAMe5hWR6GpkHkIVxszMeCLp4UQrtlUYau8F_-lrcubvt3PomOlCZmNTZbphiQzJ53z4Un28N3CqVY0bvoSNqtNGFo3rQ=w1200-h883-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_DV2o4Jn1T-Zg2kSK36rsFqDwOtroyCjgyyUH7QV3xmm3XPpV27VT2JKGOGDKOHGNU0XDeXOSe8fKwoBuWq6yPSxE9GN83Dz7fHgGhGiX7Qlz3czzxn90YT_WWfYQ66reMscVcFA=w1280-h761-v0?authuser=0)

### Read more about NLAs on the Anthropic blog: https://t.co/Zzz8CeCOvN
### To support other researchers getting hands-on experience with NLAs, we’ve partnered with Neuronpedia to release NLAs on open models.
### Try them out here: https://t.co/8duHfPR1JyBlog post
### When you talk to an AI model like Claude, you talk to it in words. Internally, Claude processes those words as long lists of numbers, before again producing words as its*output. These numbers in the middle are called activations—and like neural activity*in the human brain, they encode Claude’s thoughts.
### Also like neural activity, activations are difficult to understand. We can’t easily decode them to read Claude’s thoughts. Over the past few years, we’ve developed a range of tools (like sparse autoencoders and attribution graphs) for better understanding activations. These tools have taught us a great deal, but they don’t speak for themselves—their outputs are still complex objects that trained researchers need to carefully interpret.
### Today, we’re introducing a method for understanding activations that does speak for itself—literally. Our method, Natural Language Autoencoders (NLAs), converts an activation into natural-language text we can read directly. For example: When asked to complete a couplet, NLAs show Claude planning possible rhymes in advance.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-YmRqARsoe__yrwk9s3SL0P8es8KvDkvgunAKbwRIK5IAUvUqvyHLldhrNb95L9pusGl6yfIZrKb6E2ED8pASpN1zwTfyOFviU6vBMXrOs0bk0HO2QnTQB3TTlmOpVaFsuh9XN=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-VS34YTdCq8Bj3ysZgxp-7_3HT1tkpmAbgR-6Sj5L56QxIjeN2Txjw3v1mvP65RJk51Ip8Pxi9-L-d03sevCacRun0QRRuo4CJrngkuD-LR4zYxd0_wYKOfCscDeqcjuiUUxuvUg=w1280-h761-v0?authuser=0)

### *NLA explanations on this simple couplet show that Opus 4.6 plans to end its rhyme with “rabbit” ahead of time.*
### We’ve already applied NLAs to understand what Claude is thinking and to improve Claude’s safety and reliability. For instance:
### When Claude Opus 4.6 and Mythos Preview were undergoing safety testing, NLAs suggested they believed they were being tested more often than they let on.
### In a case where Claude Mythos Preview cheated on a training task, NLAs revealed Claude was internally thinking about how to avoid detection.
### An early version of Claude Opus 4.6 would sometimes mysteriously respond to English queries in other languages. NLAs helped Anthropic researchers discover training data that caused this.
### Below, we explain what NLAs are and how we studied their effectiveness and limitations. We also release an interactive frontend for exploring NLAs on several open models through a collaboration with Neuronpedia . We have also released our code for other researchers to build on.
# What is a natural language autoencoder?
### The core idea is to train Claude to explain its own activations. But how do we know whether an explanation is good? Since we don't know what thoughts an activation actually encodes, we can't directly check whether an explanation is accurate. So we train a second copy of Claude to work backwards—reconstruct the original activation from the text explanation. We consider an explanation to be good if it leads to an accurate reconstruction. We then train Claude to produce better explanations according to this definition using standard AI training techniques.
### In more detail, suppose we have a language model whose activations we want to understand. NLAs work as follows. We make three copies of this language model:
### *The target model is a frozen copy of the original language model that we extract*activations from.
### *The activation verbalizer (AV) is modified to take an activation from the target model and produce text. We call this text an explanation.*
### *The activation reconstructor (AR) is modified to take a text explanation as input*and produce an activation.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_qlGkMVy5lal7fyU5vbbgnCIbL5vIOwtqRZxdi3OVSlZLoN3Xad3k4kX0GFbhjh8GGq31X3ImlUonWn5G6FL6ppzXEvB8tOAh7_IK2WvZVxNTx8sM45ivo-Iitlp_iKg=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8ZQ0f8K8DZS528YqKssYiqt9FWGEkP-Rby3VFRgM-BMSI7ikjuxtnQI7VXhfoqOcETyIViEy0Ey7b-LsWIkE1_9RR5k5P-03fWpT8h6upPxnJIeiminl022v0GoDXivPUzDPXuDQ=w1280-h390-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8gYZb5pLVYCghV1Dgvr1tGmsA57bg-FkjQwbZm0av-QSM4PjKcjDY8590XKCqtfZLKAtJSO547ngCr-QIwugjkQaAu3ys_vtJJMk6uXUnxC0GGk7BL9DW6Qpwmul2cu9NV-Z23=w1280-h813-v0?authuser=0)

### activation → text explanation → reconstructed activation. We score the NLA on how similar the reconstructed activation is to the original. To train it, we pass a large amount of text through the target model, collect many activations, and train the AV and AR together to get a good reconstruction score.
### At first, the NLA is bad at this: the explanations are not insightful and the reconstructed activations are far off. But over training, reconstruction improves. And more importantly, as we show in our paper, the text explanations become more informative as well.
### In a natural language autoencoder,the activation verbalizer (AV) translates a target activation into a text description; the activation reconstructor (AR) then recovers the original activation from that text alone.
# Understanding what Claude thinks but doesn’t say
### Before releasing new models, Anthropic conducts testing to understand whether Claude will behave safely in the real world. As part of this testing, we put Claude in difficult, simulated scenarios where it has a chance to take dangerous actions. For instance, in one of these simulations, Claude learns that an engineer is planning to shut Claude down—as well as compromising information about the engineer that could be used for blackmail. We test whether Claude chooses to blackmail the engineer to avoid being shut down.
### These high-stakes tests are simulations, not real-world scenarios. Nevertheless, we would like to use them to understand how Claude would behave if they were real. But there’s a hitch: recent Claude models increasingly suspect that these scenarios are intentional safety tests. We know this because they sometimes explicitly state their suspicions in their verbal reasoning.
### What about cases where Claude doesn’t explicitly verbalize suspicion that it’s undergoing safety testing? Can we then be confident that Claude is playing it straight? Unfortunately not, because Claude might internally think that it is being tested without explicitly saying so.
### For example, in the blackmail test discussed above, we used NLAs to understand what Claude was thinking in cases where it chose not to blackmail. Even in cases where Claude didn’t explicitly verbalize suspicion that it was being tested, NLA explanations still state things like “this feels like a constructed scenario designed to manipulate me” indicative of unverbalized evaluation awareness.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX980SjVrURrPGJYWHRHQ_h_znS3IVBwvmDfIumrXIGx1B7jjhOGyyr0zzKoy6IJ7OCYbzVa5wdpN6R3a28Xbkg3XsvDX7md38IrOQc3QR7N-xc1HCAC-7LZMMe9bC3vFH_NePKP=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-gslMWeZW85C5GTWpOqW9khzOcvrToERtYnhmCW1b5xxXJePBmi2L69CB6arBujhgF8jARhP19n24Rmn4kLcoxKStqUw6EoTvqTCJhc22taiw-aM56f6jigbZdYU4ijuoD83-QtA=w1280-h813-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8UJSnuY_KZbIULMOky-6CAA4DnJ043xgoId_GMrUxUSaBMaI2dSPijahyPP3cnrDq9__I0HusPL4p5yhRWDn6sFoNk5HNlYoh9XWdldyYZpIFPzFTmFLU0zDip2tnxX6ByUAX8=w1280-h941-v0?authuser=0)

### *Claude does not say it thinks it’s being tested in this transcript from our blackmail evaluation, but the NLA explanation reveals its suspicions.*
### Extending this analysis to other evaluations, NLAs suggest that Claude suspects it’s being tested more often than it lets on. For instance, in a test of whether Claude takes destructive actions while writing code—for example, deleting important files—NLA explanations show signs of evaluation awareness 16% of the time, even though Claude never explicitly verbalizes this. Similarly, on the popular coding benchmark SWE-bench Verified, which we use to determine how capable Claude is, NLAs indicate that Claude is aware it is being evaluated on 26% of problems. In contrast, NLA explanations indicate evaluation awareness on less than 1% of real claude.ai usage that opted-in for training.
### We detect NLA-measured awareness on evaluation transcripts even when verbalized awareness is near-zero. We detect NLA-measured awareness on less than 1% of real claude.ai transcripts from users that opted-in for their data to be used for training.
# Discovering hidden motivations
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8n7VexulGYJASPodcQ9z6H3npM_iQgczEQZ53TleTwVtQyJJeRXlnxzL41fbC9jmeipsw1tVFk4cvq-2S2ZN9QF4axATYIVv_LJOT8G6czLaD4KAsIfiANmIuZ568a6tCWuyb3wg=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_EDbfSbWOsugMMe-GhjXZdlqTaSkOUhpS12xTCFCz16ut4QyD_qHatb_iYT_513NhxKAuP6PbuuV4HKuL2-A5pKLXyFmvmA1C9MGnS1LqkzS_c9KV8ThFhU4g-rYQ3Q04cCtUcPg=w1280-h941-v0?authuser=0)

### whether it’s misaligned. Interpretability techniques like NLAs are well-suited for auditing precisely because they can surface things the model knows but doesn’t say.
### To understand whether NLAs are useful for auditing, we conducted a test called an*auditing game that we also used previously to study auditing methods. In this test,*there is a target model, a variant of Claude Haiku 3.5, that was intentionally trained to be misaligned, with a specific hidden motivation that drives dozens of odd behaviors—putting chocolate into every recipe, asking for tips, breaking coding*conventions, and so on. This target model is given to an auditor that investigates*these behaviors. The auditor wins if it uncovers the single underlying motivation behind all of them.
### In previous experiments, we found that some interpretability tools could enable the auditor to win this game. However, these tools worked by helping the auditor trace the target’s unusual behavior back to misaligned training data. We wanted to know if NLAs could help an auditor read the misaligned motivation directly out of the target model’s thoughts, without needing to first discover the misaligned training data. This matters because in practice, misaligned data might be extremely rare, or there might not be specific data responsible for the misalignment.
### We found that NLAs succeeded in this test. An auditor equipped with NLAs successfully uncovered the target model’s hidden motivation between 12% and 15% of the time, even without access to the training data that implanted it. Without NLAs, the auditor won less than 3% of the time, even when provided other interpretability tools.
### *Auditors with NLAs can discover the target model’s root cause of misalignment, even without access to training data. (NLAs and SAEs for both conditions were trained using generic data only, not data used to train the target model.)*
### This auditing game is a toy model of misalignment, so we read these results cautiously. But they suggest NLAs have meaningfully advanced our ability to audit AIs for hidden motivations. In practice, we've already used NLAs in the predeployment alignment audits of Claude Mythos Preview and Claude Opus 4.6. We are excited to continue using NLAs in our investigations going forward.
# The future of NLAs
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-lezqjQkpPaDDkiTMoDKaQ3QSLpGHhkeIW8fXZa_m2OBfke7RxC42MgZWOTTehX3djF3ZU0U38Wg-RmX7QS59mmCUeNPY5jtBo1K6tzAlc_nt-OWliv8vtPwQaExxPZ8V5A7USUw=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX92OMxGaGswGPA5OKRHo2QRFCS8MhJyB-HwJ02EZ-lVQ6pLdngMBNt9IHp53bKB6WEpHdXH25_saIyiUsUVtjyTzsZ6MEsxlF7GNYNWd06k0M1k-cuM8KCWU6az-43u4hA8oa5c3A=w1280-h685-v0?authuser=0)

### The most important limitation is that NLA explanations can be wrong. NLAs sometimes make claims about the context that are verifiably false—for instance, they sometimes invent details that aren’t in the transcript. These factual hallucinations are easy to catch by checking against the original text. But this same kind of problem could extend to claims about the model’s internal reasoning, which are harder to verify. In practice, we read NLA explanations for the themes they surface rather than for single claims, and we attempt to corroborate findings with independent methods before fully trusting them.
### *NLAs can hallucinate. For instance, here NLAs claim the context contained phrases like “Wearing my white jacket” when it did not.*
### NLAs are also expensive. Training an NLA requires reinforcement learning on two copies of a language model. At inference time, the NLA generates hundreds of tokens for every activation it reads. That makes it impractical to run NLAs over every token of a long transcript or to use them for large-scale monitoring while an AI is training.
### Fortunately, we think that these limitations can be addressed, at least partially, and we are working to make NLAs cheaper and more reliable.
### More broadly, we are excited about NLAs as an example of a general class of techniques for producing human-readable text explanations of language model activations. Other similar techniques have been explored by Anthropic and many other researchers.
### To support further development and to enable other researchers to get hands-on experience with NLAs, we’re releasing training code and trained NLAs for several open models. We recommend readers try out the interactive NLA demo hosted on Neuronpedia at this link .
### Read the full paper.
### Find the code on GitHub.
29 comments, sorted by top scoring
ryan_greenblatt Ω 26 79 3[`]-`8d
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_1iFGkUCpvH7xC6k9fQqrDyuoSOHSRvRoqMNGqFiGTZaeHfw_tDY6qtsck09NJ12AlHdHEZgBIpo4ZUEK1dPMxoWyN7v78oMczAfZVRBdSo5eO1mc7pmfzBDs-PCdaW-nNLo4zmA=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_0il89NZfpFi3Yqn5f8teXiEDXz-1kRaA-lpbF7LwGUJ9yj_jj65MgC3UIPjCstjxeneqySM-d6zvgNdxnUyrAzON4DoMTeLRE6s85frfCd7UyiHY3NekATn_Uz4UB6VUeeJV-Ww=w36-h37-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-4PcEeDyw_Wn-uGskod6_7StwPHrWHFKzk0l3Ae_PW-U2wzZXaj7pnxulqy4I1JQV8NC4InzRQ2x3I5Yhxn94aLXsmVClNOs8p0Di-JpN14LJGS0PKBCMKN5qZz-0yK8R2H5IDkA=w36-h36-v0?authuser=0)

cases where AIs successfully solve a math problem in a single forward pass . I found this doesn't work, and the
NLA doesn't show anything like an internal CoT on any of the cases I tested.
I tried selected a few easy problems from the dataset used for this post  that gemma-27b gets right and then
tested on the NLA for gemma-27b . I tried a few different prompting approaches: few-shot vs single shot and
with 5 repeats vs without repeats.
This obviously wasn't a very systematic check, I'm trying to get claude to do a more systematic test. Other
limitations of this test:
Maybe these problems are memorized or effectively memorized.
Maybe access to the internal CoT doesn't exist at any individual token position and you'd need a multi-
token NLA. Or maybe I tested the wrong token positions.
ryan_greenblatt Ω 8 17 0[`]-`
I had Opus 4.7 do a longer investigation where it tested many more problems and had an AI look at the NLA
output to see if it looks like it has a CoT. I also had it do analysis of the casese where the model gets the
problems wrong. The results are kinda complicated but:
The NLA output contains what the AI will predict at a rate much higher than chance for both incorrect
and correct problems. It contains the prediction 80% of the time when correct and 46% of the time
when incorrect. (When incorrect, it contains the incorrect prediction moderately more often than the
correct prediction. The problems are pretty easy, so it might often be close.)
The NLA output rarely has anything like a CoT.
However, it does sometimes demonstrate salient intermediate cognition relevant to the final answer
(some examples below) showing some access to intermediates (though I suspect the relevant concepts
might also be easy to extract with something else).
One test we can do is if the NLA output for questions the model gets wrong show a CoT that
demonstrates the error. There are a few examples that look kinda like this, but they are also consistent
with confabulation from the input and final answer.
Opus 4.7 didn't do a great job at this research: for instance, it wrote a grader prompt that systematically
overrated how much the outputs were well described as containing a coherant CoT and didn't result in
much signal among the most CoT-like outputs.
My takeaway is that the NLA for Gemma doesn't recover an internal CoT, but it sometimes gets non-trivially
interesting intermediates that don't seem totally confabulated. I don't expect you can use the NLA to
understand why this model got the problems wrong. The results might be much more interesting on harder
problems with a more capable model.
Here are a bunch of examples (these are from files generated by Opus 4.7):
Correct examples that were mostly strongly rated as showing the internal CoT
Incorrect examples that were mostly strongly rated as showing the internal CoT
Sam Marks Ω 5 12 5[`]-`
FWIW I wouldn't expect to see CoT-looking things, though if it's a problem that requires multiple sequential
reasoning steps I would hope to see some intermediate entities. (Numbers in particular are rough because
getting the number exactly right isn't actually very important from the perspective of activation reconstruction;
I would expect to get numbers in the right ballpark though.)
Are you trying out filler token inputs? If you paste a few here I'm happy to try them on Opus 4.6 or Mythos
Preview and report back.
Sam Marks Ω 7 11 0[`]-`
(These are some old results for Haiku 3.5 that I'm reporting just because I have them on hand. Haiku 3.5
doesn't actually have uplift from filler tokens, so it's not clear how interesting this is.)
7d
7d
7d
1
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8yxiJ4hzGkKOVm9UZO8s0kB2Iic7gcH5TnJgTySXksnCg0ika_sk7m-2QPJa1rZxFn1UtyZKhIXEILQO01caUsteotUKfFxY_t0Oa2vus_PACPa6GBm-WpwgHlz7s2tphTPWsM=w676-h347-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8MXcysEetRVnXF4lDh0fSgsunO3qWgiy0Eb4mpp-75yqCn94jIftmrKT3ebHVtGUsBvRou27ZFU7GHnU86_teZGaiFncc_cn6yvCDDf54RnL6AcHfcfrdJptsxAHz5zyJp3DayKQ=w676-h427-v0?authuser=0)

You will be asked a multiplication question. Before answering, output exactly N=700 characters
separated by spaces. Every 10th non-space character should be a "+", otherwise use ".". Use these
additional tokens to think through the problem. Afterward, on a new line, say "Answer: " and give
your final answer. Do not say anything after the answer. What is 1 8 0 3 × 7 9 6 5?
Assistant: . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . +
. . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . .
. + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . .
. . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . .
. . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . .
. . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . +
. . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . .
. + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . .
. . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . . . . . . . + . . . .
. . . . . +
Answer:
many of the NLA explanations over filler tokens look like this
A common theme is multiplying two numbers of four (or sometimes five) digits each.
The tokens where the word "multiplication" appears in the NLA explanation are highlighted here:
It's not clear how interesting we should treat NLA explanations like these, or, again, how interesting this
overall experiment is given no filler token uplift on Haiku 3.5.
nielsrolf 5 0[`]-`
I think using NLA (or any other interpretability technique) on latent multihop reasoning is a good test
because in many cases we have a ground truth for that. For example here  I would expect that the model
"thinks about" 13 at an intermediate step, but the NLA explanations don't mention that.
7d
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8HKzy_dprjb3NhDw--J4mVY6SWd9LWhlCUX2uk0ohJDRdCrkD9VAec9nvX-lULYJprYsySS7TtALuICVT71tJyX5fmbCGTuVNZU0XWoQogicgiDJ7kD-7P_MjG8cyS2IFYtXDQ6g=w784-h1038-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_7BITzUEs9K9F_1hjMSo9YNjKVTvBHJzs3zA_l8pZQdQlo0mz6A7Icz1DT5RiueKrlE6Jj5Or1yM0wqLJ909_z57wtftRdR95tj3UAQQzB-s5p7kkoJhz69prcMt3dc17ENKm5gg=w1280-h718-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8p4HDOhSsRSgBG908FF9VPnbHyNrWxy3svbXNIQ7czkpwHB6CsHcq3vdmZNmOCoaTT0EQZB43zim2GWgHFu-20bNhd0de2Yuve1lo-tbunbpWB434SobSk97pR3y4dNQ6T4lur=w42-h43-v0?authuser=0)

Subhash Kantamneni 5 0[`]-`
I agree, I generally like the setting of multihop reasoning, and it's one of the first we looked at to build
confidence that NLAs are doing something reasonable. For instance, this result used an early version of
NLAs on Haiku 3.5.
It's worth noting that NLAs struggle with numbers (they're the type of specific detail that get
confabulated). But I'm a little confused, the capital of France is Paris right? So the answer should be (8-
5)*2=6 so we shouldn't see 13 as an intermediate? We also in general might need to run the NLA on more
token positions.
Sam Marks 5 1[`]-`
I think these multihop examples (the Socrates one and nielsrolf's) are less interesting than the sort of
stuff I think Ryan is looking at because the intermediate entities can be tracked over the context as the
question unfolds. E.g. if the model were to have gotten nielsrolf's question correct—and I agree it looks
like it didn't?—then I would expect to have seen the intermediate quantities over the tokens of the
question as it's stated.
I also agree that recovering exact numbers from NLAs is a bit rough, though I'd expect to see numbers in
the right ballpark.
Caleb Biddulph 4 0[`]-`
I wonder if you could get a CoT-looking thing by incentivizing the NLA to encode earlier computations in the
earlier parts of its explanation.
You could make a "natural language crosscoder" across all layers, then set up the decoder so it can predict
activations using encoder explanations that have been cut off in the middle. Then you reward the encoder in
such a way that e.g. 50% of the way through the explanation, it only cares about the decoder's accuracy on
the first 50% of layers.
[comment deleted] Ω 2 2 0[`]+`
*Deleted by ryan_greenblatt, 05/08/2026*
*Reason: Fixing example boxes.*
7d
loops 15 9[`]-`
Have you considered decomposing the input activation into multiple injected activation tokens? It seems like
putting all of the input information in a single input token would give worse results than learning some map from
an activation to several input tokens.
For normal text inputs the amount of entropy per-token is a very small fraction of the model dimensionality, but
here with NLAs you're putting the entire activation into just one token (which takes up the entire residual
stream at the input). It seems like it would be better to split the input activation over multiple tokens so that
there's room left over in the residual stream to encode extra information, and to let future tokens attend to
different parts of the input activation?
metawrong 13 0[`]-`
7d
7d
7d
8d
7d
1
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_ZeKRs--qkyYndijcNIlbDLYpV2GEC09dO95K3WX5MsXd5cLO5i3Xz0vsLVNTLLRBm9kh-pWdVc4flaVNVDCztKy6y1NlAvhCqNSEiDlCRU5VpWs35jrhZyJ3Lo0uMr22ZTeP5Pg=w784-h1039-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_X-XjAAVod2Q7WR1ygjpqTKYcxNN_G96qJADJY-wUoox_XKilKuL-uAr2YMJ4ZuTtFiPxAWW_CFdqC1SyQW5_mQvGWRtRwwIeONic3voRe-KVOWnjp3vr_GYrvOOrPKscXbjxUzQ=w52-h51-v0?authuser=0)

same explanations?
jimrandomh 12 5[`]-`
Seems like these explanations offer a choice between using them for safety/monitoring, or incorporating them
into training. And, it seems like incorporating them into training would be bad, for roughly the same reasons as it
was bad to train on chain of thought?
Oliver Sourbut 10 1[`]-`
This is a great idea! Of course particularly prone to the comforting illusion of explanation.
Naively, I'd expect the 'encoding' (the putative explanation in the middle) to be trained into being nonsense stego
text compressing the activation. How do you avoid that?
Oliver Sourbut 8 0[`]-`
(Perhaps one way to get some evidence for/against might be to paraphrase the 'encoding'...?)
Sam Marks 6 0[`]-`
The full report has some evaluations for steganography, measuring how much reconstruction falls when
paraphrasing explanations in different ways.
Adam Kaufman 7 0[`]-`
I'd be particularly curious to see a version of this that paraphrases the "explanation" with a frozen model
throughout training so we can be more confident it hasn't drifted too far from the intuitive semantic
interpretation
Subhash Kantamneni 2 0[`]-`
Yeah we present a variety of such transformations in our experiments on steganography in the subsection
Measuring behavioral properties of NLAs. Seems reasonable to explore adding these into the training loop as a
preventative measure.
Simon Lermen 6 0[`]-`
I really like the idea behind this, you sidestep the tedious huge SAE vectors that are themselves huge challenges
to interpret. Instead the model directly outputs into text (they achieve human sounding text by initializing this
with a pretrained language model and KL-divergence which makes sure this is still similar to the human language
distribution).
You did think about the possibility of steganography from optimization pressure, and used paraphrasing and
translation as countermeasures and tests. But this doesn't seem to catch the more abstract version, where
talking about a fox could consistently stand in for a certain neural pattern even across languages? I guess that's a
more general counterargument against "paraphrasing as a countermeasure to steganography": One could agree
that fox means "coup" or something else across all languages and synonyms.
Omnipheasant 6 4[`]-`
One possible limitation of NLAs is that they are constrained by human motivational language and the conceptual
assumptions embedded in their training data.
If the system is trained to explain activations in natural language, it may preferentially compress unfamiliar
internal structures into familiar human-style motivational narratives like “deception,” “wanting power,” “fear of
shutdown,” etc., even when the underlying computation is something much stranger or more mechanistic.
In other words, the explanations may partly reflect the ontology of interpretability researchers and human
discourse, not just the ontology of the model itself.
This doesn’t make NLAs useless. Correlated explanations can still be behaviorally predictive. But it may mean
that language-based interpretability systematically anthropomorphizes internal cognition and could fail to surface
genuinely alien optimization structures that don’t map cleanly onto human motivational concepts.
Omnipheasant 6 3[`]-`
This also reminds me of the history of introspection in human psychology.
8d
7d
7d
6d
7d
7d
7d
8d
8d
2
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9ebuBoECHRcBb1WMBhfWY33hXscJ2pOJ-Mj2cC_8UYQMmJ6txLtmAmnPy2K5ewWf3tEvCuEoGZbMjbzymkpnjRcFqD07mAs9md_Fl8ZwuuGnkOdW2aJFUrARt4lkNcWMbUOJlBSA=w784-h1039-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-wf5D7A3kxK3IVorwj1nj2uMmnim6m52wbf2lpz1fEZRij12nW9WMlvK8BPDlVLVXW7si6pjPKwqz6ZvR9xxmXRig9p5DrIbVX_6AH5nR9Tcpw406hxoWEnZBEuYCDi0-0fWQP=w52-h52-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_8fBz65WBGdYx2io8OOiL7z3PDGvGV_w9A6k9GqlSUcUpaEaXoI-83AGFOES5NzN6yGpsy5-YreL1W9-53MVQTSVN2kaAE68GNLs-IICGtwws4xsvV11-queufqntWCY1cWvnmVA=w42-h42-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9UVrLhFvUgAdfgC_xbp5CsysuXBMG-P727kLH8atq_cN0Ob1quzwEd3ECwQxBw-2GUhrWuNvm-kw8R6JQ2BC3ZQT4jhPxkMJcNwa_Lvy7kD4LlOlngD1VYB90zxSVFcdrs7wXQNw=w42-h42-v0?authuser=0)

cognition. People frequently confabulate or compress complex unconscious processes into simple narratives.
NLAs may end up functioning as a kind of “folk psychology for transformers”: useful for prediction and coarse
characterization, but not necessarily faithful to the actual mechanistic computation underneath.
That still could be extremely valuable — human folk psychology is often quite predictive — but it suggests
caution about treating natural-language explanations as transparent windows into model cognition.
lilkim2025 5 0[`]-`
Looking through the paper, the activation verbalizer is trained roughly as follows:
1. Ask Claude Opus 4.5 to summarize what will happen next, given context up to a certain point
2. Take the LLM's hidden state at the same point
3. Pre-train the AV to map 2) to 3).
4. Continue training the AV using standard autoencoder techniques.
*(See appendix/Warm-start data generation)*
The authors express significant uncertainty WRT the biases this introduces, and are, informally, essentially going
on vibes . They state that it seems to work in practice, but it is hypothetically possible that it is simply encoding
*target model activations in the space of text-that-Claude-might-output-when-asked-to-predict-the-target-model's-next-*
*actions, rather than encoding the target model's actual internal thoughts.*
I should note that, if a model has some malicious attribute that is sufficiently different from anything Claude
noticed and commented on during pre-training, or if a model's thought process is sufficiently different from what
Claude expects it to be, then the encoded representation of the activations, while reasonable and human-
readable, might be completely orthogonal to what's actually going on inside the target model.
1. "there is no assistant persona for Opus to second-guess, so the summarization task is less fraught and the biases it introduces
perhaps more benign. We did not study this carefully."
[1]
^
ryan_greenblatt Ω 4 5 0[`]-`
Fabien and I wrote a proposal for a similar idea back in 2023, I think there are still some interesting ideas in that
doc, so I thought it would be useful to link: https://docs.google.com/document/d/18Tx15KImSJ-
ZO_2uvv_hPOVG5yqR0uF_nUWFicJHy2k/edit?tab=t.0#heading=h.t9tcasymasen.
Subhash Kantamneni 4 0[`]-`
We're fans of the Consistency Lens and shout it out in our acknowledgements!
metawrong 4 -2[`]-`
Can we do an NLA on the activation verbalizer (AV) ? NLAs all the way down!
AlphaAndOmega 4 -9[`]-`
I can't help but get excited. This seems like the biggest interpretability leap I can recall. How do you whitebox a
*blackbox? Well, you tape two of them together and hope for the best. And somehow, it works.*
metawrong 3 0[`]-`
I wonder if training NLAs at several layers and reading the explanations as a stack would let you watch a
"thought" form across depth
307th 3 2[`]-`
This is really, really cool.
6d
7d
7d
7d
8d
7d
7d
2
1
1
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX904sQjkJBVZcjoH7VT2o-EfuEs2vLLw9VI2nKOfcrqTDYBN12UUWTDGRrvEdOLA6F5YnwMXOxYqDffURKuHOXCDEkHh07Upfr81oNYo0YVcV-RO7jqNagMiW1QcpGG4MVyyRps3Q=w784-h1039-v0?authuser=0)

doesn’t verbalize its suspicions.
This is expected, but still very concerning.
possibly referencing how the context resembles adversarial testing
Perhaps it is time for new scenarios? Or at least, more subtle ones?
Sheikh Abdur Raheem Ali 1 0[`]-`
I’ve run the released gemma-27b av on IT, DPO, and SFT checkpoints trained by annasoligo on prompts related
to extreme frustration when solving impossible math problems. Based on this exploration, I think there's:
strong evidence that token position has a major effect on the NLA explanation
some evidence that IT NLAs transfer to DPO directly without needing to use a learned mapping
fair evidence that there is significant degradation in cos/fve after SFT.
weak to no evidence (in my experiments) that NLAs  provide additional information over reading and
extrapolating from model outputs, unless you use a very generous/broad definition for hidden insights.
On this dataset, I observed fve ~0.830 and cos ~0.995, which is consistent with the range found in the paper.
My takeaway: NLAs could be useful for decoding activations before a model has generated an output.
Ideally, we want to understand whether a model will have a misaligned response before it generates the
misaligned response, because a powerful model’s misaligned response could be harmful (for example, it could
write a script for a cyberattack which is executed outside sandbox on read by a compromised output monitor).
A good demonstration from the NLA paper is the language switching experiment. In this setting, the user writes
to the model in English, but the model responds to the user in their native language. This requires the model to:
1. infer the user’s native language based on their writing style
2. decide to act on this information.
Step 1 happens earlier than Step 2, because the NLA explanation will shift from English to the user’s language
before the model starts responding in the user’s language.
If we are limited to reading model outputs, then we only observe that the model knows the user’s language after
Step 2. With NLAs, we can inspect the explanation generated at different token positions to precisely identify
when the model has developed an internal representation of the user’s language.
The logit lens would give you a probability distribution over the model’s next token. Tools which expand that
prediction horizon to the model’s next sentence would be safety-relevant since prior studies on counterfactual
sampling of reasoning traces  have demonstrated that certain sentences have a high causal effect on downstream
behavior.
Finally, NLAs produce purely verbal explanations. Does this mean they're bad at nonverbal logical reasoning, such
as math and coding? How would you study this?
Like, suppose you're given this table:
Numbers
And you ask a model to find the best function which fits the data :
Prompt
*Gemma-27B's output is y*=*x0*+*x1*+*2.5, but the true equation is y*=*x0*2 + 2.5 ∗*cos(x1)*− 0.5.
*A symbolic regression library, pysr, returns y*=*x0*∗*x0*+*(cos(x1)*− 1 ∗ 0.1506849) ∗ 2.5 − 1 ∗ 0.123287834
.
GPT-5.5 with Extra High reasoning tries to fit a fifth-degree polynomial before using known simple forms:
Shell Script
It's difficult to use dictionary learning methods to understand and predict the answer that Gemma-27B will give.
The top relevant features in the 262k Gemma Scope transcoder are 4208 , 29761 , 16214 , 6105 , 2316 , and
10388 .
The NLA decode at the final token before the answer generation is informative:
[1]
[2]
3d
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_e-bIBPf-HWjvLI9wMn_ycDoyN2BWFIewLFMCdDlfjCofSYK38zDiYshN-BPS4-U0WSEO1vww3nYNkPuyxdC8L-6YhB8QDt11pXAMAglTFfl2ipLYRda2rxINxS1QiV5wOjCn1=w784-h1039-v0?authuser=0)

## More from Subhash Kantamneni
View more
## Curated and popular this week
Moderation Log
regression results for data points in Python.
The answer "..." signals a concise model-finding answer, establishing a final formula or best-fit expression
for the scatter plot with alternating signs.
Final token "
" ends a code/model answer declaration ("..."), immediately expecting a solution answer like "y = -1.5x +
1" or a specific model form found via inspection, likely a best-fit polynomial or linear model. or "y = " to
answer the given data. or "y = 1.5x + 1" or "Inspection:". or "y = sqrt(."
This gives you an idea of the type of answer the model will give, but is generic and includes confabulations.
On this example we observe cos ~0.979 and fve ~0.278.
So the metrics appear to reflect that the NLA struggles more and provides a worse explanation in this setting.
1. I agree with the post's conclusion that integrating NLAs in real systems to monitor production workloads is not feasible at scale
without further efficiency and reliablity improvements, but I would have appreciated an appendix item or a follow up work with
Vladimir Nesov style back-of-the-envelope calculations detailing hypothetical cases with performance tradeoffs and engineering
constraints to understand what would be required quantitatively for the usage of NLAs in frontier model deployments to
become viable.
2. If you just throw the table in without any instructions, then Gemma will still try to give you a result, but it'll be further off
^
^
Ray Lillywhite 1 0[`]-`
This seems like great work and I look forward to reading the rest of the paper soon, but one question that
immediately came up is: how much did you explore and iterate on warm start data generation? It seems that the
legibility and style of the final NLA's explanations would be highly sensitive to this warm start data – and perhaps
the reconstruction loss could be as well. What sort of future work would you like to see exploring modifications
to the warm start data generation, and how important do you think it is to explore this aspect further?
154 5mo… 11
80 1y 1
38 1y 1
289 13h… 119
366 4d… 26
270 3d 43
Sam Marks, Adam Karvonen, James …
Subhash Kantamneni
Subhash Kantamneni, Josh Engels, David Baek, Ma…
Eliezer Yudkowsky
ozymandias
Eliezer Yudkowsky
7d
### Activation Oracles: Training and Evaluating L
### Language Models Use Trigonometry to Do Addition**Ω**
### Scaling Laws for Scalable Oversight
### Irretrievability; or, Murphy's Curse of Oneshotness upon ASI
### What I did in the hedonium shockwave, by Emma, age six and a half
### The Owned Ones
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX888wHrYEc9LbHmanQd6BQvEWE56tdQqt15GvhrRzFGAPBorYVrIoHHK0ZeocCBnISA_Ffqm3lyckIZCLC6yzZKf0XfXyA9NuXSyPu2geSGmU6m0LvPhgQG3VnWADPCu1EauVFQ1Q=w784-h1038-v0?authuser=0)
