# Ordinary Differential Equations -- Worked Example 11.3: SIR Epidemic Public Health Model with scipy.integrate.solve_ivp
# (book source: ch11_odes.tex, line 480)

import numpy as np
import scipy.integrate as integrate

# Epidemiological parameters
N_pop = 1000.0   # Total population
beta  = 0.4      # Transmission contact rate (per day)
gamma = 0.1      # Recovery / removal rate (per day)

# SIR System ODE vector function y = [S, I, R]
def sir_system(t, y):
    S, I, R = y
    dSdt = -beta * S * I / N_pop
    dIdt = (beta * S * I / N_pop) - (gamma * I)
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Initial conditions & time domain
y0 = [999.0, 1.0, 0.0]
t_span = (0.0, 60.0)
t_eval = np.linspace(0, 60, 200)

# Solve system using adaptive RK45 solver
sol = integrate.solve_ivp(sir_system, t_span, y0, t_eval=t_eval, method='RK45')

S_sol, I_sol, R_sol = sol.y
idx_peak = np.argmax(I_sol)

print(f"Basic Reproduction Number R0: {beta/gamma:.2f}")
print(f"Peak Infection Day:           {sol.t[idx_peak]:.1f} days")
print(f"Maximum Active Infection:     {I_sol[idx_peak]:.1f} cases")
print(f"Final Susceptible Remaining:  {S_sol[-1]:.1f} individuals")

# Output:
# Basic Reproduction Number R0: 4.00
# Peak Infection Day:           27.1 days
# Maximum Active Infection:     403.5 cases
# Final Susceptible Remaining:  22.9 individuals
