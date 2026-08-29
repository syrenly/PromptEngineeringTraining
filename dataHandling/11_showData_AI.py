# load data
# inspect data
# ask AI what's wrong
# apply cleaning
# ask AI which chart fits
# visualize chart
# improve

# ask AI what's wrong
# prompt:
# role => Act as data analyst.
# context => I have a CSV file with missing values, inconsistent text, and invalid emails.
# task => Suggest step-by-step data cleaning plan using pandas python library.
# answer:

# CSV DATA CLEANING PIPELINE
# ===========================

import pandas as pd
import numpy as np

# ============================================================
# 1. LOAD DATA
# ============================================================

INPUT_FILE = "dataHandling\\employee_data.csv"
OUTPUT_FILE = "dataHandling\\employees_cleaned.csv"
QUALITY_REPORT_FILE = "dataHandling\\data_quality_report.csv"

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("INITIAL DATASET INFORMATION")
print("=" * 60)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())


# ============================================================
# 2. CREATE A COPY
# ============================================================

# Never modify the original dataframe directly.
clean = df.copy()

original_rows = len(clean)


# ============================================================
# 3. STANDARDIZE MISSING VALUES
# ============================================================

# Different datasets may use different values to represent
# missing data.

missing_values = ["", " ", "NA", "N/A", "NULL", "null", "None", "-", "?"]

clean = clean.replace(missing_values, np.nan)


# ============================================================
# 4. REMOVE EXTRA WHITESPACE FROM TEXT COLUMNS
# ============================================================

text_columns = clean.select_dtypes(include="object").columns

for column in text_columns:
    clean[column] = clean[column].str.strip()


# ============================================================
# 5. STANDARDIZE COMMON TEXT FIELDS
# ============================================================

# Only apply these transformations if the columns exist.

if "country" in clean.columns:
    clean["country"] = clean["country"].str.title()

if "city" in clean.columns:
    clean["city"] = clean["city"].str.title()

if "name" in clean.columns:
    clean["name"] = clean["name"].str.title()


# ============================================================
# 6. STANDARDIZE COUNTRY VALUES
# ============================================================

country_map = {
    "USA": "United States",
    "US": "United States",
    "U.S.A.": "United States",
    "UK": "United Kingdom",
    "U.K.": "United Kingdom",
}

if "country" in clean.columns:
    clean["country"] = clean["country"].replace(country_map)


# ============================================================
# 7. CLEAN AND VALIDATE EMAIL ADDRESSES
# ============================================================

if "email" in clean.columns:

    # Convert to pandas string type and normalize
    clean["email"] = clean["email"].astype("string").str.strip().str.lower()

    # Basic email validation pattern
    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    clean["email_valid"] = clean["email"].notna() & clean["email"].str.match(
        email_pattern, na=False
    )

    # Replace invalid emails with missing values.
    # The original row is retained.
    clean.loc[~clean["email_valid"], "email"] = pd.NA

else:
    print("\nWarning: 'email' column was not found.")


# ============================================================
# 8. CONVERT COLUMNS TO CORRECT DATA TYPES
# ============================================================

if "age" in clean.columns:
    clean["age"] = pd.to_numeric(clean["age"], errors="coerce")

if "salary" in clean.columns:
    clean["salary"] = pd.to_numeric(clean["salary"], errors="coerce")

if "signup_date" in clean.columns:
    clean["signup_date"] = pd.to_datetime(clean["signup_date"], errors="coerce")


# ============================================================
# 9. HANDLE INVALID NUMERICAL VALUES
# ============================================================

# Age should normally be between 0 and 120.

if "age" in clean.columns:
    clean.loc[~clean["age"].between(0, 120), "age"] = np.nan


# Salary should not be negative.

if "salary" in clean.columns:
    clean.loc[clean["salary"] < 0, "salary"] = np.nan


# ============================================================
# 10. HANDLE MISSING VALUES
# ============================================================

# Numeric columns:
# Use the median because it is less sensitive to extreme values.

if "age" in clean.columns:
    age_median = clean["age"].median()

    if pd.notna(age_median):
        clean["age"] = clean["age"].fillna(age_median)


