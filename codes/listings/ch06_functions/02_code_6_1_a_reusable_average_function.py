# Functions and Code Reuse -- Code 6.1: A reusable average function
# (book source: ch06_functions.tex, line 142)

def average(numbers):
    # Compute mean: sum divided by count
    return sum(numbers) / len(numbers)

print(average([72, 85, 91]))   # Output: 82.666...
print(average([60, 78, 88]))   # Output: 75.333...
