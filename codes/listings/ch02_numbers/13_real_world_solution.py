# Playing with Numbers -- Real-World Solution
# (book source: ch02_numbers.tex, line 518)

# The Patriot kept only 23 binary places of 0.1 (a 24-bit register).
# Multiplying by 2**23, chopping with int(), and dividing back imitates that.
tenth_stored = int(0.1 * 2**23) / 2**23
loss_per_tick = 0.1 - tenth_stored

ticks = 3_600_000             # 100 hours of 0.1-second ticks
time_drift = ticks * loss_per_tick
scud_speed = 1675.0           # metres per second (about Mach 5)
position_error = scud_speed * time_drift

print(f"Stored value of 0.1: {tenth_stored:.10f}")
print(f"Loss per tick:       {loss_per_tick:.2e} seconds")
print(f"Time drift:          {time_drift:.4f} seconds")
print(f"Position error:      {position_error:.0f} metres")

# Output:
# Stored value of 0.1: 0.0999999046
# Loss per tick:       9.54e-08 seconds
# Time drift:          0.3433 seconds
# Position error:      575 metres
