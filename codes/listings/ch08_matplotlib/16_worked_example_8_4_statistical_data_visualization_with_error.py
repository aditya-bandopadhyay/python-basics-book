# Visualizing Data with Matplotlib -- Worked Example 8.4: Statistical Data Visualization with Error Bars
# (book source: ch08_matplotlib.tex, line 767)

import numpy as np
import matplotlib.pyplot as plt

# Experimental data
T_data = np.array([20, 30, 40, 50, 60])
mu_data = np.array([1.00, 0.80, 0.65, 0.54, 0.46])
sigma_mu = np.array([0.05, 0.04, 0.03, 0.04, 0.02])
print(f"[DEBUG] Loaded {len(T_data)} experimental viscosity data points")

# Theoretical model curve: mu(T) = 1.45 * exp(-0.019 * T)
T_fine = np.linspace(15, 65, 100)
mu_theory = 1.45 * np.exp(-0.019 * T_fine)

# Object-oriented figure and axes initialization
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=100)

# Plot theoretical model curve
ax.plot(T_fine, mu_theory, 'k--', label=r'Model: $\mu = 1.45\,e^{-0.019 T}$')

# Overlay experimental measurements with error bars
ax.errorbar(T_data, mu_data, yerr=sigma_mu, fmt='o', color='darkblue',
            ecolor='crimson', elinewidth=1.5, capsize=4, capthick=1.5,
            label=r'Lab Data ($\pm 1\sigma$ Uncertainty)')

ax.set_title('Fluid Viscosity vs Temperature with Measurement Error', fontweight='bold')
ax.set_xlabel(r'Temperature $T$ ($^\circ$C)', fontsize=11)
ax.set_ylabel(r'Viscosity $\mu$ (mPa$\cdot$s)', fontsize=11)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper right')
fig.tight_layout()

print("Relative Error at T=20C:", f"{sigma_mu[0]/mu_data[0]*100:.1f}%")

# Output:
# [DEBUG] Loaded 5 experimental viscosity data points
# Relative Error at T=20C: 5.0%
