"""D2: Stochastic gradient descent (one random point per update) vs full batch."""
import numpy as np

rng = np.random.default_rng(0)
x = np.linspace(0, 10, 50)
y = 2.5 * x + 4.0 + rng.normal(0, 2, 50)
n = len(x)

def mse(m, c):
    return np.mean((y - (m * x + c)) ** 2)

# Full-batch gradient descent: 2000 updates, each using all 50 points
m = c = 0.0
for _ in range(2000):
    err = y - (m * x + c)
    m -= 0.005 * (-2 / n * np.sum(x * err))
    c -= 0.005 * (-2 / n * np.sum(err))
print(f"Full batch: m = {m:.3f}, c = {c:.3f}, MSE = {mse(m, c):.3f}  (2000 x 50 = 100000 point-gradients)")

# SGD: each update uses one randomly chosen point
m = c = 0.0
for step in range(20000):
    i = rng.integers(n)
    err = y[i] - (m * x[i] + c)
    lr = 0.002 / (1 + step / 5000)          # slowly shrinking learning rate
    m -= lr * (-2 * x[i] * err)
    c -= lr * (-2 * err)
print(f"SGD:        m = {m:.3f}, c = {c:.3f}, MSE = {mse(m, c):.3f}  (20000 point-gradients)")
# SGD reaches a similar fit with far fewer gradient evaluations, but its path is noisy.
