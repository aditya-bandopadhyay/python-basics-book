"""D2: is_prime(n) from Worked Example 4.2, used to list primes up to 50."""

def is_prime(n):
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for n in range(2, 51):
    if is_prime(n):
        primes.append(n)
print(primes)
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
