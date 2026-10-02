# Functions and Code Reuse -- Worked Example 6.1: Quadratic Equation Root Finder Returning Multiple Values
# (book source: ch06_functions.tex, line 524)

import math

def solve_quadratic(a, b, c):
    """Computes real roots of ax^2 + bx + c = 0.
    Returns (root1, root2) if real roots exist, else None."""
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        print("Warning: Discriminant is negative. No real roots exist.")
        return None
    
    sqrt_d = math.sqrt(discriminant)
    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)
    return root1, root2

# Test Case 1: Equation x^2 - 5x + 6 = 0  (Roots should be 3.0 and 2.0)
result = solve_quadratic(1, -5, 6)
if result is not None:
    r1, r2 = result
    print(f"Roots of x^2 - 5x + 6 = 0 are: {r1} and {r2}")

# Test Case 2: Equation x^2 + 2x + 5 = 0  (Discriminant = 4 - 20 = -16)
result_complex = solve_quadratic(1, 2, 5)
print("Result for complex roots:", result_complex)

# Output:
# Roots of x^2 - 5x + 6 = 0 are: 3.0 and 2.0
# Warning: Discriminant is negative. No real roots exist.
# Result for complex roots: None
