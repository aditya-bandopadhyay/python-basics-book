"""
ch07_arrays_numpy.py

Simple examples using numpy arrays: creation, basic arithmetic and
statistics.
"""

import numpy as np


def demonstrate_array_operations():
    sample_values = np.array([1.0, 2.5, 3.3, 4.0])
    mean_value = sample_values.mean()
    scaled_values = sample_values * 2.0
    return sample_values, mean_value, scaled_values


if __name__ == "__main__":
    values, average_value, doubled_values = demonstrate_array_operations()
    print("Original:", values)
    print("Mean:", average_value)
    print("Doubled:", doubled_values)
