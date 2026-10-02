# Data Wrangling and Statistics -- Worked Example 12.4: Moving Average Filter for Noise Reduction
# (book source: ch12_data_stats.tex, line 607)

import numpy as np

np.random.seed(1)   # reproducible noise

# Generate underlying smooth signal + Gaussian noise
t = np.linspace(0, 10, 100)
signal_true = 25.0 + 5.0 * np.sin(0.5 * t)
noise = np.random.normal(0, 1.5, size=100)
signal_raw = signal_true + noise

# Step 1: Define 5-point moving average kernel
window_size = 5
kernel = np.ones(window_size) / window_size

# Step 2: Apply 1D convolution
signal_filtered = np.convolve(signal_raw, kernel, mode='valid')

# Standard deviation of residual noise relative to true signal
noise_raw_std = np.std(signal_raw - signal_true)
# Align true signal length to match 'valid' convolution output
noise_filt_std = np.std(signal_filtered - signal_true[2:-2])

print(f"Raw Signal Noise Std Dev:      {noise_raw_std:.4f} deg C")
print(f"Filtered Signal Noise Std Dev: {noise_filt_std:.4f} deg C")
print(f"Noise Reduction Factor:        {noise_raw_std / noise_filt_std:.2f}x")

# Output:
# Raw Signal Noise Std Dev:      1.3277 deg C
# Filtered Signal Noise Std Dev: 0.5351 deg C
# Noise Reduction Factor:        2.48x
