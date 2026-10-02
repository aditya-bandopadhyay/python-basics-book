# Data Wrangling and Statistics -- Code 12.3: Mean, median, variance, and standard deviation from scratch
# (book source: ch12_data_stats.tex, line 124)

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
