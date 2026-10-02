"""Bug 8.1 -- Axes objects have no show() method (AttributeError).

Fix: plot on the axes with ax.plot and display with plt.show() (or fig.show()).
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
