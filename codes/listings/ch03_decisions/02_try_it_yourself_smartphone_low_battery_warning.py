# Making Decisions -- Try It Yourself: Smartphone Low-Battery Warning
# (book source: ch03_decisions.tex, line 88)

battery = 15

if battery <= 5:
    print("CRITICAL: Shutting down phone!")
elif battery <= 20:
    print("WARNING: Low-Power Mode turned on.")
else:
    print("BATTERY OK: Normal performance.")
