"""D1: SIR epidemic with Euler's method (beta = 0.3, gamma = 0.05, 200 days)."""
import numpy as np
import matplotlib.pyplot as plt
from common import euler

N, beta, gamma = 1000, 0.3, 0.05

def sir(t, y):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]

t, y = euler(sir, [999, 1, 0], 0, 200, 0.1)
S, I, R = y[:, 0], y[:, 1], y[:, 2]
print(f"Peak infections: {I.max():.0f} people on day {t[np.argmax(I)]:.1f}")
print(f"Never infected after 200 days: {S[-1]:.0f} people")

fig, ax = plt.subplots()
ax.plot(t, S, label="Susceptible"); ax.plot(t, I, label="Infected"); ax.plot(t, R, label="Recovered")
ax.set_xlabel("Day"); ax.set_ylabel("People"); ax.legend(); ax.grid(True, alpha=0.3)
fig.savefig("sir_euler.png", dpi=150)
plt.show()
