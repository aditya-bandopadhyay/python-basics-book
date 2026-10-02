"""Bug 13.1 -- the step is far too large. With learning rate 10 and SUMMED (not
averaged) gradients, every update overshoots by more than the last, so the loss
grows without limit. (The signs are consistent: dm here is minus the gradient,
so '+=' moves downhill.)

Fix: average the gradient over the data and use a small learning rate.
"""
import numpy as np
rng = np.random.default_rng(0)
x_data = np.linspace(0, 10, 50)
y_data = 2.5 * x_data + 4.0 + rng.normal(0, 2, 50)

m, c = 0.0, 0.0
n = len(x_data)
for _ in range(5000):
    y_pred = m * x_data + c
    dm = 2 / n * np.sum(x_data * (y_data - y_pred))
    dc = 2 / n * np.sum(y_data - y_pred)
    m += 0.01 * dm
    c += 0.01 * dc
print(f"m = {m:.3f}, c = {c:.3f}")   # the least-squares line for this noisy data
print("np.polyfit gives", np.round(np.polyfit(x_data, y_data, 1), 3))
