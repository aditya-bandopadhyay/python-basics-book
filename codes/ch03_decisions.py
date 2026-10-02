"""
Making Decisions -- companion script for Chapter 3.
Runs the chapter's listings in the order they appear in the book.
Listings that need keyboard input, or that are fragments / deliberate
mistakes, are skipped here; every listing is in codes/listings/ch03_decisions/.
Run from the repository root:  python codes/ch03_decisions.py
"""

# ======================================================================
# Common Mistake: Single = vs. Double ==: skipped here (is a fragment / deliberate mistake); see codes/listings/ch03_decisions/01_common_mistake_single_vs_double.py
# ======================================================================

# ======================================================================
# Try It Yourself: Smartphone Low-Battery Warning
# ======================================================================
battery = 15

if battery <= 5:
    print("CRITICAL: Shutting down phone!")
elif battery <= 20:
    print("WARNING: Low-Power Mode turned on.")
else:
    print("BATTERY OK: Normal performance.")

# ======================================================================
# Code 3.1: Testing conditions with logical operators
# ======================================================================
temperature = 38
is_hot  = temperature > 35            # True
is_cold = temperature < 10            # False
is_nice = not is_hot and not is_cold  # False
print(is_hot, is_cold, is_nice)
# Output: True False False

# ======================================================================
# Code 3.2: Traffic light decision
# ======================================================================
colour = "red"

if colour == "green":
    print("Go!")
elif colour == "yellow":
    print("Slow down.")
else:
    print("Stop!")
# Output: Stop!

# ======================================================================
# Mental Model: The 4-Space Indentation Room: skipped here (is a fragment / deliberate mistake); see codes/listings/ch03_decisions/05_mental_model_the_4_space_indentation_room.py
# ======================================================================

# ======================================================================
# Common Pitfall: Separate ifs vs. if-elif-else
# ======================================================================
score = 95
# WRONG WAY: Uses separate IF statements!
if score >= 90: print("Grade A")  # True -> Prints Grade A
if score >= 80: print("Grade B")  # ALSO True -> ALSO prints Grade B!
if score >= 70: print("Grade C")  # ALSO True -> ALSO prints Grade C!

# ======================================================================
# Code 3.3: Nested decisions
# ======================================================================
hour = 14
is_weekday = True

if is_weekday:
    if 9 <= hour <= 17:
        print("Office is open: normal working hours.")
    else:
        print("Office is closed: outside working hours.")
else:
    print("Office is closed: it is the weekend.")
# Output: Office is open: normal working hours.

# ======================================================================
# Worked Example 3.1: Tiered Electricity Bill Calculator (Slab Rates)
# ======================================================================
units = 250
bill_amount = 0.0

if units <= 100:
    bill_amount = 0.0
elif units <= 200:
    bill_amount = (units - 100) * 5.0
else:
    # First 100 free + Next 100 @ Rs 5 (Rs 500) + Remaining @ Rs 8
    bill_amount = (100 * 5.0) + (units - 200) * 8.0

print(f"Units Consumed: {units} kWh")
print(f"Total Bill:     Rs {bill_amount:,.2f}")

# Output:
# Units Consumed: 250 kWh
# Total Bill:     Rs 900.00

# ======================================================================
# Worked Example 3.2: Leap Year Checker
# ======================================================================
year = 2000

# Rule: Divisible by 4 AND NOT century year, OR divisible by 400
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print(f"Year {year} is a LEAP YEAR (366 days).")
else:
    print(f"Year {year} is a REGULAR YEAR (365 days).")

# Output: Year 2000 is a LEAP YEAR (366 days).

# ======================================================================
# Real-World Solution
# ======================================================================
satellite_alert = True
missile_count = 5
radar_confirms = False

# --- Single check: one sensor decides everything ---
if satellite_alert:
    print("Single check says: ATTACK")

# --- Several checks, in the spirit of Petrov's reasoning ---
if not satellite_alert:
    status = "All clear"
elif radar_confirms and missile_count > 50:
    status = "Attack confirmed by two independent sensors"
elif radar_confirms or missile_count > 50:
    status = "Evidence is mixed: investigate urgently"
else:
    status = "Probable false alarm: report a system fault"

print("Several checks say:", status)

# Output:
# Single check says: ATTACK
# Several checks say: Probable false alarm: report a system fault
