# Chapter 13 — Optimization and Curve Fitting — Solutions

## Multiple-choice answers

Q1: (b), Q2: (b), Q3: (b), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** Walking downhill in fog corresponds to evaluating local derivative ${dJ}{d}$ and stepping in the opposite direction toward lower cost values.
- **S2.** Least-squares sums squared residuals $(y_i - f(x_i))^2$, penalizing large deviations between model predictions and experimental points.
- **S3.** $_{{new}} = _{{old}} - {dJ}{d}$.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Fit y = a x^2 + b x + c by gradient descent (three parameters). |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Stochastic gradient descent (one random point per update) vs full batch. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Fit Newton cooling T(t) = 20 + A exp(-lambda t) to coffee measurements. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Rosenbrock function with Nelder-Mead and BFGS. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 13.1 -- the step is far too large. With learning rate 10 and SUMMED (not |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 13.2 -- p0=[] gives curve_fit zero starting values for a model with one |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 13.3 -- x is in the thousands, so x*(y - y_pred) is huge and a learning |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 13.4 -- minimize_scalar MINIMISES, so it finds the lowest revenue (at the |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 13.5 -- with p0 = [0.001, 0.001] the model starts almost flat at zero, far |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 13: Least-time light path from air (n = 1.00) into glass (n = 1.50). |
