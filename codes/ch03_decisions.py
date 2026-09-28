"""
ch03_decisions.py

Illustrates conditional statements and a small function that
classifies numbers.
"""

def classify_integer_sign(number_to_classify: int) -> str:
    """Return a human-readable classification of the integer's sign."""
    if number_to_classify > 0:
        return "positive"
    elif number_to_classify < 0:
        return "negative"
    else:
        return "zero"


if __name__ == "__main__":
    examples = [10, -3, 0]
    for example_value in examples:
        description = classify_integer_sign(example_value)
        print(f"{example_value} is {description}.")
