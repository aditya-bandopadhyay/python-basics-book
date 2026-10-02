# Scientific Arrays with NumPy -- Worked Example 7.5: Astronomical Image Processing - Synthetic 7x7 CCD Telescope Grid
# (book source: ch07_arrays_numpy.tex, line 788)

import numpy as np
import matplotlib.pyplot as plt

# Step 0: Raw 7x7 telescope CCD sensor grid (ADU counts)
raw_img = np.array([
    [ 12,  15,  10,   8,  14,  11,   9],
    [ 14,  35,  42,  38,  12,  10,  15],
    [ 10,  45,  95,  50,  15, 255,  11],  # 255 is a cosmic-ray noise spike!
    [ 11,  40,  88,  42,  14,  12,  10],
    [  9,  15,  38,  16,  10,   8,  14],
    [ 15,  11,  12,  10,  30,  35,  12],  # Faint star at bottom right
    [ 10,   8,  14,  11,  32,  28,  10]
], dtype=float)

print(f"[DEBUG] Raw CCD grid: shape {raw_img.shape}, peak raw pixel = {raw_img.max():.0f} ADU")

# Step 1: Cosmic ray filter using Boolean Masking (> 200 ADU -> 12.0 ADU)
cleaned = raw_img.copy()
mask_spike = cleaned > 200.0
cleaned[mask_spike] = 12.0
print(f"[DEBUG] Filtered {np.sum(mask_spike)} cosmic-ray spike at index {np.where(mask_spike)}")

# Step 2: Contrast & Brightness Enhancement (Vectorized scalar arithmetic)
enhanced = cleaned * 1.5 + 5.0

# Step 3: Background Sky Noise Suppression (Thresholding < 25.0 ADU -> 0.0 ADU)
processed = enhanced.copy()
processed[processed < 25.0] = 0.0
print(f"[DEBUG] Background suppressed: max peak = {processed.max():.1f} ADU")

print("\n--- Final Processed 7x7 Star Field Matrix (ADU) ---")
print(np.round(processed, 1))

# Step 4: Side-by-side plot of Raw vs Processed CCD grid
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.2))

ax1.imshow(raw_img, cmap='gray', vmin=0, vmax=255)
ax1.set_title("1. Raw CCD Image (Cosmic Ray Spike at [2,5])", fontsize=10, fontweight='bold')
ax1.set_xlabel("Column Index"); ax1.set_ylabel("Row Index")

ax2.imshow(processed, cmap='magma', vmin=0, vmax=processed.max())
ax2.set_title("2. Processed Star Field (Filtered & Thresholded)", fontsize=10, fontweight='bold')
ax2.set_xlabel("Column Index"); ax2.set_ylabel("Row Index")

plt.tight_layout()
plt.savefig("fig07-03-telescope-processing.pdf")

# Output:
# [DEBUG] Raw CCD grid: shape (7, 7), peak raw pixel = 255 ADU
# [DEBUG] Filtered 1 cosmic-ray spike at index (array([2]), array([5]))
# [DEBUG] Background suppressed: max peak = 147.5 ADU
# 
# --- Final Processed 7x7 Star Field Matrix (ADU) ---
# [[  0.  27.5   0.    0.   26.    0.    0. ]
#  [ 26.  57.5 68.  62.    0.    0.   27.5]
#  [  0.  72.5 147.5 80.   27.5   0.    0. ]
#  [  0.  65.  137.  68.   26.    0.    0. ]
#  [  0.  27.5 62.   29.    0.    0.   26. ]
#  [ 27.5  0.    0.    0.   50.   57.5   0. ]
#  [  0.    0.   26.    0.   53.   47.  0. ]]
