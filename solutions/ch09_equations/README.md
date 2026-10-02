# Chapter 9 — Solving Nonlinear Equations — Solutions

## Multiple-choice answers

Q1: (b), Q2: (b), Q3: (a), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** Bisection takes an interval where a continuous function changes signs and repeatedly divides it in half, narrowing down the location of the root.
- **S2.** Newton-Raphson uses tangent lines. If the guess is near a local extremum, the slope is close to zero ($f'(x) 0$), sending the next guess to infinity and causing divergence.
- **S3.** Numerical tolerance is the acceptable threshold of error. A zero tolerance cannot be achieved because computers use finite-precision floating-point numbers.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: All real roots of x^4 - 3x^2 - 4 by bisection. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Secant method, compared with bisection and Newton-Raphson on x^3 - x - 2. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Intersection of y = x^2 and y = 3x - 1 with fsolve. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Bisection with a verbose=True option (see common.bisect). |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 9.1 -- three problems. |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 9.2 -- the starting guess x0 = 0 is where f'(x) = 3x^2 = 0, so the first |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 9.3 -- the updates are swapped. |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 9.4 -- fsolve needs a Python function, not a string (TypeError: 'str' |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 9.5 -- xtol=0.1 only asks for the root to within 0.1. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 9: Both release angles that land a shot put at 20 m. |

Helper module(s) used by the solutions above: `common.py`.
