"""Bug 7.4 -- M[1] picks a single row.

Fix: the slice M[1:3] picks rows 1 and 2 (the stop index 3 is not included).
"""
import numpy as np
M = np.arange(9).reshape(3, 3)
sub = M[1:3]
print(sub)
# Output:
# [[3 4 5]
#  [6 7 8]]
