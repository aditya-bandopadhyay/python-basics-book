"""D3: 2x2 grid of sin, cos, clipped tan, and |sin|, with a shared x-axis."""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 400)
fig, axs = plt.subplots(2, 2, figsize=(9, 6), sharex=True)
axs[0, 0].plot(x, np.sin(x));                 axs[0, 0].set_title("sin x")
axs[0, 1].plot(x, np.cos(x));                 axs[0, 1].set_title("cos x")
axs[1, 0].plot(x, np.clip(np.tan(x), -5, 5)); axs[1, 0].set_title("tan x (clipped to [-5, 5])")
axs[1, 1].plot(x, np.abs(np.sin(x)));         axs[1, 1].set_title("|sin x|")
for ax in axs.flat:
    ax.grid(True, linestyle=":")
fig.supxlabel("x (radians)")
fig.tight_layout()
fig.savefig("trig_grid.png", dpi=150)
plt.show()
