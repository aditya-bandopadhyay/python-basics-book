# Ordinary Differential Equations -- Code 11.4: Solving ODEs with SciPy
# (book source: ch11_odes.tex, line 338)

import numpy as np
from scipy.integrate import solve_ivp

k     = 0.05
T_env = 20.0
T0    = 90.0
f_cool = lambda t, T: -k * (T - T_env)

# scipy uses f(t, y) returning array-like
sol = solve_ivp(f_cool, [0, 60], [T0],
                method='RK45',  # adaptive Runge-Kutta 4(5)
                dense_output=True,
                rtol=1e-8, atol=1e-10)

t_dense = np.linspace(0, 60, 300)
T_dense = sol.sol(t_dense)[0]
print('solve_ivp succeeded:', sol.success, '| steps taken:', len(sol.t))
