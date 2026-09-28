"""
ch06_functions.py

Examples of defining and using functions with clear argument names and
docstrings. Shows how to call functions and print results.
"""

def multiply_and_add(
    x_value: float, y_value: float, additive_constant: float
) -> float:
    """Return (x_value * y_value) + additive_constant."""
    product_result = x_value * y_value
    return product_result + additive_constant


def greet_person_by_name(first_name: str, last_name: str) -> str:
    """Return a polite greeting that includes the full name."""
    return f"Hello, {first_name} {last_name}!"


if __name__ == "__main__":
    print(multiply_and_add(3.0, 4.5, 2.0))
    print(greet_person_by_name("Ada", "Lovelace"))
