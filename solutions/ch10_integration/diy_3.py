"""D3: Distance from unevenly spaced speed readings."""
import numpy as np
from scipy.integrate import trapezoid

t = np.array([0, 1, 3, 4, 8])
v = np.array([2.0, 2.5, 1.8, 3.0, 0.5])

s = trapezoid(v, t)
by_hand = sum((v[i] + v[i + 1]) / 2 * (t[i + 1] - t[i]) for i in range(len(t) - 1))
print(f"trapezoid(v, t) = {s:.2f} m")
print(f"panel by panel  = {by_hand:.2f} m")
# Output: both 15.95 m -- each panel uses its own width (1, 2, 1, 4 s).
