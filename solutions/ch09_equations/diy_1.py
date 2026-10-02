"""D1: All real roots of x^4 - 3x^2 - 4 by bisection.

x^4 - 3x^2 - 4 = (x^2 - 4)(x^2 + 1), so the real roots are x = -2 and x = 2.
"""
import numpy as np
import matplotlib.pyplot as plt
from common import bisect

f = lambda x: x ** 4 - 3 * x ** 2 - 4

x = np.linspace(-3, 3, 400)
fig, ax = plt.subplots()
ax.plot(x, f(x)); ax.axhline(0, color="gray", lw=0.8)
ax.set_xlabel("x"); ax.set_ylabel("f(x)"); ax.set_title("f(x) = x^4 - 3x^2 - 4")
fig.savefig("ch09_d1_plot.png", dpi=120)

# The plot shows one sign change on each side, e.g. in [-2.7, -1] and [1, 2.7]
for a, b in [(-2.7, -1), (1, 2.7)]:
    root, steps = bisect(f, a, b)
    print(f"Root in [{a}, {b}]: x = {root:.8f}  ({steps} steps)")
plt.show()
