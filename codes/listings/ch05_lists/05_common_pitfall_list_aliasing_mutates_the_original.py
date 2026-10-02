# Lists, Tuples, Sets, and Dictionaries -- Common Pitfall: List Aliasing Mutates the Original
# (book source: ch05_lists.tex, line 197)

a = [10, 20, 30]
b = a          # Alias: both names point to the SAME list!
b[0] = 99
print(a)       # Prints [99, 20, 30] -> Original list was modified!
