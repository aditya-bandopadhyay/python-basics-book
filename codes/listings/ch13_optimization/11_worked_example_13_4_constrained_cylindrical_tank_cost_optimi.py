# Optimization and Curve Fitting -- Worked Example 13.4: Constrained Cylindrical Tank Cost Optimization
# (book source: ch13_optimization.tex, line 576)

import numpy as np
import scipy.optimize as opt

# Cost parameters
c_base = 500.0    # Rs / m^2
c_wall = 300.0    # Rs / m^2
V_target = 1.0    # Target volume (m^3)

# Objective cost function to minimize: x = [r, h]
def cost_function(x):
    r, h = x
    area_base = np.pi * (r**2)
    area_top_sides = np.pi * (r**2) + 2.0 * np.pi * r * h
    return c_base * area_base + c_wall * area_top_sides

# Constraint: Volume equality V = pi * r^2 * h = 1.0 -> (pi * r^2 * h - 1.0) = 0
volume_constraint = {'type': 'eq', 'fun': lambda x: np.pi * (x[0]**2) * x[1] - V_target}

# Positivity bounds: r > 0.05, h > 0.05
bounds = [(0.05, None), (0.05, None)]

# Initial guess: r = 0.5 m, h = 1.0 m
x0 = [0.5, 1.0]

# Solve constrained optimization problem
res = opt.minimize(cost_function, x0, method='SLSQP', bounds=bounds, constraints=volume_constraint)

r_opt, h_opt = res.x
min_cost = res.fun

print(f"Optimal Tank Radius r*: {r_opt:.4f} m")
print(f"Optimal Tank Height h*: {h_opt:.4f} m")
print(f"Height-to-Radius Ratio: {h_opt / r_opt:.2f}")
print(f"Minimum Production Cost: Rs. {min_cost:.2f}")

# Output:
# Optimal Tank Radius r*: 0.4924 m
# Optimal Tank Height h*: 1.3130 m
# Height-to-Radius Ratio: 2.67
# Minimum Production Cost: Rs. 1827.88
