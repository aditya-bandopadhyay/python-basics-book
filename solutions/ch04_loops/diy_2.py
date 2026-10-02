"""D2: First power of 2 that exceeds 1000, found with a while loop."""
power = 0
value = 1                  # 2 ** 0
while value <= 1000:
    power += 1
    value = 2 ** power
print(f"2 ** {power} = {value}")   # Output: 2 ** 10 = 1024
