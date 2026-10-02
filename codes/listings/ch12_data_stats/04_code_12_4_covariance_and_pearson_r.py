# Data Wrangling and Statistics -- Code 12.4: Covariance and Pearson r
# (book source: ch12_data_stats.tex, line 158)
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
