"""Bug 4.5 -- i never changes, so 'i < 5' is always True: an infinite loop printing 0.

Fix: update the loop variable inside the loop.
"""
i = 0
while i < 5:
    print(i)
    i += 1
print("Done")
