# empty data could be NaN, none, null, empty cells, empty strings
# AI models do not think like humans, so bad data mean bad outputs

# Step 1: detect missing data
# Step 2: understand why data is missing (not required, bad conversions)
# Step 3: how to handle missing data:
# - drop missing data; this is the worst, because you may loose information
#   df_dropped=df.dropna() => dropna removes rows with missing values
# - fill missing data
#   df["age"]=df["age"].fillna(0) => fix empty values with defaults
#   df["salary"]=df["salary"].fillna(df["salary"]).mean()) => fix empty values with an average value

# How to choose strategy:
# Situation               Best Choice
# -----------------------------------
# Critical column         Drop
# Numeric data            Mean/Median
# Categorical data        Mode
# Unknown meaning         Keep as NaN

# Also you can ask to AI:
# Act as a data analyst: given this dataset, suggest the best strategy to handle missing values in age and salary columns

import pandas as pd

df = pd.read_csv("./employee_data.csv")

# use filtered_df

df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].mean())
