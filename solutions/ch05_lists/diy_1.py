"""D1: Celsius list with Fahrenheit equivalents."""
temps_c = [-5, 0, 12.5, 18, 21, 25, 30, 37, 42, 100]
for c in temps_c:
    f = 9 / 5 * c + 32
    print(f"{c:6.1f} C = {f:6.1f} F")
