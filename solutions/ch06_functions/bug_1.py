"""Bug 6.1 -- the function computes result but never returns it.

A function without 'return' hands back None.
"""
def double(x):
    result = x * 2
    return result

print(double(5))   # Output: 10
