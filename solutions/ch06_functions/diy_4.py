"""D4: FizzBuzz as a function."""

def fizzbuzz(n):
    """Return 'Fizz', 'Buzz', 'FizzBuzz', or the number as a string."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

for n in range(1, 21):
    print(fizzbuzz(n))
