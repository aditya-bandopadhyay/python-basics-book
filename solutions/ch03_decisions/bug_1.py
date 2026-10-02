"""Bug 3.1 -- a single = assigns; comparisons need >= (or ==).

Buggy:   if age = 18:   -> SyntaxError
Fix:     "18 or above" means >= 18.
"""
age = 20
if age >= 18:
    print("Adult")
