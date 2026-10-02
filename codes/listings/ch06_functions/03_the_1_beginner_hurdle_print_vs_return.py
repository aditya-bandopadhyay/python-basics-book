# Functions and Code Reuse -- The #1 Beginner Hurdle: print() vs. return
# (book source: ch06_functions.tex, line 155)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with TypeError.

# BUGGY FUNCTION: Uses print() instead of return!
def add_bad(a, b):
    print(a + b)  # Displays answer on screen, but HANDS NOTHING BACK!

result = add_bad(5, 10)  # Screen shows 15, but result stores None!
print(result + 2)        # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
