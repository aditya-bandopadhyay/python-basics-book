# Visualizing Data with Matplotlib -- Worked Example 8.1: Damped Harmonic Oscillator & Decay Envelopes
# (book source: ch08_matplotlib.tex, line 582)

import numpy as np
import matplotlib.pyplot as plt

# Physical constants
A = 5.0        # Initial amplitude (cm)
gamma = 0.5    # Damping rate (1/s)
omega = 2 * np.pi  # Angular frequency (rad/s)

# Time grid
t = np.linspace(0, 8, 500)
print(f"[DEBUG] Grid initialized: {len(t)} points over interval [0, {t[-1]}] s")

# Calculate displacement and envelope
x = A * np.exp(-gamma * t) * np.cos(omega * t)
env_upper = A * np.exp(-gamma * t)
env_lower = -env_upper

# Create plot
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=100)
ax.plot(t, x, 'b-', linewidth=1.8, label=r'Displacement $x(t)$')
ax.plot(t, env_upper, 'r--', linewidth=1.2, label=r'Decay Envelope $\pm A e^{-\gamma t}$')
ax.plot(t, env_lower, 'r--', linewidth=1.2)

# Styling and labels
ax.set_title('Damped Harmonic Oscillator Response', fontsize=12, fontweight='bold')
ax.set_xlabel('Time $t$ (seconds)', fontsize=11)
ax.set_ylabel('Displacement $x(t)$ (cm)', fontsize=11)
ax.axhline(0, color='black', linewidth=0.8, linestyle=':')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper right', frameon=True)
fig.tight_layout()

# Print confirmation
print(f"Max Displacement at t=0: {x[0]:.1f} cm")
print(f"Residual Amplitude at t=8s: {env_upper[-1]:.4f} cm")

# Output:
# [DEBUG] Grid initialized: 500 points over interval [0, 8.0] s
# Max Displacement at t=0: 5.0 cm
# Residual Amplitude at t=8s: 0.0916 cm
