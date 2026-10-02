# Visualizing Data with Matplotlib -- Saving Figures Silently & Export Formats
# (book source: ch08_matplotlib.tex, line 265)

import matplotlib
matplotlib.use('Agg')  # Headless non-interactive background renderer
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
fig.savefig('silent_output.pdf', dpi=300, bbox_inches='tight')
plt.close(fig)  # Free memory resources silently
