"""Helper: import the chapter's app (Code 17.1) from codes/ch17_ode_visualizer.py."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "codes"))
from ch17_ode_visualizer import OdeVisualizerApp, rk4   # noqa: E402,F401
import numpy as np


def rk4_system(f, y0, t_start, t_end, h):
    """RK4 for a system: y0 is a list, f returns a list (Chapter 11, DIY D3)."""
    t = np.arange(t_start, t_end + h / 2, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(len(t) - 1):
        k1 = np.array(f(t[i], y[i]))
        k2 = np.array(f(t[i] + h / 2, y[i] + h / 2 * k1))
        k3 = np.array(f(t[i] + h / 2, y[i] + h / 2 * k2))
        k4 = np.array(f(t[i] + h, y[i] + h * k3))
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, y
