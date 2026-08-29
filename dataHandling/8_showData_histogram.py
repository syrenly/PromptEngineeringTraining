# histogram = type of graph that shows the frequency distribution of numerical data by grouping values into adjacent intervals called bins.
# histogram bin = continuous, non-overlapping interval that groups numerical data to show the frequency of values falling within that range.

import matplotlib.pyplot as plt

ages = [18, 19, 20, 21, 22, 23, 24, 25, 30, 35, 40, 45]

# with no other instructions then ages, hist(ages) groups values into ranges automatically
plt.hist(ages, bins=5)
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.title("Age distribution")
plt.show()
