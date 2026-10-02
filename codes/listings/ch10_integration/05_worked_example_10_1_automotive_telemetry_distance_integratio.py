# Numerical Integration and Centroids -- Worked Example 10.1: Automotive Telemetry - Distance Integration from CAN-Bus Speed Logs
# (book source: ch10_integration.tex, line 293)
# NOTE: Needs code from 'Worked Example 10.1: Automotive Telemetry - Distance Integration from CAN-Bus Speed Logs' (included below as setup).

# ---- setup: code from earlier in the chapter ----
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid, cumulative_trapezoid

# OBD-II / CAN-bus vehicle speed telemetry log (t in s, v in m/s)
t_log = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40])
v_log = np.array([0, 6.2, 14.5, 22.8, 28.1, 29.5, 29.8, 25.0, 12.0])

# Compute total integrated distance over 40 seconds
total_distance = trapezoid(v_log, t_log)

# Running (cumulative) distance at every telemetry timestep
dist_cumulative = cumulative_trapezoid(v_log, t_log, initial=0)

print(f"Total Integrated Distance: {total_distance:.2f} meters")
print(f"Final Telemetry Speed:     {v_log[-1]:.1f} m/s")

# Output:
# Total Integrated Distance: 809.50 meters
# Final Telemetry Speed:     12.0 m/s

# ---- the listing itself ----
log = np.loadtxt("data/telemetry_speed.csv", delimiter=",", skiprows=1)
t_log, v_log = log[:, 0], log[:, 1]      # first and second columns
