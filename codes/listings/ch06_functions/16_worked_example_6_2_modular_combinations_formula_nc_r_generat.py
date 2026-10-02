# Functions and Code Reuse -- Worked Example 6.2: Modular Combinations Formula (nC_r) Generator
# (book source: ch06_functions.tex, line 579)

def factorial(n):
    """Computes n! = 1 * 2 * ... * n for a non-negative integer n."""
    if n < 0:
        return 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def combinations(n, r):
    """Computes nCr = n! / (r! * (n - r)!) using the factorial() function."""
    if r < 0 or r > n:
        return 0
    num = factorial(n)
    den = factorial(r) * factorial(n - r)
    return num // den

# Test: Choosing 3 committee members out of 5 candidate students (5C3)
n_students = 5
r_committee = 3
ways = combinations(n_students, r_committee)

print(f"Ways to choose {r_committee} students out of {n_students}: {ways}")
print(f"5! = {factorial(5)}, 3! = {factorial(3)}, 2! = {factorial(2)}")

# Output:
# Ways to choose 3 students out of 5: 10
# 5! = 120, 3! = 6, 2! = 2
