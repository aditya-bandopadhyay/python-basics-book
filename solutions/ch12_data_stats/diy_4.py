"""D4: Statistics and outliers for data/marks.csv. Run from the repository root."""
import numpy as np

names = np.loadtxt("data/marks.csv", delimiter=",", skiprows=1, usecols=0, dtype=str)
marks = np.loadtxt("data/marks.csv", delimiter=",", skiprows=1, usecols=(1, 2))
maths, physics = marks[:, 0], marks[:, 1]

for subject, col in [("Maths", maths), ("Physics", physics)]:
    print(f"{subject:8s} mean {col.mean():6.2f}  median {np.median(col):6.2f}  std {col.std(ddof=1):6.2f}")
print(f"Correlation r(Maths, Physics) = {np.corrcoef(maths, physics)[0, 1]:.3f}")

for subject, col in [("Maths", maths), ("Physics", physics)]:
    z = (col - col.mean()) / col.std(ddof=1)
    for name, mark, zz in zip(names, col, z):
        if abs(zz) > 2:
            print(f"Outlier: {name} has {mark:.0f} in {subject} (z = {zz:+.2f})")
# Arjun's Physics mark of 4 is flagged: it looks like a typing error for 48.
# Without it the correlation between the two subjects is much stronger.
