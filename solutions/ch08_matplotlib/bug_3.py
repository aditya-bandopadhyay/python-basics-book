"""Bug 8.3 -- a legend needs labels on the lines AND a call to ax.legend()."""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin x")
ax.plot(x, np.cos(x), label="cos x")
ax.legend()
plt.show()
