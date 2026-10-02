# Chapter 8 — Visualizing Data with Matplotlib — Solutions

## Multiple-choice answers

Q1: (a), Q2: (b), Q3: (b), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** A `Figure` is the outer window or canvas containing all plots. An `Axes` represents a single subplot container inside that canvas where data is plotted.
- **S2.** Without labels and units, readers cannot determine the scale or physical significance of the data, rendering the visualization unhelpful.
- **S3.** Starting the y-axis at a non-zero value is useful when highlighting tiny, critical fluctuations (e.g., room temperature changes). To prevent misinterpretation, clearly note the truncated axis in the caption.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Damped sine e^(-x) sin(4 pi x), saved to damped_sine.pdf. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Histogram of 1000 standard-normal samples with the theoretical PDF. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: 2x2 grid of sin, cos, clipped tan, and |sin|, with a shared x-axis. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Dual-axis chart of temperature and pressure with ax.twinx(). |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 8.1 -- Axes objects have no show() method (AttributeError). |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 8.2 -- the bars are drawn at positions 0, 1, 2 with numeric tick labels. |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 8.3 -- a legend needs labels on the lines AND a call to ax.legend(). |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 8.4 -- after the window is closed, plt.show() has finished with the figure, |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 8.5 -- plt.scatter(y, x) puts y on the horizontal axis. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 8: Climate dashboard (monthly normals for Kolkata, approximate). |
