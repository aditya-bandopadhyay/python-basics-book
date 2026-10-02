# Loops and Repetition -- Worked Example 4.1: Sum of First N Natural Numbers & Formula Verification
# (book source: ch04_loops.tex, line 441)

N = 100
accumulator_sum = 0

# Step 1: Accumulate sum using loop
for i in range(1, N + 1):
    accumulator_sum += i

# Step 2: Calculate formula sum
gauss_sum = N * (N + 1) // 2

print(f"Accumulated Sum (1..{N}): {accumulator_sum}")
print(f"Gauss Formula Sum:        {gauss_sum}")
print("Verification Match:", accumulator_sum == gauss_sum)

# Output:
# Accumulated Sum (1..100): 5050
# Gauss Formula Sum:        5050
# Verification Match: True
