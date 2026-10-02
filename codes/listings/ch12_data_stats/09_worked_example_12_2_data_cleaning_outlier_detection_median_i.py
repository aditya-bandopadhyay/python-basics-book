# Data Wrangling and Statistics -- Worked Example 12.2: Data Cleaning - Outlier Detection & Median Imputation
# (book source: ch12_data_stats.tex, line 499)

import numpy as np

raw_data = np.array([101.3, 102.1, 99.8, 450.0, 101.8, np.nan, 100.5, 101.0])
valid = raw_data[~np.isnan(raw_data)]          # drop the missing value

# Attempt 1: z-scores (distance from the mean in standard deviations)
z = (valid - np.mean(valid)) / np.std(valid)
print(f"Raw mean (corrupted): {np.mean(valid):.2f} kPa")
print(f"Largest |z|:          {np.max(np.abs(z)):.2f}")
print(f"Flagged by |z| > 2.5: {valid[np.abs(z) > 2.5]}")

# Attempt 2: distance from the median, in units of the typical spread (MAD)
med = np.median(valid)
mad = np.median(np.abs(valid - med))           # median absolute deviation
outlier_mask = np.abs(raw_data - med) > 5 * mad
print(f"Median: {med:.2f} kPa, MAD: {mad:.2f} kPa")
print(f"Flagged by median rule: {raw_data[outlier_mask]}")

# Replace outliers and missing values with the median of the clean readings
clean = raw_data.copy()
clean[outlier_mask] = np.nan
robust_median = np.nanmedian(clean)
final_data = np.where(np.isnan(clean), robust_median, clean)
print(f"Imputation value: {robust_median:.2f} kPa")
print("Clean dataset:", np.round(final_data, 2))

# Output:
# Raw mean (corrupted): 150.93 kPa
# Largest |z|:          2.45
# Flagged by |z| > 2.5: []
# Median: 101.30 kPa, MAD: 0.80 kPa
# Flagged by median rule: [450.]
# Imputation value: 101.15 kPa
# Clean dataset: [101.3  102.1   99.8  101.15 101.8  101.15 100.5  101.  ]
