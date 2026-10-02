# Data Wrangling and Statistics -- Worked Example 12.3: Stress-Strain Linear Regression & R^2 Determination
# (book source: ch12_data_stats.tex, line 557)

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
