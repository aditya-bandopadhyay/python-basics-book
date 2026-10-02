# Numerical Integration and Centroids -- Code 10.2: Cumulative position trajectory
# (book source: ch10_integration.tex, line 199)

import numpy as np
from scipy.integrate import cumulative_trapezoid

dt = 0.5   # 0.5-second time step
t = np.arange(0, 5.5, dt)
v = 3.0 * t  # Speed increasing at 3 m/s^2

# Running position with cumulative trapezoid (initial position = 0)
pos = cumulative_trapezoid(v, t, initial=0)

print(f"Time steps (s):  {t}")
print(f"Position at t (m): {np.round(pos, 2)}")
print(f"Final distance:   {pos[-1]:.2f} m (Exact 0.5*a*t^2 = {0.5*3*5**2:.2f} m)")
