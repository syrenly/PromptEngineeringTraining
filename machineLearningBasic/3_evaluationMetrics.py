# evaluation metrics = measurement of how good is a model
#
# Problem type        Example          Metrics Used
# Classification      Pass/Fail        Accuracy, F1
# Regression          Predict Salary   RMSE

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("machineLearningBasic\\student_performance.csv")
print(df.head())
x = df[["Hours_Studied", "Attendance"]]
y = df["Pass"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)
print(x_train)

# Accuracy = correct predictions/total predictions = 8/10 = 80% accuracy

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# create a model: now it knows nothing.
#
# To simplify, we call it model, but it's actually a Python object which contain the model.
model = LogisticRegression()

# train the model to learn pattern
model.fit(x_train, y_train)

# predict if the student pass => give x_test and expect it fits y_test
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy", accuracy)  # 1.0 => 100% accuracy

# F1 score = it measure how many positive cases we correctly found and how precise our predictions were.
# It balances precision, how correct the predictions are and recall how many real positives we found.

from sklearn.metrics import f1_score

model2 = LogisticRegression()

# train the model to learn pattern
model2.fit(x_train, y_train)

# predict if the student pass => give x_test and expect it fits y_test
y_pred2 = model2.predict(x_test)

f1 = f1_score(y_test, y_pred2, pos_label="Yes")
print("F1 score", f1)  # 1.0 = 100%
