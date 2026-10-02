"""Bug 3.4 -- the two messages are swapped.

'not score < 40' means 'score >= 40', which is the PASS case.
"""
score = 45
if score >= 40:
    print("Pass")
else:
    print("Fail")
