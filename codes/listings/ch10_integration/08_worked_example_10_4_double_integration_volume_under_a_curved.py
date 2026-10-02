# Numerical Integration and Centroids -- Worked Example 10.4: Double Integration - Volume Under a Curved Surface
# (book source: ch10_integration.tex, line 423)

import scipy.integrate as integrate

# 2D Surface function z = f(x, y)
surface_z = lambda y, x: x**2 + y**2

# Double integration bounds: y from 0 to 2, x from 0 to 1
volume, err = integrate.dblquad(surface_z, 0, 1, lambda x: 0, lambda x: 2)

# Analytical exact integration: integral_0^1 [2*x^2 + 8/3] dx = 2/3 + 8/3 = 10/3
volume_exact = 10.0 / 3.0

print(f"Numerical Surface Volume:  {volume:.6f}")
print(f"Exact Analytical Volume:   {volume_exact:.6f}")
print(f"Absolute Discrepancy:      {abs(volume - volume_exact):.2e}")

# Output:
# Numerical Surface Volume:  3.333333
# Exact Analytical Volume:   3.333333
# Absolute Discrepancy:      4.44e-16
