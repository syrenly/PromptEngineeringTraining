# matplotlib learning

import matplotlib.pyplot as plt

careers = ["Developer", "Data Scientist", "AI Engineer"]
salaries = [60000, 85000, 120000]
plt.bar(careers, salaries)
plt.title("Average Salary")
plt.xlabel("Careers")
plt.ylabel("Salaries")
plt.show()
