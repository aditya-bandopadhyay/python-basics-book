# Loops and Repetition -- Code 4.4: Generating AP terms and series sum
# (book source: ch04_loops.tex, line 303)

a = 2      # First term
d = 3      # Common difference
N = 5      # Total number of terms

sum_ap = 0
print("AP terms:", end=" ")
for n in range(1, N + 1):
    term = a + (n - 1) * d
    print(term, end=" ")
    sum_ap += term

print()                          # finish the line of terms
print("Sum of AP:", sum_ap)

# Output:
# AP terms: 2 5 8 11 14
# Sum of AP: 40
