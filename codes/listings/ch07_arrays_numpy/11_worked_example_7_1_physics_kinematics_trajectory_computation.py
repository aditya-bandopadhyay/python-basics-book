# Scientific Arrays with NumPy -- Worked Example 7.1: Physics Kinematics & Trajectory Computation
# (book source: ch07_arrays_numpy.tex, line 547)

import numpy as np
import matplotlib.pyplot as plt

# Physical constants and initial conditions
v0 = 40.0      # initial velocity (m/s)
g = 9.81       # gravitational acceleration (m/s^2)
t_flight = 2 * v0 / g  # total time in air (~8.16 s)

# Step 1: Generate uniform time grid using np.linspace
t = np.linspace(0, t_flight, 100)
print(f"[DEBUG] Grid created: {len(t)} time points from {t[0]:.2f}s to {t[-1]:.2f}s")

# Step 2: Compute position and velocity vectorially
y = v0 * t - 0.5 * g * (t ** 2)
v = v0 - g * t

# Step 3: Compute numerical velocity dy/dt using array differences
dt = np.diff(t)
dy = np.diff(y)
v_num = dy / dt
t_mid = (t[:-1] + t[1:]) / 2
print(f"[DEBUG] Derivative dy/dt computed for {len(v_num)} interval midpoints")

# Step 4: Find maximum height numerically and analytically
h_max_num = np.max(y)
idx_max = np.argmax(y)
h_max_analytical = (v0 ** 2) / (2 * g)
print(f"[DEBUG] Peak height reached at index {idx_max}, t = {t[idx_max]:.2f} s")

print(f"Total Flight Time:       {t_flight:.2f} s")
print(f"Numerical Max Height:    {h_max_num:.4f} m")
print(f"Analytical Max Height:   {h_max_analytical:.4f} m")
print(f"Discrepancy:             {abs(h_max_num - h_max_analytical):.6f} m")

# Step 5: Plot position and velocity curves
fig, ax1 = plt.subplots(figsize=(7, 3.5))
color = 'tab:blue'
ax1.set_xlabel('Time t (seconds)')
ax1.set_ylabel('Position y(t) (meters)', color=color)
ax1.plot(t, y, color=color, linewidth=2, label='Position y(t)')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Velocity v(t) (m/s)', color=color)
ax2.plot(t, v, color=color, linewidth=2, linestyle='--', label='Velocity v(t)')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Projectile Position y(t) and Velocity Derivative v(t)')
fig.tight_layout()
plt.savefig('fig07-02-kinematics-derivative.pdf')
