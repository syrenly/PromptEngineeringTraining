# 1. load data in python
# 2. inspect data
# 3. ask AI what's wrong
# 4. apply cleaning
# 5. ask AI which chart fits
# 6. visualize
# 7. improve

# EDA = Exploratory Data Analysis

import pandas as pd

# 1. load data in python
df = pd.read_csv("dataHandling\\clean_employee_data.csv")

# 2. inspect data
print(df.head())

print(df.info())
# RangeIndex: 20 entries, 0 to 19
# Data columns (total 6 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   employee_id  20 non-null     int64
#  1   name         20 non-null     str
#  2   age          20 non-null     int64
#  3   department   20 non-null     str
#  4   salary       20 non-null     int64
#  5   email        20 non-null     str

print(df.describe())
#        employee_id      age        salary
# count     20.00000  20.0000     20.000000
# mean      10.50000  29.8000  61200.000000
# std        5.91608   3.5333   8501.393075
# min        1.00000  24.0000  50000.000000
# 25%        5.75000  27.0000  53750.000000
# 50%       10.50000  29.5000  59000.000000
# 75%       15.25000  32.2500  69250.000000
# max       20.00000  36.0000  75000.000000

# 3. ask AI what's wrong
# Act as a data analyst. I have loaded this dataset (attach the file). Suggest key questions I should explore before visualization

# find every salary
print(df["salary"].mean())
# 61200.0

# how many employees by department
print(df["department"].value_counts())
# department
# IT           6
# HR           5
# Sales        5
# Marketing    4

# age distribution
print(df["age"].describe())
# count    20.0000
# mean     29.8000
# std       3.5333
# min      24.0000
# 25%      27.0000
# 50%      29.5000
# 75%      32.2500
# max      36.0000

# 4. apply cleaning
# see previous lectures

# 5. ask AI which chart fits
# Given this dataset with age, salary, and department, which visualizations best explain patterns? Explain why.

import matplotlib.pyplot as plt

plt.figure(1)
plt.hist(df["salary"].dropna(), bins=5)
plt.title("salary distribution")
plt.xlabel("salary")
plt.ylabel("number of employees")
plt.show()

plt.figure(2)
plt.scatter(df["age"], df["salary"])
plt.title("age vs salary")
plt.xlabel("age")
plt.ylabel("salary")
plt.show()
