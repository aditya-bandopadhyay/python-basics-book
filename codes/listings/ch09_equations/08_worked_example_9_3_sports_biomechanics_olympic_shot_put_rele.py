# Solving Nonlinear Equations -- Worked Example 9.3: Sports Biomechanics - Olympic Shot Put Release Angle Solver
# (book source: ch09_equations.tex, line 457)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Physical constants for Olympic shot put
h0 = 2.0         # Release height above ground (m)
v0 = 13.5        # Initial release speed (m/s)
g  = 9.81        # Gravitational acceleration (m/s^2)
d_target = 20.0  # Target distance mark (m)

# Trajectory height y(x; theta) in degrees
def trajectory(x, theta_deg):
    rad = np.radians(theta_deg)
    return h0 + x * np.tan(rad) - (g * x**2) / (2 * v0**2 * (np.cos(rad)**2))

# Residual function: f(theta) = landing height at target distance d_target
f_shot = lambda theta_deg: trajectory(d_target, theta_deg)

# Solve for required release angle theta using Brent's method
theta_opt = brentq(f_shot, 30.0, 40.0)

# Calculate landing distance of a standard 45-degree throw
landing_45 = brentq(lambda x: trajectory(x, 45.0), 15.0, 25.0)

print(f"Optimal Release Angle:  {theta_opt:.2f} deg (Lands exact at {d_target:.1f}m)")
print(f"Standard 45 deg Throw:  Lands at {landing_45:.2f}m")

# Output:
# Optimal Release Angle:  35.31 deg (Lands exact at 20.0m)
# Standard 45 deg Throw:  Lands at 20.40m
