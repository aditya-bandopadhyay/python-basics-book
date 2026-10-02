"""Mini-Project 10: Area and centroid of a pond-side plot from survey offsets."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40], dtype=float)
y = np.array([0.0, 3.1, 5.6, 7.9, 8.4, 7.2, 6.5, 3.8, 1.2])

def simpson_samples(y, h):
    """Simpson's rule on equally spaced samples (odd number of points)."""
    if len(y) % 2 == 0:
        raise ValueError("need an odd number of points")
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])

area = trapezoid(y, x)
x_bar = trapezoid(x * y, x) / area
y_bar = 0.5 * trapezoid(y ** 2, x) / area
area_simpson = simpson_samples(y, 5.0)
area_half = trapezoid(y[::2], x[::2])          # every other measurement

print(f"Area (trapezoid):        {area:.2f} m^2")
print(f"Area (Simpson):          {area_simpson:.2f} m^2")
print(f"Centroid:                ({x_bar:.2f} m, {y_bar:.2f} m)")
print(f"Area from every other point: {area_half:.2f} m^2 "
      f"(change {area_half - area:+.2f} m^2, {100 * (area_half - area) / area:+.1f}%)")

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.fill_between(x, y, color="tab:green", alpha=0.3, label=f"Plot, area = {area:.1f} m^2")
ax.plot(x, y, "o-", color="tab:green")
ax.plot(x_bar, y_bar, "ro", markersize=9, label=f"Centroid ({x_bar:.1f}, {y_bar:.1f})")
ax.set_xlabel("Distance along fence (m)"); ax.set_ylabel("Width (m)")
ax.set_aspect("equal"); ax.legend(loc="upper right")
fig.tight_layout(); fig.savefig("land_survey.png", dpi=150)
plt.show()
