# Scientific Arrays with NumPy -- Try It Yourself: Bicycle Ramp Elevation & Steepness Calculator
# (book source: ch07_arrays_numpy.tex, line 522)

import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
h = np.array([0.0, 0.2, 0.6, 1.2, 1.5, 1.6])

# Numerical slope = dh / dx
slope = np.diff(h) / np.diff(x)
print("Section Slopes (Rise / Run):", slope)
print(f"Steepest Section: {np.max(slope)*100:.1f}% grade")
