"""Mini-Project 9: Both release angles that land a shot put at 20 m."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from common import bisect

h0, v0, g, d = 2.0, 13.5, 9.81, 20.0

def height(x, theta_deg):
    th = np.radians(theta_deg)
    return h0 + x * np.tan(th) - g * x ** 2 / (2 * v0 ** 2 * np.cos(th) ** 2)

f = lambda theta: height(d, theta)          # landing height at x = d

# Scan f(theta) for sign changes between 1 and 89 degrees
thetas = np.linspace(1, 89, 881)
values = f(thetas)
brackets = [(thetas[i], thetas[i + 1]) for i in range(len(thetas) - 1)
            if values[i] * values[i + 1] < 0]

roots = []
for a, b in brackets:
    r, _ = bisect(f, a, b, tol=1e-10)
    roots.append(r)
    print(f"Bisection: theta = {r:.4f} deg   (brentq: {brentq(f, a, b):.4f} deg)")

# Algebraic check: with T = tan(theta), k = g d^2 / (2 v0^2):  -k T^2 + d T + (h0 - k) = 0
k = g * d ** 2 / (2 * v0 ** 2)
T = np.roots([-k, d, h0 - k])
print("Quadratic formula:", np.round(np.sort(np.degrees(np.arctan(T))), 4), "deg")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.plot(thetas, values)
ax1.axhline(0, color="gray", lw=0.8)
ax1.plot(roots, [0, 0], "ro")
ax1.set_xlabel("Release angle (deg)"); ax1.set_ylabel("Height at x = 20 m (m)")
ax1.set_title("f(theta): roots are the two hitting angles")
for r in roots:
    x = np.linspace(0, d, 200)
    ax2.plot(x, height(x, r), label=f"{r:.1f} deg")
ax2.axhline(0, color="gray", lw=0.8)
ax2.set_xlabel("Distance (m)"); ax2.set_ylabel("Height (m)")
ax2.set_title("Two trajectories that land at 20 m"); ax2.legend()
fig.tight_layout()
fig.savefig("shot_put_angles.png", dpi=150)
plt.show()
