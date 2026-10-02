"""Bug 7.2 -- M[1] is ROW 1, not column 1.

Fix: M[:, 1] means "all rows, column 1".
"""
import numpy as np
M = np.array([[1, 2, 3], [4, 5, 6]])
col = M[:, 1]
print(col)   # Output: [2 5]
