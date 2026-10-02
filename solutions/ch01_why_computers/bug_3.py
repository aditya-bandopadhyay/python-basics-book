"""Bug 1.3 -- Python is case-sensitive.

Buggy:   Print(message)   -> NameError: name 'Print' is not defined
Fix:     the built-in function is print, with a lower-case p.
"""
message = "Goodbye, World!"
print(message)
