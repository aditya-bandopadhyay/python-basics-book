# Data Wrangling and Statistics -- Code 12.2: Simulating 10,000 dice rolls
# (book source: ch12_data_stats.tex, line 96)

import numpy as np

# 1. Simulate rolling two 6-sided dice 10,000 times
die1 = np.random.randint(1, 7, size=10000)
die2 = np.random.randint(1, 7, size=10000)
dice_sum = die1 + die2

# 2. Count occurrences of each sum from 2 to 12
sums, counts = np.unique(dice_sum, return_counts=True)
probabilities = counts / 10000

print("Sum | Simulated Probability")
print("---------------------------")
for s, p in zip(sums, probabilities):
    print(f" {s:2d} | {p:.4f}")
