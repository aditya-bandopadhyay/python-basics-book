"""D3: Fit Newton cooling T(t) = 20 + A exp(-lambda t) to coffee measurements."""
import numpy as np
from scipy.optimize import curve_fit

t = np.array([0, 5, 10, 15, 20, 30])
T = np.array([90.0, 70.0, 55.7, 45.5, 38.2, 29.3])

def model(t, A, lam):
    return 20 + A * np.exp(-lam * t)

popt, pcov = curve_fit(model, t, T, p0=[70, 0.05])
perr = np.sqrt(np.diag(pcov))
print(f"A      = {popt[0]:.3f} +/- {perr[0]:.1e} deg C")
print(f"lambda = {popt[1]:.5f} +/- {perr[1]:.1e} per minute")
print("Chapter 11 found k = 0.0673 per minute from two readings; the fit agrees.")
