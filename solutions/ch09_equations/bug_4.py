"""Bug 9.4 -- fsolve needs a Python function, not a string (TypeError: 'str'
object is not callable).
"""
from scipy.optimize import fsolve
result = fsolve(lambda x: x ** 2 - 4, 1.0)
print(result)   # Output: [2.]
