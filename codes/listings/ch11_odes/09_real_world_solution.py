# Ordinary Differential Equations -- Real-World Solution
# (book source: ch11_odes.tex, line 633)

import numpy as np

def rk4(f, y0, t_start, t_end, h):
    """Fourth-order Runge-Kutta solver (Code 11.3)."""
    t = np.arange(t_start, t_end + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(len(t) - 1):
        k1 = f(t[i],        y[i])
        k2 = f(t[i] + h/2,  y[i] + h/2 * k1)
        k3 = f(t[i] + h/2,  y[i] + h/2 * k2)
        k4 = f(t[i] + h,    y[i] + h   * k3)
        y[i+1] = y[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    return t, y

T_room, T0 = 20.0, 90.0

# Step 1: the measurement T(5) = 70 fixes the cooling constant k
k = np.log((T0 - T_room) / (70.0 - T_room)) / 5.0
print(f"Cooling constant k = {k:.4f} per minute")

# Step 2: step forward with RK4 and find the first time T <= 40
f_cool = lambda t, T: -k * (T - T_room)
t, T = rk4(f_cool, T0, 0, 60, h=0.01)
first = np.argmax(T <= 40.0)          # index of the first True
print(f"RK4: coffee reaches 40 C after about {t[first]:.1f} minutes")

# Step 3: check against the exact solution T = 20 + 70 exp(-k t)
t_exact = np.log((T0 - T_room) / (40.0 - T_room)) / k
print(f"Exact formula gives {t_exact:.1f} minutes")

# Output:
# Cooling constant k = 0.0673 per minute
# RK4: coffee reaches 40 C after about 18.6 minutes
# Exact formula gives 18.6 minutes
