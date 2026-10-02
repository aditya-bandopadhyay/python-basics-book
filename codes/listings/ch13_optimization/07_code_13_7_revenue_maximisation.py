# Optimization and Curve Fitting -- Code 13.7: Revenue maximisation
# (book source: ch13_optimization.tex, line 319)

import numpy as np
import matplotlib.pyplot as plt

# Revenue R(p) = p * (200 - 20*(p-10)) = p*(400 - 20p)
def revenue(p):
    return p * (200 - 20 * (p - 10))

p_grid = np.linspace(1, 20, 300)
R_grid = revenue(p_grid)

fig, ax = plt.subplots()
ax.plot(p_grid, R_grid, color='steelblue')
ax.set_xlabel('Price (Rs.)'); ax.set_ylabel('Revenue (Rs.)')
ax.set_title('Revenue vs Price')
ax.axvline(5, color='red', linestyle='--', label='p=5 (starting)')

# scipy maximises by minimising negative revenue
from scipy.optimize import minimize_scalar
res = minimize_scalar(lambda p: -revenue(p), bounds=(1, 20), method='bounded')
print(f'Optimal price: Rs. {res.x:.2f}')
print(f'Max revenue:   Rs. {revenue(res.x):,.0f}')
ax.axvline(res.x, color='green', linestyle='-', label=f'Optimal p={res.x:.1f}')
ax.legend(); plt.tight_layout(); plt.show()
