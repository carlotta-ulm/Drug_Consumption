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

## Feature Information:

1. ID is number of record in original database. Cannot be related to participant. It can be used for reference only.

2. Age (Real) is age of participant and has one of the values: 
  - 18-24
  - 25-34
  - 35-44
  - 45-54 
  - 55-64
  - 65+

3. Gender (Real) is gender of participant.

4. Education (Real) is level of education of participant and has one of the values: 
  - Left school before 16 years 
  - Left school at 16 years
  - Left school at 17 years
  - Left school at 18 years
  - Some college or university, no certificate or degree
  - Professional certificate/ diploma
  - University degree
  - Masters degree
  - Doctorate degree

5. Country (Real) is country of current residence of participant and has one of the values:
  - Australia 
  - Canada
  - New Zealand
  - Other
  - Republic of Ireland 
  - UK 
  - USA

6. Ethnicity (Real) is ethnicity of participant and has one of the values:
  - Asian
  - Black
  - Mixed-Black/Asian
  - Mixed-White/Asian
  - Mixed-White/Black
  - Other
  - White

7. Nscore (Real) is NEO-FFI-R Neuroticism.

8. Escore (Real) is NEO-FFI-R Extraversion.

9. Oscore (Real) is NEO-FFI-R Openness to experience.

10. Ascore (Real) is NEO-FFI-R Agreeableness.

11. Cscore (Real) is NEO-FFI-R Conscientiousness.

12. Impulsive (Real) is impulsiveness measured by BIS-11. 

13. SS (Real) is sensation seeing measured by ImpSS.

## Drugs Information:

For all drugs, their usage is classified in seven categories:
  - CL0 Never Used 
  - CL1 Used over a Decade Ago
  - CL2 Used in Last Decade 
  - CL3 Used in Last Year 
  - CL4 Used in Last Month 
  - CL5 Used in Last Week 
  - CL6 Used in Last Day

14. Alcohol is class of alcohol consumption. 

15. Amphet is class of amphetamines consumption. 

16. Amyl is class of amyl nitrite consumption. 

17. Benzos is class of benzodiazepine consumption.

18. Caff is class of caffeine consumption. 

19. Cannabis is class of cannabis consumption. 

20. Choc is class of chocolate consumption.

21. Coke is class of cocaine consumption. 

22. Crack is class of crack consumption. 

23. Ecstasy is class of ecstasy consumption. 

24. Heroin is class of heroin consumption.

25. Ketamine is class of ketamine consumption.

26. Legalh is class of legal highs consumption. 

27. LSD is class of alcohol consumption. 

28. Meth is class of methadone consumption. 

29. Mushrooms is class of magic mushrooms consumption. 

30. Nicotine is class of nicotine consumption. 

31. Semer is class of fictitious drug Semeron consumption.

32. VSA is class of volatile substance abuse consumption.

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
