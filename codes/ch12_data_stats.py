"""
Data Wrangling and Statistics -- companion script for Chapter 12.
Runs the chapter's listings in the order they appear in the book.
Listings that need keyboard input, or that are fragments / deliberate
mistakes, are skipped here; every listing is in codes/listings/ch12_data_stats/.
Run from the repository root:  python codes/ch12_data_stats.py
"""

# ======================================================================
# Code 12.1: Simulating marble bag draws without replacement
# ======================================================================
import numpy as np

np.random.seed(0)   # fix the random sequence so your output matches ours

# 1. Create a bag with 5 Red and 5 Blue marbles
bag = np.array(['Red']*5 + ['Blue']*5)
n_trials = 10000
two_red_count = 0

# 2. Simulate 10,000 independent trials of drawing 2 marbles without replacement
for _ in range(n_trials):
    draw = np.random.choice(bag, size=2, replace=False)
    if draw[0] == 'Red' and draw[1] == 'Red':
        two_red_count += 1

simulated_prob = two_red_count / n_trials
theoretical_prob = (5/10) * (4/9)

print(f"Simulated Probability (2 Red):   {simulated_prob:.4f}")
print(f"Theoretical Probability (2 Red): {theoretical_prob:.4f}")
# Output:
# Simulated Probability (2 Red):   0.2226
# Theoretical Probability (2 Red): 0.2222

# ======================================================================
# Code 12.2: Simulating 10,000 dice rolls
# ======================================================================
import numpy as np

# 1. Simulate rolling two 6-sided dice 10,000 times
die1 = np.random.randint(1, 7, size=10000)
die2 = np.random.randint(1, 7, size=10000)
dice_sum = die1 + die2

# 2. Count occurrences of each sum from 2 to 12
sums, counts = np.unique(dice_sum, return_counts=True)
probabilities = counts / 10000

print("Sum | Simulated Probability")
print("---------------------------")
for s, p in zip(sums, probabilities):
    print(f" {s:2d} | {p:.4f}")

# ======================================================================
# Code 12.3: Mean, median, variance, and standard deviation from scratch
# ======================================================================
def calc_mean(data):
    return sum(data) / len(data)

def calc_median(data):
    sorted_d = sorted(data)
    n = len(sorted_d)
    mid = n // 2
    if n % 2 == 1:
        return sorted_d[mid]
    else:
        return (sorted_d[mid - 1] + sorted_d[mid]) / 2.0

def calc_variance(data, ddof=0):
    'Population (ddof=0) or sample (ddof=1) variance.'
    mu = calc_mean(data)
    return sum((x - mu)**2 for x in data) / (len(data) - ddof)

def calc_std(data, ddof=0):
    return calc_variance(data, ddof) ** 0.5

scores = [85, 90, 60, 95, 100, 30, 90]
print(f"Mean Score:   {calc_mean(scores):.2f}")
print(f"Median Score: {calc_median(scores):.2f}")
print(f"Std Dev:      {calc_std(scores, ddof=1):.2f}")

# ======================================================================
# Code 12.4: Covariance and Pearson r
# ======================================================================
# Uses calc_mean() and calc_std() from Code 12.3: run that first
def covariance(x, y):
    'Sample covariance of two sequences.'
    n  = len(x)
    mx = calc_mean(x);  my = calc_mean(y)
    total = 0
    for i in range(n):
        total += (x[i] - mx) * (y[i] - my)
    return total / (n - 1)

def pearson_r(x, y):
    'Pearson correlation coefficient.'
    return covariance(x, y) / (calc_std(x, ddof=1) * calc_std(y, ddof=1))

study_hours = [2, 3, 4, 5, 6, 7, 8]
test_scores = [55, 60, 65, 70, 78, 82, 90]
r = pearson_r(study_hours, test_scores)
print(f'Pearson r = {r:.4f}')

# ======================================================================
# Code 12.5: pandas and scipy equivalents
# ======================================================================
import pandas as pd
from scipy import stats

# Our calc_mean(data)       <->  np.mean(data)  or  pd.Series(data).mean()
# Our calc_variance(ddof=1) <->  np.var(data, ddof=1)
# Our pearson_r             <->  stats.pearsonr(x, y)  returns (r, p_value)

df = pd.read_csv('data/grades.csv')   # load real data
print(df.describe())               # count, mean, std, min, quartiles, max
print(df.corr(numeric_only=True))     # correlations between number columns

