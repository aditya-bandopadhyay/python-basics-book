# Optimization and Curve Fitting -- Code 13.2: Gradient descent for linear regression
# (book source: ch13_optimization.tex, line 151)

import numpy as np

rng = np.random.default_rng(0)
x_data = np.linspace(0, 10, 50)
y_data = 2.5 * x_data + 4.0 + rng.normal(0, 2, 50)

def gradient_descent(x, y, lr=0.01, epochs=1000):
    'Fit y = m*x + c to data by gradient descent.'
    n = len(x)
    m, c = 0.0, 0.0
    losses = []
    for _ in range(epochs):
        y_pred = m * x + c
        loss = np.mean((y - y_pred)**2)
        losses.append(loss)
        dm = -2 / n * np.sum(x * (y - y_pred))
        dc = -2 / n * np.sum(y - y_pred)
        m -= lr * dm
        c -= lr * dc
    return m, c, losses

m_fit, c_fit, losses = gradient_descent(x_data, y_data, lr=0.005, epochs=2000)
print(f'Fitted: y = {m_fit:.3f}x + {c_fit:.3f}')
print(f'True:   y = 2.500x + 4.000')
