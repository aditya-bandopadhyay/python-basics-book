"""D2: Pearson r from scratch vs np.corrcoef on y = 2x + noise."""
import numpy as np

def pearson_r(x, y):
    mx, my = np.mean(x), np.mean(y)
    cov = np.sum((x - mx) * (y - my))
    return cov / np.sqrt(np.sum((x - mx) ** 2) * np.sum((y - my) ** 2))

rng = np.random.default_rng(0)
x = rng.normal(0, 1, 500)
y = 2 * x + rng.normal(0, 0.5, 500)

r_mine = pearson_r(x, y)
r_numpy = np.corrcoef(x, y)[0, 1]
print(f"from scratch: {r_mine:.6f}   np.corrcoef: {r_numpy:.6f}   match: {np.isclose(r_mine, r_numpy)}")
# Theory: r = 2 / sqrt(4 + 0.25) = 0.970
