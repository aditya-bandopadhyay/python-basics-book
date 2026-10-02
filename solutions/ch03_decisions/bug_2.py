"""Bug 3.2 -- the body of an if must be indented.

Buggy:   print("Pass") at the left margin -> IndentationError: expected an indented block
"""
score = 85
if score >= 50:
    print("Pass")
else:
    print("Fail")
