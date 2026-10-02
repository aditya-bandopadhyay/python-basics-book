# Making Decisions -- Code 3.3: Nested decisions
# (book source: ch03_decisions.tex, line 234)

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
