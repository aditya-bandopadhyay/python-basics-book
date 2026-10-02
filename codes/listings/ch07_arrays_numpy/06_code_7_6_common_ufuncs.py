# Scientific Arrays with NumPy -- Code 7.6: Common ufuncs
# (book source: ch07_arrays_numpy.tex, line 391)

import numpy as np

x = np.linspace(0, 2 * np.pi, 5)
print(np.sin(x).round(2))   # [ 0.  1.  0. -1. -0.]  (-0. is just a tiny negative rounded)
print(np.exp([0, 1, 2]))    # [1.         2.71828183 7.3890561 ]
print(np.sqrt([4, 9, 16]))  # [2. 3. 4.]
