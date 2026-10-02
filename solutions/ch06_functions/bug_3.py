"""Bug 6.3 -- 'return' is indented inside the loop, so the function returns
after adding the first number.

Fix: return after the loop has finished (one level less indentation).
"""
def total(numbers):
    result = 0
    for x in numbers:
        result += x
    return result

print(total([4, 5, 6]))   # Output: 15
