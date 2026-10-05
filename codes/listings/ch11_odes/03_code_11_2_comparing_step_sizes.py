# Ordinary Differential Equations -- Code 11.2: Comparing step sizes
# (book source: ch11_odes.tex, line 245)
# NOTE: Needs code from 'Code 11.1: Euler's method from scratch' (included below as setup).

# ---- setup: code from earlier in the chapter ----
import numpy as np
import matplotlib.pyplot as plt

def euler(f, y0, t_start, t_end, h):
    """Solve dy/dt = f(t,y) with Euler method; step size h."""
    t = np.arange(t_start, t_end + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(len(t) - 1):
        y[i+1] = y[i] + h * f(t[i], y[i])
    return t, y

# Newton's law of cooling: dT/dt = -k*(T - T_env)
k     = 0.05      # cooling constant (per minute)
T_env = 20.0      # room temperature (deg C)
T0    = 90.0      # initial coffee temperature

f_cool = lambda t, T: -k * (T - T_env)

t_h01, T_h01 = euler(f_cool, T0, 0, 60, h=1.0)
t_h05, T_h05 = euler(f_cool, T0, 0, 60, h=5.0)

# Exact solution for comparison
t_exact = np.linspace(0, 60, 300)
T_exact = T_env + (T0 - T_env) * np.exp(-k * t_exact)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t_exact, T_exact, 'k-',  lw=2,  label='Exact')
ax.plot(t_h01,   T_h01,   'b--', lw=1.5, label='Euler h=1')
ax.plot(t_h05,   T_h05,   'r:',  lw=1.5, label='Euler h=5')
ax.set_xlabel('Time (min)'); ax.set_ylabel('Temperature (deg C)')
ax.set_title('Coffee Cooling: Euler vs Exact')
ax.legend(); ax.grid(True); plt.tight_layout(); plt.savefig('fig11-01-euler-stepsize.pdf')

# ---- the listing itself ----
# Uses the euler() function from Code 11.1: run that first
import numpy as np

k     = 0.05
T_env = 20.0
T0    = 90.0
f_cool = lambda t, T: -k * (T - T_env)

for h in [5.0, 1.0, 0.1]:
    t, T = euler(f_cool, T0, 0, 60, h=h)
    # Error at t=60 min
    T_true = T_env + (T0 - T_env) * np.exp(-k * 60)
    print(f'h={h:4.1f}  T(60)={T[-1]:.4f}  error={abs(T[-1]-T_true):.4f}')
