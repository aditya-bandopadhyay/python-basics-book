"""Bug 2.1 -- order of operations.

Buggy:   avg = a + b + c / 3      -> 40.0, because division happens before addition
Fix:     put the sum in brackets.
"""
a = 10; b = 20; c = 30
avg = (a + b + c) / 3
print(avg)   # Output: 20.0
