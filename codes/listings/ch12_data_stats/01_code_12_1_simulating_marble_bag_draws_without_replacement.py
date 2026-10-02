# Data Wrangling and Statistics -- Code 12.1: Simulating marble bag draws without replacement
# (book source: ch12_data_stats.tex, line 47)

import numpy as np

np.random.seed(0)   # fix the random sequence so your output matches ours

# 1. Create a bag with 5 Red and 5 Blue marbles
bag = np.array(['Red']*5 + ['Blue']*5)
n_trials = 10000
two_red_count = 0

# 2. Simulate 10,000 independent trials of drawing 2 marbles without replacement
for _ in range(n_trials):
    draw = np.random.choice(bag, size=2, replace=False)
    if draw[0] == 'Red' and draw[1] == 'Red':
        two_red_count += 1

simulated_prob = two_red_count / n_trials
theoretical_prob = (5/10) * (4/9)

print(f"Simulated Probability (2 Red):   {simulated_prob:.4f}")
print(f"Theoretical Probability (2 Red): {theoretical_prob:.4f}")
# Output:
# Simulated Probability (2 Red):   0.2226
# Theoretical Probability (2 Red): 0.2222
