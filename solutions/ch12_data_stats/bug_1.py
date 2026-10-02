"""Bug 12.1 -- variance is the mean of the SQUARED DEVIATIONS (x - mu)**2,
not of x**2 - mu.
"""
def variance(data):
    mu = sum(data) / len(data)
    total = 0
    for x in data:
        total += (x - mu) ** 2
    return total / len(data)

print(variance([2, 4, 4, 4, 5, 5, 7, 9]))   # Output: 4.0
