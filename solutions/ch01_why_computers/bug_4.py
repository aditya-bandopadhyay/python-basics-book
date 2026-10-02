"""Bug 1.4 -- the apostrophe ends the single-quoted string early.

Buggy:   print('It's a great day!')   -> SyntaxError
Fix:     use double quotes around a string that contains an apostrophe
         (or escape it: 'It\\'s a great day!').
"""
print("It's a great day!")
