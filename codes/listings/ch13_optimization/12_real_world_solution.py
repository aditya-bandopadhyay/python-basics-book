# Optimization and Curve Fitting -- Real-World Solution
# (book source: ch13_optimization.tex, line 689)

import numpy as np
from scipy.optimize import minimize_scalar

v1, v2 = 1.0, 1.0 / 1.333  # Light speeds in air and water

def transit_time(x):
    d1 = np.hypot(-2.0 - x, 1.5)
    d2 = np.hypot(1.5 - x, -1.5)
    return d1 / v1 + d2 / v2

res = minimize_scalar(transit_time, bounds=(-2.0, 1.5), method='bounded')
x_opt = res.x

# Verify Snell's Law: sin(theta1)/v1 == sin(theta2)/v2
sin_th1 = abs(-2.0 - x_opt) / np.hypot(-2.0 - x_opt, 1.5)
sin_th2 = abs(1.5 - x_opt) / np.hypot(1.5 - x_opt, -1.5)

print(f"Optimal interface crossing point: x* = {x_opt:.4f}")
print(f"Air Snell ratio   (sin theta1 / v1): {sin_th1 / v1:.4f}")
print(f"Water Snell ratio (sin theta2 / v2): {sin_th2 / v2:.4f}")

# Output:
# Optimal interface crossing point: x* = 0.2908
# Air Snell ratio   (sin theta1 / v1): 0.8366
# Water Snell ratio (sin theta2 / v2): 0.8366
