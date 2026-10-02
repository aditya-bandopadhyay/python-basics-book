"""
Functions and Code Reuse -- companion script for Chapter 6.
Runs the chapter's listings in the order they appear in the book.
Listings that need keyboard input, or that are fragments / deliberate
mistakes, are skipped here; every listing is in codes/listings/ch06_functions/.
Run from the repository root:  python codes/ch06_functions.py
"""

# ======================================================================
# Try It Yourself: The Universal Temperature Converter Machine
# ======================================================================
def celsius_to_fahrenheit(c):
    """Converts temperature from Celsius to Fahrenheit."""
    f = (c * 9/5) + 32
    return f

# Call the function for different temperatures
print(f"Freezing Point: {celsius_to_fahrenheit(0)} deg F")
print(f"Room Temp:      {celsius_to_fahrenheit(25)} deg F")
print(f"Human Body:     {celsius_to_fahrenheit(37)} deg F")
print(f"Boiling Point:  {celsius_to_fahrenheit(100)} deg F")

# ======================================================================
# Code 6.1: A reusable average function
# ======================================================================
def average(numbers):
    # Compute mean: sum divided by count
    return sum(numbers) / len(numbers)

print(average([72, 85, 91]))   # Output: 82.666...
print(average([60, 78, 88]))   # Output: 75.333...

# ======================================================================
# The #1 Beginner Hurdle: print() vs. return: skipped here (is a fragment / deliberate mistake); see codes/listings/ch06_functions/03_the_1_beginner_hurdle_print_vs_return.py
# ======================================================================

# ======================================================================
# Self-Documenting Code: Docstrings and Python's help() Function
# ======================================================================
def circle_area(radius):
    """Calculates and returns the area of a circle given its radius."""
    return 3.14159 * (radius ** 2)

# ======================================================================
# Code 6.2: Local scope
# ======================================================================
def double(x):
    result = x * 2   # 'result' lives only inside double()
    return result

y = double(5)
print(y)       # Output: 10
# print(result)  # NameError: name 'result' is not defined

# ======================================================================
# Code 6.3: Default arguments
# ======================================================================
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Aditya"))            # Output: Hello, Aditya!
print(greet("Meera", "Namaste"))  # Output: Namaste, Meera!

# ======================================================================
# Common Pitfall: Mutable Default Parameter Accumulates Data
# ======================================================================
def add_item(val, container=[]):
    container.append(val)
    return container

print(add_item("Apple"))  # ['Apple']
print(add_item("Banana")) # ['Apple', 'Banana'] -> Accumulated unexpectedly!

# ======================================================================
# Common Pitfall: Mutable Default Parameter Accumulates Data
# ======================================================================
def add_item(val, container=None):
    if container is None:
        container = []
    container.append(val)
    return container

# ======================================================================
# Code 6.4: Multiple return values
# ======================================================================
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([72, 85, 91, 60, 78])
print("Min:", lo, "  Max:", hi)   # Output: Min: 60   Max: 91

# ======================================================================
# Code 6.5: A recursive factorial
# ======================================================================
def factorial(n):
    if n == 0:                       # base case: stop here
        return 1
    return n * factorial(n - 1)      # recursive case: a smaller problem

print(factorial(5))   # Output: 120

# ======================================================================
# Code 6.6: lambda functions
# ======================================================================
square = lambda x: x * x            # same as: def square(x): return x * x
print(square(7))                    # Output: 49

# A lambda passed to sorted(): sort words by their length
print(sorted(["kiwi", "fig", "banana"], key=lambda w: len(w)))
# Output: ['fig', 'kiwi', 'banana']

# ======================================================================
# Code 6.7: Catching exceptions
# ======================================================================
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero; returning None.")
        return None

print(safe_divide(10, 4))
print(safe_divide(10, 0))

# Converting text that might not be a number
for text in ["42", "3.5", "abc"]:
    try:
        value = float(text)
        print("Read", value)
    except ValueError:
        print(f"'{text}' is not a number")

# Output:
# 2.5
# Cannot divide by zero; returning None.
# None
# Read 42.0
# Read 3.5
# 'abc' is not a number

