# Building a Logarithm & Antilogarithm Calculator -- Code 16.2: Retro LCD Screen Configuration
# (book source: ch16_calculator.tex, line 238)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with NameError.

# Retro Matrix LCD styling (Neon Cyan text on Dark Charcoal background)
entry_display = tk.Entry(
    root,
    textvariable=self.display_var,
    font=("Consolas", 22, "bold"),   # Monospaced digital font
    bg="#1c2833",                    # Dark Charcoal / Slate background
    fg="#00ffcc",                    # Neon Matrix Cyan glowing text
    bd=5,
    relief="sunken",
    justify="right"
)
