"""Bug 3.3 -- 'age >= 0' is true for every real age, so the or-condition is always True.

Fix: test only the condition that matters.
"""
age = 15
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
