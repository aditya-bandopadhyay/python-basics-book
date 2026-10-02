"""Bug 11.2 -- sol.y has one ROW per variable: shape (1, number_of_times).

Fix: take row 0 to get a 1-D array of values.
"""
from scipy.integrate import solve_ivp
sol = solve_ivp(lambda t, y: -y, [0, 5], [1.0])
T_values = sol.y[0]
print(T_values.shape)
