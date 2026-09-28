"""
ch12_optimization.py

Shows a tiny gradient descent implementation to minimize (x-3)^2.
"""

def gradient_of_quadratic(x_value: float) -> float:
    """Gradient of (x-3)^2 is 2*(x-3)."""
    return 2.0 * (x_value - 3.0)


def simple_gradient_descent(
    initial_guess: float, learning_rate: float, steps: int
) -> float:
    """Perform a fixed number of gradient descent steps."""
    current_estimate = initial_guess
    for _ in range(steps):
        grad = gradient_of_quadratic(current_estimate)
        current_estimate = current_estimate - learning_rate * grad
    return current_estimate


if __name__ == "__main__":
    estimate = simple_gradient_descent(0.0, 0.1, 100)
    print("Estimated minimiser:", estimate)
