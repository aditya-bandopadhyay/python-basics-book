"""Bug 5.3 -- list.remove() raises ValueError if the item is not in the list.

Fix: check with 'in' first (or catch the ValueError, Section 6.7).
"""
fruits = ["apple", "cherry", "date"]
if "banana" in fruits:
    fruits.remove("banana")
print(fruits)
