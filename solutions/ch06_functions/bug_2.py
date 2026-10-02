"""Bug 6.2 -- Python runs a script top to bottom, so square() does not exist yet
when print(square(4)) runs (NameError).

Fix: define functions before you call them.
"""
def square(n):
    return n * n

print(square(4))   # Output: 16
