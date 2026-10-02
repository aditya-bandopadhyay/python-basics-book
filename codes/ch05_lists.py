"""
Lists, Tuples, Sets, and Dictionaries -- companion script for Chapter 5.
Runs the chapter's listings in the order they appear in the book.
Listings that need keyboard input, or that are fragments / deliberate
mistakes, are skipped here; every listing is in codes/listings/ch05_lists/.
Run from the repository root:  python codes/ch05_lists.py
"""

# ======================================================================
# Try It Yourself: Supermarket Shopping Cart Scanner
# ======================================================================
cart = [45.0, 120.5, 35.0, 250.0, 85.0]

print(f"Total Items:       {len(cart)}")
print(f"Total Bill Amount: Rs {sum(cart):.2f}")
print(f"Most Expensive:    Rs {max(cart):.2f}")
print(f"Cheapest Item:     Rs {min(cart):.2f}")
print(f"Sorted Bill:       {sorted(cart)}")

# ======================================================================
# Code 5.1: Creating and indexing a list
# ======================================================================
marks = [72, 85, 91, 60, 78]
print(marks[0])    # 72  (first item)
print(marks[-1])   # 78  (last item)
print(marks[1:4])  # [85, 91, 60]  (slice)

# ======================================================================
# IndexError: Stepping Off the Edge: skipped here (is a fragment / deliberate mistake); see codes/listings/ch05_lists/03_indexerror_stepping_off_the_edge.py
# ======================================================================

# ======================================================================
# Code 5.2: Working with a list of marks
# ======================================================================
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

# ======================================================================
# Common Pitfall: List Aliasing Mutates the Original
# ======================================================================
a = [10, 20, 30]
b = a          # Alias: both names point to the SAME list!
b[0] = 99
print(a)       # Prints [99, 20, 30] -> Original list was modified!

# ======================================================================
# Common Pitfall: List Aliasing Mutates the Original
# ======================================================================
a = [10, 20, 30]
b = a.copy()   # True independent copy!
b[0] = 99
print(a)       # Prints [10, 20, 30] -> Original list is untouched!

# ======================================================================
# Code 5.3: Looping over a list and a linear search
# ======================================================================
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

# ======================================================================
# Common Pitfall: Modifying a List While Looping Over It
# ======================================================================
numbers = [10, 20, 30, 40, 50]
for x in numbers:
    if x > 15:
        numbers.remove(x)
print(numbers)  # Output: [10, 30, 50] -> 30 and 50 were skipped!

# ======================================================================
# Dictionaries as Real-World Contact Cards & Student Rosters
# ======================================================================
# Phone Contact Directory
phonebook = {"Alice": "9876543210", "Bob": "9123456789"}
print(phonebook["Alice"])   # Output: "9876543210"

# Student ID Gradebook
grades = {"Roll 101": "A+", "Roll 102": "B"}
print(grades["Roll 101"])   # Output: "A+"

# ======================================================================
# Code 5.4: Counting with a dictionary
# ======================================================================
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

# ======================================================================
# Code 5.5: Common string operations
# ======================================================================
s = "The quick brown fox"

print(len(s))              # number of characters
print(s[0], s[-3:])        # first character, last three
print(s.upper())           # new string in capitals
print(s.replace("quick", "slow"))
print("fox" in s)          # is this text inside s?
print(s.count("o"))        # how many times "o" appears

words = s.split()          # break at spaces -> list of words
print(words)
print("-".join(words))     # glue a list back together

name = "  Asha  "
print("[" + name.strip() + "]")   # remove spaces at both ends

# Output:
# 19
# T fox
# THE QUICK BROWN FOX
# The slow brown fox
# True
# 2
# ['The', 'quick', 'brown', 'fox']
# The-quick-brown-fox
# [Asha]

# ======================================================================
# Worked Example 5.1: Class Test Score Statistics Generator
# ======================================================================
# Step 1: Input list of student test scores
scores = [65, 82, 90, 45, 78, 92, 55, 88]

# Step 2: Compute summary stats
count = len(scores)
total_marks = sum(scores)
average = total_marks / count

highest = max(scores)
lowest = min(scores)

# Step 3: Sort in descending order
sorted_scores = scores.copy()
sorted_scores.sort(reverse=True)

# Step 4: Display results
print(f"Total Students: {count}")
print(f"Class Average: {average:.2f}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")
print(f"Ranked Scores (Highest to Lowest): {sorted_scores}")

# Output:
# Total Students: 8
# Class Average: 74.38
# Highest Mark: 92
# Lowest Mark: 45
# Ranked Scores (Highest to Lowest): [92, 90, 88, 82, 78, 65, 55, 45]

# ======================================================================
# Worked Example 5.2: Safe Student Gradebook Lookup Using a Dictionary
# ======================================================================
gradebook = {
    "Aditya": 92,
    "Bhavna": 85,
    "Chirag": 78,
    "Divya": 95
}

query_name = "Bhavna"  # Test search

# Safe lookup: check if key exists before indexing
if query_name in gradebook:
    score = gradebook[query_name]
    print(f"Student Found: {query_name} scored {score}/100.")
else:
    print(f"Error: '{query_name}' is not in the gradebook.")
    print("Registered students:", list(gradebook.keys()))

# Output:
# Student Found: Bhavna scored 85/100.

# ======================================================================
# Real-World Solution
# ======================================================================
# A short DNA sequence stored in a list (one letter per item)
dna_sequence = ["A", "T", "G", "C", "G", "A", "T", "A", "C", "G", "T", "A"]

# 1. Inspecting length and indexing
print("Total Sequence Length:", len(dna_sequence))
print("First Base:", dna_sequence[0], "| Last Base:", dna_sequence[-1])

# 2. Slicing a candidate gene segment (index 2 to 7)
gene_segment = dna_sequence[2:8]
print("Extracted Gene Segment:", gene_segment)

# 3. Safe copying vs aliasing
independent_copy = dna_sequence.copy()  # Prevents modifying original!
independent_copy[0] = "N"               # Change copy only
print("Original Base 0 Intact:", dna_sequence[0])

# Output:
# Total Sequence Length: 12
# First Base: A | Last Base: A
# Extracted Gene Segment: ['G', 'C', 'G', 'A', 'T', 'A']
# Original Base 0 Intact: A
