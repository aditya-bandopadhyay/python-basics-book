# Lists, Tuples, Sets, and Dictionaries -- Code 5.3: Looping over a list and a linear search
# (book source: ch05_lists.tex, line 333)

marks = [72, 85, 91, 60, 78]

# Visit every item
for m in marks:
    print(m, end=" ")
print()

# Linear search: find the position of the first mark above 90
position = -1                       # -1 means "not found yet"
for i in range(len(marks)):
    if marks[i] > 90:
        position = i
        break
print("First mark above 90 is at index", position)

# Output:
# 72 85 91 60 78
# First mark above 90 is at index 2
