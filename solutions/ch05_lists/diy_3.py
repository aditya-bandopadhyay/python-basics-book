"""D3: Remove duplicates, keeping the first appearance and the order."""
values = [3, 1, 3, 2, 1, 5]
unique = []
for x in values:
    if x not in unique:
        unique.append(x)
print(unique)   # Output: [3, 1, 2, 5]
