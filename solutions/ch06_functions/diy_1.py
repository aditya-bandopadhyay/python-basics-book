"""D1: Kilometres <-> miles, checked with a marathon distance."""

def km_to_miles(km):
    """Convert kilometres to miles."""
    return km * 0.621371

def miles_to_km(miles):
    """Convert miles to kilometres."""
    return miles / 0.621371

marathon_km = 42.195
miles = km_to_miles(marathon_km)
back = miles_to_km(miles)
print(f"{marathon_km} km = {miles:.3f} miles")
print(f"{miles:.3f} miles = {back:.3f} km")
print("Round trip matches:", abs(back - marathon_km) < 1e-9)
