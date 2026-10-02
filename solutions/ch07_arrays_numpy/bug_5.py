"""Bug 7.5 -- b = a does not copy the array; both names refer to the same data.

Fix: make an independent copy with .copy().
"""
import numpy as np
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 99
print(a)   # Output: [1 2 3]
print(b)   # Output: [99  2  3]
