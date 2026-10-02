"""D1: Trapezoidal estimate of the integral of sin x on [0, pi] (exact value 2)."""
import numpy as np
from scipy.integrate import trapezoid

for N in [10, 100, 1000]:
    x = np.linspace(0, np.pi, N)
    estimate = trapezoid(np.sin(x), x)
    print(f"N = {N:5d}: estimate = {estimate:.10f}, error = {abs(estimate - 2):.2e}")
# The error falls by about 100x for every 10x more points: O(dx^2).
