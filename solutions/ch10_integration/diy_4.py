"""D4: Simpson's rule from scratch vs the trapezoidal rule on sin x over [0, pi]."""
import numpy as np
from scipy.integrate import trapezoid

def simpson(f, a, b, n):
    """Composite Simpson's rule with n panels (n must be even)."""
    if n % 2:
        raise ValueError("n must be even")
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])

for n in [4, 10, 50]:
    x = np.linspace(0, np.pi, n + 1)
    trap = trapezoid(np.sin(x), x)
    simp = simpson(np.sin, 0, np.pi, n)
    print(f"{n + 1:3d} points: trapezoid error = {abs(trap - 2):.2e}, Simpson error = {abs(simp - 2):.2e}")
