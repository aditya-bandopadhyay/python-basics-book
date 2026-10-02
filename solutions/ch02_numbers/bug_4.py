"""Bug 2.4 -- ^ is not "power" in Python.

Buggy:   side_a ^ 2 is bitwise XOR (3 ^ 2 == 1), so the result is sqrt(1 + 6) = 2.645...
Fix:     the power operator is **.
"""
import math
side_a = 3
side_b = 4
hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
print(hypotenuse)   # Output: 5.0
