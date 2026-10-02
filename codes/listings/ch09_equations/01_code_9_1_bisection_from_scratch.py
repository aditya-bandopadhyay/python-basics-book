# Solving Nonlinear Equations -- Code 9.1: Bisection from scratch
# (book source: ch09_equations.tex, line 95)

import numpy as np

def bisect(f, a, b, tol=1e-10, max_iter=100):
    """Find root of f in [a,b] by bisection."""
    if f(a) * f(b) > 0:
        raise ValueError('f(a) and f(b) must have opposite signs')
    errors = []
    for i in range(max_iter):
        m = (a + b) / 2.0
        errors.append(abs(b - a) / 2)
        if abs(f(m)) < tol or (b - a) / 2 < tol:
            return m, errors
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2, errors

# Example: find root of x^3 - x - 2 = 0
f = lambda x: x**3 - x - 2      # a one-line function (Section 6.6)
root, errors = bisect(f, 1, 2)
print(f'Root found: {root:.10f}')
print(f'Iterations: {len(errors)}')
print(f'Final error bound: {errors[-1]:.2e}')
