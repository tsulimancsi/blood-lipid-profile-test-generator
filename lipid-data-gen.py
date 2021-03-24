## Cholesterol is measured in three categories:
# total cholesterol
# LDL, or ‘bad cholesterol”
# HDL, or ‘good cholesterol
# Calculations:
# Total Serum Cholestrol = LDL + HDL + 20% of Trig
# TG to HDL ratio = Total Cholestrol / HDL Cholestrol

import random
import numpy as np
import pandas as pd
# Number of Patients / Records initialization

N = 30000 # Number of Records
id = np.arange(0,N)

# General Attributes 

age = np.random.randint(18,70,size=N) # Age
sex = np.random.randint(2, size=N) # Sex Male = 1 , Female = 0

# Cholestrol Data Generation & Calculation 

ldl_cholestrol = np.random.randint(75,195, size=N)
hdl_cholestrol = np.random.randint(22,72,size=N)
tgly = np.random.randint(42,360,size=N)
total_chol = hdl_cholestrol + ldl_cholestrol + 0.2 * tgly 

# Round elements of the array to the nearest integer

total_chol = np.rint(total_chol)

# Other important Features

chest_pain = np.random.randint(4, size=N) 
# chest pain type 
# angina – chest pain caused by restricted blood flow to the heart muscle
# -- Value 1: typical angina
# -- Value 2: atypical angina
# -- Value 3: non-anginal pain
# -- Value 4: asymptomatic

#############################################################

trestbps = np.random.randint(94,170,size=N)  # resting blood pressure (in mm Hg on admission to the hospital)

# History of Diabetes 

dm = np.random.randint(2, size=N) # (1 = history of diabetes; 0 = no such history)

# Target Risk Predicted Value 

target = np.random.randint(2,size=N)

# Other attributes  not included 

# hyber tensive
# Hymaglobeen  normal ::  less :: function  - transfer oxygen to lee ansga  symptoms 
# Platlet count

# Join all  data

df = pd.DataFrame({'id':id, 'age':age, 'sex':sex,'cp':chest_pain,'chol':total_chol,'tgl':tgly,'hdl':hdl_cholestrol,'ldl':ldl_cholestrol,'dm':dm, 'target':target});

# Export generated data to CSV dataset file

df.to_csv(r'Blood_Lipid_Profile_Test_Fake_export.csv', index = False, header= True)

# Print the data 
df.head(1000)