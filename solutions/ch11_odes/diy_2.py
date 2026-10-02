"""D2: Van der Pol oscillator (mu = 2): Euler, RK4 and solve_ivp.

y'' - mu (1 - y^2) y' + y = 0  becomes  y1' = y2,  y2' = mu (1 - y1^2) y2 - y1.
"""
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from common import euler, rk4

mu = 2.0
def vdp(t, y):
    return [y[1], mu * (1 - y[0] ** 2) * y[1] - y[0]]

t_e, y_e = euler(vdp, [2.0, 0.0], 0, 20, 0.05)
t_r, y_r = rk4(vdp, [2.0, 0.0], 0, 20, 0.05)
sol = solve_ivp(vdp, [0, 20], [2.0, 0.0], rtol=1e-9, atol=1e-9, dense_output=True)

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t_e, y_e[:, 0], label="Euler, h = 0.05", alpha=0.8)
ax.plot(t_r, y_r[:, 0], label="RK4, h = 0.05")
ax.plot(t_r, sol.sol(t_r)[0], "k:", label="solve_ivp (reference)")
ax.set_xlabel("t"); ax.set_ylabel("y(t)"); ax.legend(); ax.grid(True, alpha=0.3)
fig.savefig("van_der_pol.png", dpi=150)
print(f"y(20): Euler {y_e[-1, 0]:.4f}, RK4 {y_r[-1, 0]:.4f}, solve_ivp {sol.sol(20)[0]:.4f}")
plt.show()
