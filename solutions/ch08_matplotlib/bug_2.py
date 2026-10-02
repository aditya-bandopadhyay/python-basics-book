"""Bug 8.2 -- the bars are drawn at positions 0, 1, 2 with numeric tick labels.

Fix: pass the category names as the x values (or set the tick labels).
"""
import matplotlib.pyplot as plt
labels = ['A', 'B', 'C']
values = [10, 25, 17]
fig, ax = plt.subplots()
ax.bar(labels, values)
plt.show()
