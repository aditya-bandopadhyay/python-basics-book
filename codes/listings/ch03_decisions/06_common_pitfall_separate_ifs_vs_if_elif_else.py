# Making Decisions -- Common Pitfall: Separate ifs vs. if-elif-else
# (book source: ch03_decisions.tex, line 171)

score = 95
# WRONG WAY: Uses separate IF statements!
if score >= 90: print("Grade A")  # True -> Prints Grade A
if score >= 80: print("Grade B")  # ALSO True -> ALSO prints Grade B!
if score >= 70: print("Grade C")  # ALSO True -> ALSO prints Grade C!
