"""Bug 5.4 -- dictionary keys are case-sensitive: "france" is not "France".

Fix: use the exact key, or normalise text before looking it up.
"""
capitals = {"France": "Paris", "Italy": "Rome"}
print(capitals["France"])                  # Output: Paris

country = "france"
print(capitals[country.capitalize()])      # Output: Paris
