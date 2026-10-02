"""D3: RK4 for systems -- see rk4() in common.py, which uses NumPy arrays for k1..k4.

Test on the oscillator x'' = -x, x(0) = 1, v(0) = 0, whose exact solution is cos t.
"""
import numpy as np
from common import rk4

t, y = rk4(lambda t, s: [s[1], -s[0]], [1.0, 0.0], 0, 2 * np.pi, 0.01)
print(f"x(2 pi) = {y[-1, 0]:.8f}   (exact 1)")
print(f"max |x - cos t| = {np.max(np.abs(y[:, 0] - np.cos(t))):.2e}")
