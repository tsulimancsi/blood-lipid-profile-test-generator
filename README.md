# Blood Lipid Profile Test Data Generator

## Introduction
A complete cholesterol test is also called a lipid panel or lipid profile. It's used by medical professional to measure the amount of “good” and “bad” cholesterol and triglycerides, a type of fat, in your blood.
Too much cholesterol can lead to:

1. Heart disease
2. Stroke
3. Atherosclerosis, a clogging or hardening of your arteries

What Does a Cholesterol Test Measure?

A complete cholesterol test measures four types of lipids, or fats, in your blood:

1. Total cholesterol: This is the total amount of cholesterol in your blood.
2. Low-density lipoprotein (LDL) cholesterol: This is referred to as “bad” cholesterol. Too much of it raises your risk of heart attack, stroke, and atherosclerosis.
3. High-density lipoprotein (HDL) cholesterol: This is referred to as “good” cholesterol because it helps remove LDL cholesterol from your blood.
4. Triglycerides: When you eat, your body converts the calories it doesn’t need into triglycerides, which are stored in your fat cells. People who are overweight, diabetic, eat too many sweets, or drink too much alcohol can have high triglyceride levels.
5. Non-HDL cholesterol: Non-HDL Cholestrol as its name implies, simply subtracts your high-density lipoprotein (HDL, or "good") cholesterol number from your total cholesterol number[1]


## Lipid Profile Test Values 

| Type of Lipids | Optimal | Intermediate | High |
| --- | --- | --- | --- |
| LDL Cholestrol | < 130  | 130 - 159 | > 159  |
| HDL Cholestrol | > 60 | 40 - 60 | < 40 |
| Triglyceried | < 150  | 150 - 199  | > 199  |
| Total Cholestrol | < 200 | 200 - 239 | > 239 |
| Non-HDL-C | < 130 | 130 - 159 | > 159  |
| TG to HDL ratio | < 3 | 3.1 - 3.8  | > 3.8 |

* Total Serum Cholestrol = LDL + HDL + 20% of Tgl
* TG to HDL ratio  = Total Cholestrol / HDL Cholestrol


In addition to the attributes provided above this data generator will generate the following attributes :

1. Age : age in years
2. Sex : Male = 1 of Female = 0 
3. CP : Chest Pain  type
4. Trestbps:  resting blood pressure (in mm Hg on admission to the hospital)
5. DM : Diabetic 
=====================================================================
6. Target : ( Predicted Value )

## Data Information 

* Number of Instances:
30000 ( can be modified )
* Data Set Characterstics : 
Multivariate
* Attribute Characterstics: 
Categorical, Real, Integer
* Associate Tasks:
Classification
* Area:
Life


## Risk Factors 


| Model to Use| Risk Factors Attributes |
| --- | --- | 
| Logistic Regression, K-Nearest Neighbor KNN ,Auto Machine Learning (AutoML) , Classification Tree, Decission Trees, Support Vector Machine SVM| Age, sex, Blood Pressure,CP , Trestbps , Lipid Profile Test data| 


## Machine Learning Algorithms

### Logistic Regression





## References

1. https://www.healthline.com/health/cholesterol-test#purpose-of-cholesterol-test