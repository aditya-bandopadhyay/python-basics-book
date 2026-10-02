# Functions and Code Reuse -- Code 6.5: A recursive factorial
# (book source: ch06_functions.tex, line 397)

def factorial(n):
    if n == 0:                       # base case: stop here
        return 1
    return n * factorial(n - 1)      # recursive case: a smaller problem

print(factorial(5))   # Output: 120
