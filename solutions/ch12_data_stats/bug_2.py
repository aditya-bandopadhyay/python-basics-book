"""Bug 12.2 -- cov / cov is always 1. Divide by the product of the standard deviations."""
def r_fixed(x, y):
    n = len(x)
    mx = sum(x) / n; my = sum(y) / n
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / (n - 1)
    sx = (sum((xi - mx) ** 2 for xi in x) / (n - 1)) ** 0.5
    sy = (sum((yi - my) ** 2 for yi in y) / (n - 1)) ** 0.5
    return cov / (sx * sy)

print(round(r_fixed([1, 2, 3, 4, 5], [2, 4, 5, 4, 5]), 4))   # Output: 0.7746
print(round(r_fixed([1, 2, 3, 4, 5], [5, 1, 4, 2, 3]), 4))   # Output: -0.3
