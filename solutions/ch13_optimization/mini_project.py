"""Mini-Project 13: Least-time light path from air (n = 1.00) into glass (n = 1.50)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

c = 1.0                       # speed of light in vacuum (units chosen so c = 1)
n1, n2 = 1.00, 1.50
xA, yA = -2.0, 1.5            # source in air (above y = 0)
xB, yB = 1.5, -1.5            # detector in glass (below y = 0)

def transit_time(x):
    return np.hypot(x - xA, yA) / (c / n1) + np.hypot(xB - x, yB) / (c / n2)

res = minimize_scalar(transit_time, bounds=(xA, xB), method="bounded")
x_star = res.x

sin1 = abs(x_star - xA) / np.hypot(x_star - xA, yA)
sin2 = abs(xB - x_star) / np.hypot(xB - x_star, yB)
print(f"Crossing point x* = {x_star:.4f}")
print(f"theta1 = {np.degrees(np.arcsin(sin1)):.2f} deg, theta2 = {np.degrees(np.arcsin(sin2)):.2f} deg")
print(f"n1 sin(theta1) = {n1 * sin1:.5f},  n2 sin(theta2) = {n2 * sin2:.5f}")

fig, ax = plt.subplots(figsize=(7, 5))
ax.axhspan(0, 2.5, color="lightskyblue", alpha=0.3, label="Air, n = 1.00")
ax.axhspan(-2.5, 0, color="lightsteelblue", alpha=0.7, label="Glass, n = 1.50")
ax.plot([xA, xB], [yA, yB], "--", color="gray", label="Straight line")
ax.plot([xA, x_star, xB], [yA, 0, yB], "-", color="crimson", lw=2.5, label="Least-time path")
ax.plot([xA, xB], [yA, yB], "ko")
ax.text(xA, yA + 0.15, "A"); ax.text(xB, yB - 0.3, "B")
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5); ax.set_aspect("equal")
ax.legend(loc="upper right", fontsize=8); ax.set_title("Fermat's principle: refraction into glass")
fig.savefig("refraction_path.png", dpi=150)
plt.show()
