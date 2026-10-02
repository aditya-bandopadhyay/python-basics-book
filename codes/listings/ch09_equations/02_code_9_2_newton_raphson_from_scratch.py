# Solving Nonlinear Equations -- Code 9.2: Newton-Raphson from scratch
# (book source: ch09_equations.tex, line 177)

import numpy as np

def newton(f, df, x0, tol=1e-10, max_iter=50):
    """Newton-Raphson root finder."""
    x = float(x0)
    errors = []
    for i in range(max_iter):
        fx = f(x)
        errors.append(abs(fx))
        if abs(fx) < tol:
            return x, errors
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError('Derivative is zero')
        x = x - fx / dfx
    return x, errors

f  = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1
root_nr, errors_nr = newton(f, df, x0=1.5)
print(f'Newton root: {root_nr:.10f}')
print(f'Iterations:  {len(errors_nr)}')
