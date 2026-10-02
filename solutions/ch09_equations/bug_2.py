"""Bug 9.2 -- the starting guess x0 = 0 is where f'(x) = 3x^2 = 0, so the first
Newton step divides by zero. (x = 0 also happens to be the root of x^3, but
the code never checks for that.)

Fix: stop as soon as f(x) is (nearly) zero, refuse to divide by a zero
derivative, and start away from flat points.
"""
def newton_fixed(f, df, x0, tol=1e-12, max_iter=100):
    x = x0
    for _ in range(max_iter):
        if abs(f(x)) < tol:
            return x
        d = df(x)
        if d == 0:
            raise ZeroDivisionError(f"f'(x) = 0 at x = {x}; choose another starting point")
        x = x - f(x) / d
    return x

print(newton_fixed(lambda x: x ** 3, lambda x: 3 * x ** 2, 0.0))   # Output: 0.0
print(newton_fixed(lambda x: x ** 3 - 8, lambda x: 3 * x ** 2, 1.0))  # Output: 2.0
