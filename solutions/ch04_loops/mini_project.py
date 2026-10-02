"""Mini-Project 4: FizzBuzz from 1 to 100."""
for n in range(1, 101):
    if n % 15 == 0:            # divisible by both 3 and 5 -- test this first!
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
