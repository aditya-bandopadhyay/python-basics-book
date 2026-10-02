"""D1: Damped sine e^(-x) sin(4 pi x), saved to damped_sine.pdf."""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 500)
f = np.exp(-x) * np.sin(4 * np.pi * x)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, f, color="steelblue")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title(r"$f(x) = e^{-x}\sin(4\pi x)$")
ax.grid(True)
fig.savefig("damped_sine.pdf", bbox_inches="tight")
plt.show()
