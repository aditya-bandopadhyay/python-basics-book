# Solving Nonlinear Equations -- Code 9.5: System solved with fsolve
# (book source: ch09_equations.tex, line 318)

import numpy as np
from scipy.optimize import fsolve

def system(vars):
    x, y = vars
    return [x**2 + y**2 - 4,   # circle of radius 2
            x - y - 1]          # line

sol = fsolve(system, x0=[1, 0])
print(f'x = {sol[0]:.6f}, y = {sol[1]:.6f}')
# Verify: plug back in
print('Residual:', system(sol))
