# A train-test split is a technique used in machine learning to divide a dataset into two distinct subsets: a training set to teach the model and a testing set to evaluate its performance on unseen data.

import pandas as pd

df = pd.read_csv("machineLearningBasic\\student_performance.csv")
print(df.head())
x = df[["Hours_Studied", "Attendance"]]
y = df["Pass"]

# split data into training data and testing data
# install scikit-learn, a simple and efficient tools for predictive data analysis

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)
# test size: percentage of data that should use to test (0.2=20%)
# random_state: number that allow the splitting to be always random, you can choose which number you want, but if you use the same, the result is reproducible
print(x_train)
