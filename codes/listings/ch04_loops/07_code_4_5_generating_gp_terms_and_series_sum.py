# Loops and Repetition -- Code 4.5: Generating GP terms and series sum
# (book source: ch04_loops.tex, line 371)

a = 3      # First term
r = 2      # Common ratio
N = 5      # Number of terms

gp_sum = 0
print("GP terms:", end=" ")
for n in range(1, N + 1):
    term = a * (r ** (n - 1))
    print(term, end=" ")
    gp_sum += term

print()
print("Sum of GP:", gp_sum)

# Output:
# GP terms: 3 6 12 24 48
# Sum of GP: 93
