# Why Computers Follow Rules -- Worked Example 1.2: Converting Temperature (^circtext{F} to ^circtext{C})
# (book source: ch01_why_computers.tex, line 440)

temp_fahrenheit = 375.0
temp_celsius = (temp_fahrenheit - 32.0) * (5.0 / 9.0)

print("Baking Temperature in Celsius:", round(temp_celsius, 1), "C")
# Output: Baking Temperature in Celsius: 190.6 C
