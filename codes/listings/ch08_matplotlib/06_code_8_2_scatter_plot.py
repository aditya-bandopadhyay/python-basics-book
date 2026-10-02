# Visualizing Data with Matplotlib -- Code 8.2: Scatter plot
# (book source: ch08_matplotlib.tex, line 313)

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
x = rng.uniform(0, 10, 50)
y = 2 * x + rng.normal(0, 3, 50)

fig, ax = plt.subplots()
ax.scatter(x, y, color='coral', alpha=0.7, edgecolors='k', s=60)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Scatter Plot with Noise')
fig.savefig('scatter_plot.pdf', bbox_inches='tight')
plt.show()
