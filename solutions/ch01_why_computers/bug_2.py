"""Bug 1.2 -- a missing comma between the two things being printed.

Buggy:   print("The answer is: " 42)    -> SyntaxError
Fix:     separate the items with a comma (print adds a space between them).
"""
print("The answer is:", 42)
