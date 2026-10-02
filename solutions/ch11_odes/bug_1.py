"""Bug 11.1 -- on the last pass, i = len(t) - 1 and y[i+1] is past the end (IndexError).

Fix: loop over range(len(t) - 1). (Also, np.arange(t0, tf, h) stops before tf;
use tf + h to include the end time.)
"""
import numpy as np

def euler_fixed(f, y0, t0, tf, h):
    t = np.arange(t0, tf + h / 2, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(len(t) - 1):
        y[i + 1] = y[i] + h * f(t[i], y[i])
    return t, y

t, y = euler_fixed(lambda t, y: -y, 1.0, 0, 1, 0.1)
print(len(t), round(y[-1], 4))   # Output: 11 0.3487
