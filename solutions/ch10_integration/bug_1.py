"""Bug 10.1 -- the arguments are swapped: trapezoid wants (y, x).

trapezoid(x, y) integrates x with respect to y, giving about 666.7.
"""
import numpy as np
from scipy.integrate import trapezoid
x = np.linspace(0, 10, 50)
y = x ** 2
area = trapezoid(y, x)
print(area)   # Output: about 333.4 (exact 1000/3)
