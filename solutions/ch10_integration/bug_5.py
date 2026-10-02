"""Bug 10.5 -- np.arange(0, 25, 5) stops BEFORE 25, giving 5 times for 6 speeds.

Fix: make the stop value one step past the last time.
"""
import numpy as np
from scipy.integrate import trapezoid
t = np.arange(0, 30, 5)            # 0, 5, 10, 15, 20, 25
v = np.array([0, 8, 15, 22, 28, 30])
total_distance = trapezoid(v, t)
print(total_distance)   # Output: 440.0 m
