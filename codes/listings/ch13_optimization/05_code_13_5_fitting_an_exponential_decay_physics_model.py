# Optimization and Curve Fitting -- Code 13.5: Fitting an exponential decay physics model
# (book source: ch13_optimization.tex, line 249)

import numpy as np
from scipy.optimize import curve_fit

# Generate synthetic experimental data: y = A * exp(-b * x) + noise
np.random.seed(42)
x_exp = np.linspace(0, 5, 25)
y_true = 10.0 * np.exp(-0.8 * x_exp)
y_exp = y_true + np.random.normal(0, 0.4, size=len(x_exp))

# Define model function to fit
def exp_decay(x, A, b):
    return A * np.exp(-b * x)

# Fit parameters (A, b)
popt, pcov = curve_fit(exp_decay, x_exp, y_exp, p0=[5.0, 1.0])
A_fit, b_fit = popt

print(f"Fitted Amplitude A: {A_fit:.4f} (True A = 10.0)")
print(f"Fitted Decay Rate b: {b_fit:.4f} (True b = 0.8)")
