"""Bug 6.5 -- countdown() calls itself forever: there is no base case.

Fix: stop when n reaches 0.
"""
def countdown(n):
    if n == 0:          # base case
        print("Lift-off!")
        return
    print(n)
    countdown(n - 1)    # smaller problem

countdown(5)
