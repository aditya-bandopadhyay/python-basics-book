# Ordinary Differential Equations -- Worked Example 11.4: 2nd-Order Non-linear Damped Pendulum ODE System
# (book source: ch11_odes.tex, line 542)

import numpy as np
import scipy.integrate as integrate

g = 9.81
L = 1.0
gamma = 0.25

# 2-variable state vector y = [theta, omega]
def pendulum_system(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -gamma * omega - (g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

y0 = [np.pi / 2.0, 0.0]  # Initial state: 90 deg release from rest
t_span = (0.0, 10.0)
t_eval = np.linspace(0, 10, 300)

sol = integrate.solve_ivp(pendulum_system, t_span, y0, t_eval=t_eval, method='RK45')
theta_res, omega_res = sol.y

print(f"Initial Angle:        {np.degrees(theta_res[0]):.1f} deg")
print(f"First Swing Peak:     {np.degrees(np.min(theta_res)):.1f} deg")
print(f"Max Angular Velocity: {np.max(np.abs(omega_res)):.4f} rad/s")

# Output:
# Initial Angle:        90.0 deg
# First Swing Peak:     -76.3 deg
# Max Angular Velocity: 4.1335 rad/s
