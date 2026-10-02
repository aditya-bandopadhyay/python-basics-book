"""
Loops and Repetition -- companion script for Chapter 4.
Runs the chapter's listings in the order they appear in the book.
Listings that need keyboard input, or that are fragments / deliberate
mistakes, are skipped here; every listing is in codes/listings/ch04_loops/.
Run from the repository root:  python codes/ch04_loops.py
"""

# ======================================================================
# Try It Yourself: Tracking a Cricket Over with a Digital Counter: skipped here (needs keyboard input); see codes/listings/ch04_loops/01_try_it_yourself_tracking_a_cricket_over_with_a_digital_count.py
# ======================================================================

# ======================================================================
# Code 4.1: Counting to 1000
# ======================================================================
for i in range(1, 1001):
    print(i)
# Output: 1, 2, 3, ..., 1000, each on its own line

# ======================================================================
# Code 4.2: while loop with accumulator
# ======================================================================
total = 0
i = 1
while i <= 100:
    total += i    # total = total + i
    i += 1        # i = i + 1
print("Sum of 1..100 =", total)   # Output: 5050

# ======================================================================
# Infinite Loop Emergency Brake (Ctrl + C) & Sentinel Values: skipped here (needs keyboard input); see codes/listings/ch04_loops/04_infinite_loop_emergency_brake_ctrl_c_sentinel_values.py
# ======================================================================

# ======================================================================
# Code 4.3: Demonstrating break and continue
# ======================================================================
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

# ======================================================================
# Code 4.4: Generating AP terms and series sum
# ======================================================================
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

# ======================================================================
# Code 4.5: Generating GP terms and series sum
# ======================================================================
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

# ======================================================================
# Worked Example 4.1: Sum of First N Natural Numbers & Formula Verification
# ======================================================================
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

# ======================================================================
# Worked Example 4.2: Prime Number Search (Trial Division Pattern)
# ======================================================================
num = 29
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Found a factor! Exit search loop early.

if is_prime:
    print(f"{num} is a PRIME number.")
else:
    print(f"{num} is NOT a prime number.")

# Output: 29 is a PRIME number.

# ======================================================================
# Real-World Solution
# ======================================================================
seconds_per_year = 60 * 60 * 24 * 365.25
moves = 0                      # T(0) = 0: no disks, no moves

for n in range(1, 65):
    moves = 2 * moves + 1      # T(n) = 2 T(n-1) + 1
    if n % 8 == 0:             # print every 8th row
        years = moves / seconds_per_year
        print(f"{n:2d} disks: {moves:>26,} moves  = {years:.3g} years")

# Output:
#  8 disks:                        255 moves  = 8.08e-06 years
# 16 disks:                     65,535 moves  = 0.00208 years
# 24 disks:                 16,777,215 moves  = 0.532 years
# 32 disks:              4,294,967,295 moves  = 136 years
# 40 disks:          1,099,511,627,775 moves  = 3.48e+04 years
# 48 disks:        281,474,976,710,655 moves  = 8.92e+06 years
# 56 disks:     72,057,594,037,927,935 moves  = 2.28e+09 years
# 64 disks: 18,446,744,073,709,551,615 moves  = 5.85e+11 years

# ======================================================================
# Qarabic*.
# ======================================================================
s = 0
for x in [1, 2, 3]:
    s += x
print(s)
