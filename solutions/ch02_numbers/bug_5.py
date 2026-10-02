"""Bug 2.5 -- floating-point numbers are approximations.

0.1 + 0.2 is stored as 0.30000000000000004, so == 0.3 is False.
Fix: compare with a tolerance, using math.isclose (or round both sides).
"""
import math
total = 0.1 + 0.2
print(math.isclose(total, 0.3))   # Output: True
print(round(total, 10) == 0.3)    # Output: True
