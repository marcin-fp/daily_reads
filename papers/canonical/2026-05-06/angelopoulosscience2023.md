
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_yMAHHAYkRJJTZoVep9id7GLkyg-gC4-4wj9llSkG8kywdlMfmRhupMFoRSMq5mk2hjqMWd7S1ppSYhWXvrOsNW9fF0kQa_jXlSRWu3rZ1D_UGNv3FavpqC-TJne_hIJ7BPJy8aA=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-08uPG3KvDvONHbtPtOWvrkLGSlT0NnQXrfGSKiLOHcFcggiZ87ZVneuazL7jlSJUlCrP9T-uBxJBbAU_FUTgQI3VN6uKZl6yzhktg1KFgi4f1JdEp8pkYdJeXRmNzSNNXqDc8pQ=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-10JSxD1HP52r0_L-Q-ZSDHjuGvA0TXW1LVFgHpYy5wXW0g0QAcvpxxqt2qsGGRfIgn3ns4kf2Iccc848_8RUwq6CPhyWfJSQjFaTlNxAAaU9sGK_0HxGHAqe5dbYzYudqjmQJtg=w1280-h32-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_ZjJpk-IXoPlW45y8NU7W3JBZf_eRUuGHSex7lrXA5LW9RNaF9Cxfs5pLXcbX3-7IT-_kksOfdDv_Ejl4kwTb8aatIODOdACC8f4Dq6D84hSAps1enotuSvMkr86_6bHe9vioYBQ=w1280-h96-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_PPRqqn2g_FRwdb8sk-6jOK9d9TXYy7bVUW4jVBmgkK8i1e-yQfIe6I7Lx_hMIFSN5I0AJvJJ-jgsz7LmdmA_vu_Hnxm_88b9hz2zE35cj9rK4jbxYzAY-BgDtUrotedFvHSghNg=w1003-h1004-v0?authuser=0)

MACHINE LEARNING
### Prediction-powered inference
Anastasios N. Angelopoulos*†, Stephen Bates*†, Clara Fannjiang*†, Michael I. Jordan*†, Tijana Zrnic*†
Prediction-powered inference is a framework for performing valid statistical inference when an experimental dataset is supplemented with predictions from a machine-learning system. The framework yields simple algorithms for computing provably valid confidence intervals for quantities such as means, quantiles, and linear and logistic regression coefficients without making any assumptions about the machine-learning algorithm that supplies the predictions. Furthermore, more accurate predictions translate to smaller confidence intervals. Prediction-powered inference could enable researchers to draw valid and more data-efficient conclusions using machine learning. The benefits of prediction-powered inference were demonstrated with datasets from proteomics, astronomy, genomics, remote sensing, census analysis, and ecology.
# I
magine a scientist has a machine-learning system that can supply accurate predictions about a phenomenon farmore cheaply than any gold-standard experimental technique. The scientist may wish to use these
predictions as evidence in drawing scientific conclusions. For example, accurate predictions of three-dimensional structures have beenmade for a vast catalog of known protein sequences (1, 2) and are now being used in proteomics studies (3, 4). Such machine-learning systems are increasingly common in modern scientific inquiry, in domains ranging from cancer prognosis to microclimate modeling. Predictions are not perfect, however, and this may lead to incorrect conclusions. Moreover, as predictions beget other predictions, the cumulative effect can amplify the imperfections. How can modern science leverage machine-learning predictions in a statistically principled way? One way to use predictions is to follow the
imputationapproach: Proceed as if they are goldstandard measurements. Although this lets the scientist draw conclusions cheaply and quickly owing to the high-throughput nature of the machine-learning system, the conclusionsmaybe invalid because the predictionsmay have biases. Another possibility is to apply the classical
approach: Ignore the machine-learning predictions and only use the available gold-standard measurements, which are typically far less abundant than predictions. The resulting discoveries will be statistically valid, but the smaller amount of data will limit the scope of possible discoveries. This manuscript presents prediction-powered
inference, a framework that achieves the best of both worlds: extracting information from the predictions of a high-throughputmachine-learning system and guaranteeing statistical
validity of the resulting conclusions. Prediction-powered inference provides a protocol for combining predictions, which are abundant but not always trustworthy, with gold-standard data, which are trusted but scarce, to compute confidence intervals and P values. The resulting confidence intervals and P values are statistically valid, as in the classical approach, but also leverage the information contained in the predictions, as in the imputation approach, to make the confidence intervals smaller and the P values more powerful. Prediction-powered inference applies to any
machine-learning system; as such, it absolves the need for case-by-case analyses dependent on the machine-learning algorithm on hand. The proposed protocol thereby could enable researchers to report on and assess the evidence for their conclusions in a fully standardized way.
Protocol for prediction-powered inference
The protocol for prediction-powered inference proceeds as follows. The scientist wishes to construct a confidence interval for a quantity q, such as the mean outcome or a regression coefficient quantifying the statistical association between the outcome and a feature. Toward this goal, they have access to a small gold-standard dataset of features paired with outcomes, X ;Yð Þ ¼ X1;Y1ð Þ;…; Xn;Ynð Þð Þ, as well as the features of a large unlabeled dataset, X ′;Y ′ð Þ ¼ X1′;Y1′
  ;…; XN′ ;YN′
   , where
the true outcomesY 0 1 ;…;Y
0 N are not observed.
Typically, N is much larger than n . Both datasets are sampled at random from a larger population. Further, for both datasets the scientist has predictions of the outcomes made by a machine-learning algorithm based on the features, denoted Ŷ1 ;…; Ŷn
  and Ŷ1′;…; ŶN′
  ,
respectively. The following exposition focuses on confidence intervals; however, by the standard duality between confidence intervals and P values, the presented tools immediately carry over to valid P-value constructions and hypothesis tests; see supplementary materials (SM) for details.
Prediction-powered inference uses the goldstandard dataset to quantify and correct for the errors made by the machine-learning algorithm on the unlabeled dataset, thereby enabling researchers to reliably incorporate predictions when constructing confidence intervals. The three-step protocol is outlined below and visualized in Fig. 1. 1) Estimand. The first step is to select an
estimand q. The estimand is the quantity the scientist is interested in knowing—for example, the mean outcome E Yi½ , median outcome median Yið Þ, a linear regression coefficient obtained by regressing Y onto X , etc. 2) Measure of fit and rectifier. The key step
is to identify the right measure of fit mq and rectifierDq for the selected estimand. For every candidate value of the estimandq, themeasure of fitmq is computed on the unlabeled dataset imputed with predictions, ðX ′; Ŷ ′Þ and quantifies how likelyq is to be equal toqon the basis of the imputed data. The closer mq is to zero, the more plausible it is for q to be equal to q. The rectifier Dq is a notion of prediction er-
ror that is relevant for the estimand of interest. It is defined as the difference of themeasure of fit mq computed on the labeled data, X ;Yð Þ, and the labeled data when the true outcomes are replaced with predicted ones, X ; Ŷ
  . If
the predictions are perfect, the rectifier is equal to zero. Table 1 states the appropriate measure of fit
and rectifier for common estimands of interest: the mean outcome, median outcome, q-quantile of the outcome, and linear and logistic regression coefficients when regressing Y onto X . A general recipe for deriving the right measure of fit and corresponding rectifier for a broad class of other estimands is provided in the SM. 3) Prediction-powered confidence inter-
val. Finally, the measure of fit and rectifier are carefully combined to form a predictionpowered confidence interval for q. This process is called rectifying the confidence interval. The prediction-powered confidence interval is constructed asCPP ¼ q such that mq þ Dqj j≤f wq að Þg and is guaranteed to contain the estimand with probability at least 1 a . Here, wq að Þ is a constant that depends on the confidence level; it is explicitly stated in Theorem S1 in the SM.
Properties of prediction-powered inference
We proved mathematically that predictionpowered inference yields a confidence interval that contains the true value of the estimand at the desired confidence level, such as 95%. Notably, this validity is guaranteed for any machine-learning algorithm and any underlying data distribution. Similarly, the corresponding P values are also valid for any machinelearning algorithm and data distribution. See SM for the details of the mathematical proof
Department of Electrical Engineering and Computer Sciences, University of California, Berkeley, Berkeley, CA 94720, USA. *Corresponding author. Email: angelopoulos@berkeley.edu (A.N.A); stephenbates@berkeley.edu (S.B.); clarafy@berkeley.edu (C.F.); michael_jordan@berkeley.edu (M.I.J.); tijana.zrnic@berkeley.edu (T.Z.) †These authors contributed equally to this work.
D ow
nloaded from  https://w
w w
.science.org at U niversity of B
ritish C olum
bia on A ugust 12, 2024
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-V7EmTA8tTe-ji6QvoxJoXSPZiI3-R7QR0j0xGzRH1HMA6IudgAF6nfTtr3hkPzRcSBFk3iw-CipZFXOJaMX1KeI_kaA6aUNWzUWhtDAGhwY49OtyuGFZcArDpUVZnM8IrkGgZGw=w483-h938-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9AZ3-IMvFDZLoNnd2a33POJ8r3vYaE_pSVRn4BzHVmFX4szAYV7abTrwaegstI_AUoSvnL-6O_kjPi6lFKdaYC0lDE229n-XqWVttIk5CoVTbpdDuU7o14_ULmz2KsRcgTTYvU7Q=w231-h76-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_cv-Bj0DRwLOBrE6HJedGpoOHHu19bNCwv_4RhR9PyWLmNgWlcDHXJTYCMCCQgbaTSIKUs4M1r0Lofv61YtKTgFQgbtnA7mW2F0FedIUPg6hrQQYtRyhJtFbSsa5L6isPkTe2dsg=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_3WAYDjTNrzViO-m9732T6eiExGZx7a5WYkZZd7t09V3Fj-f3_Ia72v0d3aIH84-oXDS0c-DLbn9Nz3XfjXrVe9RsQPeWBsqgK-_nQVRvvHCISdEfyAGmL0_tthFsFDbD3nfSfww=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8ugeg8dZzMXvbOSeOgcuK-kj04-Ob0r-M6clyaZuc3NTsoBGY3vLtQXdJtT_hYRL8uWm0TxZfWQuQyGVXvIzlTzNFvBR4JEMZMZ-2yAtzYL2Q9Fwrson3_2jKwUgj57y_QFeHD=w393-h82-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX94MwAvOZC88fg54uHqGT5EK_Or-aeNj7sAF4d2Mg313NcI6lN03r5u7vzH5732JvUGJqEXhyD5XD_wk0epfDrHgPHFWbIJJg480wckWCAndfbYQztE5u-34bAA8a2WvX6ITRM_Rw=w170-h517-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_fdh1AlF5OP-fj4xf_QMqVfpbcp-sjdIhx92sb0oAmL96VdocOaCSMnnjcljefKVjLFnywNjcRcwGnrDZf4W31zO6cKn46IGma4v8GP0hy1gewOfb7AakgtgcaYa9gTsVdB3ELAA=w263-h172-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-cg3q6OLEHIq77nB0Dq7huKrB_xhcbidZQRKigfIINIsTghWtdO2P34vEq2Dt26fdcVkuZx5rbVQfYHe65YObl75C0kJMZhbNPgFrRjUVGQz1FmkL097CyRqORMHon_XfinRYN=w170-h170-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-nUlaCLYqqJhMPHQnkXpTzJ1Myna9tlQwHRTL9ni-i7dFhiwa5fFuMr05wv-NocpOfqg5NZrVdcXXhXOcOY8IkSqengFkFpohYkhV-D8LsiqR7jYnGE5BKtBid4jD9W99Zh6S5oA=w170-h195-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-StPJhYb1ZTVmtROBs4-GfDfLrlaW8FIkDSonWG1K4wQ5WqNvPxAzOtcbw2rJJ0-e-yKgkJJDLO2nk-DwOQ94poBLhfhy-nhfttFPmA3VUT6ifgq1MSNbY89QbO81QCejSEL6hrg=w101-h188-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9mcp_3dKi5yB5hEx3l_OMuxp2Lm9otZX-Bo8fNhErI2BGov5vtqBppMDKPokP90XnwZjJtRM1YmsM51uZExMVfc15eUozMlLbhtkB7MagNzhEnoNWbOTIQ_lZOm0TVRvHXNY59Qw=w121-h517-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_UuidHurnuygQqgGulGSMjdvTSLFFX0mflLNB2G866WoInqdXLRjkaSSzd0HgDoDkuuZAmDBl6eUpg_bd1ktVxjVfwtlENugNbpO62Qf8xX-kJqr29tof1_OJhC6K9DACy3WVXMQ=w101-h45-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8xVV5aXJlt-d38kegGxo3kyTV8urXeoeZITaNTNV_zurzjlHAka2c0jE5xS6JcVBlAkmdCqLbs5BRM2Jcq_8dFu49Fksunfd6qHvPn2ci1bNg1uvhv1O0BTyfBzAeWOda2IEu4ng=w101-h45-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9bgxUkiIv9yd15QUBaLeMis7hfofGmdenC3DZCZFR8kbblOynJagOcFw2flC4JpbSEO--qAXMun3YvhW4iH7XH2vRHtQy__oBq8p6MguB1ecUHj-qwS6hQ9D_uHmWU3fas6lwg5Q=w78-h105-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9vY6Cw3qrWenG9tJhn44ZuCYUZ8pq13QSij91sRBFyTI1SDcEVQJWku2EeVDrvwaWqkMQlFDzRKyrizRaTTmcKinDgZS05IQr4-5cu8hCFV_gIMp_gpNj0dY4XLWpZ_YV5KcO0=w119-h118-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-FsFlqggE9LZyWQ6xqs962MGix_tjJIbdLAs_eoLC78opOYcF0J4vNa9FTkuQmOMkSXPGVRhIES2D3bFy-QKBfvWQrp8XOiaThDGjn_3kjHBxTcDZtP5s5qoLbJiJyyOuJepXMBg=w1280-h32-v0?authuser=0)

of validity. A researcher relying on a deep neural network for predictions can therefore draw reliable conclusions, even though its predictions will inevitably be imperfect. Further-more, prediction-powered inference enables more informative inferences than the classical approach, in which the researcher does not use machine-learning predictions: The confidence intervals are narrower, and the P values are more powerful. This is intuitive; predictionpowered inference carefully extracts information from the imputed data and thus has access to a larger sample size.
General applicability
Beyond quantities such asmeans, quantiles, and regression coefficients, the principle of predictionpowered inference can be used for constructing valid confidence intervals for any estimand that can be expressed as theminimizer of a convex objective function. Thismaster protocol,which generalizes all the special cases instantiated in Table 1, is the core technical contribution of this work. We explained prediction-powered inference in greater generality and proved its validity in this general case in the SM. Because many important quantities can be expressed in terms of a convex-optimization problem, predictionpowered inference thus addresses many data-
analysis goals beyond those explicitly demonstrated in this article.
Inference under distribution shift
Prediction-powered inference is also applicable to settings with distribution shift, i.e., the more challenging case where the unlabeled data are collected under different conditions than the gold-standard data. Two types of distribution shift are considered: label shift and covariate shift. The protocol retains the same properties as before: It is statistically valid for any machine-learning algorithm and boosts statistical power by making use of machinelearning predictions. For covariate shift—the setting where only
the feature distribution changes between the labeled and the unlabeled data—predictionpowered inference handles all estimation problems handled by the master protocol. This is done by appropriately reweighting the data; see Corollary S13 in the SM for details. For label shift—the setting where only the
label proportions change between the labeled and the unlabeled data—prediction-powered inference can be applied to estimands of the form q ¼ E n Yi′
   , for a fixed function n. For
example, choosing n yð Þ ¼ 1 y ¼ kf g asks for inference on the proportion of instances that
belong to class k. See Theorem S3 in the SM for a full description of the method.
Application of prediction-powered inference to real datasets
Wedemonstrated prediction-powered inference on several real tasks. In each, we computed a prediction-powered confidence interval for an estimand and compared it to intervals obtained through the classical approach and the imputation approach. In all cases, the imputation approach, which usesmachine-learning predictions without accounting for prediction errors, did not contain the true value of the estimand. The widths of the two valid approaches, predictionpowered and classical, were compared as a function of the amount of labeled data used. In addition, we compared the number of labeled examples needed to reject a null hypothesis at level 1 a ¼ 95% with high probability. See (5) for a Python package implementing predictionpowered inference, which contains code for reproducing the experiments, and (6) for the data used in the experiments.
Relating protein structure and posttranslational modifications
The goal was to characterize whether various types of posttranslational modifications
Fig. 1. Protocol for prediction-powered inference. The protocol is illustrated graphically as a block diagram. The inputs are the gold-standard dataset, the unlabeled dataset, and the machine-learning (ML) algorithm. The top block contains an analysis on gold-standard data, in which the rectifier, a measure of the prediction errors, is estimated using the labeled dataset. The bottom block
contains an analysis on unlabeled data, wherein the quantity of interest is estimated using predictions. These analyses combine to form the predictionpowered confidence interval. For concrete examples of the rectifier and measure of fit, see Table 1. For a detailed theoretical exposition and more general definitions of these quantities, see SM.
D ow
nloaded from  https://w
w w
.science.org at U niversity of B
ritish C olum
bia on A ugust 12, 2024
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8oqktJUCyW70KuLWK7GhBHWtLeBbPb6K3KC_8A8EQueEEo5YZe-to09adDB7bWK5kOP_guyQzlJLxzVXmoYuuPPYG5hyKYTOnOtl9N3RF2D-WetV8ENpg4EsGU3FfL1RQVaXAutw=w734-h938-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9qppY5cvcoq1_pHM2ug98-KZOMY9UmM1YKTgZrwHh8AbX6nCfHsIAfcLcyuYuRQDb3Vfk78gOaDAeSX_c7XfwqqzLP213Sc8tCYlHK5Rfcumqk2hdsMa0BpM-wLoBMRUD7k4D-8Q=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_dhGk-5lfsqJQCkVJjQfXoaVLvHumO5_pF3Bdf-ne1cBzHM63BlJiw2iKFIKVpnlKS69JM_CWXGA7B9DlSxNnbC3e19hxI2YgprPdwc7aRVOu2s5-JtKZjeMnAuyE0AKhz6BcQBg=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-QwWpmC_ozDQfcgdQRymxIhLjO5aersRcECtdS9ltUb1QIBvkWWRr-dfWaGDnofeHlB6teMXz0R-IrcF-_m5C_qpfjABKgm0q9R5IkC1AfTrdvOUvrV_G9n0fW13mALNEFRNSe=w1280-h32-v0?authuser=0)

