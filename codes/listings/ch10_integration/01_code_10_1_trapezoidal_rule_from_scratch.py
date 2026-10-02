# Numerical Integration and Centroids -- Code 10.1: Trapezoidal rule from scratch
# (book source: ch10_integration.tex, line 153)

def trapezoid_scratch(f, a, b, n=100):
    """Integrate f(x) from a to b across n equal panels."""
    dx = (b - a) / n
    # Endpoints carry half weight; interior points carry full weight
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * dx)
    return total * dx

# Test: Integral of x^2 from 0 to 3 (exact analytical answer = 9.0)
f = lambda x: x**2
approx = trapezoid_scratch(f, 0, 3, n=100)
print(f"Trapezoidal approximation: {approx:.6f}")
print(f"Discretization error:     {abs(approx - 9.0):.2e}")
