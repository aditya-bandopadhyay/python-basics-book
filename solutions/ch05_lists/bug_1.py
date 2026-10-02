"""Bug 5.1 -- a list of 5 items has indices 0..4, so scores[5] is out of range.

Fix: the last item is scores[4], or more simply scores[-1].
"""
scores = [10, 20, 30, 40, 50]
print(scores[-1])   # Output: 50
