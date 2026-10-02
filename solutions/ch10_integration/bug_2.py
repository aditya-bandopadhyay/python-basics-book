"""Bug 10.2 -- each trapezoid's area is the AVERAGE height times the width.

Fix: divide (y[i] + y[i+1]) by 2.
"""
import numpy as np
from scipy.integrate import trapezoid

def trapezoid_fixed(y, dx):
    total = 0
    for i in range(len(y) - 1):
        total += (y[i] + y[i + 1]) / 2 * dx
    return total

x = np.linspace(0, 3, 101)
print(trapezoid_fixed(x ** 2, x[1] - x[0]), trapezoid(x ** 2, x))   # both about 9.00045
