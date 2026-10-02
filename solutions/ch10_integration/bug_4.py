"""Bug 10.4 -- the centroid is MOMENT / AREA, not area / moment."""
import numpy as np
from scipy.integrate import trapezoid
x = np.linspace(0, 2, 200)
y = 4 - x ** 2
numerator = trapezoid(x * y, x)
area = trapezoid(y, x)
x_centroid = numerator / area
print(round(x_centroid, 4))   # Output: 0.75
