"""Mini-Project 11: Large-angle pendulum with RK4 vs the small-angle approximation."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from common import rk4

g, L, theta0 = 9.81, 1.0, 1.2

full = lambda t, s: [s[1], -(g / L) * np.sin(s[0])]
small = lambda t, s: [s[1], -(g / L) * s[0]]

t, y = rk4(full, [theta0, 0.0], 0, 10, 0.001)
_, y_small = rk4(small, [theta0, 0.0], 0, 10, 0.001)

def period(t, theta):
    """Average time between successive downward zero crossings."""
    idx = np.where((theta[:-1] > 0) & (theta[1:] <= 0))[0]
    crossings = t[idx] - theta[idx] * (t[idx + 1] - t[idx]) / (theta[idx + 1] - theta[idx])
    return np.mean(np.diff(crossings))

sol = solve_ivp(full, [0, 10], [theta0, 0.0], method="DOP853", rtol=1e-10, atol=1e-12, dense_output=True)
ref = sol.sol(t)[0]

print(f"Period (full equation, RK4):  {period(t, y[:, 0]):.4f} s")
print(f"Period (small-angle):         {period(t, y_small[:, 0]):.4f} s  "
      f"(formula 2*pi*sqrt(L/g) = {2 * np.pi * np.sqrt(L / g):.4f} s)")
print(f"Max |RK4 - DOP853| over 10 s: {np.max(np.abs(y[:, 0] - ref)):.2e} rad")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t, np.degrees(y[:, 0]), label="Full equation (RK4)")
ax.plot(t, np.degrees(y_small[:, 0]), "--", label="Small-angle approximation")
ax.set_xlabel("Time (s)"); ax.set_ylabel("Angle (deg)"); ax.legend(); ax.grid(True, alpha=0.3)
fig.savefig("pendulum_compare.png", dpi=150)
plt.show()
