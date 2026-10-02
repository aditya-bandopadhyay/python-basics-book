"""
Why Computers Follow Rules -- companion script for Chapter 1.
Runs the chapter's listings in the order they appear in the book.
Listings that need keyboard input, or that are fragments / deliberate
mistakes, are skipped here; every listing is in codes/listings/ch01_why_computers/.
Run from the repository root:  python codes/ch01_why_computers.py
"""

# ======================================================================
# Code 1.1: Your first Python line
# ======================================================================
print("Hello, World!")
# Output: Hello, World!

# ======================================================================
# Worked Example 1.1: Calculating Body Mass Index (BMI)
# ======================================================================
# Step 1: Store inputs in variables
weight_kg = 65.0
height_m = 1.75

# Step 2: Calculate BMI using the formula
bmi = weight_kg / (height_m ** 2)

# Step 3: Print the result
print("Calculated BMI:", round(bmi, 2))

# Output: Calculated BMI: 21.22

# ======================================================================
# Worked Example 1.2: Converting Temperature (^circtext{F} to ^circtext{C})
# ======================================================================
temp_fahrenheit = 375.0
temp_celsius = (temp_fahrenheit - 32.0) * (5.0 / 9.0)

print("Baking Temperature in Celsius:", round(temp_celsius, 1), "C")
# Output: Baking Temperature in Celsius: 190.6 C

# ======================================================================
# Real-World Solution
# ======================================================================
# The sending team meant 100 pound-force seconds (lbf*s)
impulse_lbf_s = 100.0

# --- Problem: the receiving code uses the raw number as N*s ---
impulse_used = impulse_lbf_s
print("Impulse used by navigation (N s):", impulse_used)

# --- Solution: state the unit and convert explicitly ---
newtons_per_lbf = 4.44822
impulse_N_s = impulse_lbf_s * newtons_per_lbf
print("Correct impulse (N s):", round(impulse_N_s, 2))

# Output:
# Impulse used by navigation (N s): 100.0
# Correct impulse (N s): 444.82
