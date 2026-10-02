"""Bug 2.3 -- after a = b the old value of a is lost.

Fix 1: keep the old value in a temporary variable.
Fix 2 (Pythonic): swap with a tuple assignment, a, b = b, a.
"""
a = 5
b = 10
temp = a
a = b
b = temp
print(a, b)   # Output: 10 5

a, b = 5, 10
a, b = b, a
print(a, b)   # Output: 10 5
