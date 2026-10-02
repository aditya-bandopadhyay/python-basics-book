# Loops and Repetition -- Code 4.2: while loop with accumulator
# (book source: ch04_loops.tex, line 108)

total = 0
i = 1
while i <= 100:
    total += i    # total = total + i
    i += 1        # i = i + 1
print("Sum of 1..100 =", total)   # Output: 5050
