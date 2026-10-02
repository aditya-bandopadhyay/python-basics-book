# Lists, Tuples, Sets, and Dictionaries -- Common Pitfall: Modifying a List While Looping Over It
# (book source: ch05_lists.tex, line 361)

numbers = [10, 20, 30, 40, 50]
for x in numbers:
    if x > 15:
        numbers.remove(x)
print(numbers)  # Output: [10, 30, 50] -> 30 and 50 were skipped!
