"""
Numerical Integration and Centroids -- companion script for Chapter 10.
Runs the chapter's listings in the order they appear in the book.
Listings that need keyboard input, or that are fragments / deliberate
mistakes, are skipped here; every listing is in codes/listings/ch10_integration/.
Run from the repository root:  python codes/ch10_integration.py
"""

# ======================================================================
# Code 10.1: Trapezoidal rule from scratch
# ======================================================================
def trapezoid_scratch(f, a, b, n=100):
    """Integrate f(x) from a to b across n equal panels."""
    dx = (b - a) / n
    # Endpoints carry half weight; interior points carry full weight
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * dx)
    return total * dx

# Test: Integral of x^2 from 0 to 3 (exact analytical answer = 9.0)
f = lambda x: x**2
approx = trapezoid_scratch(f, 0, 3, n=100)
print(f"Trapezoidal approximation: {approx:.6f}")
print(f"Discretization error:     {abs(approx - 9.0):.2e}")

# ======================================================================
# From Scratch to SciPy: scipy.integrate.trapezoid: skipped here (is a fragment / deliberate mistake); see codes/listings/ch10_integration/02_from_scratch_to_scipy_scipy_integrate_trapezoid.py
# ======================================================================

# ======================================================================
# Code 10.2: Cumulative position trajectory
# ======================================================================
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

# ======================================================================
# Worked Example 10.1: Automotive Telemetry - Distance Integration from CAN-Bus Speed Logs
# ======================================================================
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid, cumulative_trapezoid

# OBD-II / CAN-bus vehicle speed telemetry log (t in s, v in m/s)
t_log = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40])
v_log = np.array([0, 6.2, 14.5, 22.8, 28.1, 29.5, 29.8, 25.0, 12.0])

# Compute total integrated distance over 40 seconds
total_distance = trapezoid(v_log, t_log)

# Running (cumulative) distance at every telemetry timestep
dist_cumulative = cumulative_trapezoid(v_log, t_log, initial=0)

print(f"Total Integrated Distance: {total_distance:.2f} meters")
print(f"Final Telemetry Speed:     {v_log[-1]:.1f} m/s")

# Output:
# Total Integrated Distance: 809.50 meters
# Final Telemetry Speed:     12.0 m/s

# ======================================================================
# Worked Example 10.1: Automotive Telemetry - Distance Integration from CAN-Bus Speed Logs
# ======================================================================
log = np.loadtxt("data/telemetry_speed.csv", delimiter=",", skiprows=1)
t_log, v_log = log[:, 0], log[:, 1]      # first and second columns

# ======================================================================
# Worked Example 10.2: Land Surveying - Irregular Property Area & Centroid Location
# ======================================================================
import numpy as np
from scipy.integrate import trapezoid

# Surveyor field measurements along riverbank (meters)
x_survey = np.array([0, 5, 10, 15, 20, 25, 30])
y_survey = np.array([4.2, 6.8, 8.1, 7.5, 5.9, 3.0, 0.0])

# 1. Total Land Area: Integral of y dx
land_area = trapezoid(y_survey, x_survey)

# 2. First Moment of Area: Integral of x * y dx
first_moment_x = trapezoid(x_survey * y_survey, x_survey)

# 3. Centroid x-coordinate: First Moment / Area
x_centroid = first_moment_x / land_area

print(f"Total Property Land Area: {land_area:.2f} m^2")
print(f"Centroid x-coordinate:    {x_centroid:.2f} meters")

# Output:
# Total Property Land Area: 167.00 m^2
# Centroid x-coordinate:    12.59 meters

# ======================================================================
# Worked Example 10.3: Arc Length of a Curve using scipy.integrate.quad
# ======================================================================
import numpy as np
import scipy.integrate as integrate

# Define arc length integrand: f(x) = sqrt(1 + cos^2(x))
integrand = lambda x: np.sqrt(1.0 + np.cos(x)**2)

# Compute definite integral over [0, pi] using QUADPACK
arc_length, abs_error = integrate.quad(integrand, 0, np.pi)

# Compare with baseline straight line distance between (0,0) and (pi,0)
straight_line = np.pi

print(f"Calculated Arc Length L: {arc_length:.6f}")
print(f"Straight Line Distance:   {straight_line:.6f}")
print(f"Curvature Stretch Ratio:  {arc_length / straight_line:.4f}")
print(f"SciPy Estimated Error:   {abs_error:.2e}")

# Output:
# Calculated Arc Length L: 3.820198
# Straight Line Distance:   3.141593
# Curvature Stretch Ratio:  1.2160
# SciPy Estimated Error:   1.30e-13

# ======================================================================
# Worked Example 10.4: Double Integration - Volume Under a Curved Surface
# ======================================================================
import scipy.integrate as integrate

# 2D Surface function z = f(x, y)
surface_z = lambda y, x: x**2 + y**2

# Double integration bounds: y from 0 to 2, x from 0 to 1
volume, err = integrate.dblquad(surface_z, 0, 1, lambda x: 0, lambda x: 2)

# Analytical exact integration: integral_0^1 [2*x^2 + 8/3] dx = 2/3 + 8/3 = 10/3
volume_exact = 10.0 / 3.0

print(f"Numerical Surface Volume:  {volume:.6f}")
print(f"Exact Analytical Volume:   {volume_exact:.6f}")
print(f"Absolute Discrepancy:      {abs(volume - volume_exact):.2e}")

# Output:
# Numerical Surface Volume:  3.333333
# Exact Analytical Volume:   3.333333
# Absolute Discrepancy:      4.44e-16
