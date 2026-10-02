# Data Wrangling and Statistics -- Real-World Solution
# (book source: ch12_data_stats.tex, line 702)

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
