"""Bug 13.5 -- with p0 = [0.001, 0.001] the model starts almost flat at zero, far
from the data, and the optimiser can wander off or stop early.

Fix: start from sensible guesses read off the data: A is about y at x = 0, and
lam is about 1 / (time for y to fall to a third).
"""
from scipy.optimize import curve_fit
import numpy as np
np.random.seed(0)
x = np.linspace(0, 5, 20)
y = 5 * np.exp(-2 * x) + np.random.normal(0, 0.1, 20)
popt, _ = curve_fit(lambda x, A, lam: A * np.exp(-lam * x), x, y, p0=[y[0], 1.0])
print(np.round(popt, 2))   # close to [5, 2]
