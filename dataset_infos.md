# Drug consumption (quantified) Data Set

**Source:** https://archive.ics.uci.edu/ml/datasets/Drug+consumption+(quantified)

**Abstract:** Classify type of drug consumer by personality data

## Data Set Information:

Database contains records for **1885 respondents**. For each respondent **12 attributes** are known: **Personality measurements which include NEO-FFI-R (neuroticism, extraversion, openness to experience, agreeableness, and conscientiousness), BIS-11 (impulsivity), and ImpSS (sensation seeking), level of education, age, gender, country of residence and ethnicity**. All input attributes are originally categorical and are quantified. After quantification values of all input features can be considered as real-valued. In addition, participants were questioned concerning their **use of 18 legal and illegal drugs (alcohol, amphetamines, amyl nitrite, benzodiazepine, cannabis, chocolate, cocaine, caffeine, crack, ecstasy, heroin, ketamine, legal highs, LSD, methadone, mushrooms, nicotine and volatile substance abuse (VSA) and one fictitious drug (Semeron) which was introduced to identify over-claimers**. For each drug they have to select one of the answers: never used the drug, used it over a decade ago, or in the last decade, year, month, week, or day.
Database contains 18 classification problems. Each of independent label variables contains seven classes: **"Never Used", "Used over a Decade Ago", "Used in Last Decade", "Used in Last Year", "Used in Last Month", "Used in Last Week", and "Used in Last Day".**

**Problem which can be solved:**
* Seven class classifications for each drug separately.
* Problem can be transformed to binary classification by union of part of classes into one new class. For example, "Never Used", "Used over a Decade Ago" form class "Non-user" and all other classes form class "User".
* The best binarization of classes for each attribute.
* Evaluation of risk to be drug consumer for each drug.

Detailed description of database and process of data quantification are presented in E. Fehrman, A. K. Muhammad, E. M. Mirkes, V. Egan and A. N. Gorban, "The Five Factor Model of personality and evaluation of drug consumption risk.," arXiv [Web Link], 2015
**Paper above solve binary classification problem for all drugs. For most of drugs sensitivity and specificity are greater than 75%.**

## Attribute Information:

1. ID is number of record in original database. Cannot be related to participant. It can be used for reference only.

2. Age (Real) is age of participant and has one of the values:
Value Meaning Cases Fraction
-0.95197 18-24 643 34.11%
-0.07854 25-34 481 25.52%
0.49788 35-44 356 18.89%
1.09449 45-54 294 15.60%
1.82213 55-64 93 4.93%
2.59171 65+ 18 0.95%
Descriptive statistics
Min Max Mean Std.dev.
-0.95197 2.59171 0.03461 0.87813

3. Gender (Real) is gender of participant:
Value Meaning Cases Fraction
0.48246 Female 942 49.97%
-0.48246 Male 943 50.03%
Descriptive statistics
Min Max Mean Std.dev.
-0.48246 0.48246 -0.00026 0.48246

4. Education (Real) is level of education of participant and has one of the values:
Value Meaning Cases Fraction
-2.43591 Left school before 16 years 28 1.49%
-1.73790 Left school at 16 years 99 5.25%
-1.43719 Left school at 17 years 30 1.59%
-1.22751 Left school at 18 years 100 5.31%
-0.61113 Some college or university, no certificate or degree 506 26.84%
-0.05921 Professional certificate/ diploma 270 14.32%
0.45468 University degree 480 25.46%
1.16365 Masters degree 283 15.01%
1.98437 Doctorate degree 89 4.72%
Descriptive statistics
Min Max Mean Std.dev.
-2.43591 1.98437 -0.00379 0.95004

5. Country (Real) is country of current residence of participant and has one of the values:
Value Meaning Cases Fraction
-0.09765 Australia 54 2.86%
0.24923 Canada 87 4.62%
-0.46841 New Zealand 5 0.27%
-0.28519 Other 118 6.26%
0.21128 Republic of Ireland 20 1.06%
0.96082 UK 1044 55.38%
-0.57009 USA 557 29.55%
Descriptive statistics
Min Max Mean Std.dev.
-0.57009 0.96082 0.35554 0.70015

6. Ethnicity (Real) is ethnicity of participant and has one of the values:
Value Meaning Cases Fraction
-0.50212 Asian 26 1.38%
-1.10702 Black 33 1.75%
1.90725 Mixed-Black/Asian 3 0.16%
0.12600 Mixed-White/Asian 20 1.06%
-0.22166 Mixed-White/Black 20 1.06%
0.11440 Other 63 3.34%
-0.31685 White 1720 91.25%
Descriptive statistics
Min Max Mean Std.dev.
-1.10702 1.90725 -0.30958 0.16618

7. Nscore (Real) is NEO-FFI-R Neuroticism. Possible values are presented in table below:
Nscore Cases Value Nscore Cases Value Nscore Cases Value
12 1 -3.46436 29 60 -0.67825 46 67 1.02119
13 1 -3.15735 30 61 -0.58016 47 27 1.13281
14 7 -2.75696 31 87 -0.46725 48 49 1.23461
15 4 -2.52197 32 78 -0.34799 49 40 1.37297
16 3 -2.42317 33 68 -0.24649 50 24 1.49158
17 4 -2.34360 34 76 -0.14882 51 27 1.60383
18 10 -2.21844 35 69 -0.05188 52 17 1.72012
19 16 -2.05048 36 73 0.04257 53 20 1.83990
20 24 -1.86962 37 67 0.13606 54 15 1.98437
21 31 -1.69163 38 63 0.22393 55 11 2.12700
22 26 -1.55078 39 66 0.31287 56 10 2.28554
23 29 -1.43907 40 80 0.41667 57 6 2.46262
24 35 -1.32828 41 61 0.52135 58 3 2.61139
25 56 -1.19430 42 77 0.62967 59 5 2.82196
26 57 -1.05308 43 49 0.73545 60 2 3.27393
27 65 -0.92104 44 51 0.82562
28 70 -0.79151 45 37 0.91093
Descriptive statistics
Min Max Mean Std.dev.
-3.46436 3.27393 0.00004 0.99808

8. Escore (Real) is NEO-FFI-R Extraversion. Possible values are presented in table below:
Escore Cases Value Escore Cases Value Escore Cases Value
16 2 -3.27393 31 55 -1.23177 45 91 0.80523
18 1 -3.00537 32 52 -1.09207 46 69 0.96248
19 6 -2.72827 33 77 -0.94779 47 64 1.11406
20 3 -2.53830 34 68 -0.80615 48 62 1.28610
21 3 -2.44904 35 58 -0.69509 49 37 1.45421
22 8 -2.32338 36 89 -0.57545 50 25 1.58487
23 5 -2.21069 37 90 -0.43999 51 34 1.74091
24 9 -2.11437 38 106 -0.30033 52 21 1.93886
25 4 -2.03972 39 107 -0.15487 53 15 2.12700
26 21 -1.92173 40 130 0.00332 54 10 2.32338
27 23 -1.76250 41 116 0.16767 55 9 2.57309
28 23 -1.63340 42 109 0.32197 56 2 2.85950
29 32 -1.50796 43 105 0.47617 58 1 3.00537
30 38 -1.37639 44 103 0.63779 59 2 3.27393
Descriptive statistics
Min Max Mean Std.dev.
-3.27393 3.27393 -0.00016 0.99745

9. Oscore (Real) is NEO-FFI-R Openness to experience. Possible values are presented in table below:
Oscore Cases Value Oscore Cases Value Oscore Cases Value
24 2 -3.27393 38 64 -1.11902 50 83 0.58331
26 4 -2.85950 39 60 -0.97631 51 87 0.72330
28 4 -2.63199 40 68 -0.84732 52 87 0.88309
29 11 -2.39883 41 76 -0.71727 53 81 1.06238
30 9 -2.21069 42 87 -0.58331 54 57 1.24033
31 9 -2.09015 43 86 -0.45174 55 63 1.43533
32 13 -1.97495 44 101 -0.31776 56 38 1.65653
33 23 -1.82919 45 103 -0.17779 57 34 1.88511
34 25 -1.68062 46 134 -0.01928 58 19 2.15324
35 26 -1.55521 47 107 0.14143 59 13 2.44904
36 39 -1.42424 48 116 0.29338 60 7 2.90161
37 51 -1.27553 49 98 0.44585
Descriptive statistics
Min Max Mean Std.dev.
-3.27393 2.90161 -0.00053 0.99623

10. Ascore (Real) is NEO-FFI-R Agreeableness. Possible values are presented in table below:
Ascore Cases Value Ascore Cases Value Ascore Cases Value
12 1 -3.46436 34 42 -1.34289 48 104 0.76096
16 1 -3.15735 35 45 -1.21213 49 85 0.94156
18 1 -3.00537 36 62 -1.07533 50 68 1.11406
23 1 -2.90161 37 83 -0.91699 51 58 1.2861
24 2 -2.78793 38 82 -0.76096 52 39 1.45039
25 1 -2.70172 39 102 -0.60633 53 36 1.61108
26 7 -2.53830 40 98 -0.45321 54 36 1.81866
27 7 -2.35413 41 114 -0.30172 55 16 2.03972
28 8 -2.21844 42 101 -0.15487 56 14 2.23427
29 13 -2.07848 43 105 -0.01729 57 8 2.46262
30 18 -1.92595 44 118 0.13136 58 7 2.75696
31 24 -1.77200 45 112 0.28783 59 1 3.15735
32 30 -1.62090 46 100 0.43852 60 1 3.46436
33 34 -1.47955 47 100 0.59042
Descriptive statistics
Min Max Mean Std.dev.
-3.46436 3.46436 -0.00024 0.99744

11. Cscore (Real) is NEO-FFI-R Conscientiousness. Possible values are presented in table below:
Cscore Cases Value Cscore Cases Value Cscore Cases Value
17 1 -3.46436 32 39 -1.25773 46 113 0.58489
19 1 -3.15735 33 49 -1.13788 47 95 0.7583
20 3 -2.90161 34 55 -1.01450 48 95 0.93949
21 2 -2.72827 35 55 -0.89891 49 76 1.13407
22 5 -2.57309 36 69 -0.78155 50 47 1.30612
23 5 -2.42317 37 81 -0.65253 51 43 1.46191
24 6 -2.30408 38 77 -0.52745 52 34 1.63088
25 9 -2.18109 39 87 -0.40581 53 28 1.81175
26 13 -2.04506 40 97 -0.27607 54 27 2.04506
27 13 -1.92173 41 99 -0.14277 55 13 2.33337
28 25 -1.78169 42 105 -0.00665 56 8 2.63199
29 24 -1.64101 43 90 0.12331 57 3 3.00537
30 29 -1.51840 44 111 0.25953 59 1 3.46436
31 41 -1.38502 45 111 0.41594
Descriptive statistics
Min Max Mean Std.dev.
-3.46436 3.46436 -0.00039 0.99752

12. Impulsive (Real) is impulsiveness measured by BIS-11. Possible values are presented in table below:
Impulsiveness Cases Fraction
-2.55524 20 1.06%
-1.37983 276 14.64%
-0.71126 307 16.29%
-0.21712 355 18.83%
0.19268 257 13.63%
0.52975 216 11.46%
0.88113 195 10.34%
1.29221 148 7.85%
1.86203 104 5.52%
2.90161 7 0.37%
Descriptive statistics
Min Max Mean Std.dev.
-2.55524 2.90161 0.00721 0.95446

13. SS (Real) is sensation seeing measured by ImpSS. Possible values are presented in table below:
SS Cases Fraction
-2.07848 71 3.77%
-1.54858 87 4.62%
-1.18084 132 7.00%
-0.84637 169 8.97%
-0.52593 211 11.19%
-0.21575 223 11.83%
0.07987 219 11.62%
0.40148 249 13.21%
0.76540 211 11.19%
1.22470 210 11.14%
1.92173 103 5.46%
Descriptive statistics
Min Max Mean Std.dev.
-2.07848 1.92173 -0.00329 0.96370 


## Relevant Papers:

E. Fehrman, A. K. Muhammad, E. M. Mirkes, V. Egan and A. N. Gorban, "The Five Factor Model of personality and evaluation of drug consumption risk.," arXiv [Web Link], 2015

E. Fehrman, V. Egan, A. N. Gorban, J. Levesley, E. M. Mirkes, A. K. Muhammad, "Personality Traits and Drug Consumption. A Story Told by Data." Springer, Cham, 2019. [Web Link]. ISBN 978-3-030-10441-2 [a book of Original Owners of Database]

D. Kumari, S. Kilam, P. Nath, et al. "Prediction of alcohol abused individuals using artificial neural network." Int. J. Inf. Tecnol. 10, 233–237 2018. [Web Link]

P. Nath, S. Kilam and A. Swetapadma, A machine learning approach to predict volatile substance abuse for drug risk analysis, 2017 Third International Conference on Research in Computational Intelligence and Communication Networks (ICRCICN), Kolkata, 2017, pp. 255-258. IEEE. [Web Link]

M. L. Eric, "Predicting illicit drug use with artificial neural network." European Journal of Humanities and Social Sciences, (3), 131-137, 2019. [Web Link]

X. Luo, Y. Li, W. Wang, et al. "A robust multilayer extreme learning machine using kernel risk-sensitive loss criterion." Int. J. Mach. Learn. & Cyber. 11, 197–216, 2020. [Web Link]

K. I. Adenuga, I. O. Muniru, F. I. Sadiq, et al. "Big Data in Healthcare: Are we getting useful insights from this avalanche of data?." In ICSIE '19: Proceedings of the 2019 8th International Conference on Software and Information Engineering, April 2019 Pages 196–199, 2019. IEEE. [Web Link]

A. Sies, I. Van Mechelen, "C443: a Methodology to See a Forest for the Trees." J Classif (2020). [Web Link]

S. Adinugroho, Y. A. Sari and N. Hidayat, "Drug usage duration classification using Extreme Learning Machine based on personality features," 2019 International Conference on Sustainable Information Engineering and Technology (SIET), Lombok, Indonesia, 2019, pp. 33-37. IEEE. [Web Link]

Z. T. Qiao, Q. Chai, X. Zhang, et al. "Predicting potential drug abusers using machine learning techniques," 2019 International Conference on Intelligent Informatics and Biomedical Sciences (ICIIBMS), Shanghai, China, 2019, pp. 283-286. IEEE. [Web Link]

B. Trevizan, J. Chamby-Diaz, A. L. Bazzan, M. Recamonde-Mendoza, "A comparative evaluation of aggregation methods for machine learning over vertically partitioned data." Expert Systems with Applications, 113406, 2020. [Web Link]

D. Benkeser, M. Petersen, M. J. van der Laan, "Improved small-sample estimation of nonlinear cross-validated prediction metrics." Journal of the American Statistical Association, 1-16, 21 Oct 2019. [Web Link]

A. Shahriar, F. Faisal, S. U. Mahmud, et al. "A Machine Learning Approach to Predict Vulnerability to Drug Addiction." In 2019 22nd International Conference on Computer and Information Technology (ICCIT) (pp. 1-7) 2019. IEEE. [Web Link]

R. Sen, K. Shanmugam, S. Shakkottai, "Contextual bandits with stochastic experts." arXiv preprint [Web Link], 2018. [Web Link]

S. Garg, Z. Ghodsi, C. Hazay, et al. "Outsourcing private machine learning via lightweight secure arithmetic computation." arXiv preprint [Web Link], 2018. [Web Link]