# Solving Nonlinear Equations -- Code 9.4: scipy equivalents
# (book source: ch09_equations.tex, line 248)

import numpy as np
from scipy.optimize import brentq, newton as sp_newton

f  = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1

# brentq: robust bracketing method (like bisection but faster)
root_bq = brentq(f, 1, 2, xtol=1e-10)

# newton: Newton-Raphson (or secant if fprime not given)
root_sp = sp_newton(f, x0=1.5, fprime=df, tol=1e-10)

print(f"Brentq root: {root_bq:.10f}")
print(f"SciPy Newton root: {root_sp:.10f}")
