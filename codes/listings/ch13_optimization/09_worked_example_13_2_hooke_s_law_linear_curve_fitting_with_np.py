# Optimization and Curve Fitting -- Worked Example 13.2: Hooke's Law Linear Curve Fitting with np.polyfit
# (book source: ch13_optimization.tex, line 481)

import numpy as np

# Experimental data
m = np.array([0.1, 0.2, 0.3, 0.4, 0.5])       # mass (kg)
x_cm = np.array([1.2, 2.5, 3.6, 4.9, 6.1])   # extension (cm)

g = 9.81
F_N = m * g                                  # Force (N)
x_m = x_cm / 100.0                           # Extension (m)

# Perform degree-1 linear fit: F = k * x + F0
k_stiffness, F0_bias = np.polyfit(x_m, F_N, 1)

# Calculate model predictions and residual norm
F_pred = k_stiffness * x_m + F0_bias
residual_rmse = np.sqrt(np.mean((F_N - F_pred)**2))

print(f"Spring Stiffness k:   {k_stiffness:.2f} N/m")
print(f"Zero-Load Bias F0:    {F0_bias:.4f} N")
print(f"Fit RMSE:             {residual_rmse:.4f} N")

# Output:
# Spring Stiffness k:   80.37 N/m
# Zero-Load Bias F0:    0.0016 N
# Fit RMSE:             0.0322 N
