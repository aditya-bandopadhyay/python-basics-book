# Optimization and Curve Fitting -- Worked Example 13.3: Exponential Decay Non-linear Fitting with curve_fit
# (book source: ch13_optimization.tex, line 527)

import numpy as np
import scipy.optimize as opt

# Lab data
t_data = np.array([0, 2, 4, 6, 8, 10])
N_data = np.array([1000, 735, 540, 400, 290, 215])

# Non-linear model function
def decay_model(t, N0, lambda_decay):
    return N0 * np.exp(-lambda_decay * t)

# Perform non-linear least squares fit
initial_guess = [1000.0, 0.1]
popt, pcov = opt.curve_fit(decay_model, t_data, N_data, p0=initial_guess)

N0_fit, lambda_fit = popt
perr = np.sqrt(np.diag(pcov))  # Parameter 1-sigma standard errors

half_life = np.log(2) / lambda_fit

print(f"Fitted Initial Count N0: {N0_fit:.2f} +/- {perr[0]:.2f}")
print(f"Decay Constant lambda:   {lambda_fit:.4f} +/- {perr[1]:.4f} 1/hr")
print(f"Calculated Half-Life:    {half_life:.2f} hours")

# Output:
# Fitted Initial Count N0: 999.99 +/- 1.52
# Decay Constant lambda:   0.1538 +/- 0.0005 1/hr
# Calculated Half-Life:    4.51 hours
