# Scientific Arrays with NumPy -- Code 7.7: Masks, reshape, and axis
# (book source: ch07_arrays_numpy.tex, line 408)

import numpy as np

temps = np.array([21.5, 34.0, 28.2, 41.7, 19.9, 36.4])

hot = temps > 30              # a Boolean mask: True where the test holds
print(hot)
print(temps[hot])             # keep only the True positions
print(np.sum(hot))            # True counts as 1, so this counts them

capped = temps.copy()
capped[capped > 40] = 40.0    # change only the selected elements
print(capped)

grid = np.arange(6).reshape(2, 3)   # 6 numbers -> 2 rows, 3 columns
print(grid)
print(grid.sum(axis=0))       # down each column
print(grid.sum(axis=1))       # along each row
print(np.argmax(temps))       # index of the largest value

# Output:
# [False  True False  True False  True]
# [34.  41.7 36.4]
# 3
# [21.5 34.  28.2 40.  19.9 36.4]
# [[0 1 2]
#  [3 4 5]]
# [3 5 7]
# [ 3 12]
# 3
