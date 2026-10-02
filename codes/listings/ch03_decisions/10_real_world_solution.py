# Making Decisions -- Real-World Solution
# (book source: ch03_decisions.tex, line 451)

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
