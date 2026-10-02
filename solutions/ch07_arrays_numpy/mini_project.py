"""Mini-Project 7: Signal generator -- mean, peak and RMS, with and without noise."""
import numpy as np

np.random.seed(7)
t = np.linspace(0, 1, 200)
y = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 12 * t)

def rms(signal):
    """Root-mean-square value: sqrt of the mean of the squares."""
    return np.sqrt(np.mean(signal ** 2))

y_noisy = y + np.random.normal(0, 0.1, size=len(t))

print(f"Clean signal:  mean = {np.mean(y):+.4f}, max = {np.max(y):.4f}, RMS = {rms(y):.4f}")
print(f"Noisy signal:  mean = {np.mean(y_noisy):+.4f}, max = {np.max(y_noisy):.4f}, RMS = {rms(y_noisy):.4f}")
print(f"RMS increased by {rms(y_noisy) - rms(y):.4f}")

# Theory check: for two sine waves, RMS = sqrt(1**2/2 + 0.5**2/2) = 0.7906.
# Independent noise of standard deviation 0.1 adds in quadrature:
# sqrt(0.7906**2 + 0.1**2) = 0.7969, an increase of about 0.006.
