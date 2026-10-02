"""Bug 4.3 -- the list has 3 items (indices 0, 1, 2) but range(4) also asks for index 3.

Fix: loop over the items directly (or use range(len(fruits))).
"""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
