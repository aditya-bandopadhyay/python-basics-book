"""Bug 6.4 -- 'total' is a local variable of compute(); it vanishes when the
function ends.

Fix: return the value and store it in a variable outside the function.
"""
def compute():
    total = 42
    return total

total = compute()
print(total)   # Output: 42
