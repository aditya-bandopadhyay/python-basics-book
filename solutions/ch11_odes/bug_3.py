"""Bug 11.3 -- the 4th positional argument of solve_ivp is 'method', so 0.1 is
taken as a method name and rejected. The step limit is the keyword max_step.
"""
from scipy.integrate import solve_ivp
sol = solve_ivp(lambda t, y: -y, [0, 5], [1.0], max_step=0.1)
print(sol.success, len(sol.t))
