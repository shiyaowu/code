## group task 3 
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm

main_dir = "/Users/shiyaowu/Desktop/PUBPOL590/"
root = main_dir + "data/3_task_data/"

df = pd.read_csv(root + "allocation_subsamp.csv")

# 1. create 5 unique vectors using the data from allocation_subsamp.csv 
Ctrl = df["ID"][df.tariff == "E"]
A1 = df["ID"][(df.tariff == "A")&(df.stimulus == "1")]
A3 = df["ID"][(df.tariff == "A")&(df.stimulus == "3")]
B1 = df["ID"][(df.tariff == "B")&(df.stimulus == "1")]
B3 = df["ID"][(df.tariff == "B")&(df.stimulus == "3")]

# 2. set the random seed to 1789
np.random.seed(1789)

# 3. use the function np.random.choice and extract the following sample size 
# without replacement: (THE ORDER MATTERS)
ctrl = np.random.choice(Ctrl, size=300, replace=False)
a1 = np.random.choice(A1, size=150, replace=False)
a3 = np.random.choice(A3, size=150, replace=False)
b1 = np.random.choice(B1, size=50, replace=False)
b3 = np.random.choice(B3, size=50, replace=False)

# 4. create a DataFrame with all the sampled IDs.
d = {'',
    ''}
df = pd.DataFrame(d)


# 5. import the consumption data from kwh_redux_pretrial.csv
df1 = pd.read_csv(root + "kwh_redux_pretrial.csv")

# 6. merge the consumption data with the sampled IDs, which will strip away a 
# large portion of the original consumption dataframe.
