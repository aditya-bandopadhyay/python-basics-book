"""Bug 11.5 -- one value is already in y, so only len(t) - 1 more steps are needed.

range(len(t) - 2) does one step too few.
"""
import numpy as np

def euler_fixed(f, y0, t):
    y = [y0]
    for i in range(len(t) - 1):
        y.append(y[-1] + (t[1] - t[0]) * f(t[i], y[-1]))
    return y

t = np.linspace(0, 1, 11)
y = euler_fixed(lambda t, y: -y, 1.0, t)
print(len(t), len(y))   # Output: 11 11
