# Playing with Numbers -- Common Mistake: Direct Decimal Comparison
# (book source: ch02_numbers.tex, line 69)

import math
print(math.isclose(0.1 + 0.2, 0.3))  # Prints True! Safe and reliable
