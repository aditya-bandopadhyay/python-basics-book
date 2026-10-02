"""D2: Secant method, compared with bisection and Newton-Raphson on x^3 - x - 2."""
from common import bisect, newton

def secant(f, x0, x1, tol=1e-12, max_iter=50):
    for k in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x2 - x1) < tol:
            return x2, k
        x0, x1 = x1, x2
    return x1, max_iter

f = lambda x: x ** 3 - x - 2
df = lambda x: 3 * x ** 2 - 1

for name, (root, steps) in [("Bisection", bisect(f, 1, 2, tol=1e-12)),
                            ("Newton", newton(f, df, 1.5)),
                            ("Secant", secant(f, 1.0, 2.0))]:
    print(f"{name:10s} root = {root:.12f}  steps = {steps}")
# Bisection needs about 40 steps; secant (order ~1.6) needs a few more than Newton
# (order 2) but never needs the derivative.
