# scatter plot = type of mathematical diagram that uses Cartesian coordinates to display values for two numeric variables in a dataset.
import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6]
marks = [35, 40, 50, 65, 75, 90]
plt.scatter(hours_studied, marks)
plt.xlabel("Hours studied")
plt.ylabel("Marks obtained")
plt.title("Study time vs marks")
plt.show()
