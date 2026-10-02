# Making Decisions -- Common Mistake: Single = vs. Double ==
# (book source: ch03_decisions.tex, line 70)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with SyntaxError.

# MISTAKE: Gives an immediate SyntaxError!
if score = 100:
    print("Full marks!")
