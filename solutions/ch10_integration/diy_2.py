"""D2: Full centroid (x_bar, y_bar) of the plate under y = 4 - x^2, 0 <= x <= 2.

Exact values: area = 16/3, x_bar = 3/4, y_bar = (1/2) * (256/15) / (16/3) = 1.6.
"""
import numpy as np
from scipy.integrate import trapezoid

x = np.linspace(0, 2, 2001)
y = 4 - x ** 2

area = trapezoid(y, x)
x_bar = trapezoid(x * y, x) / area
y_bar = 0.5 * trapezoid(y ** 2, x) / area
print(f"Area = {area:.5f}  (exact 5.33333)")
print(f"Centroid = ({x_bar:.5f}, {y_bar:.5f})  (exact (0.75, 1.6))")
