"""Bug 8.4 -- after the window is closed, plt.show() has finished with the figure,
so savefig() saves a new, empty figure.

Fix: save first, then show.
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
plt.plot(x, x ** 2)
plt.savefig('out.png')
plt.show()
