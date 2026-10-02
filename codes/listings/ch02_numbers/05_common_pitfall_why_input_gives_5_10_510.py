# Playing with Numbers -- Common Pitfall: Why input() Gives "5" + "10" = "510"
# (book source: ch02_numbers.tex, line 190)
# This program asks you to type input in the terminal.

a = input("Enter first number: ")   # User types 5 -> a stores "5"
b = input("Enter second number: ")  # User types 10 -> b stores "10"
print(a + b)                        # Output: "510" (Glues text, does not add!)
