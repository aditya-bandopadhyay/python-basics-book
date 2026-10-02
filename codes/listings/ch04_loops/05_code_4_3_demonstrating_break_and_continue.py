# Loops and Repetition -- Code 4.3: Demonstrating break and continue
# (book source: ch04_loops.tex, line 210)

# Example of continue: Skip number 3
print("Testing continue:")
for n in range(1, 6):
    if n == 3:
        continue  # Skip 3!
    print(n, end=" ")
# Output: 1 2 4 5

print("\n\nTesting break:")
# Example of break: Stop as soon as 3 is reached
for n in range(1, 6):
    if n == 3:
        break     # Stop loop right now!
    print(n, end=" ")
# Output: 1 2
