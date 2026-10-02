"""D4: Rosenbrock function with Nelder-Mead and BFGS."""
import numpy as np
from scipy.optimize import minimize

def rosen(p):
    x, y = p
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

for method in ["Nelder-Mead", "BFGS"]:
    res = minimize(rosen, x0=[-1.2, 1.0], method=method)
    print(f"{method:12s} minimum at ({res.x[0]:.5f}, {res.x[1]:.5f}), "
          f"iterations = {res.nit}, function evaluations = {res.nfev}")
# BFGS uses gradient information and needs far fewer iterations than Nelder-Mead.
