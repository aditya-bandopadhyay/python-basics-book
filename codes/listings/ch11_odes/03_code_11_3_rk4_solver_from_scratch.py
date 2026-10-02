# Ordinary Differential Equations -- Code 11.3: RK4 solver from scratch
# (book source: ch11_odes.tex, line 205)

import numpy as np

def rk4(f, y0, t_start, t_end, h):
    """Fourth-order Runge-Kutta solver."""
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

k     = 0.05
T_env = 20.0
T0    = 90.0
f_cool = lambda t, T: -k * (T - T_env)

t_rk4, T_rk4 = rk4(f_cool, T0, 0, 60, h=5.0)
T_true = T_env + (T0 - T_env) * np.exp(-k * 60)
err = abs(T_rk4[-1] - T_true)
print(f'RK4  h=5.0  T(60)={T_rk4[-1]:.6f}  error={err:.2e}')
