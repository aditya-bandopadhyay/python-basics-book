"""Bug 2.2 -- / always gives a decimal answer.

Buggy:   weeks = days / 7   -> 52.142857...
Fix:     floor division // gives the number of whole weeks.
"""
days = 365
weeks = days // 7
print("Whole weeks:", weeks)   # Output: Whole weeks: 52
