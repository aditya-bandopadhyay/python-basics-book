"""
Playing with Numbers -- companion script for Chapter 2.
Runs the chapter's listings in the order they appear in the book.
Listings that need keyboard input, or that are fragments / deliberate
mistakes, are skipped here; every listing is in codes/listings/ch02_numbers/.
Run from the repository root:  python codes/ch02_numbers.py
"""

# ======================================================================
# Common Mistake: Direct Decimal Comparison
# ======================================================================
print(0.1 + 0.2)          # Prints 0.30000000000000004
print((0.1 + 0.2) == 0.3) # Prints False! (Direct check fails)

# ======================================================================
# Common Mistake: Direct Decimal Comparison
# ======================================================================
import math
print(math.isclose(0.1 + 0.2, 0.3))  # Prints True! Safe and reliable

# ======================================================================
# Variables and Variable Assignment
# ======================================================================
count = 10             # Stores integer 10 in variable 'count'
name = "Subhasree"     # Stores text "Subhasree" in variable 'name'
price = 49.99          # Stores decimal 49.99 in variable 'price'

# ======================================================================
# Code 2.1: Creating and printing variables
# ======================================================================
age = 42
name = "Aditya"
pi_approx = 3.14159
print(age, name, pi_approx)
# Output: 42 Aditya 3.14159

# ======================================================================
# Common Pitfall: Why input() Gives "5" + "10" = "510": skipped here (needs keyboard input); see codes/listings/ch02_numbers/05_common_pitfall_why_input_gives_5_10_510.py
# ======================================================================

# ======================================================================
# Common Pitfall: Why input() Gives "5" + "10" = "510": skipped here (needs keyboard input); see codes/listings/ch02_numbers/06_common_pitfall_why_input_gives_5_10_510.py
# ======================================================================

# ======================================================================
# Code 2.2: Checking types with type()
# ======================================================================
print(type(7))        # <class 'int'>
print(type(7.0))      # <class 'float'>
print(type(2 + 3j))   # <class 'complex'>

# ======================================================================
# Code 2.3: Formatted output with f-strings
# ======================================================================
import math

price = 1250.758
speed_light = 299792458
val_pi = math.pi

print(f"Item Price: Rs {price:.2f}")            # Item Price: Rs 1250.76
print(f"Speed of Light: {speed_light:,.1f} m/s") # Speed of Light: 299,792,458.0 m/s
print(f"Scientific Notation: {speed_light:.3e}") # Scientific Notation: 2.998e+08
print(f"Formatted Pi: {val_pi:8.4f}")            # Formatted Pi:   3.1416

# ======================================================================
# Code 2.4: Trying out arithmetic operators
# ======================================================================
x = 7
y = 3
print(x + y)   # 10
print(x - y)   # 4
print(x * y)   # 21
print(x / y)   # 2.3333... (always a float)
print(x // y)  # 2  (floor division: whole number)
print(x % y)   # 1  (remainder)
print(x ** y)  # 343 (7 raised to power 3)

# ======================================================================
# Code 2.5: Flat-Rate Loan Calculator
# ======================================================================
# Monthly payment on a flat-rate loan (interest charged on the full amount)
principal = 120000.0   # Total loan amount in Rupees
interest_rate = 0.08   # 8% annual interest rate
years = 5              # Loan duration in years

total_interest = principal * interest_rate * years
total_payable = principal + total_interest
monthly_payment = total_payable / (years * 12)

print(f"Total Interest:    Rs {total_interest:,.2f}")
print(f"Total Amount Due:  Rs {total_payable:,.2f}")
print(f"Monthly Payment:   Rs {monthly_payment:,.2f}")

# Output:
# Total Interest:    Rs 48,000.00
# Total Amount Due:  Rs 168,000.00
# Monthly Payment:   Rs 2,800.00

# ======================================================================
# Worked Example 2.1: Simple Interest & Total Amount Calculator
# ======================================================================
# Step 1: Input values
principal = 50000.0     # Principal in Rupees
rate_percent = 7.5      # Annual interest rate in %
time_years = 3.0        # Time duration in years

# Step 2: Calculate Simple Interest and Total Amount
simple_interest = (principal * rate_percent * time_years) / 100.0
total_amount = principal + simple_interest

# Step 3: Print the formatted results
print(f"Principal Deposit: Rs {principal:,.2f}")
print(f"Simple Interest:   Rs {simple_interest:,.2f}")
print(f"Total Amount:      Rs {total_amount:,.2f}")

# Output:
# Principal Deposit: Rs 50,000.00
# Simple Interest:   Rs 11,250.00
# Total Amount:      Rs 61,250.00

# ======================================================================
# Worked Example 2.2: Breaking Down Seconds into Hours, Minutes, and Seconds
# ======================================================================
total_seconds = 7542

# Step 1: Calculate hours (3600 seconds in 1 hour)
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

# Step 2: Calculate minutes and leftover seconds (60 seconds in 1 minute)
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")
# Output: 7542 seconds = 2h 5m 42s

# ======================================================================
# Real-World Solution
# ======================================================================
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
