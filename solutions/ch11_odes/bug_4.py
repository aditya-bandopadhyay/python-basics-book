"""Bug 11.4 -- the derivatives must be returned in the SAME order as the state.

The state is [x, v], so return [dx/dt, dv/dt], not [dv/dt, dx/dt].
"""
import numpy as np
from scipy.integrate import solve_ivp

def good_system(t, state):
    x, v = state
    dxdt = v
    dvdt = -x
    return [dxdt, dvdt]

sol = solve_ivp(good_system, [0, np.pi], [1.0, 0.0], rtol=1e-9)
print(round(sol.y[0, -1], 6))   # Output: -1.0  (x = cos t, so x(pi) = -1)
