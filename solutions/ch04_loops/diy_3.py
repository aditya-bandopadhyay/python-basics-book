"""D3: Sum of integers from 1 to 100 divisible by 3 or 5."""
total = 0
for n in range(1, 101):
    if n % 3 == 0 or n % 5 == 0:
        total += n
print(total)   # Output: 2418
