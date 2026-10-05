# Ordinary Differential Equations -- Worked Example 11.1: Forward Euler RC Circuit Step Response
# (book source: ch11_odes.tex, line 434)

import numpy as np
import matplotlib.pyplot as plt

# Physical constants for RC electrical circuit
R = 1000.0      # Resistance (Ohms)
C = 1e-4        # Capacitance (Farads)
tau = R * C     # Time constant = 0.1 s
Vin = 5.0       # Input Voltage (V)

# Time grid setup
h = 0.01        # Step size (s)
t = np.arange(0, 0.5 + h, h)
N = len(t)

# Array allocation for voltage
V_euler = np.zeros(N)
V_euler[0] = 0.0  # Initial condition V(0) = 0

# Step 1: Forward Euler loop
for n in range(N - 1):
    dVdt = (Vin - V_euler[n]) / tau
    V_euler[n + 1] = V_euler[n] + h * dVdt

# Step 2: Analytical exact solution
V_exact = Vin * (1.0 - np.exp(-t / tau))
max_err = np.max(np.abs(V_euler - V_exact))

print(f"Time Constant tau:         {tau:.2f} s")
print(f"Euler Voltage at t=1*tau:  {V_euler[10]:.4f} V")
print(f"Exact Voltage at t=1*tau:  {V_exact[10]:.4f} V")
print(f"Maximum Discrepancy:       {max_err:.4f} V")

# Output:
# Time Constant tau:         0.10 s
# Euler Voltage at t=1*tau:  3.2566 V
# Exact Voltage at t=1*tau:  3.1606 V
# Maximum Discrepancy:       0.0960 V
