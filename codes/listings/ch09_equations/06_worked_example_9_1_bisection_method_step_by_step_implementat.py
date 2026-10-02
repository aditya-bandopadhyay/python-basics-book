# Solving Nonlinear Equations -- Worked Example 9.1: Bisection Method Step-by-Step Implementation
# (book source: ch09_equations.tex, line 342)

import numpy as np

def bisection(f, a, b, tol=1e-6, max_iter=50):
    if f(a) * f(b) >= 0:
        raise ValueError("Function must have opposite signs at bracket endpoints.")
    
    print(f"{'k':<3} | {'a':<9} | {'b':<9} | {'c (Midpoint)':<12} | {'f(c)':<11} | {'Error':<9}")
    print("-" * 62)
    
    for k in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)
        err = (b - a) / 2.0
        
        if k <= 5 or err < tol:  # Print first 5 steps and final step
            print(f"{k:<3} | {a:<9.6f} | {b:<9.6f} | {c:<12.6f} | {fc:<11.4e} | {err:<9.2e}")
            
        if abs(fc) < 1e-12 or err < tol:
            return c, k
            
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    return (a + b) / 2.0, max_iter

# Target function f(x) = x^3 - 4x - 9
f = lambda x: x**3 - 4*x - 9
root, iterations = bisection(f, 2.0, 3.0, tol=1e-6)
print(f"\nFinal Root: x = {root:.6f} found in {iterations} iterations.")

# Output:
# k   | a         | b         | c (Midpoint) | f(c)        | Error    
# --------------------------------------------------------------
# 1   | 2.000000  | 3.000000  | 2.500000     | -3.3750e+00 | 5.00e-01
# 2   | 2.500000  | 3.000000  | 2.750000     | 7.9688e-01  | 2.50e-01
# 3   | 2.500000  | 2.750000  | 2.625000     | -1.4121e+00 | 1.25e-01
# 4   | 2.625000  | 2.750000  | 2.687500     | -3.3911e-01 | 6.25e-02
# 5   | 2.687500  | 2.750000  | 2.718750     | 2.2092e-01  | 3.12e-02
# 20  | 2.706528  | 2.706530  | 2.706529     | 1.2747e-05  | 9.54e-07
# 
# Final Root: x = 2.706529 found in 20 iterations.
