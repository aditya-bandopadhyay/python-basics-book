# Solving Nonlinear Equations -- Code 9.3: Bisection vs Newton-Raphson convergence
# (book source: ch09_equations.tex, line 206)
# NOTE: Needs code from earlier listings in this chapter (included below as setup).

# ---- setup: code from earlier in the chapter ----
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

# ---- the listing itself ----
# Uses bisect() and newton() from Codes 9.1 and 9.2: run those first
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1

root, errors = bisect(f, 1, 2)
root_nr, errors_nr = newton(f, df, x0=1.5)

fig, ax = plt.subplots(figsize=(8, 4))
ax.semilogy(errors,    marker='o', label='Bisection')
ax.semilogy(errors_nr, marker='s', label='Newton-Raphson')
ax.set_xlabel('Iteration'); ax.set_ylabel('Error measure (log scale)')
ax.set_title('Convergence Comparison'); ax.legend(); ax.grid(True)
plt.tight_layout(); plt.savefig('fig09-01-convergence.pdf')
