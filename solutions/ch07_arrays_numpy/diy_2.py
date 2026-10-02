"""D2: 4x4 matrix with entry i*j, built by broadcasting."""
import numpy as np

col = np.arange(4).reshape(4, 1)   # shape (4, 1): 0, 1, 2, 3 down a column
row = np.arange(4)                 # shape (4,):   0, 1, 2, 3 along a row
M = col * row                      # broadcasting gives shape (4, 4)
print(M)
# Output:
# [[0 0 0 0]
#  [0 1 2 3]
#  [0 2 4 6]
#  [0 3 6 9]]
