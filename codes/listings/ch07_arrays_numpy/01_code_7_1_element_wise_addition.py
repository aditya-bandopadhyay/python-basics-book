# Scientific Arrays with NumPy -- Code 7.1: Element-wise addition
# (book source: ch07_arrays_numpy.tex, line 39)

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)    # [5 7 9]
print(a * b)    # [ 4 10 18]
print(a ** 2)   # [1 4 9]
print(a.dtype)  # int64 (int32 on some Windows set-ups)
