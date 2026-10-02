# Loops and Repetition -- Try It Yourself: Tracking a Cricket Over with a Digital Counter
# (book source: ch04_loops.tex, line 39)
# This program asks you to type input in the terminal.

total_runs = 0

for ball in range(1, 7):          # balls 1, 2, 3, 4, 5, 6
    runs = int(input(f"Runs on ball {ball}: "))
    total_runs += runs            # add this ball's runs to the total
    print(f"Total so far: {total_runs}")

print(f"Over total: {total_runs} runs")
