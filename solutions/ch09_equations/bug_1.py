"""Bug 9.1 -- three problems.

1. 'b = a' should be 'b = m': the bracket must shrink towards the midpoint.
2. 'while True' has no stopping test, so even a correct update loops forever.
3. If the midpoint lands exactly on the root (here m = 1 on the first step),
   f(a) * f(m) is 0, the code moves a to the root and then walks away from it.
   Return m as soon as f(m) == 0.
"""
def bisect_fixed(f, a, b, tol=1e-10):
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

print(bisect_fixed(lambda x: x - 1, 0, 2))     # Output: 1.0
print(round(bisect_fixed(lambda x: x ** 2 - 2, 0, 2), 8))   # Output: 1.41421356
