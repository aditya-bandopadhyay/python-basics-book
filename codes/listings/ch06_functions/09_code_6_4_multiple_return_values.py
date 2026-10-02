# Functions and Code Reuse -- Code 6.4: Multiple return values
# (book source: ch06_functions.tex, line 381)

def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([72, 85, 91, 60, 78])
print("Min:", lo, "  Max:", hi)   # Output: Min: 60   Max: 91
