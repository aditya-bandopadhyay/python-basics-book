"""Bug 1.5 -- an unexpected space at the start of the second line.

Buggy:    print("Line one")
           print("Line two")     -> IndentationError: unexpected indent
Fix:     lines at the top level of a script must start at the left margin.
"""
print("Line one")
print("Line two")
