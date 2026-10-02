# Numerical Integration and Centroids -- Worked Example 10.3: Arc Length of a Curve using scipy.integrate.quad
# (book source: ch10_integration.tex, line 376)

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
