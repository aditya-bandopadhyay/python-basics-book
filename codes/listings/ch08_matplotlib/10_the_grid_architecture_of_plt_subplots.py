# Visualizing Data with Matplotlib -- The Grid Architecture of plt.subplots()
# (book source: ch08_matplotlib.tex, line 431)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with NameError.

for ax in axs.flat:
    ax.grid(True, linestyle=':')
