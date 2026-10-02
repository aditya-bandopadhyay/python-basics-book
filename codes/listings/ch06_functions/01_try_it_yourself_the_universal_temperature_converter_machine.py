# Functions and Code Reuse -- Try It Yourself: The Universal Temperature Converter Machine
# (book source: ch06_functions.tex, line 38)

def celsius_to_fahrenheit(c):
    """Converts temperature from Celsius to Fahrenheit."""
    f = (c * 9/5) + 32
    return f

# Call the function for different temperatures
print(f"Freezing Point: {celsius_to_fahrenheit(0)} deg F")
print(f"Room Temp:      {celsius_to_fahrenheit(25)} deg F")
print(f"Human Body:     {celsius_to_fahrenheit(37)} deg F")
print(f"Boiling Point:  {celsius_to_fahrenheit(100)} deg F")
