# Scientific Arrays with NumPy -- Code 7.3: 2-D arrays and slicing
# (book source: ch07_arrays_numpy.tex, line 134)

import numpy as np

M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(M.shape)    # (3, 3)
print(M[1, 2])    # 6     (row 1, column 2)
print(M[:, 0])    # [1 4 7]  (all rows, column 0)
print(M[0, :])    # [1 2 3]  (row 0, all columns)
