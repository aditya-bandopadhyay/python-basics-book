# Chapter 11 — Ordinary Differential Equations — Solutions

## Multiple-choice answers

Q1: (b), Q2: (a), Q3: (b), Q4: (a), Q5: (b).

## Short-answer hints

- **S1.** Euler's method evaluates slope $f(t_n, y_n)$ at current point and steps forward along the local tangent: $y_{n+1} = y_n + h f(t_n, y_n)$.
- **S2.** Cumulative integration sums rates $v(t)$ dependent only on time $t$. ODEs involve rates ${dy}{dt} = f(t, y)$ that depend dynamically on the state $y$ itself.
- **S3.** SciPy's `solve_ivp` calculates local error estimates at each step, shrinking $h$ in steep regions and expanding $h$ in smooth regions.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: SIR epidemic with Euler's method (beta = 0.3, gamma = 0.05, 200 days). |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Van der Pol oscillator (mu = 2): Euler, RK4 and solve_ivp. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: RK4 for systems -- see rk4() in common.py, which uses NumPy arrays for k1..k4. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Global error vs step size for Euler and RK4 (Newton cooling, 0..60 min). |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 11.1 -- on the last pass, i = len(t) - 1 and y[i+1] is past the end (IndexError). |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 11.2 -- sol.y has one ROW per variable: shape (1, number_of_times). |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 11.3 -- the 4th positional argument of solve_ivp is 'method', so 0.1 is |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 11.4 -- the derivatives must be returned in the SAME order as the state. |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 11.5 -- one value is already in y, so only len(t) - 1 more steps are needed. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 11: Large-angle pendulum with RK4 vs the small-angle approximation. |

Helper module(s) used by the solutions above: `common.py`.
