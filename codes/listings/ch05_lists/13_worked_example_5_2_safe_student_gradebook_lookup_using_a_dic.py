# Lists, Tuples, Sets, and Dictionaries -- Worked Example 5.2: Safe Student Gradebook Lookup Using a Dictionary
# (book source: ch05_lists.tex, line 589)

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
