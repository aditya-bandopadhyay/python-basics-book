# Making Decisions -- Worked Example 3.2: Leap Year Checker
# (book source: ch03_decisions.tex, line 384)

year = 2000

# Rule: Divisible by 4 AND NOT century year, OR divisible by 400
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print(f"Year {year} is a LEAP YEAR (366 days).")
else:
    print(f"Year {year} is a REGULAR YEAR (365 days).")

# Output: Year 2000 is a LEAP YEAR (366 days).
