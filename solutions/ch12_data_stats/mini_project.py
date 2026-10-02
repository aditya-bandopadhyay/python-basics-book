"""Mini-Project 12: Class report for data/grades.csv. Run from the repository root."""
import numpy as np
import matplotlib.pyplot as plt

# ---- from-scratch statistics (Code 12.3) ----
def calc_mean(data):
    return sum(data) / len(data)

def calc_median(data):
    s = sorted(data); n = len(s); mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2

def calc_std(data, ddof=1):
    mu = calc_mean(data)
    return (sum((x - mu) ** 2 for x in data) / (len(data) - ddof)) ** 0.5

# ---- load the data (with the csv module, Chapter 18) ----
import csv
with open("data/grades.csv", newline="") as f:
    rows = list(csv.reader(f))
header, rows = rows[0], rows[1:]
subjects = header[1:]                                   # Maths, Science, English
names = [r[0] for r in rows]
scores = {s: [float(r[i + 1]) for r in rows] for i, s in enumerate(subjects)}

report = ["CLASS REPORT", "=" * 40, f"Students: {len(names)}", ""]
report.append(f"{'Subject':10s} {'Mean':>7s} {'Median':>7s} {'Std':>7s}")
for s in subjects:
    d = scores[s]
    report.append(f"{s:10s} {calc_mean(d):7.2f} {calc_median(d):7.2f} {calc_std(d):7.2f}")

matrix = np.corrcoef([scores[s] for s in subjects])
report += ["", "Correlation matrix:", " " * 10 + "".join(f"{s:>10s}" for s in subjects)]
for s, row in zip(subjects, matrix):
    report.append(f"{s:10s}" + "".join(f"{v:10.3f}" for v in row))

report += ["", "Students more than 1.5 std below the mean:"]
flagged = False
for s in subjects:
    cut = calc_mean(scores[s]) - 1.5 * calc_std(scores[s])
    for name, mark in zip(names, scores[s]):
        if mark < cut:
            report.append(f"  {name:8s} {s:8s} {mark:5.0f}  (cut-off {cut:.1f})")
            flagged = True
if not flagged:
    report.append("  none")
print("\n".join(report))

fig, ax = plt.subplots(figsize=(7, 4))
ax.boxplot([scores[s] for s in subjects])
ax.set_xticks(range(1, len(subjects) + 1), subjects)
ax.set_ylabel("Mark"); ax.set_title("Marks by subject"); ax.grid(True, axis="y", alpha=0.3)
fig.savefig("class_report_boxplot.png", dpi=150)
plt.show()
