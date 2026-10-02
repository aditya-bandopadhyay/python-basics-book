# Optimization and Curve Fitting -- Code 13.1: Gradient descent to minimize J(theta) = theta^2 - 4theta + 5
# (book source: ch13_optimization.tex, line 113)

import numpy as np

# Cost function J(theta) and its derivative dJ/dtheta
def J(theta):
    return theta**2 - 4*theta + 5

def dJ(theta):
    return 2*theta - 4

# Gradient descent optimization
theta = 10.0      # Initial guess far from minimum
alpha = 0.1       # Learning rate
tolerance = 1e-6

for step in range(100):
    grad = dJ(theta)
    theta_new = theta - alpha * grad
    if abs(theta_new - theta) < tolerance:
        print(f"Converged in {step+1} steps!")
        break
    theta = theta_new

print(f"Optimal theta: {theta:.6f} (Exact minimum is theta = 2.0)")
