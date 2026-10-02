# Scientific Arrays with NumPy -- Code 7.9: Numerical differentiation of y = sin(x)
# (book source: ch07_arrays_numpy.tex, line 484)

import numpy as np

# 1. Create a fine grid for x and evaluate y = sin(x)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 2. Compute numerical derivative dy/dx using array differences
dx = np.diff(x)
dy = np.diff(y)
slope_approx = dy / dx

# 3. Midpoint x-coordinates corresponding to differences
x_mid = (x[:-1] + x[1:]) / 2

# 4. Compare numerical slope with exact derivative cos(x)
exact_slope = np.cos(x_mid)
max_error = np.max(np.abs(slope_approx - exact_slope))
print(f"Maximum difference between dy/dx and cos(x): {max_error:.6f}")
