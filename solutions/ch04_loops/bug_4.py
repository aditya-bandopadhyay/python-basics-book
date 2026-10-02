"""Bug 4.4 -- break leaves the whole loop at the first negative number.

Fix: continue skips just that item and carries on with the next one.
"""
numbers = [3, -1, 7, -5, 2]
for n in numbers:
    if n < 0:
        continue
    print(n)
# Output: 3, 7, 2 (one per line)
