"""D4: Leap-year checker, tested with 2024, 2000, 1900 and 2023."""
year = int(input("Year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Expected results: 2024 leap, 2000 leap, 1900 not leap, 2023 not leap.
