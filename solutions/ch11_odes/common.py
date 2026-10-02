"""Euler and RK4 solvers that work for single equations AND systems (DIY D3)."""
import numpy as np

def euler(f, y0, t_start, t_end, h):
    t = np.arange(t_start, t_end + h / 2, h)
    y = np.zeros((len(t), np.size(y0)))
    y[0] = y0
    for i in range(len(t) - 1):
        y[i + 1] = y[i] + h * np.asarray(f(t[i], y[i]))
    return t, y.squeeze()

def rk4(f, y0, t_start, t_end, h):
    """Classical RK4. y0 may be a number or a list/array (a system)."""
    t = np.arange(t_start, t_end + h / 2, h)
    y = np.zeros((len(t), np.size(y0)))
    y[0] = y0
    for i in range(len(t) - 1):
        k1 = np.asarray(f(t[i], y[i]))
        k2 = np.asarray(f(t[i] + h / 2, y[i] + h / 2 * k1))
        k3 = np.asarray(f(t[i] + h / 2, y[i] + h / 2 * k2))
        k4 = np.asarray(f(t[i] + h, y[i] + h * k3))
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, y.squeeze()