# ======================================================================
# Code 6.8: Raising your own exception
# ======================================================================
def check_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age

try:
    check_age(-3)
except ValueError as err:
    print("Error:", err)

# Output: Error: age cannot be negative

# ======================================================================
# Code 6.9: Writing and reading a text file
# ======================================================================
marks = [72, 85, 91]

# Write one mark per line
with open("marks.txt", "w") as f:
    for m in marks:
        f.write(f"{m}\n")          # write() does not add a newline itself

# Read them back: looping over a file gives one line (a string) at a time
total = 0
with open("marks.txt") as f:
    for line in f:
        total += int(line.strip())   # remove the newline, convert to int

print("Total from file:", total)   # Output: Total from file: 248

# ======================================================================
# Worked Example 6.1: Quadratic Equation Root Finder Returning Multiple Values
# ======================================================================
import math

def solve_quadratic(a, b, c):
    """Computes real roots of ax^2 + bx + c = 0.
    Returns (root1, root2) if real roots exist, else None."""
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        print("Warning: Discriminant is negative. No real roots exist.")
        return None
    
    sqrt_d = math.sqrt(discriminant)
    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)
    return root1, root2

# Test Case 1: Equation x^2 - 5x + 6 = 0  (Roots should be 3.0 and 2.0)
result = solve_quadratic(1, -5, 6)
if result is not None:
    r1, r2 = result
    print(f"Roots of x^2 - 5x + 6 = 0 are: {r1} and {r2}")

# Test Case 2: Equation x^2 + 2x + 5 = 0  (Discriminant = 4 - 20 = -16)
result_complex = solve_quadratic(1, 2, 5)
print("Result for complex roots:", result_complex)

# Output:
# Roots of x^2 - 5x + 6 = 0 are: 3.0 and 2.0
# Warning: Discriminant is negative. No real roots exist.
# Result for complex roots: None

# ======================================================================
# Worked Example 6.2: Modular Combinations Formula (nC_r) Generator
# ======================================================================
def factorial(n):
    """Computes n! = 1 * 2 * ... * n for a non-negative integer n."""
    if n < 0:
        return 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def combinations(n, r):
    """Computes nCr = n! / (r! * (n - r)!) using the factorial() function."""
    if r < 0 or r > n:
        return 0
    num = factorial(n)
    den = factorial(r) * factorial(n - r)
    return num // den

# Test: Choosing 3 committee members out of 5 candidate students (5C3)
n_students = 5
r_committee = 3
ways = combinations(n_students, r_committee)

print(f"Ways to choose {r_committee} students out of {n_students}: {ways}")
print(f"5! = {factorial(5)}, 3! = {factorial(3)}, 2! = {factorial(2)}")

# Output:
# Ways to choose 3 students out of 5: 10
# 5! = 120, 3! = 6, 2! = 2

# ======================================================================
# Real-World Solution
# ======================================================================
# --- One gravity function, reused for every planet ---
G_CONST = 6.67430e-11  # Universal Gravitational Constant (m^3 kg^-1 s^-2)

def compute_gravitational_force(mass_body_kg, mass_craft_kg, distance_m):
    """Compute Newton's gravitational attraction force (Newtons)."""
    force_N = G_CONST * (mass_body_kg * mass_craft_kg) / (distance_m ** 2)
    return force_N

# Spacecraft mass (Voyager 1): 722 kg
voyager_mass = 722.0

# 1. Jupiter: closest approach about 349,000 km from the planet's centre
f_jupiter = compute_gravitational_force(1.898e27, voyager_mass, 349_000_000)
print(f"Gravity Force at Jupiter Flyby: {f_jupiter:.2f} N")

# 2. Saturn: closest approach about 184,000 km from the planet's centre
f_saturn = compute_gravitational_force(5.683e26, voyager_mass, 184_000_000)
print(f"Gravity Force at Saturn Flyby: {f_saturn:.2f} N")

# Output:
# Gravity Force at Jupiter Flyby: 750.91 N
# Gravity Force at Saturn Flyby: 808.88 N
