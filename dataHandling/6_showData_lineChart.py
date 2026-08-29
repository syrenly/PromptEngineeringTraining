# matplotlib learning

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
views = [120, 300, 500, 700, 900]
plt.plot(days, views)
# labels are important to AI too, to understand the context of the data
plt.xlabel("Days")
plt.ylabel("Views")
plt.title("Youtube Channel Growth")
plt.show()
