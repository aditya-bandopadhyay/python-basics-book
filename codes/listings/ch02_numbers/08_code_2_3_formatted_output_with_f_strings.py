# Playing with Numbers -- Code 2.3: Formatted output with f-strings
# (book source: ch02_numbers.tex, line 304)

import math

price = 1250.758
speed_light = 299792458
val_pi = math.pi

print(f"Item Price: Rs {price:.2f}")            # Item Price: Rs 1250.76
print(f"Speed of Light: {speed_light:,.1f} m/s") # Speed of Light: 299,792,458.0 m/s
print(f"Scientific Notation: {speed_light:.3e}") # Scientific Notation: 2.998e+08
print(f"Formatted Pi: {val_pi:8.4f}")            # Formatted Pi:   3.1416
