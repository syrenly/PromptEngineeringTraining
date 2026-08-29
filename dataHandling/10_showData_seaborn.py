# Sea Born = python library used for statistical data visualization; it's built on top of matplotlib, but it makes plots more informative
# it's used for exploratory data analysis, before giving data to AI
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "age": [22, 25, 30, 35, 40, 45, 50],
    "salary": [30000, 35000, 50000, 60000, 70000, 80000, 90000],
    "department": ["IT", "IT", "HR", "HR", "Sales", "Sales", "IT"],
}

df = pd.DataFrame(data)

# countplot = shows frequency of each category, how many employees belong each department
plt.figure(1)
sns.countplot(x="department", data=df)
plt.title("countplot")

# barplot = see average or aggregate, average salary by department
# for each bar it shows a black line in the middle, which is the confidence interval; more the line is long, the more the data are less consistent
plt.figure(2)
sns.barplot(x="department", y="salary", data=df)
plt.title("barplot")
plt.show()

# bloxplot = shows median, spread and outliers; it shows how data are distributed, not just average
# box is delimited by first and third quartile and divided in its inside by the median
# first quartile = 25% percentile, the median of lower half of the dataset
# third quartile = 75% percentile, the median of lower half of the dataset
# median = reorder the data and pick up the value in the middle (for IT is 35000); if the number values is even, make the mean of the 2 medians
plt.figure(3)
sns.boxplot(x="department", y="salary", data=df)
plt.title("boxplot")
plt.show()

# scatterplot = show relationships between data
plt.figure(4)
sns.scatterplot(x="age", y="salary", hue="department", data=df)
plt.title("scatterplot")
plt.show()
