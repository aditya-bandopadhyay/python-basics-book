# Making Decisions -- Mental Model: The 4-Space Indentation Room
# (book source: ch03_decisions.tex, line 158)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with NameError.

if score >= 50:
    print("Congratulations!")     # Inside the room (Runs ONLY if score >= 50)
    print("You passed the exam.") # Inside the room (Runs ONLY if score >= 50)

print("Thank you for appearing.") # Outside the room (always runs)