(PTMs) occurred more frequently in intrinsically disordered regions (IDRs) of proteins (7). Recently, Bludau et al. (3) studied this relationship on an unprecedented proteomewide scale by using structures predicted by AlphaFold (1) to predict IDRs, in contrast to previous work, which was limited to far fewer experimentally derived structures. To quantify the association between PTMs
and IDRs, the authors applied the imputation approach: They computed the odds ratio between AlphaFold-based IDR predictions and PTMs on a dataset of hundreds of thousands of protein sequence residues (8). Using pre-diction-powered inference, we could combine AlphaFold-based predictions together with gold-standard IDR labels to give a confidence interval for the true odds ratio that is statistically valid, in contrast with the interval constructed with the imputation approach, and smaller than the interval constructed using the classical approach. We used the fact that the odds ratio could be written in terms of two means and applied the recipe from the first row of Table 1; see SM for details. We had 10,803 data points fromBludau et al.
(3). For each of 100 trials, we randomly sampled n points to serve as the labeled dataset and treated the remaining N ¼ 10; 803 n points as the unlabeled dataset for which we did not observe the IDR labels. For all values of n and all three different types of PTMs that we examined, the prediction-powered confidence intervals were smaller than classical intervals; see row A in Fig. 2. Often, the classical intervals were large enough that they contained the odds ratio value of one, which means the direction of the association could not be determined from the confidence interval. However, the imputed confidence interval
was far too small and significantly overestimated the true odds ratio. To reject the null hypothesis that the odds ratio is no greater than one, prediction-powered inference requiredn ¼ 316 labeled observations, and the classical approach required n ¼ 799 labeled observations; see row A in Table 2.
Galaxy classification
The goal was to determine the demographics of galaxies with spiral arms, which are correlated with star formation in the disks of low-redshift galaxies, and therefore, contribute to the understanding of star formation in the Local Universe. A large citizen science initiative called Galaxy Zoo 2 (9) has collected human annotations of roughly 300,000 images of galaxies from the Sloan Digital Sky Survey (10) with the goal of measuring these demographics. We sought to explore the use of machine learning to improve the effective sample size and decrease the requisite number of human-annotated galaxies. We focused on estimating the fraction of
galaxies with spiral arms. We had 1,364,122 labeled galaxy images from Galaxy Zoo 2, from which we simulated labeled and unlabeled datasets as follows. For each of 100 trials, we randomly sampled n points to serve as the labeled dataset and used the remaining N ¼ 1; 364; 122 n points as the unlabeled dataset. We then used the first row of Table 1 to construct prediction-powered intervals. The prediction-powered confidence intervals for the mean were consistently much smaller than the classical intervals and they retained validity, and the imputation strategy failed to cover the ground truth; see Fig. 2, row B. To reject the null hypothesis that the fraction of galaxies with spiral arms is at most 0.2, prediction-
powered inference required n ¼ 189 labeled examples, and classical inference required n ¼ 449 examples; see Table 2, row B.
Distribution of gene expression levels
Next, we constructed prediction-powered confidence intervals on quantiles that characterize how a population of promoter sequences affects gene expression. Recently, Vaishnav et al. (11) trained a state-of-the-art transformer model to predict the expression level of a particular gene induced by a promoter sequence. They used the model’s predictions to study the effects of promoters—for example, by assessing how quantiles of predicted expression levels differ between different populations of promoters. Here we focused on estimating different
quantiles of gene expression levels induced by native yeast promoters. We had 61,150 labeled native yeast promoter sequences from Vaishnav et al. (11), fromwhich we simulated labeled and unlabeled datasets as follows. For each of 100 trials, we randomly sampled n points to serve as the labeled dataset and used the remainingN ¼ 61; 150 n points as the unlabeled dataset. We then used the second and third row of Table 1 to construct prediction-powered intervals for the median, as well as the 25% and 75% quantiles, of the expression levels. The prediction-powered confidence intervals for all three quantiles were much smaller than the classical intervals for all values ofn. See row C in Fig. 2 for the results for the median and fig. S6 for the other two quantiles. We also evaluated the number of labeled examples required by prediction-powered inference and classical inference, respectively, to reject the null hypothesis that the median gene expression level is atmost five. Prediction-powered inference requiredn ¼ 764 examples and classical inference required n ¼ 900 examples; see row C in Table 2.
Estimating deforestation in the Amazon
The goal was to estimate the fraction of the Amazon rainforest lost between 2000 and 2015. Gold-standard deforestation labels for parcels of land are scarce, having been collected in large part through field visits, an expensive process not suited for large areas (12). However, machine-learning predictions of forest cover based on satellite imagery are readily available for the entire Amazon (13). We began with 1596 gold-standard deforestation labels for parcels of land in the Amazon. For each of 100 trials, we randomly sampled n data points to serve as the labeled dataset and used the remaining data points as the unlabeled dataset. We used the first row of Table 1 to construct the prediction-powered intervals. The imputation approach yielded a small confidence interval that failed to cover the true deforestation fraction. The classical
Table 1. Prediction-powered inference for common statistical problems. Given a measure of fit mq and rectifier Dq, prediction-powered inference computes a confidence interval as CPP ¼ q such that mq þ Dqj j ≤ wq að Þf g, where wq að Þ is a constant that depends on the error level a (see Theorem S1 in the SM). Algorithms S1 to S6 are stated in the SM. The last row (“convex minimizer”) refers to a method that generalizes the methods in previous rows.
Estimand Measure of fit mq Rectifier Dq Procedure
Mean outcome q 1 N
XN
i¼1 Ŷi′
1 n
Xn
i¼1 Ŷi  Yi
  Alg. S1
.. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
Median outcome 1 2N
XN
i¼1 sign q‐Ŷi′
  1 n
Xn
i¼1 1 Yi ≤ qf g  1 Ŷi ≤ q
n o  Alg. S2
.. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
q-quantile of outcome qþ 1
N
XN
i¼1 1 Ŷ 0
i ≤ q n o
1 n
Xn
i¼1 1 Yi ≤ qf g  1 Ŷi ≤ q
n o  Alg. S3
.. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
Linear regression q ðX′ÞþŶ ′ XþðŶ  YÞ Alg. S4 .. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
Logistic regression 1 N
XN
i¼1 Xi′
1
1þe q> X
i ′  Ŷi′
 	 1 n
Xn
i¼1 Xi Ŷi  Yi  
Alg. S5 .. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
Convex minimizer
1 N
XN
i¼1 rLq Xi′; Ŷi′
  1 n
Xn
i¼1 rLq Xi; Ŷi
  rLq Xi; Yið Þ
  Alg. S6
.. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
D ow
nloaded from  https://w
w w
.science.org at U niversity of B
ritish C olum
bia on A ugust 12, 2024
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9wbAor8-uCT8NQ_QlCx710_NWa1cC1yvXwAAhXk8KRayQQtJl2qVwJPc2-he0G6fC34CMvohe4o5m56b58tkOFWfSuvwGyjtMe3IRHOPgcdtVB5O8X8hRNzl1ax0uk3Rm3RoaFZQ=w483-h938-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-GCMLrd0x0yvTJC_opqgh-YZ3S1IxtkIjO1HP_HmoYtKt28iCs9hIklrrS7JC1ziOY9Xobv1Jcw8DEFfj7UZX9RS9m1SEFPHxCU4AT3fv7OQ-eovb7iw6rIfSOvVWJxCicY_NHGQ=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8zyyNkaUMInLLPk-pKMlKoMlTelEfjZruKvtEopXZQG9Rv5Kjn0YlFcMtVpwr1V_3GeG5-FU9u5zsUxuNvc98kqoqzR4j5h0OsBRjIvwv-GEzoBWQlJbABR9-9W9cgGL-JkirZuA=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-sZ-kFv21XUgSm-n2Xnfew8MYQVze-9FTLMn1qX5WIXReefGHY5sP06v5rFgi28GtXnf4ZutZsSYHsZLpZLSb8V2mT6bHM47BXBhxnKiuKNYzJacrs9swf6GuIBSS0UtPTA-o8aA=w313-h193-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-ijxnlPyx27hYfrp4eLF0qDYiPlW9Dm6vjYjYcQrO6r7DNeflVhEgwCGVSFWceezpGXJqAD8DRK4WtOv5JHXIIeLoTHECvE7i6aFla5UEAbG8IA9rbkhbAKZfFP2hmdFJt6S0TyQ=w341-h163-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-rYE7eSe5jjz4bEI8ldAfSwgQX8ToZUh5hh7j1UpE8igAP3Cq_pFeGhF4iYjxtZkHfcURzupu2Oew5SWzDItGDVnQcHNqruIaFIM5iGA7nj8R5O4_0CdmllTau030tHk5hchDfTw=w271-h188-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9dR79frYxApE_PInWAqOZlj8zCrtqAwVXjk0c6qMrRwKuPeTSxem7rtoAMM1N4nRgdAOofl2mhyM9KLiy1isf2HiA3iXAdaBYJbf4Ch40IfVXQ9GdhpTTAWefhWEmO3HkSIj8J8w=w106-h216-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_CWUa4zwc9PTEQKkOD6XesZk5z3T58d58kYRXtXK68ebZP-3jcvKFCMPVFUydJqJUSNU7hzhXhUYBGkm3phHRVwg9nragKzp89hkWEB22-oBClBZ6xId_RHI-yHoXqVQvpICON=w106-h216-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX94odKXQsFGqrmytUCNCa-qA4TO1rdP26hzpa86RQzGHLSBTnLkzN2Xrzk1CBCzDJf91u1chKCmjL7Ezo8YvSWxS-68w0aoL-CcnoPGTd5zbeuvu4uSExuZ3ggB6Ar5cuzTDLsd9Q=w106-h60-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8OR9PrT5-RBfpWaiwZJNowXf5j35FP34_xmu3nW7M8hWOxCkwtObUW5JUKgD35UriWtGCU1myueIdG6xh-CfxXELBElDMVMUBlTTJfR2ST_E2v1krSxk7l1y-GigDGroDa4vdrxA=w249-h159-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-jbKkqE6-83ZOe6zvEbav5XMWd_rqG3SmUTD-nhR1aUxgIOHt7Kr63ZN6KWbWiJGoVOGoXbrfOsNLM4_3eQALzi4gUSJp5NLsmwdDEkNCWtn2sCuyFTFWz-Xm21V7AqD1doWxw_A=w365-h199-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-P_OS2qWsJIhFSEEwk4FFevi93ORm7cvD2rf28U-SXfNJhqUNebi41cO371cfxWy2EUB2rsUUYmoX8Enxs3oBJce-IvHME2QB11A0e-kh6Y8LwqDwsMm7gQnhKzS5LeI_9aN3XyQ=w167-h177-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-9nJB1ad4gQpuBvaIyqcHWfyt4NML4cTkzjLkiN2NFti32XUZNU5ELVTeQVjy3DfQtNkWGw9bQlcPZClv8-AdH-sirCENrL9_LN-jHDoju5rsKMzATRw06i57tYZn7lCBxOmrkjA=w138-h158-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9WOxO62BRlaC56BvdDRpghi3ezvEVKbqe0lPJSSsUiXn5IPBVI_FjrSjGcn-WPkZXTWevT09e3zRADc37HTV5orirUeSMbWNAmuKqAUda6k-uEOh3uJVTAcjB1cl8zyctdhQBgTQ=w360-h181-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9_5aQhL7cCnYCBzY1mxbE4yG8VioZm4C3rvEc78MVpCpA6rX3Nir-jGBAVn-rGTCjjL1ugF_MRUYzSx_koeVv1FUzkMegrxwU9j4y76giHg0_By4VlbceEHevKcAuD2FT4UM2hzw=w1280-h32-v0?authuser=0)

approach did cover the truth at the expense of a wider interval and, accordingly, diminished inferential power. The prediction-powered intervals were smaller than the classical intervals and retained validity; see row D in Fig. 2. We also compared the number of gold-standard deforestation labels required by prediction-powered inference and the classical approach to reject the null hypothesis that there is no deforestation. We obtainn ¼ 21 labels for prediction-powered inference and n ¼ 35 labels for the classical approach; see row D in Table 2.
Relationship between income and private health insurance
The goal was to investigate the quantitative effect of income on the procurement of private health insurance using US census data. Con-cretely, we used the Folktables interface (14) to download census data from California in the year 2019 (378,817 individuals). As the labeled dataset with the health insurance indicator, n census entries were randomly sampled. The remaining data were used as the unlabeled dataset. We used a gradient-boosted tree (15) trained on the previous year’s data to predict the health insurance indicator in 2019. We constructed a prediction-powered confidence interval on the logistic regression coefficient using the fifth row of Table 1. Results in row E in Fig. 2 show that prediction-powered inference covered the ground truth, the classical interval was wider, and the imputation strategy failed to cover the ground truth. We also compared the number of gold-standard labels required by prediction-powered inference and the classical approach to reject the null hypothesis that the logistic regression coefficient is no greater than 1:5 105 . We observed a significant sample size reduction with prediction-powered inference, which required n ¼ 5569 labels, whereas classical inference required n ¼ 6653 labels.
Relationship between age and income in a covariate-shifted population
The goal was to investigate the relationship between age and income using US census data. The same dataset was used as in the previous experiment, but the features were age and sex, and the target was yearly income in dollars. Furthermore, a shift in the distribution of the covariates was introduced between the goldstandard and unlabeled datasets by randomly sampling the unlabeled dataset with sampling weights of 0.8 for females and 0.2 for males. We used a gradient-boosted tree (15) trained on the previous year’s raw data to predict the income in 2019. We constructed a predictionpowered confidence interval on the ordinary least squares (OLS) regression coefficient using a covariate-shift robust version of predictionpowered inference, stated in Corollary S13 in the SM. Results in row F in Fig. 2 show that
**A**
**B**
**C**
**D**
**E**
**F**
**G**
Fig. 2. Comparison of prediction-powered inference to the classical and imputation approaches on real tasks. Each row (A to G) is a different application domain. Panel 1 plots confidence intervals computed using the three approaches; for prediction-powered inference and the classical approach, intervals for five randomly chosen splits into labeled and unlabeled data are plotted. The value denoted as “ground truth” is the estimate computed on all nþ N data points (the true labels were available for all data points for the purpose of conducting the experiments). Panel 2 plots the average confidence interval width, as well as the width in five randomly chosen trials, for varying n, for prediction-powered inference and the classical approach; both are statistically valid solutions. The last problem setting (G) does not have a classical counterpart because the data are collected under distribution shift, hence the classical approach is not valid.
D ow
nloaded from  https://w
w w
.science.org at U niversity of B
ritish C olum
bia on A ugust 12, 2024
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8X7w4wNEGXS3t8x7krtTR_XPLi1W568MJmwJmpJaFoFkyT0hCsLIaMceAtTSqWI8k4eqXoGTdSZLf-ycfUF9cNSHLGlZrzKzGKN2WqQUrW4wZRR4_2L7xqFl4BxRWhOMdUHBrlCg=w483-h938-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8LUTKuqBYvMATS7YGUAOUHPknPkJATY2fCbGCia_Bknlbo0HTaMDCSyTee2_Ux9FxntT5SFQoFgmXws2fxTBnwR8-F5xWNz2iOv8HXr49KbzBi2t6wooZr6rVXCZbwJ08VI4VoVA=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8kXf3Qx2mhD0gikQ-GDbmOOLMGaZvSjIUNxLTofyM6qxX96Nmaflcg7rCI95RRjLbGbGeXG7UJT0NL5Nxs5kNZx4HExv2uFkl8y2EpjgU2CHH4qEZiKb0eDynu2hP15KQuHgvY=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX94E6lGA3a3COtctPfbhOS8qUtqRCfMBYCeEZ9V8AMvn9_EEQEEH8T2UkbHsT-y17FFBeEa0J3vHQQtxdA4J6fiNV8h_6N_LePmknRXgk940V0aSV0WMNPgrpwpeaNkKk7evTx0HA=w1280-h32-v0?authuser=0)

