"""Bug 8.5 -- plt.scatter(y, x) puts y on the horizontal axis.

Fix: scatter(x, y) -- the first argument is always the horizontal coordinate.
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.xlabel('x'); plt.ylabel('y')
plt.show()
