"""Bug 7.1 -- ** is not defined for Python lists (TypeError).

Fix: convert the list to a NumPy array first.
"""
import numpy as np
data = np.array([1, 2, 3, 4])
result = data ** 2
print(result)   # Output: [ 1  4  9 16]