prediction-powered inference covered the ground truth, the classical interval was wider, and the imputation strategy failed to cover the ground truth. We also compared the number of gold-standard labels required by predictionpowered inference and the classical approach to reject the null hypothesis that the OLS regression coefficient is no greater than800 .We observed a significant sample size reduction with prediction-powered inference, which requiredn ¼ 177labels, whereas classical inference required n ¼ 282 labels.
Counting plankton
Assessment of the increases in phytoplankton growth during springtime warming is important for the study of global biogeochemical cycling in response to climate change. We counted the number of plankton observed by the Imaging FlowCytobot (16, 17), an automated, submersible flow cytometry system, at Woods Hole Oceanographic Institution in the year 2014. We had access to data from 2013, which were labeled, and we imputed the 2014 data with machine-learning predictions from a state-of-the-art ResNet finetuned on all data up to and including 2012. The features, Xi, are images of organic matter taken by the FlowCytobot and the labels, Yi , are one of {detritus, plankton}, where detritus represents unspecified organic matter. The labeled dataset consisted of 421,238
image–label pairs from 2013, and we received 329,832 labeled images from 2014. We used the data from 2014 as our unlabeled data and confirmed our results against those that were hand-labeled. The years 2013 and 2014 had a distribution shift, primarily caused by the change in the base frequency of plankton observations with respect to detritus. To apply prediction-powered inference to count the number of plankton recorded in 2014, we used the label-shift-robust technique described in Theorem S3 in the SM. The results in row G in Fig. 2 show that predictionpowered inference covered the ground truth and the imputation strategy failed to cover the ground truth.
Related work Thematically, prediction-powered inference is most similar to the work of Wang et al. (18), who introduced a method to correct machinelearning predictions for the purpose of subsequent inference. However, this procedure is not guaranteed to provide coverage in general and requires strong assumptions about the relationship between the prediction model and the true response, whereas predictionpowered inference provides provably valid conclusions under minimal assumptions about the data-generating distribution. There has been an increasing body of work
on estimationwithmany unlabeled data points and few labeleddata points (19–27), focusing on efficiency in semiparametric or high-dimensional regimes. Prediction-powered inference continues in this vein but focuses on the setting where the scientist has access to a good predictive model fit on separate data. This allows tackling a much wider range of estimands (e.g., minimizers of any convex objective) and gives valid inferences without assumptions about the machine-learning model. Second, prediction-powered inference goes beyond random sampling and applies to certain forms of distribution shift. Prediction-powered inference is conceptual-
ly related to conformal prediction (28). Both methodologies leverage a predictive model and a labeled dataset. From this point on, however, the twomethods diverge: Prediction-powered inference has additional unlabeled data and gives a confidence set that contains a population-level quantity such as the mean outcomewith high probability; conformal prediction gives a confidence set for a test instance that contains the true label with high probability. Thus, the goals of prediction-powered inference and conformal prediction differ greatly from the statistical perspective. Fur-thermore, the mathematical tools used in the frameworks are entirely different, and neither method can be applied nontrivially to solve the objective of the other. See SMfor a furtherdiscussionof relatedwork
and the relationship of prediction-powered
inference to existing baselines, as well as for empirical comparisons.
Conclusions
The past decade has witnessed rapid development and deployment of large-scale machinelearning systems across science. This surge is proceeding, however, with little statistical justification to allow these black-box systems to be used to draw scientific conclusions responsibly. Prediction-powered inference is a standardized protocol for constructing provably valid confidence intervals and P values, allowing the scientist to use the power and scale of machine-learning systems. On an array of scientific problems, we demonstrated that prediction-powered inference achieved high statistical power owing to the use of machinelearning predictions and retained statistical validity. One question that remains open is how to
handle more general forms of distribution shift. In practice, distribution shifts are often a result of a joint influence of several different forms of shift, including covariate shift and label shift and possibly others. Understanding how to handle such settings remains an important avenue for future work. A limitation of prediction-powered inference
is that it does not improve upon the classical approach when the predictions are not accurate enough or when the unlabeled dataset is not large enough compared to the gold-standard dataset. These points are demonstrated, both theoretically and empirically, in SM section “CasesWhere Prediction-Powered Inference Is Underpowered.”Nevertheless, given the growing number of settings with excellent predictive models and abundant unlabeled data, there is increasing potential for prediction-powered inference to benefit scientific research.
REFERENCES AND NOTES
1. J. Jumper et al., Nature 596, 583–589 (2021). 2. K. Tunyasuvunakool et al., Nature 596, 590–596 (2021). 3. I. Bludau et al., PLOS Biol. 20, e3001636 (2022). 4. I. Barrio-Hernandez et al., Clustering predicted structures at the
scale of the known protein universe. bioRxiv 2023-03 (2023). 5. A. N. Angelopoulos, S. Bates, C. Fannjiang, M. I. Jordan,
T. Zrnic, ppi-py: A Python package for scientific discovery using machine learning, Zenodo (2023); https://doi.org/10.5281/zenodo.8403931.
6. A. N. Angelopoulos, S. Bates, C. Fannjiang, M. I. Jordan, T. Zrnic, Prediction-Powered Inference: Data Sets, Zenodo (2023); https://doi.org/10.5281/zenodo.8397451.
7. L. M. Iakoucheva et al., Nucleic Acids Res. 32, 1037–1049 (2004).
8. UniProt Consortium, Nucleic Acids Res. 43, D204–D212 (2015). 9. K. W. Willett et al., Mon. Not. R. Astron. Soc. 435, 2835–2860
(2013). 10. D. G. York et al., Astron. J. 120, 1579–1587 (2000). 11. E. D. Vaishnav et al., Nature 603, 455–463 (2022). 12. E. L. Bullock, C. E. Woodcock, C. Souza Jr., P. Olofsson,
Glob. Chang. Biol. 26, 2956–2969 (2020). 13. J. O. Sexton et al., Int. J. Digit. Earth 6, 427–448 (2013). 14. F. Ding, M. Hardt, J. Miller, L. Schmidt, in Advances in Neural
Information Processing Systems 34 (2021), pp. 6478–6490. 15. T. Chen, C. Guestrin, in Proceedings of the 22nd ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining (2016), pp. 785–794.
Table 2. Number of labeled examples needed to make a discovery with prediction-powered inference and classical inference. The rows (A to F) correspond to the application domains from Fig. 2. For each application, a null hypothesis about q is tested at level 95%. For details, see the SM.
Problem Prediction-powered inference Classical inference
A Proteomic analysis with AlphaFold n ¼ 316 n ¼ 799 .. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
B Galaxy classification with computer vision n ¼ 189 n ¼ 449 .. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
C Gene expression analysis with transformers n ¼ 764 n ¼ 900 .. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
D Deforestation analysis with computer vision n ¼ 21 n ¼ 35 .. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
E Health insurance analysis with boosted trees n ¼ 5569 n ¼ 6653 .. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
F Income analysis with boosted trees n ¼ 177 n ¼ 282 .. .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... .. ... ... .. ... ... .. ... ... .. .
D ow
nloaded from  https://w
w w
.science.org at U niversity of B
ritish C olum
bia on A ugust 12, 2024
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-Y6hZC83MyUHOy2zPV_V4GDDIwi1khg5oXgnBPDBGmYGjowMZXdts3IPufai8s0splckzghI3jjmnAdqR6vJJ3G_x2_cdZBOEOQ_GUFz_iZIGqH73CFkpITXD5TI7o5o7YGKlblQ=w483-h938-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8YVbmtjOuDPxE9042QMGOqI-FxPsab9UstiUmTp6qCHQ-AmT_eds3Mfi1iNe9ZJQGH1-RzeIrX0U94WasAuxZ-hUYveS3-ZWgw_p4kZmM7dttttfMZe3HZVRuGk3RcUmaNHfN04Q=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-FlMbnpW8GsaK80YAwINrzfuL7u3og8e9q06-aPS_DG14ihOjRiXw1_gvq8rRmcvzdl--BrGG5_vv7h1BJFL6zVdaetERwaQzHwMLDjf1dUOX7xwsGI5IhdioAehyJOdrhfHwjwA=w32-h1280-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9GWG-ds9IpbehUXFRMXkWoe5QxxKhbebD_ywiNGaZ0o9O-zixIN1GR6Eps1gbRl2sdUoHgUyrA51v0cIT7IdoAl_7qK_QMPuzwBefImyefnTaZInke8esOum1nMNZ3kRjc7Ajueg=w1280-h32-v0?authuser=0)

16. R. J. Olson, A. Shalapyonok, H. M. Sosik, Deep Sea Res. Part I Oceanogr. Res. Pap. 50, 301–315 (2003).
17. E. C. Orenstein, O. Beijbom, E. E. Peacock, H. M. Sosik, WHOI-Plankton- A large scale fine grained visual recognition benchmark dataset for plankton classification. arXiv:1510.00745 [cs.CV] (2015).
18. S. Wang, T. H. McCormick, J. T. Leek, Proc. Natl. Acad. Sci. U.S.A. 117, 30266–30275 (2020).
19. M. S. Pepe, Biometrika 79, 355–365 (1992). 20. J. Lafferty, L. Wasserman, in Advances in Neural Information
Processing Systems 20 (2007), pp. 801–808. 21. A. Zhang, L. D. Brown, T. T. Cai, Ann. Stat. 47, 2538–2566
(2019). 22. A. Chakrabortty, G. Dai, E. Tchetgen Tchetgen, A general
framework for treatment effect estimation in semi-supervised and high dimensional settings. arXiv:2201.00468 [stat.ME] (2022).
23. A. Chakrabortty, T. Cai, Ann. Stat. 46, 1541–1572 (2018).
24. Y. Zhang, J. Bradic, Biometrika 109, 387–403 (2022).
25. S. Deng, Y. Ning, J. Zhao, H. Zhang, Optimal and safe estimation for high-dimensional semi-supervised learning. arXiv:2011.14185 [stat.ME] (2020).
26. D. Azriel et al., J. Am. Stat. Assoc. 117, 2238–2251 (2022). 27. A. Chakrabortty, G. Dai, R. J. Carroll, Semi-supervised quantile
estimation: robust and efficient inference in high dimensional settings. arXiv:2201.10208 [stat.ME] (2022).
28. V. Vovk, A. Gammerman, G. Shafer, Algorithmic Learning in a Random World (Springer, 2005), vol. 5.
ACKNOWLEDGMENTS
We thank A. Kohli for suggesting the term “rectifier,” E. Orenstein for helpful discussions related to the WHO-I Plankton dataset, and S. Wang for help with the remote-sensing experiment. Funding: Office of Naval Research grant N00014-21-1-2840 (M.I.J.); National Science Foundation Graduate Research Fellowship (A.N.A., C.F.). Author contributions: Conceptualization: A.N.A., S.B., C.F., M.I.J., T.Z.; Methodology: A.N.A., S.B., C.F., M.I.J., T.Z.; Formal analysis: A.N.A., S.B., C.F., M.I.J., T.Z.; Funding acquisition: M.I.J.;
Supervision: M.I.J.; Writing – original draft: A.N.A., S.B., C.F., M.I.J., T.Z.; Writing – review and editing: A.N.A., S.B., C.F., M.I.J., T.Z. Competing interests: None declared. Data and materials availability: The data and code are available in the accompanying Python package (5) and data repository (6). All other data needed to evaluate the conclusions in the paper are present in the paper or the Supplementary Materials. License information: Copyright © 2023 the authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original US government works. https://www.sciencemag.org/about/science-licenses-journal-article-reuse
SUPPLEMENTARY MATERIAL
science.org/doi/10.1126/science.adi6000 Supplementary Text Figs. S1 to S6 References (29–56)
Submitted 7 May 2023; accepted 5 October 2023 10.1126/science.adi6000
D ow
nloaded from  https://w
w w
.science.org at U niversity of B
ritish C olum
bia on A ugust 12, 2024
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8RlIH2s6uF33VLgKkVWoqVt9KErnncNCA9JHkvJeI0BX6JWFBhTiKTuUfEuIgglHt6WQGxG3mQYaC7VgWLiPGJErXmGyenzQh42ZOgoPrcYhWHHCg8ffz1NfOLmMunk5-dtRUBbg=w403-h146-v0?authuser=0)

### Supplementary Materials for
**Prediction-powered inference**
*Anastasios N. Angelopoulos et al.*
Corresponding authors: Anastasios N. Angelopoulos, angelopoulos@berkeley.edu; Stephen Bates,
stephenbates@berkeley.edu; Clara Fannjiang, clarafy@berkeley.edu; Michael I. Jordan, michael_jordan@berkeley.edu;
Tijana Zrnic, tijana.zrnic@berkeley.edu
**Science 382, 669 (2023)**
DOI: 10.1126/science.adi6000
**The PDF file includes:**
Supplementary Text
Figs. S1 to S6
References
Comparison to Baseline Procedures The prediction-powered inference procedure was compared to three baseline procedures that also combine labeled and unlabeled data in performing statistical inference. The baselines were:
1. Post-prediction inference. The post-prediction inference procedure of Wang et al. (18) was used for estimating ordinary least-squares (OLS) coefficients. The procedure first fits a regression r to predict Y from Ŷ on the goldstandard dataset. Subsequently, the regression function is used to correct the imputed labels on the unlabeled dataset. Confidence intervals are formed using the r(Ŷ ′) as if they were gold-standard data. This procedure has no theoretical guarantees in general and requires strong distributional assumptions on the relationship between Y and Ŷ to provide coverage. Our experiments indicated that this approach fails to cover in realistic conditions.
2. Semi-supervised mean estimation. The semi-supervised mean estimation procedure of Zhang and Bradic (24) involves cross-fitting a (possibly-regularized) linear model on K distinct folds of the gold-standard dataset. The average of the K model predictions on each unlabeled data point is taken as its corresponding Ŷ ′, and the average bias Ŷ − Y of the K models is also computed and used to debias the resulting mean estimate. The formal validity of this approach applies to mean estimation and requires the cross-fitting of linear models; it does not have formal guarantees for more flexible model classes. For this reason, it provided little improvement over the classical confidence interval in our experiments, since the variance reduction possible with linear models is typically limited.
3. Conformal prediction for mean estimation. A version of conformal prediction (28) was used to construct prediction intervals, which are then ensembled into a mean estimate. The procedure involves using the goldstandard data to construct conformal prediction sets with the residual score function at level α/N for each unlabeled example. The lower- and upper- endpoints of these sets were averaged to produce a confidence interval for the mean. This confidence interval is guaranteed validity for arbitrary models and distributions, unlike the other baseline approaches. However, it is extremely conservative: it output infinite intervals in the experiments. An ablation is performed without a Bonferroni correction (i.e., sets were constructed at level α instead of α/N ), but this remained conservative and did not provide an improvement over the classical intervals.
Experimental Protocol The methods were evaluated on an income prediction task on the same census dataset used for the logistic regression experiments in the main text. In the case of the semi-supervised and conformal baselines, the goal was to estimate the mean income in California in the year 2019 among employed individuals using a small amount of labeled data and a large amount of covariates. In the case of the post-prediction inference baseline, the target of inference was the OLS coefficient between age and income. The setup was the same as the logistic regression experiment described in the main text (including the use of the Folktables (14) interface and the gradient-boosted tree as the predictor).
Comparison to Post-Prediction Inference Results of the post-prediction inference protocol as compared to the classical and prediction-powered approaches are shown in Fig. S1 for the previously-described OLS coefficient between age and income. The procedure did not cover at the proper rate and the intervals were biased.
Comparison to Semi-Supervised Mean Estimation Results of the semi-supervised mean estimation protocol as compared to the classical and prediction-powered approaches are shown in Fig. S2 for the previously described mean income estimation task. The prediction-powered intervals dominated both the semi-supervised intervals and the classical ones in the experiment for all values of n.
Comparison to Conformal Prediction for Mean Estimation Results of the conformal mean estimation protocol, with and without a Bonferroni correction, were compared to the prediction-powered approach for the previously described mean income estimation task. The prediction-powered
1000 1200 OLS coeff
250 500 750 1000 n
0
500
1000
1500
wi dt
h
Figure S1: Comparison to the post-prediction inference procedure. On the left are five independent random draws of intervals with n = 1000. On the right is a line plot of interval width as a function of n, averaged over 100 independent trials. Five draws of interval widths are shown as a scatter plot at their respective n. The post-prediction inference approach is shown in red, the classical approach is in gray, and the prediction-powered approach is in green. The post-prediction inference approach had diminishing coverage in the experiment.
40000 45000 50000
Income
250 500 750 1000
n
10000
20000
30000
w id
th
Figure S2: Comparison to the semi-supervised mean estimation procedure. The plot is the same as in Fig. S1, but with semi-supervised inference shown in red. The semi-supervised intervals had a similar width to the classical ones in this experiment, while the prediction-powered intervals dominated.
intervals dominated the conformal intervals for all values of n. The conformal intervals with Bonferroni correction were infinite in size and thus could not be plotted. Without the Bonferroni correction, though the method is statistically invalid, it remained quite conservative in the experiment, as can be seen by examining Fig. S3.
Cases Where Prediction-Powered Inference is Underpowered Since standard confidence intervals scale with the standard error of the estimator, prediction-powered inference is powerful when a machine-learning model can provide a reduction in the estimator variance. At a high level, this happens when N is large enough relative to n and the model is accurate enough. This was the case in all the experiments shown in the main text. This section precisely quantifies what it means to have an accurate enough model and large enough N . Corroborating the theory, two cases where classical inference outperforms prediction-powered inference are presented: one where the model is not good enough and another where N is too small.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9LE4fTJQ0QlgQ7essuU9w0Oxa37e6HtR2JR-rK_-pKpxHW41L0LYD8Yp6S63UUAVi_BaCVoGfCt7epplgM5pZTcLZ5mY26Az2Hs17ykQXhoFL1SnaVAvV9aWm8CGvjDzoQcxPHdA=w436-h218-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9MXxsYHdKaIYnEv75u9dmwgroc-jxRn7HsWtqFs2ij7CM4DKDFIOX57RAEsLS_uVkoqk5jaeZiDTFKRP0Z35MoHe6oKOc6KvuMyI4j0R5du9BlO0Q_aoTRZpkVzbUqG2ABiO0MLA=w436-h218-v0?authuser=0)

0 50000 100000
Income
500 1000
n
0
50000
100000
150000
w id
th
Figure S3: Comparison to conformal prediction for mean estimation. The plot is the same as in Fig. S1, but with conformal prediction (without a Bonferroni correction) shown in red. The intervals produced by conformal prediction with a Bonferroni correction were infinite and thus could not be plotted. Even the conformal intervals without a Bonferroni correction were wide compared to the prediction-powered intervals.
Mathematical Derivation Consider the case of mean estimation, θ∗ = E[Yi]. The classical estimate of θ∗ is the sample average of the outcomes on the labeled dataset,
θ̂class = 1
n
n∑ i=1
Yi.
Prediction-powered inference, on the other hand, computes the estimate
θ̂PP = 1
N
N∑ i=1
Ŷ ′ i −
1
n
n∑ i=1
(Ŷi − Yi).
Notice that both θ̂class and θ̂PP are unbiased, seeing that E[Ŷ ′ i ] = E[Ŷi].
The widths of the classical confidence interval based on the central limit theorem and the prediction-powered confidence interval based on Theorem S1 scale with Var(θ̂class) and Var(θ̂PP), respectively. The classical estimator has variance equal to
Var(θ̂class) = 1
n Var(Yi).
The variance of the prediction-powered estimator equals
Var(θ̂PP) = 1
N Var(Ŷ ′
i ) + 1
n Var(Ŷi − Yi),
where independence of the two terms in the estimator is applied. Therefore, the prediction-powered confidence interval will be tighter when
1
N Var(Ŷ ′
i ) + 1
n Var(Ŷi − Yi) <
1
n Var(Yi).
Since the predictions Ŷ ′ i will typically have a variance that is of the same order as the variance of Yi, if N ≈ n one
should not expect prediction-powered inference to help. Gains are expected when N ≫ n. In that case, 1 NVar(Ŷ ′
i )≪ 1 nVar(Ŷi − Yi), and thus prediction-powered inference helps when
Var(Ŷi − Yi) < Var(Yi).
In other words, prediction-powered inference gives tighter confidence intervals when the predictions explain away some of the outcome variance.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_OEld1cDGMf4PH0RF0j_svDyB55yM_q6L7AuQQ9F_axHIQoSzAGhEW1wGD8yCyLMBUtIkMjDW61gNrESxWxtB5AgQmkFzKxHbbAF0EbnePv7dc2jn_M1sxLtIQyPAqCV9iqqn9pg=w436-h218-v0?authuser=0)

