# Functions and Code Reuse -- Code 6.8: Raising your own exception
# (book source: ch06_functions.tex, line 467)

def check_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age

try:
    check_age(-3)
except ValueError as err:
    print("Error:", err)

# Output: Error: age cannot be negative
