"""D1: mode(data) that reports every value in a tie."""

def mode(data):
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    highest = max(counts.values())
    winners = [value for value, c in counts.items() if c == highest]
    return winners[0] if len(winners) == 1 else sorted(winners)

print(mode([3, 7, 7, 2, 9]))          # Output: 7
print(mode([1, 2, 2, 3, 3, 4]))       # Output: [2, 3]   (a tie)