To gain further intuition, suppose that the outcomes are binary, Yi ∼ Bern(p), where Bern(p) denotes the Bernoulli distribution with parameter p. In this case, θ∗ = p. For simplicity, suppose that P (Ŷi = 0|Yi = 1) = P (Ŷi = 1|Yi = 0) = η. Then, a direct variance calculation gives Var(Ŷi − Yi) = η − η2(1 − 2p)2 and Var(Yi) = p(1 − p). This allows for a direct comparison of the variances in terms of the outcome bias p and model error η. For example, when p = 0.5, the model error η has to be smaller than 25% for prediction-powered inference to help; when p = 0.1, meaning the outcomes themselves have low variance, the model error η has to be smaller than about 9.5%. In general, the lower the variance of the outcome, the lower the model error has to be for prediction-powered inference to be helpful.
Putting everything together, the main takeaway is as follows: prediction-powered inference should only be applied when N is (preferably substantially) larger than n, and when the model has a high enough predictive accuracy to explain away some of the outcome variance. While this derivation focused on mean estimation, a similar intuition holds for other estimation problems.
Inaccurate Machine-Learning Model The deforestation analysis experiment from the main text was repeated. However, instead of a gradient-boosted tree, a linear regression module was used as the machine-learning model. This led to a substantial enough reduction in performance that the classical baseline outperformed the prediction-powered approach. See Fig. S4 for the results. Due to the reduction of power, for the same null hypothesis as in the main text, the prediction-powered approach required n = 40 data points to reject, while the classical baseline required n = 35.
0.1 0.2
Fraction of deforested areas
100 200 300 400 500
n
0.10
0.15
0.20
w id
th
Figure S4: Deforestation analysis with a linear model. This is the same figure as Fig. 2D, with the same color coding; the prediction-powered approach is green, the classical approach is gray, and the imputation approach is gold. However, here the gradient-boosted tree was replaced with an ordinary linear regression. The drop in performance causes the classical intervals to outperform the prediction-powered intervals in terms of power.
Unlabeled Data Set is Too Small The AlphaFold-based proteomic analysis from the main text was repeated. However, N = 1000 data points were randomly chosen as the unlabeled dataset. The rest of the procedure is performed exactly the same way as described in the main text. The decrease in sample size led to a reduction in power, and in the regime n > N , the classical baseline outperformed the prediction-powered approach. See Fig. S5 for the results. For the same null hypothesis as in the main text, the prediction-powered approach required n = 869 data points to reject, while the classical baseline required n = 652.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_Zvf2mX5iH-Fpv2NGKCOxEB3bwNdeAFeiksjlwIxKngogEwOQlnV9j3scHkNAGHhHLy7FyNc9mSKn9I7UvBnhJfRy2ACXvGcrgJqgb51QgT3p0nozV-4dDUXqCRiKuKNIDLHFngQ=w436-h218-v0?authuser=0)

2 4 6 8
Odds ratio
1000 2000 3000
n
2
4
6
8
10
12
w id
th
Figure S5: AlphaFold analysis with a small unlabeled dataset. This is the same figure as Fig. 2A, with the same color coding; the prediction-powered approach is green, the classical approach is gray, and the imputation approach is gold. However, here N was taken to be 1000. It can be seen that, when n > N , the classical baseline outperforms the prediction-powered one.
Validity of Prediction-Powered Inference Our main contribution is a technique for inference on estimands that can be expressed as the solution to a convex optimization problem. Formally, estimands of the following form are considered
θ∗ = argmin θ∈Rp
E [Lθ(Xi, Yi)] ,
for a loss function Lθ : X ×Y → R that is convex in θ ∈ Rp, for some p ∈ N. This paradigm captures problems such as mean estimation, median and general quantile estimation, estimation of linear and logistic regression coefficients, among others.
In the following, the term ∇Lθ denotes a subgradient of Lθ with respect to θ. Under mild conditions, convexity ensures that θ∗ can also be expressed as the value solving
E [∇Lθ∗(Xi, Yi)] = 0. (S1)
Henceforth, convex estimation problems where θ∗ satisfies (S1) will be called nondegenerate, and mild conditions that ensure this regularity will be later discussed.
The measure of fit on the imputed data will be defined as:
mθ = 1
N
N∑ i=1
∇Lθ(X ′ i, Ŷ
′ i ).
Next, the rectifier is defined as the difference between the measure of fit computed on the labeled data, (X,Y ), and the labeled data when the true outcomes are replaced with predicted ones, (X, Ŷ ):
∆θ = 1
n
n∑ i=1
( ∇Lθ(Xi, Yi)−∇Lθ(Xi, Ŷi)
) .
Further denoting by∇Lθ,j(x, y) the j-th coordinate of∇Lθ(x, y), the corresponding standard deviations are denoted as:
σ̂2 ∆θ,j
= 1
n
n∑ i=1
( ∇Lθ,j(Xi, Yi)−∇Lθ,j(Xi, Ŷi)−∆θ,j
)2 ; σ̂2
mθ,j =
1
N
N∑ i=1
( ∇Lθ,j(X
′ i, Ŷ
′ i )−mθ,j
)2 ,
for j ∈ [p].
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9oCVpBFbb3NA48Qdd7jBSBToYwDpieDJI04o_m26E59Ql8F6mt9aNm_G-D0JkoHH8Yy2vhVLBjuHke-vjR3Gd_qMjVPX94o2ut_s-AA8_wOc0vP9uMAYVfF5iWzzGqUyjq7BGjlw=w436-h218-v0?authuser=0)

Throughout, zq denotes the q-quantile of the standard normal distribution.
The main mathematical result of this work is stated in Theorem S1.
Theorem S1 (Validity of prediction-powered inference). Let the labeled and unlabeled data be sampled i.i.d.. Suppose that the convex estimation problem is nondegenerate as in (S1) and that n
N → p, for some p ∈ (0, 1). Fix α ∈ (0, 1) and let
CPP α = {θ : |mθ +∆θ| ≤ wθ(α)} , (S2)
where wθ(α) ∈ Rp has j-th coordinate equal to wθ,j(α) = z1−α/(2p)
√ σ̂2 ∆θ,j
n + σ̂2 mθ,j
N , and the inequality in (S2) is applied coordinatewise. Then,
lim inf n,N→∞
P (θ∗ ∈ CPP α ) ≥ 1− α.
Proof. The proof will show that θ∗ ̸∈ CPP α with probability at most α in the limit; that is,
lim sup n,N→∞
P
|∆θ∗,j +mθ∗,j | > z1−α/(2p)
√ σ̂2 ∆θ∗ ,j
n +
σ̂2 mθ∗ ,j
N , ∀j ∈ [p]
 ≤ α.
For each j ∈ [p], the central limit theorem implies that √ n(∆θ∗,j − E[∆θ∗,j ])⇒ N (0, σ2
∆θ∗ ,j ); √ N(mθ∗,j − E[mθ∗,j ])⇒ N (0, σ2
mθ∗ ,j ),
where σ2 ∆θ∗ ,j
is the variance of ∇Lθ∗,j(Xi, Yi) − ∇Lθ∗,j(Xi, Ŷi) and σ2 mθ∗ ,j
is the variance of ∇Lθ∗,j(Xi, Ŷi). Therefore, by Slutsky’s theorem,
√ N (∆θ∗,j +mθ∗,j − E[∆θ∗,j +mθ∗,j ]) =
√ n (∆θ∗,j − E[∆θ∗,j ])
√ N
n + √ N (mθ∗,j − E[mθ∗,j ])
⇒ N ( 0,
1
p σ2 ∆θ∗ ,j
+ σ2 mθ∗ ,j
) .
This in turn implies
lim sup n,N→∞
P
( |∆θ∗,j +mθ∗,j − E [∆θ∗,j +mθ∗,j ]| > z1−α/(2p)
σ̂j√ N
) ≤ α
p ,
where σ̂2 j is a consistent estimate of the variance 1
pσ 2 ∆θ∗ ,j
+ σ2 mθ∗ ,j
. Define σ̂2 j = σ̂2
∆θ∗ ,j N n + σ̂2
mθ∗ ,j ; this estimate is
consistent because the two terms are individually consistent estimates of the respective variances. Now notice that
E [∆θ∗ +mθ∗ ] = E [ (∇Lθ∗(Xi, Yi)−∇Lθ∗(Xi, Ŷi)) +∇Lθ∗(X ′
i, Ŷ ′ i ) ] = E[∇Lθ∗(Xi, Yi)] = 0,
where the last step follows by the nondegeneracy condition. Putting together the previous two displays and the choice of σ̂j derived above, and applying a union bound yields
lim sup n,N→∞
P
∃j ∈ [p] : |∆θ∗,j +mθ∗,j | > z1−α/(2p)
√ σ̂2 ∆θ∗ ,j
n +
σ̂2 mθ∗ ,j
N
 ≤
p∑ j=1
lim sup n,N→∞
P
|∆θ∗,j +mθ∗,j | > z1−α/(2p)
√ σ̂2 ∆θ∗ ,j
n +
σ̂2 mθ∗ ,j
N
 =
