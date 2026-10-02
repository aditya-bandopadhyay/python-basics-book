"""Bug 5.2 -- 'count = 1' resets the counter instead of adding to it.

Fix: count += 1.
"""
marks = [45, 72, 55, 88, 91, 60]
count = 0
for m in marks:
    if m > 60:
        count += 1
print("Above 60:", count)   # Output: Above 60: 3
