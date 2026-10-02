# Data Wrangling and Statistics -- Code 12.6: t-test from scratch vs scipy
# (book source: ch12_data_stats.tex, line 242)
# NOTE: Needs code from 'Code 12.3: Mean, median, variance, and standard deviation from scratch' (included below as setup).

# ---- setup: code from earlier in the chapter ----
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

# ---- the listing itself ----
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
