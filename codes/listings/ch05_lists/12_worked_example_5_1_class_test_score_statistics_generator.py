# Lists, Tuples, Sets, and Dictionaries -- Worked Example 5.1: Class Test Score Statistics Generator
# (book source: ch05_lists.tex, line 545)

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
