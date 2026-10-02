"""Bug 13.4 -- minimize_scalar MINIMISES, so it finds the lowest revenue (at the
edge of the range). To find a maximum, minimise the negative.
"""
from scipy.optimize import minimize_scalar

def revenue(p):
    return p * (200 - 20 * (p - 10))

res = minimize_scalar(lambda p: -revenue(p), bounds=(1, 20), method='bounded')
print(f"Best price: Rs. {res.x:.2f}, revenue Rs. {revenue(res.x):.0f}")   # Rs. 10.00, 2000
