# Visualizing Data with Matplotlib -- Worked Example 8.2: Subplots - Signal Analysis in Time & Frequency Domains
# (book source: ch08_matplotlib.tex, line 645)

import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
fs = 500       # Sampling frequency (Hz)
N = 500        # Total samples (1 second)
t = np.linspace(0, 1.0, N, endpoint=False)
print(f"[DEBUG] Signal sampling: N={N} points at fs={fs} Hz")

# Composite signal
y = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Compute FFT magnitude
fft_vals = np.fft.rfft(y)
freqs = np.fft.rfftfreq(N, 1/fs)
magnitude = 2.0 / N * np.abs(fft_vals)
print(f"[DEBUG] Real FFT computed: {len(freqs)} positive frequency bins")

# Create stacked subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=False)

# Top Panel: Time Domain
ax1.plot(t, y, color='teal', linewidth=1.5)
ax1.set_title('Composite Electrical Signal (Time Domain)', fontweight='bold')
ax1.set_xlabel('Time $t$ (s)')
ax1.set_ylabel('Amplitude (V)')
ax1.grid(True, linestyle=':')

# Bottom Panel: Frequency Domain
ax2.stem(freqs[:50], magnitude[:50], linefmt='crimson', markerfmt='ro', basefmt='k-')
ax2.set_title('FFT Frequency Magnitude Spectrum', fontweight='bold')
ax2.set_xlabel('Frequency $f$ (Hz)')
ax2.set_ylabel('Magnitude')
ax2.grid(True, linestyle=':')

plt.tight_layout()

print(f"Dominant Frequencies Detected: {freqs[np.argsort(magnitude)[-2:]]} Hz")

# Output:
# [DEBUG] Signal sampling: N=500 points at fs=500 Hz
# [DEBUG] Real FFT computed: 251 positive frequency bins
# Dominant Frequencies Detected: [20.  5.] Hz
