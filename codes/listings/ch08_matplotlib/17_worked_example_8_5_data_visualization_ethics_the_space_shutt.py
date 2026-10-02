# Visualizing Data with Matplotlib -- Worked Example 8.5: Data Visualization Ethics - The Space Shuttle Challenger O-Ring Dataset
# (book source: ch08_matplotlib.tex, line 824)

import numpy as np
import matplotlib.pyplot as plt

# 23 pre-Challenger flights: launch temperature (deg F) and number of
# field-joint O-rings showing thermal distress (Dalal et al., 1989)
temps = np.array([66, 70, 69, 68, 67, 72, 73, 70, 57, 63, 70, 78,
                  67, 53, 67, 75, 70, 81, 76, 79, 75, 76, 58])
incidents = np.array([0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                      0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1])

damaged = incidents > 0
print(f"[DEBUG] {len(temps)} flights, {np.sum(damaged)} with O-ring damage")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))

# Panel 1: only the flights that had damage
ax1.scatter(temps[damaged], incidents[damaged], color='crimson', s=70)
ax1.set_xlim(25, 85); ax1.set_ylim(-0.2, 2.5)
ax1.set_title('Damaged Flights Only\n(7 of 23 flights)', fontsize=10, fontweight='bold')
ax1.set_xlabel('Launch Temperature (deg F)')
ax1.set_ylabel('O-Rings with Damage')
ax1.grid(True, linestyle='--', alpha=0.5)

# Panel 2: all 23 flights, plus the Challenger launch temperature
ax2.scatter(temps[~damaged], incidents[~damaged], color='navy', s=60,
            alpha=0.7, label='No damage (16 flights)')
ax2.scatter(temps[damaged], incidents[damaged], color='crimson', s=70,
            label='Damage (7 flights)')
ax2.axvline(31, color='red', linestyle=':', linewidth=2,
            label='Challenger launch (31 deg F)')
ax2.axvspan(25, temps.min(), color='gray', alpha=0.15,
            label='Colder than any previous launch')
ax2.set_xlim(25, 85); ax2.set_ylim(-0.2, 2.5)
ax2.set_title('All 23 Flights', fontsize=10, fontweight='bold')
ax2.set_xlabel('Launch Temperature (deg F)')
ax2.set_ylabel('O-Rings with Damage')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper right', fontsize=8)

fig.tight_layout()
fig.savefig('challenger_oring_analysis.pdf')

cold = temps < 65
print(f"Below 65 F: {np.sum(damaged & cold)} of {np.sum(cold)} flights damaged")
print(f"65 F and above: {np.sum(damaged & ~cold)} of {np.sum(~cold)} flights damaged")

# Output:
# [DEBUG] 23 flights, 7 with O-ring damage
# Below 65 F: 4 of 4 flights damaged
# 65 F and above: 3 of 19 flights damaged
