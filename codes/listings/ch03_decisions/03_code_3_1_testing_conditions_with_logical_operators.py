# Making Decisions -- Code 3.1: Testing conditions with logical operators
# (book source: ch03_decisions.tex, line 123)

temperature = 38
is_hot  = temperature > 35            # True
is_cold = temperature < 10            # False
is_nice = not is_hot and not is_cold  # False
print(is_hot, is_cold, is_nice)
# Output: True False False
