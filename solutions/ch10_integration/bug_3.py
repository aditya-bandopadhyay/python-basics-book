"""Bug 10.3 -- np.cumsum adds up speeds, not distances.

Each step covers speed x time, so multiply by dt. A plain cumsum is the
rectangle rule; cumulative_trapezoid is more accurate.
"""
import numpy as np
from scipy.integrate import cumulative_trapezoid

dt = 0.5
t = np.arange(0, 5 + dt, dt)
v = 3 * t
print(np.cumsum(v) * dt)                               # rectangle rule: 41.25 at t = 5
print(cumulative_trapezoid(v, t, initial=0))           # trapezoid: 37.5 at t = 5 (exact)
