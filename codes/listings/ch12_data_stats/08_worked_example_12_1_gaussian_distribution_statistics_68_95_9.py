# Data Wrangling and Statistics -- Worked Example 12.1: Gaussian Distribution Statistics & 68-95-99.7 Rule
# (book source: ch12_data_stats.tex, line 440)

import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Generate 1000 Gaussian samples
mu_true, sigma_true = 75.0, 10.0
scores = np.random.normal(mu_true, sigma_true, 1000)

# Sample statistics
mean_score = np.mean(scores)
std_score = np.std(scores, ddof=1)
median_score = np.median(scores)
q75, q25 = np.percentile(scores, [75, 25])
iqr_score = q75 - q25

# Step 2: Calculate empirical percentages within 1, 2, 3 std deviations
within_1sig = np.sum(np.abs(scores - mean_score) <= std_score) / 1000 * 100
within_2sig = np.sum(np.abs(scores - mean_score) <= 2 * std_score) / 1000 * 100
within_3sig = np.sum(np.abs(scores - mean_score) <= 3 * std_score) / 1000 * 100

print(f"Sample Mean:     {mean_score:.2f} (Target: {mu_true:.1f})")
print(f"Sample Std Dev:  {std_score:.2f} (Target: {sigma_true:.1f})")
print(f"Median:          {median_score:.2f} | IQR: {iqr_score:.2f}")
print(f"Within 1-Sigma:  {within_1sig:.1f}% (Theory: 68.3%)")
print(f"Within 2-Sigma:  {within_2sig:.1f}% (Theory: 95.4%)")
print(f"Within 3-Sigma:  {within_3sig:.1f}% (Theory: 99.7%)")

# Output:
# Sample Mean:     75.19 (Target: 75.0)
# Sample Std Dev:  9.79 (Target: 10.0)
# Median:          75.25 | IQR: 12.96
# Within 1-Sigma:  68.6% (Theory: 68.3%)
# Within 2-Sigma:  95.6% (Theory: 95.4%)
# Within 3-Sigma:  99.7% (Theory: 99.7%)
