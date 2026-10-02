"""Mini-Project 5: Class report card."""
n = int(input("How many students? "))
records = []                          # list of (mark, name) tuples
for i in range(n):
    name = input(f"Name of student {i + 1}: ").strip()
    mark = float(input(f"Mark of {name}: "))
    records.append((mark, name))

marks = []
for mark, name in records:
    marks.append(mark)

best_mark, best_name = max(records)   # tuples compare by mark first
average = sum(marks) / len(marks)
passed = 0
for m in marks:
    if m >= 50:
        passed += 1

print("\n--- Class Report ---")
print(f"Highest mark: {best_mark:g} ({best_name})")
print(f"Class average: {average:.2f}")
print(f"Students passed (>= 50): {passed} of {n}")
print("Ranking:")
rank = 1
for mark, name in sorted(records, reverse=True):
    print(f"  {rank}. {name:<12} {mark:g}")
    rank += 1
