"""D2: Histogram of 1000 standard-normal samples with the theoretical PDF."""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)
samples = rng.normal(0, 1, 1000)

x = np.linspace(-4, 4, 300)
pdf = np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)

fig, ax = plt.subplots()
ax.hist(samples, bins=30, density=True, color="lightsteelblue", edgecolor="white",
        label="1000 samples")
ax.plot(x, pdf, "r-", lw=2, label="Standard normal PDF")
ax.set_xlabel("x")
ax.set_ylabel("Probability density")
ax.legend()
fig.savefig("normal_histogram.png", dpi=150, bbox_inches="tight")
plt.show()
