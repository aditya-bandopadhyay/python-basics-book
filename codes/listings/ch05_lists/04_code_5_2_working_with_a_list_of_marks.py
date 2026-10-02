# Lists, Tuples, Sets, and Dictionaries -- Code 5.2: Working with a list of marks
# (book source: ch05_lists.tex, line 154)

marks = [72, 85, 91, 60, 78]
marks.append(88)          # add 88 to the end
marks.sort()              # sort in place (smallest to largest)
print("Highest:", marks[-1])
print("Lowest:",  marks[0])
print("Average:", sum(marks) / len(marks))
marks.remove(60)          # remove first occurrence of 60
print("Count now:", len(marks))

# Output:
# Highest: 91
# Lowest: 60
# Average: 79.0
# Count now: 5
