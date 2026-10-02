"""Bug 4.1 -- range(10) gives 0..9, so the sum is 45 instead of 55.

Fix: range(1, 11) gives 1..10 (the stop value is not included).
"""
total = 0
for i in range(1, 11):
    total += i
print(total)   # Output: 55
