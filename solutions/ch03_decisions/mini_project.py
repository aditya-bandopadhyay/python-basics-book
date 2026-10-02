"""Mini-Project 3: Number guessing game (one guess; Chapter 4 adds a loop)."""
secret = 42
guess = int(input("Guess my number (1-100): "))

if guess > secret:
    print("Too high! Guess a smaller number.")
elif guess < secret:
    print("Too low! Guess a larger number.")
else:
    print("Congratulations! You guessed it right!")
