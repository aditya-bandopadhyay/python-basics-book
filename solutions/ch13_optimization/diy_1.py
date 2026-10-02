"""D1: Fit y = a x^2 + b x + c by gradient descent (three parameters)."""
import numpy as np

rng = np.random.default_rng(0)
x = np.linspace(-2, 2, 60)
y = 1.5 * x ** 2 - 0.8 * x + 2.0 + rng.normal(0, 0.3, len(x))

a = b = c = 0.0
lr = 0.02
n = len(x)
for epoch in range(5000):
    pred = a * x ** 2 + b * x + c
    err = y - pred
    da = -2 / n * np.sum(x ** 2 * err)
    db = -2 / n * np.sum(x * err)
    dc = -2 / n * np.sum(err)
    a -= lr * da; b -= lr * db; c -= lr * dc

print(f"Gradient descent: a = {a:.3f}, b = {b:.3f}, c = {c:.3f}")
print("np.polyfit check:", np.round(np.polyfit(x, y, 2), 3))