p∑ j=1
lim sup n,N→∞
P ( |∆θ∗,j +mθ∗,j | > z1−α/(2p)σ̂j
) ≤
p∑ j=1
α
p
= α.
Therefore, lim supn,N→∞ P (θ∗ ̸∈ CPP α ) ≤ α.
Most practical problems are nondegenerate (S1). For example, if the loss is differentiable for all θ ∈ Rp, then the problem is immediately nondegenerate. Furthermore, if the data distribution does not have point masses and, for every θ, Lθ(x, y) is nondifferentiable only for a measure-zero set of (x, y) pairs, then the problem is again nondegenerate.
Algorithms Prediction-Powered Confidence Intervals The algorithms previously referenced in Table 1 are presented. The algorithms are derived by instantiating Theorem S1 with the appropriate loss function dependent on the estimand. In addition, guarantees of their formal validity are stated.
Algorithm S1 Prediction-powered mean estimation
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), error level α ∈ (0, 1)
1: θ̂PP ← θ̂ −∆ := 1 N
∑N i=1 Ŷ
′ i − 1
n
∑n i=1(Ŷi − Yi)
2: σ̂2 Ŷ ′ ← 1
N
∑N i=1(Ŷ
′ i − θ̂)2
3: σ̂2 Ŷ−Y
← 1 n
∑n i=1(Ŷi − Yi −∆)2
4: w(α)← z1−α/2
√ σ̂2 Ŷ −Y
n + σ̂2 Ŷ ′ N
Output: prediction-powered confidence set CPP α =
( θ̂PP ± w(α)
)
Algorithm S2 Prediction-powered median estimation
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), error level α ∈ (0, 1) 1: Construct fine grid Θgrid between mini∈[N ] Ŷ
′ i and maxi∈[N ] Ŷ
′ i
2: for θ ∈ Θgrid do 3: ∆θ ← 1
n
∑n i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
}) 4: mθ ← 1
2N
∑N i=1 sign
( θ − Ŷ ′
i
) 5: σ̂2
∆θ ← 1
n
∑n i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
} −∆θ
)2 6: σ̂2
mθ ← 1
N
∑N i=1
( 1
{ Ŷ ′ i ≤ θ
} −mθ
)2 7: wθ(α)← z1−α/2
√ σ̂2 ∆θ
n + σ̂2 mθ
N
Output: prediction-powered confidence set CPP α = {θ ∈ Θgrid : |mθ +∆θ| ≤ wθ(α)}
Algorithm S3 Prediction-powered quantile estimation
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), quantile q, error level α ∈ (0, 1) 1: Construct fine grid Θgrid between mini∈[N ] Ŷ
′ i and maxi∈[N ] Ŷ
′ i
2: for θ ∈ Θgrid do 3: ∆θ ← 1
n
∑n i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
}) 4: F̂θ ← 1
N
∑N i=1 1
{ Ŷ ′ i ≤ θ
} 5: σ̂2
∆θ ← 1
n
∑n i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
} −∆θ
)2 6: σ̂2
Ŷ ′,θ ← 1
N
∑N i=1
( 1
{ Ŷ ′ i ≤ θ
} − F̂θ
)2 7: wθ(α)← z1−α/2
√ σ̂2 ∆θ
n + σ̂2 Ŷ ′,θ N
Output: prediction-powered confidence set CPP α =
{ θ ∈ Θgrid : |F̂θ +∆θ − q| ≤ wθ(α)
}
Algorithm S4 Prediction-powered linear regression
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), coefficient j∗, error level α ∈ (0, 1)
1: θ̂PP ← θ̂ −∆ := X ′†Ŷ ′ −X†(f − Y )
2: Σ′ ← 1 N (X ′)⊤X ′, M ′ ← 1
N
∑N i=1(Ŷ
′ i − (X ′
i) ⊤θ̂)2X ′
i(X ′ i)
⊤
3: V ′ ← (Σ′)−1M ′(Σ′)−1
4: Σ← 1 nX
⊤X , M ← 1 n
∑n i=1(Ŷi − Yi −X⊤
i ∆)2XiX ⊤ i
5: V ← Σ−1MΣ−1
6: w(α)← z1−α/2
√ Vj∗j∗
n + V ′ j∗j∗
N
Output: prediction-powered confidence set CPP α =
( θ̂PP j∗ ± w(α)
) Algorithm S5 Prediction-powered logistic regression
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), error level α ∈ (0, 1) 1: Construct fine grid Θgrid ⊂ Rd of possible coefficients 2: ∆j ← 1
n
∑n i=1 Xi,j(Ŷi − Yi), j ∈ [d]
3: σ̂2 ∆,j ← 1
n
∑n i=1
( Xi,j(Ŷi − Yi)−∆j
)2 , j ∈ [d]
4: for θ ∈ Θgrid do 5: mθ,j ← 1
N
∑N i=1 X
′ i,j
( µθ(X
′ i)− Ŷ ′
i
) , j ∈ [d], where µθ(x) =
1 1+exp(−x⊤θ)
6: σ̂2 mθ,j
← 1 N
∑N i=1
( X ′
i,j(µθ(X ′ i)− Ŷ ′
i )−mθ,j
)2 , j ∈ [d]
7: wθ,j(α)← z1−α/(2d)
√ σ̂2 ∆,j
n + σ̂2 mθ,j
N , j ∈ [d]
Output: prediction-powered confidence set CPP α = {θ ∈ Θgrid : |mθ,j +∆j | ≤ wθ,j(α),∀j ∈ [d]}
Algorithm S6 Prediction-powered convex risk minimization
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), error level α ∈ (0, 1) , gradient function ∇Lθ : X × Y → Rp
1: Construct fine grid Θgrid ⊂ Rp of possible solutions 2: for θ ∈ Θgrid do 3: ∆θ,j ← 1
n
∑n i=1
( ∇Lθ,j(Xi, Yi)−∇Lθ,j(Xi, Ŷi)
) , j ∈ [p]
4: σ̂2 ∆θ,j
← 1 n
∑n i=1
( ∇Lθ,j(Xi, Yi)−∇Lθ,j(Xi, Ŷi)−∆θ,j
)2 , j ∈ [p]
5: mθ,j ← 1 N
∑N i=1∇Lθ,j(X
′ i, Ŷ
′ i ), j ∈ [p]
6: σ̂2 mθ,j
← 1 N
∑N i=1
( ∇Lθ,j(X
′ i, Ŷ
′ i )−mθ,j
)2 , j ∈ [p]
7: wθ,j(α)← z1−α/(2p)
√ σ̂2 ∆θ,j
n + σ̂2 mθ,j
N , j ∈ [p]
Output: prediction-powered confidence set CPP α = {θ ∈ Θgrid : |mθ,j +∆θ,j | ≤ wθ,j(α),∀j ∈ [p]}
Regularity conditions. All algorithms stated in this section rely on confidence intervals derived from the central limit theorem. For such intervals to be asymptotically valid, it is required that the two quantities whose mean is being estimated, namely∇Lθ(Xi, Yi)−∇Lθ(Xi, Ŷi) and∇Lθ(Xi, Ŷi), have at least the first two moments (see Proposition S2).
For Corollary S3 to hold, the same conditions are required as those needed for classical linear regression intervals to cover the target. These conditions are very weak; in particular, it is not required that the true data-generating process be linear or the errors be homoskedastic. See Buja et al. (29) for a detailed discussion. The following are the required conditions, as stated in Theorem 3 of Halbert White’s seminal paper (30). The data (X1, Y1), . . . , (Xn, Yn) is generated as Xi = h(Zi), Yi = g(Zi) + ϵi, where (Zi, ϵi) are mean-zero i.i.d. random draws from some distribution
such that E[ZiZ ⊤ i ] and E[XiX
⊤ i ] are finite and nonsingular, and E[ϵ2i ], E[Y 2
i XiX ⊤ i ], and E[X2
ijXiX ⊤ i ] are all finite.
In addition, it is assumed that h and g are measurable. Under these conditions, √ n(θ̂OLS − θ∗)⇒ N (0,Σ−1V Σ−1),
where θ∗ = argminθ E[(Y1 − X⊤ 1 θ)2], θ̂OLS = argminθ
1 n
∑n i=1(Yi − X⊤
i θ)2, Σ = E[X1X ⊤ 1 ], V = E[(Y1 −
X⊤ 1 θ∗)2X1X
⊤ 1 ]. Moreover, 1
nX ⊤X → Σ and 1
n
∑n i=1(Yi −X⊤
i θ̂OLS) 2XiX
⊤ i → V almost surely.
Corollary S1 (Mean estimation). Let θ∗ be the mean outcome:
θ∗ = E[Yi].
Then, the prediction-powered confidence interval in Algorithm S1 is valid: lim infn,N→∞ P ( θ∗ ∈ CPP
α
) ≥ 1− α.
Proof. The prediction-powered confidence set constructed in Algorithm S1 is a special case of the prediction-powered confidence set constructed in Theorem S1. The proof then follows directly by the guarantee of Theorem S1.
Since∇Lθ(y) = θ − y, one has
∆θ ≡∆ = 1
n
n∑ i=1
(Ŷi − Yi); mθ = θ − 1
N
N∑ i=1
Ŷ ′ i .
Therefore, the set CPP α from Theorem S1 can be written as
CPP α =
{ θ :
∣∣∣∣∣θ − 1
N
N∑ i=1
Ŷ ′ i +
1
n
n∑ i=1
(Ŷi − Yi)
∣∣∣∣∣ ≤ wθ(α)
} =
( 1
N
N∑ i=1
Ŷ ′ i −
1
n
n∑ i=1
(Ŷi − Yi)± wθ(α)
) .
This is exactly the set constructed in Algorithm S1, which completes the proof.
The median algorithm (Algorithm S2) is a special case of the general quantile algorithm (Algorithm S3), obtained by setting q = 0.5. Therefore, we only state the guarantees for Algorithm S3.
Corollary S2 (Quantile estimation). Let θ∗ be the q-quantile:
θ∗ = min{θ : P (Yi ≤ θ) ≥ q}.
Then, the prediction-powered confidence set in Algorithm S3 is valid: lim infn,N→∞ P ( θ∗ ∈ CPP
α
) ≥ 1− α.
Proof. Like in the proof of Corollary S1, we proceed by showing that the prediction-powered confidence set constructed in Algorithm S3 is a special case of the prediction-powered confidence set constructed in Theorem S1. Then, we simply invoke Theorem S1.
Since∇Lθ(y) = −q + 1 {y ≤ θ}, we have
∆θ = 1
n
n∑ i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
}) ; mθ = −q + F̂θ,
where F̂θ = 1 N
∑N i=1 1
{ Ŷ ′ i ≤ θ
} . Therefore, the set CPP
α from Theorem S1 can be written as
CPP α =
{ θ :
∣∣∣∣∣ 1n n∑
i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
}) − q + F̂θ
∣∣∣∣∣ ≤ wθ(α)
} = { θ : ∣∣∣F̂θ +∆θ − q
∣∣∣ ≤ wθ(α) } .
This is exactly the set constructed in Algorithm S3. Therefore, the guarantee of Corollary S2 follows by the guarantee of Theorem S1.
Corollary S3 (Linear regression). Fix j∗ ∈ [d]. Let θ∗ be the linear regression solution:
θ∗ = argmin θ∈Rd
E[(Yi −X⊤ i θ)2].
Then, the prediction-powered confidence interval in Algorithm S4 is valid: lim infn,N→∞ P ( θ∗j∗ ∈ CPP
α
) ≥ 1− α.
Proof. For linear regression, we can derive more powerful prediction-powered confidence intervals than those implied by Theorem S1 by exploiting the linearity of the least-squares estimator.
As in Theorem S1, we assume that n N → p, for some fraction p ∈ (0, 1).
Theorem 3 of White (31) implies that √ n(∆− ∆̄)⇒ N (0,W );
√ N(θ̂ − θ̄)⇒ N (0,W ′),
for appropriately defined coviariance matrices W and W ′, where θ̄ = (E[XiX ⊤ i ])−1E[XiŶi] and ∆̄ = (E[XiX
⊤ i ])−1E[Xi(Ŷi−
Yi)]. With this, we can write the target estimand as θ∗ = (E[XiX ⊤ i ])−1E[XiYi] = θ̄ − ∆̄.
Combining Theorem 3 of White with Slutsky’s theorem, we get
√ N(θ̂PP − θ∗) =
√ N(θ̂ − θ̄)−
√ n(∆− ∆̄)
√ N
n ⇒ N
( 0,W
1
p +W ′
) .
White also shows that V and V ′, as defined in Algorithm S4, are consistent estimates of W and W ′, respectively. Therefore, θ̂PP is asymptotically normal and consistent, and we have a consistent estimate of its covariance. In particular,
Vj∗j∗ N
n + V ′
j∗j∗ →Wj∗j∗ 1
p +W ′
j∗j∗ .
This means that we can construct asymptotically valid confidence intervals via a normal approximation by choosing
width z1−α/2
√ Vj∗j∗
N n + V ′
j∗j∗
√ 1 N = z1−α/2
√ Vj∗j∗
n + V ′ j∗j∗
N , and this is precisely what Algorithm S4 accomplishes.
Corollary S4 (Logistic regression). Let θ∗ be the logistic regression solution:
θ∗ = argmin θ∈Rd
E [ −Yiθ
⊤Xi + log(1 + exp(θ⊤Xi)) ] .
Then, the prediction-powered confidence set in Algorithm S5 is valid: lim infn,N→∞ P ( θ∗ ∈ CPP
α
) ≥ 1− α.
Proof. The proof follows a similar pattern as the first two corollaries, by arguing that the prediction-powered confidence set constructed in Algorithm S5 is a special case of the prediction-powered confidence set constructed in Theorem S1.
Since∇Lθ(x, y) = x(µθ(x)− y), we have
∆θ ≡∆ = 1
n
n∑ i=1
Xi(Ŷi − Yi); mθ = 1
N
N∑ i=1
X ′ i(µθ(X
′ i)− Ŷ ′
i ).
These quantities are explicitly computed in Algorithm S5. Moreover, the set CPP α constructed in Algorithm S5 exactly
follows the recipe of Theorem S1, so the proof immediately follows.
Corollary S5 (Convex risk minimization). Let θ∗ be the convex risk minimizer:
θ∗ = argmin θ∈Rp
E [Lθ(Xi, Yi)] .
Then, the prediction-powered confidence set in Algorithm S6 is valid: lim infn,N→∞ P ( θ∗ ∈ CPP
α
) ≥ 1− α.
The validity of Algorithm S6 follows directly by Theorem S1.
Prediction-Powered p-values By relying on the standard duality between confidence intervals and p-values, we can immediately repurpose the presented theory to compute valid prediction-powered p-values.
To formalize this, suppose that we want to test the hull hypothesis H0 : θ∗ ∈ Θ0, for some set Θ0 ∈ Rp (for example, a common choice when p = 1 is Θ0 = R≤0). Let Cα be a valid confidence interval. Then, we can construct a valid p-value as
P = inf{α : θ0 ̸∈ Cα,∀θ0 ∈ Θ0}.
A p-value P is valid if it is super-uniform under the null, meaning P (P ≤ u) ≤ u for all u ∈ [0, 1]. This is indeed the case for the p-value defined above, because when θ∗ ∈ Θ0, we have
P (P ≤ u) ≤ P (θ∗ ̸∈ Cu) ≤ u.
The first inequality follows by the definition of P and the fact that θ∗ ∈ Θ0, and the second inequality follows by the validity of Cu at level 1− u. We are implicitly using the fact that Cu ⊆ Cu′ when u ≥ u′.
The above derivation is a general recipe for deriving p-values from confidence intervals. For the predictionpowered confidence interval stated in Theorem S1, the corresponding prediction-powered p-value is given by:
PPP = inf {α : |mθ0 +∆θ0 | > wθ0(α), ∀θ0 ∈ Θ0} .
Below we state analogues of Algorithms 1-5 when the goal is to compute a prediction-powered p-value.
Algorithm S7 Prediction-powered p-value for the mean
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), null set Θ0
1: θ̂PP ← θ̂ −∆ := 1 N
∑N i=1 Ŷ
′ i − 1
n
∑n i=1(Ŷi − Yi)
2: σ̂2 Ŷ ′ ← 1
N
∑N i=1(Ŷ
′ i − θ̂)2
3: σ̂2 Ŷ−Y
← 1 n
∑n i=1(Ŷi − Yi −∆)2
4: Define w(α) := z1−α/2
√ σ̂2 Ŷ −Y
n + σ̂2 Ŷ ′ N
Output: prediction-powered p-value PPP = inf{α : θ0 ̸∈ (θ̂PP ± w(α)),∀θ0 ∈ Θ0}
Algorithm S8 Prediction-powered p-value for the median
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), null set Θ0
1: for θ ∈ Θ0 do 2: ∆θ ← 1
n
∑n i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
}) 3: mθ ← 1
2N
∑N i=1 sign
( θ − Ŷ ′
i
) 4: σ̂2
∆θ ← 1
n
∑n i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
} −∆θ
)2 5: σ̂2
mθ ← 1
N
∑N i=1
( 1
{ Ŷ ′ i ≤ θ
} −mθ
)2 6: Define wθ(α) := z1−α/2
√ σ̂2 ∆θ
n + σ̂2 mθ
N
Output: prediction-powered p-value PPP = inf {α : θ ∈ Θgrid : |mθ0 +∆θ0 | > wθ0(α),∀θ0 ∈ Θ0}
Algorithm S9 Prediction-powered p-value for the q-quantile
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), quantile q, null set Θ0
1: for θ ∈ Θ0 do 2: ∆θ ← 1
n
∑n i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
}) 3: F̂θ ← 1
N
∑N i=1 1
{ Ŷ ′ i ≤ θ
} 4: σ̂2
∆θ ← 1
n
∑n i=1
( 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
} −∆θ
)2 5: σ̂2
Ŷ ′,θ ← 1
N
∑N i=1
( 1
{ Ŷ ′ i ≤ θ
} − F̂θ
)2 6: Define wθ(α) := z1−α/2
√ σ̂2 ∆θ
n + σ̂2 Ŷ ′,θ N
Output: prediction-powered p-value PPP = inf { α : |F̂θ0 +∆θ0 − q| > wθ0(α),∀θ0 ∈ Θ0
} Algorithm S10 Prediction-powered p-value for linear regression coefficients
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), coefficient j∗, null set Θ0
1: θ̂PP ← θ̂ −∆ := X ′†Ŷ ′ −X†(Ŷ − Y )
2: Σ′ ← 1 N (X ′)⊤X ′, M ′ ← 1
N
∑N i=1(Ŷ
′ i − (X ′
i) ⊤θ̂)2X ′
i(X ′ i)
⊤
3: V ′ ← (Σ′)−1M ′(Σ′)−1
4: Σ← 1 nX
⊤X , M ← 1 n
∑n i=1(Ŷi − Yi −X⊤
i ∆)2XiX ⊤ i
5: V ← Σ−1MΣ−1
6: Define w(α) := z1−α/2
√ Vj∗j∗
n + V ′ j∗j∗
N
Output: prediction-powered confidence set CPP α = inf{α : θ0 ̸∈ (θ̂PP
j∗ ± w(α)),∀θ0 ∈ Θ0}
Algorithm S11 Prediction-powered p-value for logistic regression coefficients
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), null set Θ0
1: ∆j ← 1 n
∑n i=1 Xi,j(Ŷi − Yi), j ∈ [d]
2: σ̂2 ∆,j ← 1
n
∑n i=1
( Xi,j(Ŷi − Yi)−∆j
)2 , j ∈ [d]
3: for θ ∈ Θ0 do 4: mθ,j ← 1
N
∑N i=1 X
′ i,j
( µθ(X
′ i)− Ŷ ′
i
) , j ∈ [d], where µθ(x) =
1 1+exp(−x⊤θ)
5: σ̂2 mθ,j
← 1 N
∑N i=1
( X ′
i,j(µθ(X ′ i)− Ŷ ′
i )−mθ,j
)2 , j ∈ [d]
6: Define wθ,j(α) := z1−α/(2d)
√ σ̂2 ∆,j
n + σ̂2 mθ,j
N , j ∈ [d]
Output: prediction-powered p-value PPP = inf {α : |mθ0,j +∆j | > wθ0,j(α),∀j ∈ [d], θ0 ∈ Θ0}
Corollary S6 (Mean p-value). Let θ∗ be the mean outcome:
θ∗ = E[Yi].
Then, the prediction-powered p-value in Algorithm S7 is valid: under the null, lim infn,N→∞ P ( PPP ≤ u
) ≤ u,∀u ∈ [0, 1].
Corollary S7 (Quantile p-value). Let θ∗ be the q-quantile:
θ∗ = min{θ : P (Yi ≤ θ) ≥ q}.
Then, the prediction-powered p-value in Algorithm S9 is valid: under the null, lim infn,N→∞ P ( PPP ≤ u
) ≤ u,∀u ∈ [0, 1].
Corollary S8 (Linear regression p-value). Fix j∗ ∈ [d]. Let θ∗ be the linear regression solution:
θ∗ = argmin θ∈Rd
E[(Yi −X⊤ i θ)2].
Then, the prediction-powered p-value in Algorithm S10 is valid: under the null, lim infn,N→∞ P ( PPP ≤ u
) ≤ u,∀u ∈ [0, 1].
Corollary S9 (Logistic regression p-value). Let θ∗ be the logistic regression solution:
θ∗ = argmin θ∈Rd
E [ −Yiθ
⊤Xi + log(1 + exp(θ⊤Xi)) ] .
Then, the prediction-powered p-value in Algorithm S11 is valid: under the null, lim infn,N→∞ P ( PPP ≤ u
) ≤ u,∀u ∈ [0, 1].
Nonasymptotic Analysis of Prediction-Powered Inference Just like in most common confidence interval constructions, in Theorem S1 we used an argument based on the central limit theorem to construct the prediction-powered confidence set; as a result, the validity statement is asymptotic. We opted to present Theorem S1 as the main technical result due to its interpretability. However, the key underlying principles of prediction-powered inference can also be applied nonasymptotically. In this section we state the nonasymptotic counterparts of the previous results.
Validity Below we state a nonasymptotic analogue of Theorem S1.
To state the result, let m̄θ denote the population-level measure of fit on the imputed data:
m̄θ = E[∇Lθ(Xi, Ŷi)].
Similarly, we let ∆̄θ denote the population-level rectifier:
∆̄θ = E [ ∇Lθ(Xi, Yi)−∇Lθ(Xi, Ŷi)
] .
Theorem S2 (Validity of prediction-powered inference: nonasymptotic). Let the labeled and unlabeled data be sampled i.i.d.. Suppose that the convex estimation problem is nondegenerate as in (S1). Fix α ∈ (0, 1) and δ ∈ (0, α). Suppose that, for any θ ∈ Rp, we can constructRθ(δ) and Tθ(α− δ) satisfying
P ( ∆̄θ ∈ Rθ(δ)
) ≥ 1− δ; P (m̄θ ∈ Tθ(α− δ)) ≥ 1− (α− δ).
Let CPP α = {θ : 0 ∈ Rθ(δ) + Tθ(α− δ)}, where + denotes the Minkowski sum.1 Then,
P (θ∗ ∈ CPP α ) ≥ 1− α.
Proof. We show that θ∗ ∈ CPP α with probability at least 1− α; that is, with probability at least 1− α it holds that
0 ∈ Rθ∗(δ) + Tθ∗(α− δ).
Consider the event E = {∆̄θ∗ ∈ Rθ∗(δ)} ∩ {m̄θ∗ ∈ Tθ∗(α− δ)}. By a union bound, P (E) ≥ 1 − α. On the event E, we have that
E[∇Lθ∗(Xi, Yi)] = E[∇Lθ∗(Xi, Yi)]− E[∇Lθ∗(Xi, Ŷi)] + E[∇Lθ∗(Xi, Ŷi)]
= ∆̄θ∗ + m̄θ∗ ∈ Rθ∗(δ) + Tθ∗(α− δ).
The theorem finally follows by invoking the nondegeneracy condition, which ensures E[∇Lθ∗(Xi, Yi)] = 0, so we have shown 0 ∈ Rθ∗(δ) + Tθ∗(α− δ).
We note that, because m̄θ and ∆̄θ are mean values of a well-specified quantity, the sets Rθ(δ) and Tθ(α− δ) can be constructed using any off-she-shelf algorithm for computing a confidence intervals for the mean. In our explicit algorithm statements below, we choose a variance-adaptive confidence interval for the mean due to Waudby-Smith and Ramdas (32), which we state in Algorithm S15. We opt to present this construction as the default nonasymptotic confidence interval for the mean because of its strong practical performance. The only assumption required to apply Algorithm S15 is that the observations are almost surely bounded within a known interval.
1The Minkowski sum of two sets A and B is equal to {a+ b : a ∈ A, b ∈ B}.
Algorithms We state nonasymptotically-valid algorithms for prediction-powered mean estimation, quantile estimation, and logistic regression. These are nonasymptotic counterparts of Algorithms S1, S3, and S5, and they rely on the abstract recipe from Theorem 2.
Algorithm S12 Prediction-powered mean estimation (nonasymptotic)
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), error levels α, δ ∈ (0, 1), bound B
1: (Ŷ l(α− δ), Ŷ u(α− δ))← MeanCI ( {Ŷ ′
i }Ni=1, err = α− δ, range = [0, B] )
2: (Rl(δ),Ru(δ))← MeanCI ( {Ŷi − Yi}ni=1, err = δ, range = [−B,B]
) Output: prediction-powered confidence set CPP
α = ( Ŷ l(α− δ)−Ru(δ), Ŷ u(α− δ)−Rl(δ)
) Algorithm S13 Prediction-powered quantile estimation (nonasymptotic)
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), quantile q, error levels α, δ ∈ (0, 1) 1: Construct fine grid Θgrid between mini∈[N ] Ŷ
′ i and maxi∈[N ] Ŷ
′ i
2: for θ ∈ Θgrid do 3: (Rl
θ(δ),Ru θ (δ))← MeanCI
({ 1 {Yi ≤ θ} − 1
{ Ŷi ≤ θ
}}n
i=1 , err = δ, range = [−1, 1]
) 4: (F̂ l
θ(α− δ), F̂u θ (α− δ))← MeanCI
({ 1
{ Ŷ ′ i ≤ θ
}}N
i=1 , err = α− δ, range = [0, 1]
) Output: prediction-powered confidence set CPP
α = { θ ∈ Θgrid : q ∈
( F̂ l θ(α− δ) +Rl
θ(δ), F̂ u θ (α− δ) +Ru
θ (δ) )}
Algorithm S14 Prediction-powered logistic regression (nonasymptotic)
Input: labeled data (X,Y ), unlabeled features X ′, predictions (Ŷ, Ŷ ′), error levels α, δ ∈ (0, 1), bounds Bj
1: Construct fine grid Θgrid ⊂ Rd of possible coefficients
2: (Rl j(δ),Ru
j (δ))← MeanCI ( {Xi,j(Ŷi − Yi)}ni=1, err = δ, range = [−Bj , Bj ]
) , j ∈ [d]
3: for θ ∈ Θgrid do 4: (ml
θ,j(α−δ),mu θ,j(α−δ))← MeanCI
( {X ′
i,j
( µθ(X
′ i)− Ŷ ′
i
) }Ni=1, err =
α−δ d , range = [−Bj , Bj ]
) , j ∈ [d],
5: where µθ(x) = 1
1+exp(−x⊤θ)
Output: prediction-powered confidence set CPP α =
{ θ ∈ Θgrid : 0 ∈
[ ml
θ,j(α− δ) +Rl j(δ),m
u θ,j(α− δ) +Ru
j (δ) ] ,∀j ∈ [d]
} Corollary S10 (Mean estimation: nonasymptotic). Let θ∗ be the mean outcome:
θ∗ = E[Yi].
Suppose that Yi, Ŷi ∈ [0, B] almost surely. Then, the prediction-powered confidence set in Algorithm S12 is valid: P (θ∗ ∈ CPP
α ) ≥ 1− α.
Proof. The proof follows by instantiating the terms in Theorem 2. In particular, we have E[∇Lθ(Ŷi)] = θ − E[Ŷi], hence it is valid to construct Tθ(α− δ) as:
mθ ∈ Tθ(α− δ) = θ − (Ŷ l(α− δ), Ŷ u(α− δ)).
Therefore, the condition 0 ∈ R(δ) + Tθ(α− δ) becomes
0 ∈ (Rl(δ),Ru(δ)) + θ − (Ŷ l(α− δ), Ŷ u(α− δ)),
which after rearranging and simplifying is equivalent to
θ ∈ ( Ŷ l(α− δ)−Ru(δ), Ŷ u(α− δ)−Rl(δ)
) .
This set exactly matches the set CPP α constructed in Algorithm S12.
Corollary S11 (Quantile estimation: nonasymptotic). Let θ∗ be the q-quantile:
θ∗ = min{θ : P (Yi ≤ θ) ≥ q}.
Then, the prediction-powered confidence set in Algorithm S13 is valid: P (θ∗ ∈ CPP α ) ≥ 1− α.
Proof. The proof follows by instantiating the terms in Theorem 2. First, we have E[∇Lθ(Ŷi)] = −q + P (Ŷi ≤ θ); therefore, it is valid to construct Tθ(α− δ) as:
E[∇Lθ(Ŷi)] ∈ Tθ(α− δ) = −q + ( F̂ l θ(α− δ), F̂u
θ (α− δ) ) .
Therefore, the condition 0 ∈ Rθ(δ) + Tθ(α− δ) becomes
q ∈ ( F̂ l θ(α− δ) +Rl
θ(δ), F̂ u θ (α− δ) +Ru
θ (δ) ) ,
which matches the condition used to form CPP α in Algorithm S13.
Corollary S12 (Logistic regression: nonasymptotic). Let θ∗ be the logistic regression solution:
θ∗ = argmin θ∈Rd
E[−Yiθ ⊤Xi + log(1 + exp(θ⊤Xi))].
Suppose that |Xi,j | ≤ Bj and Yi, Ŷi ∈ [0, 1] almost surely. Then, the prediction-powered confidence set in Algorithm S14 is valid: P (θ∗ ∈ CPP
α ) ≥ 1− α.
Proof. We instantiate the relevant terms in Theorem 2. We have E[∇Lθ(Xi, Ŷi)] = E [ −XiŶi +Xi
1 1+exp(−X⊤
i θ)
] .
Note that, because Xi is coordinatewise bounded, and Yi, 1
1+exp(−X⊤ i θ) ∈ [0, 1], we have |(∇Lθ(Xi, Ŷi))j | ≤ Bj
almost surely. Therefore, we can construct Tθ(α− δ) as:
mθ ∈ Tθ(α− δ) = ( ml
θ(α− δ),mu θ (α− δ)
) = ( ml
θ,1(α− δ),mu θ,1(α− δ)
) × · · · ×
( ml
θ,d(α− δ),mu θ,d(α− δ)
) .
Since the rectifier has no dependence on θ, the condition 0 ∈ Rθ(δ) + Tθ(α− δ) becomes
0 ∈ (Rl j(δ),Ru
j (δ)) + ( ml
θ,j(α− δ),mu θ,j(α− δ)
) , ∀j ∈ [d],
which matches the condition in CPP α in Algorithm S14.
We note that there exists an analogous nonasymptotic algorithm for linear regression, however we do not recommend it in practice. The reason is that the refined (but asymptotic) analysis used to prove Corollary S3 shows that it is sufficient to analyze a one-dimensional rectifier, while directly invoking Theorem 2 would require analyzing a d-dimensional rectifier and thus yields more conservative intervals.
Algorithm S15 MeanCI (see Proposition S1)
Input: data points {Z1, . . . , Zn}, error level α ∈ (0, 1), range [L,U ] s.t. Zi ∈ [L,U ] 1: For all i ∈ [n], let Zi ← (Zi − L)/(U − L) ▷ normalize data to interval [0, 1] 2: Construct fine grid Mgrid of interval [0, 1] 3: Initialize active set A = Mgrid
4: for t ∈ 1, . . . , n do 5: Set µ̂t ←
0.5+ ∑t
j=1 Zj
t+1 , σ̂2 t ←
0.25+ ∑t
j=1(Zj−µ̂t) 2
t+1 , λt ← √
2 log(2/α) nσ̂2
t−1
6: for m ∈ A do 7: M+
t (m)← ( 1 + min
( λt,
0.5 m
) (Zt −m)
) M+
t−1(m)
8: M− t (m)←
( 1−min
( λt,
0.5 1−m
) (Zt −m)
) M−
t−1(m)
9: Mt(m)← 1 2 max
{ M+
t (m), M− t (m)
} ▷ construct test martingale for m ∈ [0, 1]
10: if Mt(m) ≥ 1/α then 11: A ← A \ {m} ▷ Remove m from active set Output: Confidence set for the mean Cα = {m(U − L) + L : m ∈ A}
Inference Under Distribution Shift In the main text we focused on forming prediction-powered confidence intervals when the labeled and unlabeled data come from the same distribution. Herein, we extend our tools to the case where the labeled data (X,Y ) comes from P and the unlabeled data (X ′, Y ′)—which defines the target of inference θ∗—comes from Q, and these are related by either a label shift or a covariate shift. For covariate shift, we handle all estimation problems previously studied; for label shift, we handle certain types of linear problems.
We will write EQ,EP, etc to indicate which distribution the data inside the expectation is sampled from.
Covariate Shift First, we assume that Q is a known covariate shift of P. That is, if we denote by Q = QX ·QY |X and P = PX · PY |X the relevant marginal and conditional distributions, we assume that QY |X = PY |X . As in previous sections, we consider estimands of the form
θ∗ = argmin θ∈Θ
EQ[Lθ(Xi, Yi)]. (S3)
Estimands of the form (S3) can be related to risk minimizers on P using the Radon-Nikodym derivative. In particular, suppose that QX is dominated by PX and assume that the Radon-Nikodym derivative w(x) = QX
PX (x) is
known. Then, we can rewrite (S3) as θ∗ = argmin
θ∈Θ EP[L
w θ (Xi, Yi)],
where Lw θ (x, y) = w(x)Lθ(x, y). In words, risk minimizers on Q can simply be written as risk minimizers on P, but
with a reweighted loss function. This permits inference on the rectifier to be based on data sampled from P as before. For concreteness, we explain the approach in detail for convex risk minimizers. Let
m̄w θ = EP
[ ∇Lw
θ (Xi, Ŷi) ] ; ∆̄w
θ = EP
[ ∇Lw
θ (Xi, Yi)−∇Lw θ (Xi, Ŷi)
] ,
where ∇Lw θ (x, y) = ∇Lθ(x, y) · w(x) and ∇Lθ is a subgradient of Lθ as before. A confidence set for the above
rectifier suffices for prediction-powered inference on θ∗.
Corollary S13 (Covariate shift). Let the unlabeled data distribution be a covariate shift of the labeled data distribution. Suppose that the problem (S3) is a nondegenerate convex estimation problem. Fix α ∈ (0, 1) and δ ∈ (0, α). Suppose that, for any θ ∈ Rp, we can constructRθ(δ) and Tθ(α− δ) satisfying
P ( ∆̄w
θ ∈ Rθ(δ) ) ≥ 1− δ; P (m̄w
θ ∈ Tθ(α− δ)) ≥ 1− (α− δ).
Let CPP α = {θ : 0 ∈ Rθ(δ) + Tθ(α− δ)}, where + denotes the Minkowski sum. Then,
P (θ∗ ∈ CPP α ) ≥ 1− α.
Label Shift Next, we analyze classification problems where the proportions of the classes in the labeled data is different from those in the unlabeled data. This problem has been studied before in the literature on domain adaptation, e.g. by Lipton et al. (33), but our treatment focuses on the formation of confidence intervals. Formally, let Y = {1, ...,K} be the label space and assume that QX|Y = PX|Y . We consider estimands of the form
θ∗ = EQY [ν(Y )],
where ν : Y → R is a fixed function. For example, choosing ν(y) = 1 {y = k} for some k ∈ [K] asks for inference on the proportion of instances that belong to class k.
Using an analogous decomposition to the one for mean estimation, we can write
θ∗ = EQŶ [ν(Ŷ )] + (EQY
[ν(Y )]− EQŶ [ν(Ŷ )]) = θ̄ + ∆̄,
where QŶ denotes the distribution of the prediction Ŷ based on features X ∼ QX . The quantity θ̄ can be estimated using the unlabeled data from Q and the model. Estimating the quantity ∆̄ using samples from P will require leveraging the structure of the distribution shift. Central to our analysis will be the confusion matrix
Kj,l = Q ( Ŷ = j
∣∣∣ Y = l ) , j, l ∈ [K].
The label-shift assumption implies thatKj,l = P ( Ŷ = j | Y = l
) , which can be estimated from labeled data sampled
from P. In particular, we estimate K from the labeled data as
K̂j,l = 1
n(l)
n∑ i=1
1
{ Ŷi = j, Yi = l
} , where n(l) =
n∑ i=1
1 {Yi = l} .
Similarly, we can estimate QŶ (k), k ∈ [K] as
Q̂Ŷ (k) = 1
N
N∑ i=1
1
{ Ŷ ′ i = k
} .
Treating QŶ and QY as vectors, notice that we can write QŶ = KQY , and hence QY = K−1QŶ . This leads to a natural estimate of QY , Q̂Y = K̂−1Q̂Ŷ . Below, we use these quantities to construct a prediction-powered confidence interval for θ∗ = EQY
[ν(Y )].
Theorem S3 (Label shift). Let the unlabeled data distribution be a label shift of the labeled data distribution. Fix α ∈ (0, 1) and δ ∈ (0, α). Let
CPP α =
( EQ̂Y
[ν(Y )]±
( max
l,k∈[K] max p∈Cl,k
|K̂l,k − p|+ √
1
2N log
2
α− δ
)) ,
where
Cl,k =
{ p : n(k)K̂l,k ∈
[ F−1 Binom(n(k),p)
( δ
2K2
) , F−1
Binom(n(k),p)
( 1− δ
2K2
)]} and FBinom(n(k),p) denotes the Binomial CDF. Then,
P (θ∗ ∈ CPP α ) ≥ 1− α.
Naturally, the confidence interval becomes more conservative as the number of classes grows. Also, the power of the bound depends on the smallest number of instances observed for a particular class.
Proof. Notice that we can write EQY [ν(Y )] = ν⊤QY , where on the right-hand side we are treating ν = (ν(1), . . . , ν(K))
and QY = (QY (1), . . . ,QY (K)) as vectors of length K. We can write similar expressions for QŶ , Q̂Y , etc. Using this notation, by triangle inequality we have
|θ∗ − ν⊤Q̂Y | = |ν⊤QY − ν⊤Q̂Y | ≤ ∣∣∣ν⊤K̂−1(QŶ − Q̂Ŷ )
∣∣∣+ ∣∣∣ν⊤K−1QŶ − ν⊤K̂−1QŶ
∣∣∣ . We bound the first term using Hölder’s inequality,∣∣∣ν⊤K̂−1(QŶ − Q̂Ŷ )
∣∣∣ ≤ ∥ν⊤K̂−1∥1∥QŶ − Q̂Ŷ ∥∞.
For the second term, we write∣∣∣ν⊤K−1QŶ − ν⊤K̂−1QŶ
∣∣∣ = ∣∣∣ν⊤K̂−1(K̂ − K)K−1QŶ
∣∣∣ . In the above equation, the factor on the right, K−1QŶ , is exactly equal to QY , and thus lives on the simplex, which we denote by ∆. Using this fact and Hölder’s inequality,∣∣∣ν⊤K̂−1(K̂ − K)K−1QŶ
∣∣∣ ≤ sup q∈∆
∣∣∣ν⊤K̂−1(K̂ − K)q ∣∣∣ ≤ ∥∥∥ν⊤K̂−1
∥∥∥ 1 sup q∈∆
∥∥∥(K̂ − K)q∥∥∥ ∞
.
Next, we have sup q∈∆ ∥(K̂ − K)q∥∞ = max
k∈[K] ∥K̂k −Kk∥∞,
where Kk indexes the k-th column of K. This yields the expression∥∥∥ν⊤K̂−1 ∥∥∥ 1 sup q∈∆
∥∥∥(K̂ − K)q∥∥∥ ∞
= ∥∥∥ν⊤K̂−1
∥∥∥ 1 max k∈[K]
∥K̂k −Kk∥∞.
Putting everything together, we have
|ν⊤QY − ν⊤Q̂Y | ≤ ∥ν⊤K̂−1∥1 ( ∥QŶ − Q̂Ŷ ∥∞ + max
k∈[K] ∥K̂k −Kk∥∞
) .
Since ∥ν⊤K̂−1∥1 can be evaluated empirically, it remains to bound the distributional distances ∥QŶ − Q̂Ŷ ∥∞ and maxk∈[K] ∥K̂k −Kk∥∞.
For the first distance, ∥QŶ − Q̂Ŷ ∥∞, we can simply apply the DKWM inequality (34, 35), which gives
∥QŶ − Q̂Ŷ ∥∞ ≤ √
2
N log
2
α− δ
with probability 1− (α− δ). See (36) for details.
For the second term, maxk∈[K] ∥K̂k − Kk∥∞, since we only have n observations for estimation, we use a more adaptive concentration result. In particular, for each l, k ∈ [K], n(k)K̂l,k (conditional on the k-th column) follows a binomial distribution with n(k) draws and success probability Kl,k. Therefore, if we let
Cl,k =
{ p : n(k)K̂l,k ∈
( F−1 Binom(n(k),p)
( δ
2K2
) , F−1
Binom(n(k),p)
( 1− δ
2K2
))} ,
where FBinom(n(k),p) denotes the Binomial CDF, then by a union bound:
P
( max k∈[K]
∥K̂k −Kk∥∞ ≥ max l,k∈[K]
max p∈Cl,k
|K̂l,k − p| ) ≤ δ.
Combining the last three inequalities yields the final result.
Extensions Beyond Convex Estimation The tools developed previously were tailored to unconstrained convex optimization problems. More specifically, they relied on the property given by equation (S1). In general, however, inferential targets can be defined in terms of nonconvex losses or they may have (possibly even nonconvex) constraints. For such general optimization problems, we cannot expect the condition (S1) to hold. In this section we generalize our approach to a broad class of risk minimizers:
θ∗ = argmin θ∈Θ
E[Lθ(Xi, Yi)], (S4)
where Lθ : X × Y → R is a possibly nonconvex loss function and Θ is an arbitrary set of admissible parameters. As before, if θ∗ is not a unique minimizer, our method will return a set that contains all minimizers. We note that, technically, the approach in Algorithms S1-S6 is valid even for nonconvex problems as long as we know that condition (S1) holds; e.g., if the loss is differentiable and the optimization is unconstrained. However, even then the set of points satisfying the condition may be too large and thus the returned confidence sets could be large as well if the optimization problem does not have a unique minimizer.
The problem (S4) subsumes all previously studied settings. Indeed, when the loss Lθ is convex and subdifferentiable and Θ = Rp for some p—which is the case for all problems previously studied—θ∗ can be equivalently
characterized via the condition (S1). In this section we provide a solution that can handle problems of the form (S4) in full generality. For concreteness, we provide an analogue of the previous nonasymptotic result, however one can analogously derive an analogue of the asymptotic statement. We note that the solution does not reduce to the one in Algorithms S1-S6 for convex estimation problems, and we expect the methods from Algorithms S1-S6 to be more powerful for convex estimation problems with low-dimensional rectifiers.
We rely on the following population-level measure of fit and rectifier:
m̄θ = E[Lθ(Xi, Ŷi)]; ∆̄θ = E [ Lθ(Xi, Yi)− Lθ(Xi, Ŷi)
] . (1)
Notice that the rectifier (1) is always one-dimensional, while previously the rectifier was p-dimensional.
One key difference relative to the approach designed for convex problems is that we have an additional step of data splitting. We need the additional step because, unlike in convex estimation where we know E[∇Lθ∗(Xi, Yi)] = 0, for general problems we do not know the value of E[Lθ∗(Xi, Yi)]. To circumvent this issue, we estimate E[Lθ∗(Xi, Yi)] by approximating θ∗ with an imputed estimate on the first N/2 unlabeled data points (for simplicity, take N to be even). To state the main result, we define
θ̂ = argmin θ∈Θ
2
N
N/2∑ i=1
Lθ(X ′ i, Ŷ
′ i ), LŶ
θ := 2
N
N∑ i=N/2+1
Lθ(X ′ i, Ŷ
′ i ).
Theorem S4 (General risk minimization). Let the labeled and unlabeled data be sampled i.i.d.. Fix α ∈ (0, 1) and δ ∈ (0, α). Suppose that, for any θ ∈ Θ, we can construct (Rl
θ(δ/2),Ru θ (δ/2)) and
( T l θ
( α−δ 2
) , T u
θ
( α−δ 2
)) such
that
P ( ∆̄θ ≤ Ru
θ (δ/2) ) ≥ 1− δ/2; P
( ∆̄θ ≥ Rl
θ(δ/2) ) ≥ 1− δ/2;
P
( LŶ θ − m̄θ ≤ T u
θ
( α− δ
2
)) ≥ 1− α− δ
2 ; P
( LŶ θ − m̄θ ≥ T l
θ
( α− δ
2
)) ≥ 1− α− δ
2 .
Let
CPP α =
{ θ ∈ Θ : LŶ
θ ≤ LŶ θ̂ −Rl
θ
( δ
2
) +Ru
θ̂
( δ
2
) + T u
θ
( α− δ
2
) − T l
θ̂
( α− δ
2
)} .
Then, we have P ( θ∗ ∈ CPP
α
) ≥ 1− α.
For example, if the loss Lθ(x, y) takes values in [0, B] for all x, y, then we can set Tθ(α− δ) = B √
log(1/(α−δ)) N . The
validity of this choice follows by Hoeffding’s inequality.
Proof. Define L̄θ = E[ℓθ(Xi, Yi)], L̄Ŷ
θ = E[Lθ(Xi, Ŷi)].
By the definition of θ∗, we have
LŶ θ∗ = (LŶ
θ∗ − L̄θ∗) + (L̄θ∗ − L̄θ̂) + (L̄θ̂ − LŶ θ̂ ) + LŶ
θ̂
≤ (LŶ θ∗ − L̄θ∗) + (L̄θ̂ − LŶ
θ̂ ) + LŶ
θ̂ .
By applying the validity of the confidence bounds, a union bound implies that with probability 1− α we have
LŶ θ∗ ≤ (L̄Ŷ
θ∗ − L̄θ∗) + (L̄θ̂ − L̄Ŷ θ̂ ) + LŶ
θ̂ + T u
θ∗
( α− δ
2
) − T l
θ̂
( α− δ
2
) = −∆̄θ∗ + ∆̄θ̂ + LŶ
θ̂ + T u
θ∗
( α− δ
2
) − T l
θ̂
( α− δ
2
) ≤ −Rl
θ∗(δ/2) +Ru θ̂ (δ/2) + LŶ
θ̂ + T u
θ∗
( α− δ
2
) − T l
θ̂
( α− δ
2
) .
Therefore, with probability 1− α we have that θ∗ ∈ CPP α , as desired.
Mode estimation. A commonplace inference task that does not fall under convex estimation is the problem of estimating the mode of the outcome distribution. When the outcome takes values in a discrete set Θ, this can be done by using the loss function Lθ(y) = 1 {y ̸= θ} , θ ∈ Θ. A generalization of this approach to continuous outcome distributions is obtained by defining the loss Lθ(y) = 1 {|y − θ| > η}, for some width parameter η > 0. The target of inference is thus the point θ ∈ R that has the most probability mass in its η-neighborhood, θ∗ = argminθ∈R P (|Yi − θ| > η). Theorem 4 applies directly in both the discrete and continuous cases.
Tukey’s biweight robust mean. The Tukey biweight loss function is a commonly used loss in robust statistics that results in an outlier-robust mean estimate. It behaves approximately like a quadratic near the origin and is constant far away from the origin. Formally, Tukey’s biweight loss function is given by
Lθ(y) =
 c2
