"""Bug 7.3 -- shapes (3,) and (4,) cannot be broadcast: the trailing sizes differ
and neither is 1.

Fix (one option): make the arrays the same length. Another option is to make one
of them a column, (3, 1) + (4,) -> a (3, 4) table of sums.
"""
import numpy as np
a = np.ones(3)
b = np.ones(3)
print(a + b)                          # Output: [2. 2. 2.]

table = np.ones(3).reshape(3, 1) + np.ones(4)
print(table.shape)                    # Output: (3, 4)
