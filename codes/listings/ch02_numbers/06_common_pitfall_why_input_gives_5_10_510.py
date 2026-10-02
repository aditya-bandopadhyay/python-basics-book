# Playing with Numbers -- Common Pitfall: Why input() Gives "5" + "10" = "510"
# (book source: ch02_numbers.tex, line 196)
# This program asks you to type input in the terminal.

a = int(input("Enter first number: "))   # Converts "5" -> 5
b = int(input("Enter second number: "))  # Converts "10" -> 10
print(a + b)                             # Output: 15 (Correct mathematical sum!)
