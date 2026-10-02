# Why Computers Follow Rules -- Worked Example 1.1: Calculating Body Mass Index (BMI)
# (book source: ch01_why_computers.tex, line 414)

# Step 1: Store inputs in variables
weight_kg = 65.0
height_m = 1.75

# Step 2: Calculate BMI using the formula
bmi = weight_kg / (height_m ** 2)

# Step 3: Print the result
print("Calculated BMI:", round(bmi, 2))

# Output: Calculated BMI: 21.22
