# Functions and Code Reuse -- Code 6.6: lambda functions
# (book source: ch06_functions.tex, line 417)

square = lambda x: x * x            # same as: def square(x): return x * x
print(square(7))                    # Output: 49

# A lambda passed to sorted(): sort words by their length
print(sorted(["kiwi", "fig", "banana"], key=lambda w: len(w)))
# Output: ['fig', 'kiwi', 'banana']
