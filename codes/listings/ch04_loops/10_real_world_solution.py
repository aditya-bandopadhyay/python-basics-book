# Loops and Repetition -- Real-World Solution
# (book source: ch04_loops.tex, line 575)

seconds_per_year = 60 * 60 * 24 * 365.25
moves = 0                      # T(0) = 0: no disks, no moves

for n in range(1, 65):
    moves = 2 * moves + 1      # T(n) = 2 T(n-1) + 1
    if n % 8 == 0:             # print every 8th row
        years = moves / seconds_per_year
        print(f"{n:2d} disks: {moves:>26,} moves  = {years:.3g} years")

# Output:
#  8 disks:                        255 moves  = 8.08e-06 years
# 16 disks:                     65,535 moves  = 0.00208 years
# 24 disks:                 16,777,215 moves  = 0.532 years
# 32 disks:              4,294,967,295 moves  = 136 years
# 40 disks:          1,099,511,627,775 moves  = 3.48e+04 years
# 48 disks:        281,474,976,710,655 moves  = 8.92e+06 years
# 56 disks:     72,057,594,037,927,935 moves  = 2.28e+09 years
# 64 disks: 18,446,744,073,709,551,615 moves  = 5.85e+11 years
