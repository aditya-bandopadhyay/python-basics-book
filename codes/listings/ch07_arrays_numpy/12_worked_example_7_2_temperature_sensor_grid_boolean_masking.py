# Scientific Arrays with NumPy -- Worked Example 7.2: Temperature Sensor Grid & Boolean Masking
# (book source: ch07_arrays_numpy.tex, line 621)

import numpy as np

# 5x5 Temperature matrix (deg C) across plate
T = np.array([
    [25.0, 30.0, 32.0, 30.0, 25.0],
    [30.0, 42.5, 48.0, 43.0, 30.0],
    [32.0, 46.2, 51.5, 47.8, 32.0],
    [30.0, 41.0, 44.5, 40.0, 30.0],
    [25.0, 30.0, 32.0, 30.0, 25.0]
])
print(f"[DEBUG] Grid initialized: shape {T.shape}, total {T.size} sensors")

# Step 1: Extract interior 3x3 subgrid using 2D slicing
T_interior = T[1:4, 1:4]
print(f"[DEBUG] Extracted interior subgrid shape: {T_interior.shape}")

# Step 2: Boolean mask for critical temperatures
mask_overheat = T > 45.0
overheat_count = np.sum(mask_overheat)
print(f"[DEBUG] Found {overheat_count} sensors exceeding 45.0 C threshold")

# Step 3: Apply safety cap inplace
T_capped = T.copy()
T_capped[mask_overheat] = 45.0

print("Interior Subgrid (3x3):\n", T_interior)
print(f"Overheated Sensors Count: {overheat_count}")
print("Capped Matrix:\n", T_capped)

# Output:
# [DEBUG] Grid initialized: shape (5, 5), total 25 sensors
# [DEBUG] Extracted interior subgrid shape: (3, 3)
# [DEBUG] Found 4 sensors exceeding 45.0 C threshold
# Interior Subgrid (3x3):
#  [[42.5 48.  43. ]
#   [46.2 51.5 47.8]
#   [41.  44.5 40. ]]
# Overheated Sensors Count: 4
# Capped Matrix:
#  [[25.  30.  32.  30.  25. ]
#   [30.  42.5 45.  43.  30. ]
#   [32.  45.  45.  45.  32. ]
#   [30.  41.  44.5 40.  30. ]
#   [25.  30.  32.  30.  25. ]]
