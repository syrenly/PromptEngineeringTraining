# Data Cleaning with Python
# prepare raw data to be ready to be used by AI and other system processes.
# remove duplicates, invalid entries, normalize names and numbers
# ask AI the following prompt: act as an AI engineer: I've a messy csv file, suggest python steps to clean age, salary,country, duplicates by email field. Beginner friendly response, no complex libraries. Step by step python logic.
# this version shows limitations; it's suggested to use a library like `pandas`
# install pandas library


import csv

def clean_age(value):
    value = value.strip()

    if value == "":
        return None

    try:
        age = int(value)
    except ValueError:
        return None

    if age < 0 or age > 120:
        return None

    return age


def clean_salary(value):
    value = value.strip()

    if value == "":
        return None

    value = value.replace("$", "")
    value = value.replace("€", "")
    value = value.replace(",", "")

    try:
        salary = float(value)
    except ValueError:
        return None

    if salary < 0:
        return None

    return salary


def clean_country(value):
    value = value.strip().lower()

    country_map = {
        "usa": "United States",
        "us": "United States",
        "u.s.a.": "United States",
        "uk": "United Kingdom",
        "england": "United Kingdom",
    }

    if value == "":
        return None

    return country_map.get(value, value.title())


def clean_email(value):
    return value.strip().lower()


# 1. Read CSV
with open("dataCleaning\\employees.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)


# 2. Clean fields
for row in rows:
    row["age"] = clean_age(row["age"])
    row["salary"] = clean_salary(row["salary"])
    row["country"] = clean_country(row["country"])
    row["email"] = clean_email(row["email"])


# 3. Remove duplicate emails
seen_emails = set()
cleaned_rows = []

for row in rows:
    email = row["email"]

    # Skip rows with no email
    if email == "":
        continue

    # Skip duplicate emails
    if email in seen_emails:
        continue

    seen_emails.add(email)
    cleaned_rows.append(row)


# 4. Save cleaned CSV
with open("dataCleaning\\employees_cleaned.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = cleaned_rows[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(cleaned_rows)

print("Cleaning complete!")
print("Original rows:", len(rows))
print("Cleaned rows:", len(cleaned_rows))


# import pandas as pd

# # ============================================
# # 1. Load CSV
# # ============================================

# df = pd.read_csv("dataCleaning\\employees.csv")

# print("Original data:")
# print(df.head())
# print("\nColumns:")
# print(df.columns.tolist())


# # ============================================
# # 2. Clean column names
# # ============================================

# df.columns = df.columns.str.strip().str.lower()


# # ============================================
# # 3. Clean AGE
# # ============================================

# # Convert age to numbers.
# # Invalid values such as "unknown" become NaN.
# df["age"] = pd.to_numeric(df["age"], errors="coerce")

# # Remove unrealistic ages.
# df.loc[(df["age"] < 18) | (df["age"] > 100), "age"] = None


# # ============================================
# # 4. Clean SALARY
# # ============================================

# # Convert salary to string first so string operations work.
# df["salary"] = df["salary"].astype(str)

# # Remove common formatting characters.
# df["salary"] = (
#     df["salary"]
#     .str.replace("$", "", regex=False)
#     .str.replace("€", "", regex=False)
#     .str.replace(",", "", regex=False)
#     .str.strip()
# )

# # Convert to numbers.
# # Values such as "unknown" become NaN.
# df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# # Remove negative salaries.
# df.loc[df["salary"] < 0, "salary"] = None


# # ============================================
# # 5. Clean COUNTRY
# # ============================================

# df["country"] = (
#     df["country"]
#     .astype(str)
#     .str.strip()
#     .str.lower()
# )

# # Standardize common country variations.
# country_map = {
#     "usa": "United States",
#     "us": "United States",
#     "u.s.a.": "United States",
#     "uk": "United Kingdom",
#     "u.k.": "United Kingdom",
#     "italy": "Italy"
# }

# df["country"] = df["country"].replace(country_map)


# # ============================================
# # 6. Clean EMAIL
# # ============================================

# df["email"] = (
#     df["email"]
#     .astype(str)
#     .str.strip()
#     .str.lower()
# )

# # Treat empty emails as missing.
# df["email"] = df["email"].replace("", None)
# df["email"] = df["email"].replace("nan", None)


# # ============================================
# # 7. Find duplicate emails
# # ============================================

# duplicates = df[df.duplicated("email", keep=False)]

# print("\nDuplicate records:")
# print(duplicates)


# # ============================================
# # 8. Remove duplicate emails
# # ============================================

# # Keep the first record for each email.
# df = df.drop_duplicates(
#     subset="email",
#     keep="first"
# )


# # ============================================
# # 9. Final validation
# # ============================================

# print("\nCleaned data:")
# print(df.head())

# print("\nMissing values:")
# print(df.isnull().sum())

# print("\nNumber of duplicate emails:")
# print(df["email"].duplicated().sum())

# print("\nFinal number of rows:", len(df))


# # ============================================
# # 10. Save cleaned CSV
# # ============================================

# df.to_csv("dataCleaning\\employees_cleaned.csv", index=False)

# print("\nCleaning complete!")
# print("Saved as: employees_cleaned.csv")