6
( 1−
( 1− (y−θ)2
c2
)3) , |y − θ| ≤ c,
c2
6 , otherwise,
where c is a user-specified tuning parameter. It is not hard to see that the function Lθ(y) is nonconvex and hence not amenable to the initial analysis; however, Theorem 4 applies.
Model selection. Nonconvex risk minimization problems are ubiquitous in model selection. For example, a common model selection strategy is best subset selection, which optimizes the squared loss, Lθ(x, y) = (y− x⊤θ)2, subject to the constraint Θ = {θ ∈ Rd : ∥θ∥0 ≤ k}. Here, Θ is the space of all k-sparse vectors for a user-chosen parameter k. Even though the loss function is convex, Θ is a nonconvex constraint set and hence we cannot rely on the condition (S1) to find the minimizer. However, Theorem 4 still applies.
Inference on a Finite Population The techniques developed in this paper directly translate to the finite-population setting. Here, we treat (X ′, Y ′) as a fixed finite population consisting of N feature-outcome pairs, without imposing any distributional assumptions on the data points. Analogously to the i.i.d. setting, we observe all features X ′ and a small set of outcomes. Specifically, we assume that we observe (Y ′
i )i∈I , where I = {i1, . . . , in} is a uniformly sampled subset of [N ] of size n≪ N . In this section we adapt all our main results to the finite-population context.
Given a loss function Lθ and parameter space Θ, the target estimand is the risk minimizer we would compute if we could observe the whole population:
θ∗ = argmin θ∈Θ
1
N
N∑ i=1
Lθ(X ′ i, Y
′ i ). (2)
The following results mirror the results for convex estimation. All results in this section are proved essentially identically as their i.i.d. counterparts.
In what follows, we construct prediction-powered confidence sets CPP α assuming a valid confidence set around
the rectifier (defined below for the finite-population context). The confidence set for the rectifier can be constructed from (X ′
i, Y ′ i )i∈I via a direct application of off-the-shelf results: in Proposition S4 we state an asymptotically valid
interval for the mean based on a finite-population version of the central limit theorem, and in Proposition S3 we state a nonasymptotically valid interval for the mean for finite populations due to Waudby-Smith and Ramdas (32). The only assumption required to apply the latter is that∇Lθ(X
′ i, Y
′ i )−∇Lθ(X
′ i, Ŷ
′ i ) has a known bound valid for all i ∈ [N ].
In the finite-population setting, the mild nondegeneracy condition ensured by convexity takes the form
1
N
N∑ i=1
∇Lθ∗(X ′ i, Y
′ i ) = 0, (3)
where∇Lθ is a subgradient of Lθ. The population-level rectifier is thus:
∆̄θ = 1
N
N∑ i=1
( ∇Lθ(X
′ i, Y
′ i )−∇Lθ(X
′ i, Ŷ
′ i ) ) .
Theorem S 5 (Convex estimation, finite population). Let the labeled data be sampled uniformly at random from a finite population. Suppose that the convex estimation problem is nondegenerate (3). Fix α ∈ (0, 1). Suppose that, for any θ ∈ Rp, we can constructRθ(α) satisfying
P ( ∆̄θ ∈ Rθ(α)
) ≥ 1− α.
Let CPP α =
{ θ : − 1
N
∑N i=1∇Lθ(X
′ i, Ŷ
′ i ) ∈ Rθ(α)
} . Then,
P (θ∗ ∈ CPP α ) ≥ 1− α.
We apply Theorem S5 in the context of mean estimation, quantile estimation, logistic regression, and linear regression. The target estimand θ∗ is defined as in (2) with the loss function chosen appropriately. We remark that, just like in the i.i.d. case, the analysis for linear regression follows a more refined approach, as in the proof of Corollary S3.
Corollary S14 (Mean estimation, finite population). Let θ∗ be the mean outcome. Fix α ∈ (0, 1). Suppose that, for any θ ∈ R, we can construct an interval (Rl(α),Ru(α)) such that P
( ∆̄ ∈ (Rl(α),Ru(α))
) ≥ 1− α, where
∆̄ = 1
N
N∑ i=1
( Ŷ ′ i − Y ′
i
) .
Let
CPP α =
( 1
N
N∑ i=1
Ŷ ′ i −Ru(α),
1
N
N∑ i=1
Ŷ ′ i −Rl(α)
) .
Then, P ( θ∗ ∈ CPP
α
) ≥ 1− α.
Corollary S15 (Quantile estimation, finite population). Let θ∗ be the q-quantile. Fix α ∈ (0, 1). Suppose that, for any θ ∈ R, we can construct an interval (Rl
θ(α),Ru θ (α)) such that P
( ∆̄θ ∈ (Rl
θ(α),Ru θ (α))
) ≥ 1− α, where
∆̄θ = 1
N
N∑ i=1
( 1 {Y ′
i ≤ θ} − 1 { Ŷ ′ i ≤ θ
}) .
Let
CPP α =
{ θ ∈ R :
1
N
N∑ i=1
1
{ Ŷ ′ i ≤ θ
} ∈ ( q −Ru
θ (α), q −Rl θ(α)
)} .
Then, P ( θ∗ ∈ CPP
α
) ≥ 1− α.
Corollary S16 (Linear regression, finite population). Let θ∗ be the linear regression solution. Fix α ∈ (0, 1). Suppose that we can constructRl(α),Ru(α) ∈ Rd such that P (∆̄j ∈ (Rl
j(α),Ru j (α)),∀j ∈ [d]) ≥ 1− α, where
∆̄ = X ′†(Ŷ ′ − Y ′).
Let CPP α =
( X ′†Ŷ ′ −Ru(α), X ′†Ŷ ′ −Rl(α)
) .
Then, P (θ∗ ∈ CPP
α ) ≥ 1− α.
Corollary S 17 (Logistic regression, finite population). Let θ∗ be the logistic regression solution. Fix α ∈ (0, 1). Suppose that we can constructRl(α),Ru(α) ∈ Rd such that P (∆̄j ∈ (Rl
j(α),Ru j (α)),∀j ∈ [d]) ≥ 1− α, where
∆̄ = 1
N
N∑ i=1
X ′ i(Ŷ
′ i − Y ′
i ).
Let
CPP α =
{ θ ∈ Rd :
1
N
N∑ i=1
X ′ i,j
( Ŷ ′ i −
1
1 + exp(−θ⊤X ′ i)
) ∈ ( Rl
j(α),Ru j (α)
) ,∀j ∈ [d]
} .
Then, P (θ∗ ∈ CPP
α ) ≥ 1− α.
Confidence Intervals for the Mean We give an overview of off-the-shelf confidence intervals for the mean. We state the results for two observation models: first for the i.i.d. sampling model considered in the main body and then for the finite-population setting discussed in the SM. In both cases, we provide a construction with nonasymptotic guarantees and one with asymptotic guarantees.
For the nonasymptotic confidence intervals, we rely on the results of Waudby-Smith and Ramdas (32), specifically their Theorem 3 and Theorem 4. We opt for these results because of their strong practical performance, which is primarily driven by variance adaptivity. These results assume that the observed random variables are bounded within a known interval. Without loss of generality we assume that the observations are bounded in [0, 1] (otherwise we can always normalize the observations to [0, 1]).
For the asymptotic confidence intervals, we rely on the central limit theorem (CLT) and its variant for sampling without replacement; see (37, 38) for classical references.
Inference with i.i.d. Samples
In the following two results, assume that we observe Z1, . . . , Zn i.i.d.∼ P and let µ = E[Z1].
Proposition S1 (Nonasymptotic CI: Theorem 3 in (32)). Assume supp(P) ⊆ [0, 1]. Let
µ̂t = 0.5 +
∑t j=1 Zj
t+ 1 , σ̂2
t = 0.25 +
∑t j=1(Zj − µ̂t)
2
t+ 1 , λt =
√ 2 log(2/α)
nσ̂2 t−1
.
For every m ∈ [0, 1], define the supermartingale:
Mt(m) = 1
2 max
 t∏
