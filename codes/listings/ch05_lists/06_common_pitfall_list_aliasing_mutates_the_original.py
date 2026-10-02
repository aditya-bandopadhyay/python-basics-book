# Lists, Tuples, Sets, and Dictionaries -- Common Pitfall: List Aliasing Mutates the Original
# (book source: ch05_lists.tex, line 204)

a = [10, 20, 30]
b = a.copy()   # True independent copy!
b[0] = 99
print(a)       # Prints [10, 20, 30] -> Original list is untouched!
