# Scientific Arrays with NumPy -- Code 7.5: Matrix multiplication with @
# (book source: ch07_arrays_numpy.tex, line 309)

import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
C = A @ B          # same as np.dot(A, B)
print(C)           # [[19 22]
                   #  [43 50]]
