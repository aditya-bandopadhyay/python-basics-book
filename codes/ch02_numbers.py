"""
ch02_numbers.py

Demonstrates integers, floats, and simple helper functions for
number checks.
"""

def is_even_integer(value_to_check: int) -> bool:
    """Return True if the integer is even, False otherwise."""
    return value_to_check % 2 == 0


def convert_seconds_to_hours_minutes_seconds(total_seconds: int):
    """Convert seconds to (hours, minutes, seconds) tuple."""
    hours = total_seconds // 3600
    remaining_seconds_after_hours = total_seconds % 3600
    minutes = remaining_seconds_after_hours // 60
    seconds = remaining_seconds_after_hours % 60
    return hours, minutes, seconds


if __name__ == "__main__":
    sample_number = 42
    print(f"Is {sample_number} even?", is_even_integer(sample_number))
    seconds_in_a_week = 7 * 24 * 60 * 60
    h, m, s = convert_seconds_to_hours_minutes_seconds(seconds_in_a_week)
    print(f"There are {h} hours, {m} minutes and {s} seconds in a week.")
