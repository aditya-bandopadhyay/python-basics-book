# Data Wrangling and Statistics -- Simpson's Paradox: Confounding in Aggregated Groups
# (book source: ch12_data_stats.tex, line 406)

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
