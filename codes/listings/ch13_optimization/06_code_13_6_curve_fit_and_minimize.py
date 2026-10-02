# Optimization and Curve Fitting -- Code 13.6: curve_fit and minimize
# (book source: ch13_optimization.tex, line 278)
# NOTE: Needs code from 'Code 13.2: Gradient descent for linear regression' (included below as setup).

# ---- setup: code from earlier in the chapter ----
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

# ---- the listing itself ----
from scipy.optimize import curve_fit, minimize

# Uses x_data, y_data: the straight-line data from Code 13.2
# curve_fit: non-linear least squares
def model(x, m, c):
    return m * x + c

popt, pcov = curve_fit(model, x_data, y_data, p0=[1.0, 0.0])
print(f'curve_fit: m={popt[0]:.4f}, c={popt[1]:.4f}')
perr = np.sqrt(np.diag(pcov))
print(f'Uncertainties: dm={perr[0]:.4f}, dc={perr[1]:.4f}')

# minimize: general optimiser (Nelder-Mead, BFGS, etc.)
def mse(params):
    m, c = params
    return np.mean((y_data - (m * x_data + c))**2)

result = minimize(mse, x0=[0.0, 0.0], method='Nelder-Mead')
print(f'minimize: m={result.x[0]:.4f}, c={result.x[1]:.4f}')
