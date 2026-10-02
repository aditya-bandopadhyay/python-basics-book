# Scientific Arrays with NumPy -- Code 7.2: Array creation functions
# (book source: ch07_arrays_numpy.tex, line 94)

import numpy as np

zeros_arr = np.zeros(5)           # [0. 0. 0. 0. 0.]
ones_mat = np.ones((2, 3))        # 2x3 matrix of 1.0
step_range = np.arange(0, 10, 2)  # [0 2 4 6 8]
lin_grid = np.linspace(0, 1, 5)   # [0.   0.25 0.5  0.75 1.  ]
