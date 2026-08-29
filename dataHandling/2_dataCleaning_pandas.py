# Data Cleaning with Python
# prepare raw data to be ready to be used by AI and other system processes.
# remove duplicates, invalid entries, normalize names and numbers
# ask AI the following prompt: act as an AI engineer: I've a messy csv file, suggest python steps to clean age, salary,country, duplicates by email field. Beginner friendly response, use pandas and no other libraries . Step by step python logic.
# install pandas library => is a python library used to store, clean, analyze and manipulate data.

import pandas as pd

# 1. Load
df = pd.read_csv("dataHandling\\employee_data.csv")
original_columns = df.columns.tolist()

# 2. Clean column names
df.columns = df.columns.str.strip().str.lower()

# 3. Format email
df["email"] = df["email"].astype(str).str.strip().str.lower()

# 4. Clean age
df["age"] = df["age"].astype(str).str.strip()
df["age"] = df["age"].str.extract(r"(\d+)")
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Remove unrealistic ages
df.loc[(df["age"] < 18) | (df["age"] > 75), "age"] = pd.NA

# 5. Clean salary
df["salary"] = df["salary"].astype(str).str.strip()

df["salary"] = (
    df["salary"]
    .str.replace("$", "", regex=False)
    .str.replace("€", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Remove negative salaries
df.loc[df["salary"] < 0, "salary"] = pd.NA

# 6. Clean country
df["country"] = df["country"].astype(str).str.strip().str.lower()

country_mapping = {
    "USA": "U.S.A.",
    "usa": "U.S.A.",
}

df["country"] = df["country"].replace(country_mapping).str.title()

# 7. Clean email

df["email"] = df["email"].replace("", pd.NA)

# If you simply want to remove duplicates: df = df.drop_duplicates(subset="email", keep="first"); I'm preferring to merge duplicates rows instead.
# Merge duplicate emails
df = df.groupby("email", as_index=False, sort=False).first()

# 8. Remove rows without an email
df = df.dropna(subset=["email"])

# 9. Restore order column (groupby can reorder columns)
df = df[original_columns]

# 10. Validate
print("Rows:", len(df))
print("Duplicate emails:", df["email"].duplicated().sum())
print("\nMissing values:")
print(df.isna().sum())

# 10. Save
df.to_csv("dataHandling\\employees_cleaned.csv", index=False)