j=1
( 1 + min
( λj ,
0.5
m
) (Zj −m)
) ,
t∏ j=1
( 1−min
( λj ,
0.5
1−m
) (Zj −m)
) .
Let
C = n⋂
t=1
{m ∈ [0, 1] : Mt(m) < 1/α} .
Then, P (µ ∈ C) ≥ 1− α.
Intuitively, the supermartingale Mt(m) should be thought of as the amount of evidence against m being the true mean. That is, Mt(m) being big suggests that m is unlikely to be the true mean, so the final confidence set is the collection of all m for which the amount of such evidence is small.
For large n, computing the intersection in the definition of C can be intractable, so we conservatively choose a subsequence of 1, . . . , n for the computation.
Proposition S2 (Asymptotic CI: CLT interval). Assume P has a finite second moment. Let
C =
( 1
n
n∑ i=1
Zi ± z1−α/2 σ̂√ n
) ,
where σ̂ = √
1 n
∑n i=1(Zi − 1
n
∑n j=1 Zj)2. Then,
lim inf n→∞
P (µ ∈ C) ≥ 1− α.
Inference on a Finite Population In the following two results, we assume that there exists a fixed sequence Z1, . . . , ZN , and we observe {Zi : i ∈ I}, where I = {i1, . . . , in} is a uniform random subset of [N ] with cardinality n. We let µ = 1
N
∑N i=1 Zi. For the
asymptotic result, we assume that Z1, . . . , ZN is the first N entries of an infinite underlying sequence Z1, Z2, . . . .
Proposition S3 (Nonasymptotic CI: Theorem 4 in (32)). Assume Zi ∈ [0, 1], i ∈ [N ]. Let
µ̂t = 0.5 +
∑t j=1 Zij
t+ 1 , σ̂2
t = 0.25 +
∑t j=1(Zij − µ̂t)
2
t+ 1 , λt =
√ 2 log(2/α)
nσ̂2 t−1
.
For every m ∈ [0, 1], define the supermartingale:
Mt(m) = 1
2 max
 t∏
j=1
( 1 + min
( λj ,
0.5
µt(m)
) (Zij − µt(m))
) ,
t∏ j=1
( 1−min
( λj ,
0.5
1− µt(m)
) (Zij − µt(m))
) ,
where µt(m) = Nm−
∑t−1 j=1 Zij
N−t+1 is the putative mean. Let
C = n⋂
t=1
{m ∈ [0, 1] : Mt(m) < 1/α} .
Then, P (µ ∈ C) ≥ 1− α.
Proposition S4 (Asymptotic CI: CLT for sampling without replacement). Let σ2 = 1 N
∑N i=1(Zi − µ)2, and σ̂2 =
1 n
∑ i∈I(Zi − µ̂)2. Assume that µ and σ have a limit and that n/N → p for some p ∈ (0, 1). Let
C =
( 1
n
∑ i∈I
Zi ± z1−α/2 σ̂√ n
√ N − n
N
) .
Then, lim inf n,N→∞
P (µ ∈ C) ≥ 1− α.
Further Experimental Particulars Relating Protein Structure and Post-Translational Modifications The predictive model of whether a sequence position is in an IDR, f , is a logistic regression model that maps the relative solvent-accessible surface area (RSA) of each position, computed based on the AlphaFold-predicted structure using Bio.PDB (39), to a probability that the position is in an IDR. Following Bludau et al. (3), the RSA was locally smoothed with a window of 5, 10, 15, 20, 25, 30, or 35 amino acids, and a sigmoid function was used to predict disorder from this smoothed RSA quantity. To fit the sigmoid, we used the data in (3) that had disorder labels but no PTM labels. The smoothing window size used for the final model was the value that resulted in the lowest variance of the bias, Y − f , on this data.
Galaxy Classification We fine-tune a ResNet50 (40) on the training split of the Galaxy Zoo 2 data with a batch size of 32 and a learning rate of 0.0001 using Adam (41). We tune the entire backbone, not just the last layer. We use the remaining validation split as our labeled and unlabeled data, taking n = [50, 100, 200, 300, 500, 750, 1000]. We use Algorithm S1 for the naive prediction-powered approach, and Proposition S2 for the classical and imputation approaches.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-bfoc0zoEOLSrGRac_0N3J1AnuQXsJFiyXwnm01Orq4FkJNJH5rXE6oG0vvCCcF8yV5GP8M0UCQsu_GZitYw5S5rfUSEue57nmowBAK3A26g0gZ3RHVYtFTkEvuimpmDvrkLMnxA=w984-h535-v0?authuser=0)

Distribution of Gene Expression Levels We used the transformer model developed and trained by Vaishnav et al. (11) to predict gene expression level, with the following modification that we found improved predictive performance. Given n labeled data points, five were randomly selected and used to train an affine (two-parameter) function mapping the scalar prediction of the transformer in (11) to a prediction of the conditional median of the label, using quantile regression. The predictions of this final model were used for the unlabeled dataset, and the remaining n − 5 data points that weren’t used to fine-tune the transformer model were used as the labeled dataset. We use Algorithm S3 to form the prediction-powered confidence intervals and the standard quantile CLT confidence interval for the classical and imputation approaches. Results analogous to Fig. 2C in the main text for the 0.25- and 0.75-quantiles are plotted in Fig. S6.
1.5 2.0 2.5 3.0
0.25-quantile gene expression
0 500 1000 1500 2000
n
0.5
1.0
1.5
2.0
2.5
w id
th
10 11 12
0.75-quantile gene expression
0 500 1000 1500 2000
n
0
1
2
3
4
5
w id
th
imputed
prediction-powered
classical
ground truth
Figure S6: Confidence intervals on gene expression quantiles for q = 0.25 (top) and q = 0.75 (bottom). Following Fig. 2 in the main text, the left panel shows prediction-powered (green) and classical (gray) confidence intervals computed with five random splits of labeled and unlabeled data. The right panel shows the average interval width for varying values of n, the number of labeled data points, as well as the width for five randomly chosen trials.
Estimating Deforestation in the Amazon The machine-learning model given by (13) outputs forest-cover predictions at 30m resolution for 3192 data points. We correspond these by latitude and longitude with gold-standard data points labeled as one of {deforestation, no deforestation} from (12). In the first step, we split off half of the data to train a histogram-based gradientboosted tree to predict deforestation labels from the forest-cover predictions. We take a random sample of n = 100 data points as the gold-standard data, and try to cover the true fraction of deforestation events on the N = 1596 remaining data points. We use Algorithm S1 to produce the prediction-powered confidence interval and Proposition S2 for the classical and imputation approaches.
Relationship Between Income and Private Health Insurance We train a gradient-boosted tree (15) on the California Census data from 2018 acquired using the Folktables (14) interface. The boosted tree takes as input several covariates such as income, race, and sex, to predict whether an individual has private health insurance coverage. In the new year, 2019, we use n = [200, 300, 500, 1000, 2000, 5000, 10000] labeled data points. We use Algorithm S5 to produce the prediction-powered confidence interval and the standard CLT confidence interval for the classical and imputation approaches.
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8nQmS54eP-KRvqlt2_g1gwis7bIomZHgm-JZV4m-KgkdAO2sHmV8SdXZqGRtEWWlKOFnZ8nNB9PXWDFfyFFlTrsxUSsW1F17bd5dCiwDMTdYuHvJAhy-cnpVy235RYVORNkLRc2Q=w362-h285-v0?authuser=0)

