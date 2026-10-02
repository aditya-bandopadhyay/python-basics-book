# Loops and Repetition -- Worked Example 4.2: Prime Number Search (Trial Division Pattern)
# (book source: ch04_loops.tex, line 474)

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
