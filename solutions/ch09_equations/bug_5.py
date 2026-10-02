"""Bug 9.5 -- xtol=0.1 only asks for the root to within 0.1.

Fix: ask for a tolerance far smaller than the precision you print.
"""
from scipy.optimize import brentq
root = brentq(lambda x: x ** 3 - x - 2, 1, 2, xtol=1e-12)
print(f'{root:.6f}')   # Output: 1.521380
