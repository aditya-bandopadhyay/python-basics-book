"""
ch04_loops.py

Shows `for` and `while` loops with clear variable names and comments.
"""

def sum_first_n_integers(n: int) -> int:
    """Return the sum of the first n positive integers using a loop."""
    running_total = 0
    for current_integer in range(1, n + 1):
        running_total += current_integer
    return running_total


def countdown_from(start_value: int) -> None:
    """Prints a simple countdown using a while loop."""
    current_value = start_value
    while current_value > 0:
        print(f"T-minus {current_value}")
        current_value -= 1
    print("Liftoff!")


if __name__ == "__main__":
    print("Sum of first 10 integers:", sum_first_n_integers(10))
    countdown_from(5)
