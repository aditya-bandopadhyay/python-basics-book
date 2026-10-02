# Solving Nonlinear Equations -- Worked Example 9.4: Multivariable Non-linear System of Equations
# (book source: ch09_equations.tex, line 508)

import numpy as np
import scipy.optimize as opt

# Non-linear 2D system vector function
def system(vec):
    x, y = vec
    f1 = x**2 + y**2 - 4.0   # Circle constraint
    f2 = x * y - 1.0         # Hyperbola constraint
    return [f1, f2]

# Initial guess in first quadrant
x0 = [1.5, 0.5]

# Solve system using SciPy's 'hybr' (Powell hybrid) solver
sol = opt.root(system, x0, method='hybr')

x_sol, y_sol = sol.x
residuals = sol.fun

print(f"Intersection Point: x = {x_sol:.6f}, y = {y_sol:.6f}")
print(f"Residual Vector:   [{residuals[0]:.2e}, {residuals[1]:.2e}]")
print(f"Solver Success:    {sol.success}")

# Output:
# Intersection Point: x = 1.931852, y = 0.517638
# Residual Vector:   [1.33e-13, 6.86e-13]   (tiny; exact digits vary)
# Solver Success:    True
