# Lists, Tuples, Sets, and Dictionaries -- Code 5.4: Counting with a dictionary
# (book source: ch05_lists.tex, line 472)

fruits = ["apple", "mango", "apple", "banana", "apple"]
counts = {}

for f in fruits:
    if f in counts:
        counts[f] += 1        # seen before: add one
    else:
        counts[f] = 1         # first time: start at one

for fruit, n in counts.items():
    print(fruit, n)

# Output:
# apple 3
# mango 1
# banana 1
