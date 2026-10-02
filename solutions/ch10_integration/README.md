# Chapter 10 — Numerical Integration and Centroids — Solutions

## Multiple-choice answers

Q1: (b), Q2: (b), Q3: (a), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** The Trapezoidal Rule uses slanted lines connecting adjacent points $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$, hugging smooth curves closely unlike flat rectangular boxes.
- **S2.** Cumulative integration (`np.cumsum`) accumulates area step-by-step to compute position $y(t) = y_0 + v() d$, forming an initial value problem.
- **S3.** Compute total area $A = y \, dx$ using `trapezoid(y, x)` and moment $M_x = x y \, dx$ using `trapezoid(x*y, x)` (from `scipy.integrate`); by symmetry the answer is ${x} = 0$. The centroid is ${x} = M_x / A$.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Trapezoidal estimate of the integral of sin x on [0, pi] (exact value 2). |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Full centroid (x_bar, y_bar) of the plate under y = 4 - x^2, 0 <= x <= 2. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Distance from unevenly spaced speed readings. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Simpson's rule from scratch vs the trapezoidal rule on sin x over [0, pi]. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 10.1 -- the arguments are swapped: trapezoid wants (y, x). |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 10.2 -- each trapezoid's area is the AVERAGE height times the width. |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 10.3 -- np.cumsum adds up speeds, not distances. |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 10.4 -- the centroid is MOMENT / AREA, not area / moment. |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 10.5 -- np.arange(0, 25, 5) stops BEFORE 25, giving 5 times for 6 speeds. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 10: Area and centroid of a pond-side plot from survey offsets. |
