# Visualizing Data with Matplotlib -- Code 8.5: 1 row, 2 columns of axes
# (book source: ch08_matplotlib.tex, line 447)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, np.sin(x), color='steelblue')
ax1.set_title('Sine')

ax2.plot(x, np.cos(x), color='coral')
ax2.set_title('Cosine')

for ax in (ax1, ax2):
    ax.set_xlabel('x (rad)')
    ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')

fig.suptitle('Trigonometric Functions', fontsize=14)
fig.tight_layout()
fig.savefig('subplots.pdf', bbox_inches='tight')
plt.show()
