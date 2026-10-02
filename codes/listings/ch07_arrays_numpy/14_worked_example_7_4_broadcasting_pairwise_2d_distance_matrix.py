# Scientific Arrays with NumPy -- Worked Example 7.4: Broadcasting - Pairwise 2D Distance Matrix
# (book source: ch07_arrays_numpy.tex, line 738)

import numpy as np

# Coordinates of 4 stations (N, 2)
coords = np.array([
    [0.0, 0.0],   # Station A
    [3.0, 4.0],   # Station B
    [6.0, 8.0],   # Station C
    [10.0, 0.0]   # Station D
])

# Step 1: Expand dimensions for broadcasting (4, 1, 2) and (1, 4, 2)
P1 = coords[:, np.newaxis, :]  # Shape (4, 1, 2)
P2 = coords[np.newaxis, :, :]  # Shape (1, 4, 2)
print(f"[DEBUG] Reshaped station coordinates: P1 {P1.shape}, P2 {P2.shape}")

# Step 2: Compute coordinate differences and Euclidean distance
diff = P1 - P2                 # Shape (4, 4, 2)
D = np.sqrt(np.sum(diff ** 2, axis=-1))  # Shape (4, 4)
print(f"[DEBUG] Evaluated pairwise diff shape {diff.shape} -> distance D shape {D.shape}")

print("4x4 Pairwise Distance Matrix (km):\n", np.round(D, 2))

# Output:
# [DEBUG] Reshaped station coordinates: P1 (4, 1, 2), P2 (1, 4, 2)
# [DEBUG] Evaluated pairwise diff shape (4, 4, 2) -> distance D shape (4, 4)
# 4x4 Pairwise Distance Matrix (km):
#  [[ 0.    5.   10.   10.  ]
#   [ 5.    0.    5.    8.06]
#   [10.    5.    0.    8.94]
#   [10.    8.06  8.94  0.  ]]
