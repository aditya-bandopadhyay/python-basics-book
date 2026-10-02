"""Bug 12.4 -- np.corrcoef(x) correlates x with itself (1.0). Pass both arrays and
take the off-diagonal entry of the 2x2 matrix.
"""
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
r = np.corrcoef(x, y)[0, 1]
print(round(r, 4))   # Output: 0.7746
