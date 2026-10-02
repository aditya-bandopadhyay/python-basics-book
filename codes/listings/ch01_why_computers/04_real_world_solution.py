# Why Computers Follow Rules -- Real-World Solution
# (book source: ch01_why_computers.tex, line 499)

# The sending team meant 100 pound-force seconds (lbf*s)
impulse_lbf_s = 100.0

# --- Problem: the receiving code uses the raw number as N*s ---
impulse_used = impulse_lbf_s
print("Impulse used by navigation (N s):", impulse_used)

# --- Solution: state the unit and convert explicitly ---
newtons_per_lbf = 4.44822
impulse_N_s = impulse_lbf_s * newtons_per_lbf
print("Correct impulse (N s):", round(impulse_N_s, 2))

# Output:
# Impulse used by navigation (N s): 100.0
# Correct impulse (N s): 444.82
