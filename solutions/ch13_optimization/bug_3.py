"""Bug 13.3 -- x is in the thousands, so x*(y - y_pred) is huge and a learning
rate of 0.01 makes each step overshoot wildly.

Fix: rescale x (measure it in thousands), fit, then convert the slope back.
"""
import numpy as np
x = np.array([1000, 2000, 3000, 4000])
y = np.array([300, 600, 900, 1200], dtype=float)

xs = x / 1000.0                     # 1, 2, 3, 4
m, c = 0.0, 0.0
lr = 0.01
for _ in range(5000):
    y_pred = m * xs + c
    dm = -2 * np.mean(xs * (y - y_pred))
    dc = -2 * np.mean(y - y_pred)
    m -= lr * dm; c -= lr * dc

print(f"slope per unit x = {m / 1000:.4f}, intercept = {c:.3f}")   # 0.3000 and about 0
