"""D4: Right-angled triangle of stars."""
n = 5
for row in range(1, n + 1):
    line = ""
    for _ in range(row):
        line += "*"
    print(line)
# A shorter version uses string repetition:  print("*" * row)
