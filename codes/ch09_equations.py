"""
ch09_equations.py

Solves a quadratic equation ax^2 + bx + c = 0 using the standard formula
with clear variable names and comments.
"""

import math


def solve_quadratic(
    a_coefficient: float, b_coefficient: float, c_coefficient: float
):
    """Return the real roots of the quadratic or [] if none exist."""
    disc = (
        b_coefficient ** 2 - 4 * a_coefficient * c_coefficient
    )
    if disc < 0:
        return []
    elif disc == 0:
        root = -b_coefficient / (2 * a_coefficient)
        return [root]
    else:
        sqrt_discriminant = math.sqrt(disc)
        denom = 2 * a_coefficient
        root_one = (-b_coefficient + sqrt_discriminant) / denom
        root_two = (-b_coefficient - sqrt_discriminant) / denom
        return [root_one, root_two]


if __name__ == "__main__":
    print("Roots for x^2 - 3x + 2:", solve_quadratic(1, -3, 2))
    print("Roots for x^2 + 1:", solve_quadratic(1, 0, 1))
