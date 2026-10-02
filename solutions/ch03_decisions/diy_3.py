"""D3: Traffic light (Code 3.2) with a check for unknown colours."""
colour = input("Signal colour (green/yellow/red): ").strip().lower()

if colour == "green":
    print("Go!")
elif colour == "yellow":
    print("Slow down.")
elif colour == "red":
    print("Stop!")
else:
    print("Unknown signal colour!")
