# Functions and Code Reuse -- Real-World Solution
# (book source: ch06_functions.tex, line 676)

# --- One gravity function, reused for every planet ---
G_CONST = 6.67430e-11  # Universal Gravitational Constant (m^3 kg^-1 s^-2)

def compute_gravitational_force(mass_body_kg, mass_craft_kg, distance_m):
    """Compute Newton's gravitational attraction force (Newtons)."""
    force_N = G_CONST * (mass_body_kg * mass_craft_kg) / (distance_m ** 2)
    return force_N

# Spacecraft mass (Voyager 1): 722 kg
voyager_mass = 722.0

# 1. Jupiter: closest approach about 349,000 km from the planet's centre
f_jupiter = compute_gravitational_force(1.898e27, voyager_mass, 349_000_000)
print(f"Gravity Force at Jupiter Flyby: {f_jupiter:.2f} N")

# 2. Saturn: closest approach about 184,000 km from the planet's centre
f_saturn = compute_gravitational_force(5.683e26, voyager_mass, 184_000_000)
print(f"Gravity Force at Saturn Flyby: {f_saturn:.2f} N")

# Output:
# Gravity Force at Jupiter Flyby: 750.91 N
# Gravity Force at Saturn Flyby: 808.88 N
