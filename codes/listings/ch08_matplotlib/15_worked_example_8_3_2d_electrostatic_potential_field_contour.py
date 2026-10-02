# Visualizing Data with Matplotlib -- Worked Example 8.3: 2D Electrostatic Potential Field Contour Plot
# (book source: ch08_matplotlib.tex, line 710)

import numpy as np
import matplotlib.pyplot as plt

# Generate 2D spatial grid
x = np.linspace(-3, 3, 201)   # odd count, so x = 0 is a grid point
y = np.linspace(-3, 3, 201)
X, Y = np.meshgrid(x, y)
print(f"[DEBUG] Spatial grid X, Y created with shape {X.shape}")

# Evaluate potential field V(x, y)
V = 1.0 / np.sqrt(X**2 + Y**2 + 0.5)
print(f"[DEBUG] Potential V evaluated: min={V.min():.2f} V, max={V.max():.2f} V")

# Plot filled contours using object-oriented ax interface
fig, ax = plt.subplots(figsize=(7, 6), dpi=100)
contour_filled = ax.contourf(X, Y, V, levels=12, cmap='plasma')
cbar = fig.colorbar(contour_filled, ax=ax)
cbar.set_label('Electric Potential $V$ (Volts)', fontsize=11)

# Overlay contour lines with numerical labels
lines = ax.contour(X, Y, V, levels=6, colors='white', linewidths=0.8)
ax.clabel(lines, inline=True, fontsize=8, fmt='%.2f')

ax.set_title('2D Electrostatic Potential Field Distribution', fontweight='bold')
ax.set_xlabel('Spatial Position $x$ (m)')
ax.set_ylabel('Spatial Position $y$ (m)')
ax.set_aspect('equal')
fig.tight_layout()

print(f"Peak Potential at Origin: {V[100, 100]:.4f} V")

# Output:
# [DEBUG] Spatial grid X, Y created with shape (201, 201)
# [DEBUG] Potential V evaluated: min=0.23 V, max=1.41 V
# Peak Potential at Origin: 1.4142 V