# ======================================================================
# Code 12.6: t-test from scratch vs scipy
# ======================================================================
# Uses calc_mean() and calc_std() from Code 12.3: run that first
import numpy as np

# Two groups: exam scores before and after a revision class
before = np.array([55, 60, 58, 62, 57, 63, 59, 61])
after  = np.array([70, 68, 72, 65, 74, 69, 71, 67])

# From-scratch: paired t-statistic
diff = after - before
t_stat = calc_mean(list(diff)) / (calc_std(list(diff), ddof=1) / len(diff)**0.5)
print(f'Hand-computed t = {t_stat:.4f}')

# scipy equivalent
from scipy.stats import ttest_rel
t, p = ttest_rel(after, before)
print(f'scipy t={t:.4f}  p={p:.4f}')
print('Significant (p<0.05)?', p < 0.05)

# ======================================================================
# Simpson's Paradox: Confounding in Aggregated Groups
# ======================================================================
import numpy as np

# Success counts and total patients: [Mild, Severe]
cured_A = np.array([18, 40])
total_A = np.array([20, 100])

cured_B = np.array([80, 6])
total_B = np.array([100, 20])

rate_A = cured_A / total_A
rate_B = cured_B / total_B

agg_rate_A = np.sum(cured_A) / np.sum(total_A)
agg_rate_B = np.sum(cured_B) / np.sum(total_B)

print("Subgroup Recovery Rates (Treatment A vs B):")
print(f"  Mild:   A = {rate_A[0]:.1%}, B = {rate_B[0]:.1%}  --> A is superior")
print(f"  Severe: A = {rate_A[1]:.1%}, B = {rate_B[1]:.1%}  --> A is superior")
print("Aggregated Recovery Rates:")
print(f"  Total:  A = {agg_rate_A:.1%}, B = {agg_rate_B:.1%}  --> B appears superior!")

# ======================================================================
# Worked Example 12.1: Gaussian Distribution Statistics & 68-95-99.7 Rule
# ======================================================================
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

# ======================================================================
# Worked Example 12.2: Data Cleaning - Outlier Detection & Median Imputation
# ======================================================================
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

# ======================================================================
# Worked Example 12.3: Stress-Strain Linear Regression & R^2 Determination
# ======================================================================
import numpy as np

strain = np.array([0.000, 0.001, 0.002, 0.003, 0.004, 0.005])
stress = np.array([2.0, 71.5, 138.0, 209.0, 281.0, 348.0])  # MPa

# Step 1: Pearson correlation matrix
r_matrix = np.corrcoef(strain, stress)
r = r_matrix[0, 1]

# Step 2: Linear regression slope (Young's Modulus E) and intercept
slope, intercept = np.polyfit(strain, stress, 1)
E_GPa = slope / 1000.0  # Convert MPa to GPa

# Step 3: Compute R^2 coefficient of determination
stress_pred = slope * strain + intercept
SS_res = np.sum((stress - stress_pred) ** 2)
SS_tot = np.sum((stress - np.mean(stress)) ** 2)
R_squared = 1.0 - (SS_res / SS_tot)

print(f"Pearson Correlation r:  {r:.6f}")
print(f"Young's Modulus E:      {E_GPa:.2f} GPa")
print(f"Stress Intercept:       {intercept:.2f} MPa")
print(f"R-squared (R^2):        {R_squared:.6f}")

# Output:
# Pearson Correlation r:  0.999939
# Young's Modulus E:      69.41 GPa
# Stress Intercept:       1.38 MPa
# R-squared (R^2):        0.999879

# ======================================================================
# Worked Example 12.4: Moving Average Filter for Noise Reduction
# ======================================================================
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

# ======================================================================
# Real-World Solution
# ======================================================================
import numpy as np

# A made-up graduating class of 100 (salaries in lakh rupees per year)
typical = np.linspace(3.5, 5.9, 85)      # 85 students between 3.5 and 5.9 lakh
good    = np.full(12, 20.0)              # 12 students at 20 lakh
star    = np.full(3, 188.0)              # 3 international offers of 1.88 crore
salaries = np.concatenate([typical, good, star])

print(f"Mean salary:   {np.mean(salaries):.1f} lakh")
print(f"Median salary: {np.median(salaries):.1f} lakh")
print(f"Share earning under 6 lakh: {np.mean(salaries < 6) * 100:.0f}%")

# Output:
# Mean salary:   12.0 lakh
# Median salary: 4.9 lakh
# Share earning under 6 lakh: 85%
