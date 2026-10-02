# Data Wrangling and Statistics -- Code 12.5: pandas and scipy equivalents
# (book source: ch12_data_stats.tex, line 217)

import pandas as pd
from scipy import stats

# Our calc_mean(data)       <->  np.mean(data)  or  pd.Series(data).mean()
# Our calc_variance(ddof=1) <->  np.var(data, ddof=1)
# Our pearson_r             <->  stats.pearsonr(x, y)  returns (r, p_value)

df = pd.read_csv('data/grades.csv')   # load real data
print(df.describe())               # count, mean, std, min, quartiles, max
print(df.corr(numeric_only=True))     # correlations between number columns
