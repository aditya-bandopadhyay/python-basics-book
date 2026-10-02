# Visualizing Data with Matplotlib -- Try It Yourself: Tracking Seedling Growth Over 14 Days
# (book source: ch08_matplotlib.tex, line 48)

import matplotlib.pyplot as plt

days = list(range(1, 15))
heights = [0.5, 0.8, 1.2, 1.9, 2.8, 4.0, 5.5, 7.2, 9.0, 10.8, 12.5, 13.8, 14.8, 15.4]

plt.plot(days, heights, marker='o', color='green')
plt.xlabel("Day")
plt.ylabel("Height (cm)")
plt.title("Chickpea Seedling Growth")
plt.grid(True)
plt.show()
