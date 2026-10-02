# Visualizing Data with Matplotlib -- Code 8.6: Comparing axis scales
# (book source: ch08_matplotlib.tex, line 486)

import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 7)
sales  = np.array([1020, 1035, 1028, 1042, 1031, 1055])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

# Left: truncated y-axis
ax1.plot(months, sales, marker='o', color='crimson')
ax1.set_ylim(1015, 1060)
ax1.set_title('Sales (Truncated Axis)')

# Right: zero-based y-axis
ax2.plot(months, sales, marker='o', color='steelblue')
ax2.set_ylim(0, 1100)
ax2.set_title('Sales (Zero-Based Axis)')

for ax in (ax1, ax2):
    ax.set_xlabel('Month'); ax.set_ylabel('Units sold')

fig.tight_layout()
plt.show()
