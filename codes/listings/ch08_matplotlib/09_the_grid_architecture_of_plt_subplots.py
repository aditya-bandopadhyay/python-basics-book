# Visualizing Data with Matplotlib -- The Grid Architecture of plt.subplots()
# (book source: ch08_matplotlib.tex, line 413)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with NameError.

fig, axs = plt.subplots(nrows, ncols, figsize=(width, height))
