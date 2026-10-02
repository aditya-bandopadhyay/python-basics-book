# Playing with Numbers -- Common Mistake: Direct Decimal Comparison
# (book source: ch02_numbers.tex, line 63)

print(0.1 + 0.2)          # Prints 0.30000000000000004
print((0.1 + 0.2) == 0.3) # Prints False! (Direct check fails)
