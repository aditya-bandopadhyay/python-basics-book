# Lists, Tuples, Sets, and Dictionaries -- Real-World Solution
# (book source: ch05_lists.tex, line 669)

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
