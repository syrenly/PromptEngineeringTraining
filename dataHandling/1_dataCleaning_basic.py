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
with open("dataHandling\\employee_data.csv", "r", encoding="utf-8") as file:
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
with open(
    "dataHandling\\employees_cleaned.csv", "w", newline="", encoding="utf-8"
) as file:
    fieldnames = cleaned_rows[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(cleaned_rows)

print("Cleaning complete!")
print("Original rows:", len(rows))
print("Cleaned rows:", len(cleaned_rows))
