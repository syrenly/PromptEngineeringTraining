import pandas as  pd

df=pd.read_csv("dataHandling\\employee_data.csv")
print(df.head())

# FILTERING

# filter data which salary is valid
filtered_df=df[df["salary"].notna()]
filtered_df["salary"]=pd.to_numeric(filtered_df["salary"],errors="coerce")

# filter data which age is greater than 25
filtered_df["age"]=pd.to_numeric(filtered_df["age"],errors="coerce")
filtered_df=filtered_df[filtered_df["age"]>25]

# AGGREGATION

# calculate mean salary
average_salary=filtered_df["salary"].mean()
print("average salary:", average_salary)

# GROUPING

grouped_data=filtered_df.groupby("country")["salary"].mean()
print("average salary per country", grouped_data)

# MULTIPLE AGGREGATION

grouped_data=filtered_df.groupby("country")["salary"].agg(["mean","max","count"])
print("average, max and count salary per country", grouped_data)