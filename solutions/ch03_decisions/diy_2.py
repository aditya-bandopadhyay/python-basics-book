"""D2: Letter grade from a percentage."""
score = float(input("Percentage score: "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 45:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)
