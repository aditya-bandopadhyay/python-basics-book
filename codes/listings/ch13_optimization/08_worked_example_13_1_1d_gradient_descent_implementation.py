# Optimization and Curve Fitting -- Worked Example 13.1: 1D Gradient Descent Implementation
# (book source: ch13_optimization.tex, line 422)

import numpy as np

# Target function and exact derivative
f = lambda x: x**4 - 3*x**3 + 2
df = lambda x: 4*x**3 - 9*x**2

x = 3.0           # Initial guess
alpha = 0.01      # Learning rate (step size multiplier)
tol = 1e-6

print(f"{'Step k':<7} | {'x_k':<10} | {'f(x_k)':<10} | {'df/dx':<10}")
print("-" * 44)

for k in range(1, 101):
    grad = df(x)
    fx = f(x)
    
    if k <= 5 or abs(grad) < tol:
        print(f"{k:<7} | {x:<10.6f} | {fx:<10.6f} | {grad:<10.4e}")
        
    if abs(grad) < tol:
        break
        
    x -= alpha * grad  # Gradient descent update rule

print(f"\nMinimum found at x = {x:.6f} with f(x) = {f(x):.6f} in {k} steps.")

# Output:
# Step k  | x_k        | f(x_k)     | df/dx     
# --------------------------------------------
# 1       | 3.000000   | 2.000000   | 2.7000e+01
# 2       | 2.730000   | -3.493533  | 1.4310e+01
# 3       | 2.586904   | -5.151411  | 9.0184e+00
# 4       | 2.496721   | -5.832834  | 6.1518e+00
# 5       | 2.435202   | -6.156391  | 4.3932e+00
# 72      | 2.250000   | -6.542969  | 8.0377e-07
# 
# Minimum found at x = 2.250000 with f(x) = -6.542969 in 72 steps.
