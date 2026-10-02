"""Bug 13.2 -- p0=[] gives curve_fit zero starting values for a model with one
parameter (A), so it cannot work out how many parameters to fit.

Fix: give one starting guess per parameter (or leave p0 out entirely). Note that
this model fixes the decay rate at 1, so the fit is approximate; adding a second
parameter for the rate fits the data exactly.
"""
from scipy.optimize import curve_fit
import numpy as np
x = np.linspace(0, 5, 10)
y = 3 * np.exp(-0.5 * x)
popt, _ = curve_fit(lambda x, A: A * np.exp(-x), x, y, p0=[1.0])
print("One parameter:", popt)
popt2, _ = curve_fit(lambda x, A, k: A * np.exp(-k * x), x, y, p0=[1.0, 1.0])
print("Two parameters:", np.round(popt2, 4))   # Output: [3.  0.5]
