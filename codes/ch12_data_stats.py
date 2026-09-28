"""
ch11_data_stats.py

Simple statistics examples using Python's built-in `statistics` module.
"""

import statistics


def compute_basic_statistics(numeric_sequence: list):
    """Return a small dict containing mean, median and stdev."""
    return {
        "mean": statistics.mean(numeric_sequence),
        "median": statistics.median(numeric_sequence),
        "stdev": statistics.pstdev(numeric_sequence),
    }


if __name__ == "__main__":
    sample_data = [2, 3, 7, 4, 9, 3]
    stats = compute_basic_statistics(sample_data)
    print("Sample data:", sample_data)
    print("Statistics:", stats)
