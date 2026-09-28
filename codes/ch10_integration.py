# Chapter 10: Numerical Integration and Centroids
import numpy as np

# 1. Trapezoidal Rule from Scratch
def trapz_scratch(x, y):
    h = x[1] - x[0]
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

x = np.linspace(0, np.pi, 100)
y = np.sin(x)
print(f"Integral of sin(x) from 0 to pi: {trapz_scratch(x, y):.6f} (Exact: 2.0)")

# 2. Cumulative Integration (np.cumsum)
v = np.array([0, 5, 10, 15, 20])  # velocity (m/s)
dt = 1.0  # time step (s)
position = np.cumsum(v) * dt
print(f"Position sequence: {position}")

# 3. Centroid of a Parabolic Curve
x_parab = np.linspace(0, 2, 200)
y_parab = 4 - x_parab**2
area = np.trapz(y_parab, x_parab)
moment_x = np.trapz(x_parab * y_parab, x_parab)
x_centroid = moment_x / area
print(f"Centroid x-coordinate: {x_centroid:.4f}")
