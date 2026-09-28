"""
ch08_matplotlib.py

Demonstrates a minimal matplotlib example that creates data and plots it.
This file is safe to read and to use as an example; running it requires
matplotlib to be installed and a display if not running headless.
"""

import math
import matplotlib.pyplot as plt


def create_simple_plot():
    x_values = [i * 0.1 for i in range(0, 63)]
    y_values = [math.sin(x) for x in x_values]
    plt.figure(figsize=(6, 3))
    plt.plot(x_values, y_values, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Simple sine plot')
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("Creating a simple plot (requires matplotlib).")
    create_simple_plot()