if "salary" in clean.columns:
    salary_median = clean["salary"].median()

    if pd.notna(salary_median):
        clean["salary"] = clean["salary"].fillna(salary_median)


# Categorical fields:
# Use "Unknown" rather than guessing a value.

if "country" in clean.columns:
    clean["country"] = clean["country"].fillna("Unknown")

if "city" in clean.columns:
    clean["city"] = clean["city"].fillna("Unknown")


# ============================================================
# 11. CHECK FOR DUPLICATE ROWS
# ============================================================

duplicate_count = clean.duplicated().sum()

print("\nDuplicate rows found:", duplicate_count)

# Remove exact duplicate rows.
clean = clean.drop_duplicates()


# ============================================================
# 12. CHECK FOR DUPLICATE EMAILS
# ============================================================

if "email" in clean.columns:

    duplicate_emails = clean[
        clean["email"].notna() & clean["email"].duplicated(keep=False)
    ].sort_values("email")

    print("Records with duplicate emails:", len(duplicate_emails))

    # We do NOT automatically delete duplicate emails.
    # Multiple records can legitimately share an email address.


# ============================================================
# 13. CREATE DATA-QUALITY FLAGS
# ============================================================

if "email" in clean.columns:

    # email_valid was created earlier.
    # Missing emails are considered invalid for this flag.
    clean["email_valid"] = clean["email"].notna() & clean["email"].str.match(
        email_pattern, na=False
    )


# Check for missing required fields.

required_columns = [column for column in ["name", "email"] if column in clean.columns]

if required_columns:
    clean["missing_required"] = clean[required_columns].isna().any(axis=1)


# ============================================================
# 14. FINAL DATA QUALITY CHECKS
# ============================================================

print("\n" + "=" * 60)
print("FINAL DATA QUALITY REPORT")
print("=" * 60)

print(f"Original rows: {original_rows}")
print(f"Final rows:    {len(clean)}")
print(f"Rows removed:  {original_rows - len(clean)}")

print("\nMissing values:")
print(clean.isna().sum().sort_values(ascending=False))

print("\nDuplicate rows:")
print(clean.duplicated().sum())

if "email_valid" in clean.columns:
    print("\nInvalid/missing emails:", (~clean["email_valid"]).sum())


# ============================================================
# 15. VALIDATE BUSINESS RULES
# ============================================================

if "age" in clean.columns:
    assert clean["age"].dropna().between(0, 120).all(), "Invalid age values found."


if "salary" in clean.columns:
    assert (clean["salary"].dropna() >= 0).all(), "Negative salary values found."


# ============================================================
# 16. CREATE DATA QUALITY REPORT
# ============================================================

quality_report = pd.DataFrame(
    {
        "column": clean.columns,
        "data_type": [str(clean[column].dtype) for column in clean.columns],
        "missing_count": [clean[column].isna().sum() for column in clean.columns],
        "missing_percentage": [
            round(clean[column].isna().mean() * 100, 2) for column in clean.columns
        ],
        "unique_values": [
            clean[column].nunique(dropna=True) for column in clean.columns
        ],
    }
)


# ============================================================
# 17. SAVE CLEANED DATA
# ============================================================

clean.to_csv(OUTPUT_FILE, index=False)

quality_report.to_csv(QUALITY_REPORT_FILE, index=False)


# ============================================================
# 18. COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("CLEANING COMPLETED")
print("=" * 60)

print(f"Cleaned data saved to: {OUTPUT_FILE}")
print(f"Quality report saved to: {QUALITY_REPORT_FILE}")


# ask AI which chart fits
# prompt: I have employee salary data by department; which visualization is best to compare distributions and why
# answer: For employee salary distributions across departments, a box plot is usually the best choice.
#
# if AI does not provide code example:
# prompt: Generate a seaborn boxplot compare salary distribution by department

import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataHandling\\employees_cleaned.csv")

plt.figure(figsize=(12, 6))

sns.boxplot(data=df, x="department", y="salary")

plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
