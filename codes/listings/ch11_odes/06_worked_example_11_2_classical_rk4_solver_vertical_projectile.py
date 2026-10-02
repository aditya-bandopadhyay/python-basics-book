# Ordinary Differential Equations -- Worked Example 11.2: Classical RK4 Solver - Vertical Projectile with Air Resistance
# (book source: ch11_odes.tex, line 416)

import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.81
m = 0.2
k_drag = 0.005
v0 = 30.0

# Derivative function dv/dt = f(t, v)
def acceleration(t, v):
    return -g - (k_drag / m) * v * abs(v)

# Time grid
h = 0.1
t = np.arange(0, 2.5 + h, h)
N = len(t)
v_rk4 = np.zeros(N)
v_rk4[0] = v0

# Step 1: Classical RK4 Integration Loop
for n in range(N - 1):
    tn = t[n]
    vn = v_rk4[n]
    
    k1 = acceleration(tn, vn)
    k2 = acceleration(tn + 0.5 * h, vn + 0.5 * h * k1)
    k3 = acceleration(tn + 0.5 * h, vn + 0.5 * h * k2)
    k4 = acceleration(tn + h, vn + h * k3)
    
    v_rk4[n + 1] = vn + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

print(f"Initial Velocity:   {v_rk4[0]:.2f} m/s")
print(f"Velocity at t=1.0s: {v_rk4[10]:.4f} m/s")
print(f"Velocity at t=2.0s: {v_rk4[20]:.4f} m/s")

# Output:
# Initial Velocity:   30.00 m/s
# Velocity at t=1.0s: 10.6165 m/s
# Velocity at t=2.0s: -0.0642 m/s
