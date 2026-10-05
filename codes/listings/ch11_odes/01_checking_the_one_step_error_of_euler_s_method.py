# Ordinary Differential Equations -- Checking the one-step error of Euler's method
# (book source: ch11_odes.tex, line 111)

import math

k, T_room, T0 = 0.05, 20.0, 90.0          # coffee: dT/dt = -k (T - T_room)
exact = lambda t: T_room + (T0 - T_room) * math.exp(-k * t)

print(" step h   Euler T(h)   exact T(h)   error after one step")
for h in [2.0, 1.0, 0.5, 0.25]:
    slope = -k * (T0 - T_room)            # slope at the start of the step
    T_next = T0 + h * slope               # y_{n+1} = y_n + h * slope
    error = abs(T_next - exact(h))
    print(f"{h:6.2f}   {T_next:10.4f}   {exact(h):10.4f}   {error:10.5f}")

# Output:
#  step h   Euler T(h)   exact T(h)   error after one step
#   2.00      83.0000      83.3386      0.33862
#   1.00      86.5000      86.5861      0.08606
#   0.50      88.2500      88.2717      0.02169
#   0.25      89.1250      89.1304      0.00545
