"""Mini-Project 6: A small statistics library written with plain Python."""

def mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2

def mode(data):
    """Return a list of the most common value(s) (there may be a tie)."""
    counts = {}
    for x in data:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    highest = max(counts.values())
    modes = []
    for value, c in counts.items():
        if c == highest:
            modes.append(value)
    return sorted(modes)

def variance(data, sample=True):
    """Sample variance (divide by n - 1) by default; population if sample=False."""
    m = mean(data)
    total = 0
    for x in data:
        total += (x - m) ** 2
    n = len(data)
    return total / (n - 1) if sample else total / n

def std_dev(data, sample=True):
    return variance(data, sample) ** 0.5


marks = [72, 85, 91, 60, 78, 85, 67, 94, 55, 85]

print("Statistics report for 10 exam marks")
print("-----------------------------------")
print(f"Marks:              {marks}")
print(f"Mean:               {mean(marks):.2f}")
print(f"Median:             {median(marks):.2f}")
print(f"Mode:               {mode(marks)}")
print(f"Variance (sample):  {variance(marks):.2f}")
print(f"Std dev (sample):   {std_dev(marks):.2f}")