Relationship Between Age and Income The setting is the same as the above experiment on income and private health insurance, the main difference being that income is used as the target, and not as a covariate. We used Algorithm S4 to produce the prediction-powered confidence interval and the standard CLT confidence interval for the classical and imputation approaches.
Counting Plankton We fine-tune a ResNet152 (40) on the WHOI-Plankton dataset (17) in the years 2006-2013 for two epochs with a batch size of 32 and a learning rate of 0.0001 using AdamW (42), with 5% of the data saved for validation. We tune the entire backbone, not just the last layer. Then we test in the year 2014, using all available data. We use Theorem S3 to produce the prediction-powered intervals and Proposition S2 for the imputation approach.
Related Work This section expands the discussion of related work from the main body of the paper. Thematically, prediction-powered inference is most similar to the work of Wang et al. (18), who also introduce a method to correct machine-learning predictions for the purpose of subsequent inference. However, prediction-powered inference provides provably valid conclusions under minimal assumptions about the data-generating distribution, whereas the procedure of Wang et al. does not provide coverage in general and requires strong assumptions about the relationship between the prediction model and the true response. We compare against this baseline in “Comparison to Baseline Procedures” in the SM.
The technical results of this paper generalize tools from the model-assisted survey sampling literature (43), which provides methods to improve inference from surveys in the presence of auxiliary information. In particular, the prediction-powered mean estimator is the difference estimator, closely related to generalized regression estimators (44). It has long been recognized that model predictions can be leveraged as auxiliary data (45), and much work has gone into producing asymptotically valid confidence intervals when the predictive model is fit on the same data that is used for inference—see (46) for a recent overview. Prediction-powered inference is also related to the statistical literature on semiparametric inference, missing data, and multiple imputation (47). In particular, (48-51) study regression with missing data. The rectifier resembles debiasing strategies that are pervasive in this literature, an example being the AIPW estimator (49). Likewise, prediction-powered inference is related to measurement error (e.g., 52, 53). Prediction-powered inference aims to provide simple, broadly applicable algorithms using similar debiasing tricks, while allowing the use of state-of-the-art black-box machine-learning systems.
There has been an increasing a body of work on estimation with many unlabeled data points and few labeled data points (19-22), focusing on efficiency in semiparametric or high-dimensional regimes. In particular, Chakrabortty and Cai (23), Deng et al. (25), and Azriel et al. (26) study efficient estimation of linear regression parameters, Chakrabortty et al. (27) study efficient quantile estimation, and Zhang and Bradic (24) study mean estimation in a high-dimensional setting. Finally, Song et al. (55) study M-estimation, using a projection-based correction to the classical M-estimator loss based on simple statistics (e.g. low-order polynomials) of the features. Prediction-powered inference continues in this vein but focuses on the setting where the scientist has access to a good predictive model fit on separate data and makes no assumptions about the model (such as consistency). The confidence intervals and resulting p-values from previous work rely on asymptotic approximations, while prediction-powered inference has both asymptotic and nonasymptotic variants. Furthermore, prediction-powered inference goes beyond random sampling and considers certain forms of distribution shift.
More distantly, the setting of prediction-powered inference, in which the scientist has access to some labeled data alongside unlabeled data, also appears in semi-supervised learning (54)—this literature studies the question of how to improve prediction accuracy with unlabeled data. Even further along is the literature on transfer learning, wherein estimation rates improve with access to out-of-distribution data; a similar debiasing technique also appears there (56).
Prediction-powered inference is conceptually related to conformal prediction (28). Both methodologies leverage a predictive model and a labeled dataset. From this point on, the two methods diverge: prediction-powered inference has additional unlabeled data and gives a confidence set that contains a population-level quantity such as the mean outcome; conformal prediction gives a confidence set for a test instance that contains the true label. These are two distinct goals, and neither method can be applied straightforwardly to solve the objective of the other.
**References and Notes**
1. J. Jumper, R. Evans, A. Pritzel, T. Green, M. Figurnov, O. Ronneberger, K. Tunyasuvunakool,
R. Bates, A. Žídek, A. Potapenko, A. Bridgland, C. Meyer, S. A. A. Kohl, A. J. Ballard,
A. Cowie, B. Romera-Paredes, S. Nikolov, R. Jain, J. Adler, T. Back, S. Petersen, D.
Reiman, E. Clancy, M. Zielinski, M. Steinegger, M. Pacholska, T. Berghammer, S.
Bodenstein, D. Silver, O. Vinyals, A. W. Senior, K. Kavukcuoglu, P. Kohli, D. Hassabis,
**Highly accurate protein structure prediction with AlphaFold. Nature 596, 583–589**
(2021). doi:10.1038/s41586-021-03819-2 Medline
2. K. Tunyasuvunakool, J. Adler, Z. Wu, T. Green, M. Zielinski, A. Žídek, A. Bridgland, A.
Cowie, C. Meyer, A. Laydon, S. Velankar, G. J. Kleywegt, A. Bateman, R. Evans, A.
Pritzel, M. Figurnov, O. Ronneberger, R. Bates, S. A. A. Kohl, A. Potapenko, A. J.
Ballard, B. Romera-Paredes, S. Nikolov, R. Jain, E. Clancy, D. Reiman, S. Petersen, A.
W. Senior, K. Kavukcuoglu, E. Birney, P. Kohli, J. Jumper, D. Hassabis, Highly accurate
**protein structure prediction for the human proteome. Nature 596, 590–596 (2021).**
doi:10.1038/s41586-021-03828-1 Medline
3. I. Bludau, S. Willems, W.-F. Zeng, M. T. Strauss, F. M. Hansen, M. C. Tanzer, O. Karayel, B.
A. Schulman, M. Mann, The structural context of posttranslational modifications at a
**proteome-wide scale. PLOS Biol. 20, e3001636 (2022).**
doi:10.1371/journal.pbio.3001636 Medline
4. I. Barrio-Hernandez, J. Yeo, J. Jänes, T. Wein, M. Varadi, S. Velankar, P. Beltrao, M.
Steinegger, Clustering predicted structures at the scale of the known protein universe.
**bioRxiv 2023-03 (2023).**
5. A. N. Angelopoulos, S. Bates, C. Fannjiang, M. I. Jordan, T. Zrnic, ppi-py: A Python package
for scientific discovery using machine learning, Zenodo (2023);
https://doi.org/10.5281/zenodo.8403931.
6. A. N. Angelopoulos, S. Bates, C. Fannjiang, M. I. Jordan, T. Zrnic, Prediction-Powered
Inference: Data Sets, Zenodo (2023); https://doi.org/10.5281/zenodo.8397451.
7. L. M. Iakoucheva, P. Radivojac, C. J. Brown, T. R. O’Connor, J. G. Sikes, Z. Obradovic, A.
*K. Dunker, The importance of intrinsic disorder for protein phosphorylation. Nucleic*
**Acids Res. 32, 1037–1049 (2004). doi:10.1093/nar/gkh253 Medline**
**8. UniProt Consortium, UniProt: A hub for protein information. Nucleic Acids Res. 43, D204–**
D212 (2015). doi:10.1093/nar/gku989 Medline
9. K. W. Willett, C. J. Lintott, S. P. Bamford, K. L. Masters, B. D. Simmons, K. R. V. Casteels,
E. M. Edmondson, L. F. Fortson, S. Kaviraj, W. C. Keel, T. Melvin, R. C. Nichol, M. J.
Raddick, K. Schawinski, R. J. Simpson, R. A. Skibba, A. M. Smith, D. Thomas, Galaxy
Zoo 2: Detailed morphological classifications for 304 122 galaxies from the Sloan Digital
**Sky Survey. Mon. Not. R. Astron. Soc. 435, 2835–2860 (2013).**
doi:10.1093/mnras/stt1458
10. D. G. York, J. Adelman, J. E. Anderson Jr., S. F. Anderson, J. Annis, N. A. Bahcall, J. A.
Bakken, R. Barkhouser, S. Bastian, E. Berman, W. N. Boroski, S. Bracker, C. Briegel, J.
W. Briggs, J. Brinkmann, R. Brunner, S. Burles, L. Carey, M. A. Carr, F. J. Castander, B.
Chen, P. L. Colestock, A. J. Connolly, J. H. Crocker, I. Csabai, P. C. Czarapata, J. E.
Davis, M. Doi, T. Dombeck, D. Eisenstein, N. Ellman, B. R. Elms, M. L. Evans, X. Fan,
G. R. Federwitz, L. Fiscelli, S. Friedman, J. A. Frieman, M. Fukugita, B. Gillespie, J. E.
Gunn, V. K. Gurbani, E. de Haas, M. Haldeman, F. H. Harris, J. Hayes, T. M. Heckman,
G. S. Hennessy, R. B. Hindsley, S. Holm, D. J. Holmgren, C. Huang, C. Hull, D. Husby,
S.-I. Ichikawa, T. Ichikawa, Ž. Ivezić, S. Kent, R. S. J. Kim, E. Kinney, M. Klaene, A. N.
Kleinman, S. Kleinman, G. R. Knapp, J. Korienek, R. G. Kron, P. Z. Kunszt, D. Q.
Lamb, B. Lee, R. F. Leger, S. Limmongkol, C. Lindenmeyer, D. C. Long, C. Loomis, J.
Loveday, R. Lucinio, R. H. Lupton, B. MacKinnon, E. J. Mannery, P. M. Mantsch, B.
Margon, P. McGehee, T. A. McKay, A. Meiksin, A. Merelli, D. G. Monet, J. A. Munn,
V. K. Narayanan, T. Nash, E. Neilsen, R. Neswold, H. J. Newberg, R. C. Nichol, T.
Nicinski, M. Nonino, N. Okada, S. Okamura, J. P. Ostriker, R. Owen, A. G. Pauls, J.
Peoples, R. L. Peterson, D. Petravick, J. R. Pier, A. Pope, R. Pordes, A. Prosapio, R.
Rechenmacher, T. R. Quinn, G. T. Richards, M. W. Richmond, C. H. Rivetta, C. M.
Rockosi, K. Ruthmansdorfer, D. Sandford, D. J. Schlegel, D. P. Schneider, M. Sekiguchi,
G. Sergey, K. Shimasaku, W. A. Siegmund, S. Smee, J. A. Smith, S. Snedden, R. Stone,
C. Stoughton, M. A. Strauss, C. Stubbs, M. SubbaRao, A. S. Szalay, I. Szapudi, G. P.
Szokoly, A. R. Thakar, C. Tremonti, D. L. Tucker, A. Uomoto, D. Vanden Berk, M. S.
Vogeley, P. Waddell, S. Wang, M. Watanabe, D. H. Weinberg, B. Yanny, N. Yasuda, N.
**Yasuda, The Sloan digital sky survey: Technical summary. Astron. J. 120, 1579–1587**
(2000). doi:10.1086/301513
11. E. D. Vaishnav, C. G. de Boer, J. Molinet, M. Yassour, L. Fan, X. Adiconis, D. A.
Thompson, J. Z. Levin, F. A. Cubillos, A. Regev, The evolution, evolvability and
**engineering of gene regulatory DNA. Nature 603, 455–463 (2022). doi:10.1038/s41586-**
022-04506-6 Medline
12. E. L. Bullock, C. E. Woodcock, C. Souza Jr., P. Olofsson, Satellite-based estimates reveal
**widespread forest degradation in the Amazon. Glob. Chang. Biol. 26, 2956–2969 (2020).**
doi:10.1111/gcb.15029 Medline
13. J. O. Sexton, J. X.-P. Song, M. Feng, P. Noojipady, A. Anand, C. Huang, D.-H. Kim, K. M.
Collins, S. Channan, C. DiMiceli, J. R. Townshend, Global, 30-m resolution continuous
fields of tree cover: Landsat-based rescaling of MODIS vegetation continuous fields with
**lidar-based estimates of error. Int. J. Digit. Earth 6, 427–448 (2013).**
doi:10.1080/17538947.2013.786146
14. F. Ding, M. Hardt, J. Miller, L. Schmidt, “Retiring adult: New datasets for fair machine
**learning” in Advances in Neural Information Processing Systems 34 (2021), pp. 6478–**
6490.
*15. T. Chen, C. Guestrin, “XGBoost: A scalable tree boosting system” in Proceedings of the*
*22nd ACM SIGKDD International Conference on Knowledge Discovery and Data*
*Mining (2016), pp. 785–794.*
16. R. J. Olson, A. Shalapyonok, H. M. Sosik, An automated submersible flow cytometer for
*analyzing pico-and nanophytoplankton: FlowCytobot. Deep Sea Res. Part I Oceanogr.*
**Res. Pap. 50, 301–315 (2003). doi:10.1016/S0967-0637(03)00003-7**
17. E. C. Orenstein, O. Beijbom, E. E. Peacock, H. M. Sosik, WHOI-Plankton- A large scale fine
grained visual recognition benchmark dataset for plankton classification.
arXiv:1510.00745 [cs.CV] (2015).
18. S. Wang, T. H. McCormick, J. T. Leek, Methods for correcting inference based on outcomes
**predicted by machine learning. Proc. Natl. Acad. Sci. U.S.A. 117, 30266–30275 (2020).**
doi:10.1073/pnas.2001238117 Medline
**19. M. S. Pepe, Inference using surrogate outcome data and a validation sample. Biometrika 79,**
355–365 (1992). doi:10.1093/biomet/79.2.355
*20. J. Lafferty, L. Wasserman, “Statistical analysis of semi-supervised regression” in Advances*
**in Neural Information Processing Systems 20 (2007), pp. 801–808.**
21. A. Zhang, L. D. Brown, T. T. Cai, Semi-supervised inference: General theory and estimation
**of means. Ann. Stat. 47, 2538–2566 (2019). doi:10.1214/18-AOS1756**
22. A. Chakrabortty, G. Dai, E. Tchetgen Tchetgen, A general framework for treatment effect
estimation in semi-supervised and high dimensional settings. arXiv:2201.00468 [stat.ME]
(2022).
23. A. Chakrabortty, T. Cai, Efficient and adaptive linear regression in semi-supervised settings.
**Ann. Stat. 46, 1541–1572 (2018). doi:10.1214/17-AOS1594**
24. Y. Zhang, J. Bradic, High-dimensional semi-supervised learning: In search of optimal
**inference of the mean. Biometrika 109, 387–403 (2022). doi:10.1093/biomet/asab042**
25. S. Deng, Y. Ning, J. Zhao, H. Zhang, Optimal and safe estimation for high-dimensional
semi-supervised learning. arXiv:2011.14185 [stat.ME] (2020).
26. D. Azriel, L. D. Brown, M. Sklar, R. Berk, A. Buja, L. Zhao, Semi-supervised linear
**regression. J. Am. Stat. Assoc. 117, 2238–2251 (2022).**
doi:10.1080/01621459.2021.1915320
27. A. Chakrabortty, G. Dai, R. J. Carroll, Semi-supervised quantile estimation: robust and
efficient inference in high dimensional settings. arXiv:2201.10208 [stat.ME] (2022).
*28. V. Vovk, A. Gammerman, G. Shafer, Algorithmic Learning in a Random World (Springer,*
2005), vol. 5.
29. A. Buja, L. Brown, R. Berk, E. George, E. Pitkin, M. Traskin, K. Zhang, L. Zhao, Models as
**approximations I: Consequences illustrated with linear regression. Stat. Sci. 34, 523–544**
(2019). doi:10.1214/18-STS693
*30. H. White, Using least squares to approximate unknown regression functions. Int. Econ. Rev.*
**21, 149–170 (1980). doi:10.2307/2526245**
31. H. White, A heteroskedasticity-consistent covariance matrix estimator and a direct test for
**heteroskedasticity. Econometrica 48, 817–838 (1980). doi:10.2307/1912934**
*32. I. Waudby-Smith, A. Ramdas, Estimating means of bounded random variables by betting. J.*
*R. Stat. Soc. Series B Stat. Methodol. qkad009 (2023). doi:10.1093/jrsssb/qkad009*
33. Z. Lipton, Y.-X. Wang, A. Smola, “Detecting and correcting for label shift with black box
*predictors” in International Conference on Machine Learning (2018), pp. 3122–3130.*
34. A. Dvoretzky, J. Kiefer, J. Wolfowitz, Asymptotic minimax character of the sample
**distribution function and of the classical multinomial estimator. Ann. Math. Stat. 27, 642–**
669 (1956). doi:10.1214/aoms/1177728174
*35. P. Massart, The tight constant in the Dvoretzky-Kiefer-Wolfowitz inequality. Ann. Probab.*
**18, 1269–1283 (1990). doi:10.1214/aop/1176990746**
36. C. L. Canonne, A short note on learning discrete distributions. arXiv:2002.11457 [math.ST]
(2020).
*37. P. Erdos, On the central limit theorem for samples from a finite population. Publ Math. Inst.*
**Hung. Acad. Sci. 4, 49–61 (1959).**
**38. T. Höglund, Sampling from a finite population. A remainder term estimate. Scand. J. Stat. 5,**
69–71 (1978).
39. T. Hamelryck, B. Manderick, PDB file parser and structure class implemented in Python.
**Bioinformatics 19, 2308–2310 (2003). doi:10.1093/bioinformatics/btg299 Medline**
40. K. He, X. Zhang, S. Ren, J. Sun, “Deep residual learning for image recognition” in
*Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*
*(CVPR) (2016), pp. 770–778.*
41. D. P. Kingma, J. Ba, “Adam: A method for stochastic optimization” in International
Conference on Learning Representations (2014).
*42. I. Loshchilov, F. Hutter, “Decoupled Weight Decay Regularization” in International*
*Conference on Learning Representations (2018).*
*43. C.-E. Särndal, B. Swensson, J. Wretman, Model Assisted Survey Sampling (Springer Science*
& Business Media, 1992).
44. C. M. Cassel, C. E. Särndal, J. H. Wretman, Some results on generalized difference
**estimation and generalized regression estimation for finite populations. Biometrika 63,**
615–620 (1976). doi:10.1093/biomet/63.3.615
45. C. Wu, R. R. Sitter, A model-calibration approach to using complete auxiliary information
**from survey data. J. Am. Stat. Assoc. 96, 185–193 (2001).**
doi:10.1198/016214501750333054
46. F. J. Breidt, J. D. Opsomer, Model-assisted survey estimation with modern prediction
**techniques. Stat. Sci. 32, 190–205 (2017). doi:10.1214/16-STS589**
*47. R. J. Little, D. B. Rubin, Statistical Analysis with Missing Data (Wiley, 2019), vol. 793.*
48. J. M. Robins, A. Rotnitzky, L. P. Zhao, Estimation of regression coefficients when some
**regressors are not always observed. J. Am. Stat. Assoc. 89, 846–866 (1994).**
doi:10.1080/01621459.1994.10476818
49. J. M. Robins, A. Rotnitzky, Semiparametric efficiency in multivariate regression models with
**missing data. J. Am. Stat. Assoc. 90, 122–129 (1995).**
doi:10.1080/01621459.1995.10476494
50. J. Chen, N. E. Breslow, Semiparametric efficient estimation for the auxiliary outcome
**problem with the conditional mean model. Can. J. Stat. 32, 359–372 (2004).**
doi:10.2307/3316021
*51. M. Yu, B. Nan, A revisit of semiparametric regression models with missing data. Stat. Sin.*
**2006, 1193–1212 (2006).**
52.*R. J. Carroll, D. Ruppert, L. A. Stefanski, C. M. Crainiceanu, Measurement Error in Nonlinear Models: A Modern Perspective (Chapman and Hall/CRC, 2006).*
53.*X. Chen, H. Hong, E. Tamer, Measurement error models with auxiliary data. Rev. Econ. Stud.***72, 343–366 (2005). doi:10.1111/j.1467-937X.2005.00335.x**
54.*X. Zhu, A. B. Goldberg, Introduction to Semi-Supervised Learning, Synthesis Lectures on*Artificial Intelligence and Machine Learning, vol. 3 (2009), pp. 1–130.
55.*S. Song, Y. Lin, Y. Zhou, A general M-estimation theory in semi-supervised framework. J. Am. Stat. Assoc., 1–11 (2023). doi:10.1080/01621459.2023.2169699*
56.*Y. Tian, Y. Feng, Transfer learning under high-dimensional generalized linear models. J. Am. Stat. Assoc., 1–14 (2022). doi:10.1080/01621459.2022.2071278*