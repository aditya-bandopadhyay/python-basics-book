# Functions and Code Reuse -- Code 6.7: Catching exceptions
# (book source: ch06_functions.tex, line 434)

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero; returning None.")
        return None

print(safe_divide(10, 4))
print(safe_divide(10, 0))

# Converting text that might not be a number
for text in ["42", "3.5", "abc"]:
    try:
        value = float(text)
        print("Read", value)
    except ValueError:
        print(f"'{text}' is not a number")

# Output:
# 2.5
# Cannot divide by zero; returning None.
# None
# Read 42.0
# Read 3.5
# 'abc' is not a number
