"""D3: Intersection of y = x^2 and y = 3x - 1 with fsolve.

Algebra: x^2 = 3x - 1  ->  x^2 - 3x + 1 = 0  ->  x = (3 +/- sqrt(5)) / 2,
i.e. x = 0.381966 and x = 2.618034.
"""
import numpy as np
from scipy.optimize import fsolve

def system(v):
    x, y = v
    return [y - x ** 2, y - (3 * x - 1)]

for guess in ([0, 0], [3, 8]):
    x, y = fsolve(system, guess)
    print(f"start {guess}: x = {x:.6f}, y = {y:.6f}")

print("Exact x values:", (3 - np.sqrt(5)) / 2, (3 + np.sqrt(5)) / 2)
