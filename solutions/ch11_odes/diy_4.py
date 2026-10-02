"""D4: Global error vs step size for Euler and RK4 (Newton cooling, 0..60 min)."""
import numpy as np
import matplotlib.pyplot as plt
from common import euler, rk4

k, T_env, T0 = 0.05, 20.0, 90.0
f = lambda t, T: -k * (T - T_env)
exact = lambda t: T_env + (T0 - T_env) * np.exp(-k * t)

hs = np.array([2, 1, 0.5, 0.25, 0.1])
err_e, err_r = [], []
for h in hs:
    t, T = euler(f, T0, 0, 60, h); err_e.append(np.max(np.abs(T - exact(t))))
    t, T = rk4(f, T0, 0, 60, h);   err_r.append(np.max(np.abs(T - exact(t))))

slope_e = np.polyfit(np.log(hs), np.log(err_e), 1)[0]
slope_r = np.polyfit(np.log(hs), np.log(err_r), 1)[0]
print(f"Euler slope = {slope_e:.2f} (expect 1),  RK4 slope = {slope_r:.2f} (expect 4)")

fig, ax = plt.subplots()
ax.loglog(hs, err_e, "o-", label=f"Euler (slope {slope_e:.2f})")
ax.loglog(hs, err_r, "s-", label=f"RK4 (slope {slope_r:.2f})")
ax.set_xlabel("step size h"); ax.set_ylabel("max error"); ax.legend(); ax.grid(True, which="both", alpha=0.3)
fig.savefig("error_vs_h.png", dpi=150)
plt.show()
