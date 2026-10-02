# Functions and Code Reuse -- Code 6.3: Default arguments
# (book source: ch06_functions.tex, line 346)

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Aditya"))            # Output: Hello, Aditya!
print(greet("Meera", "Namaste"))  # Output: Namaste, Meera!
