# Loops and Repetition -- Infinite Loop Emergency Brake (Ctrl + C) & Sentinel Values
# (book source: ch04_loops.tex, line 191)
# This program asks you to type input in the terminal.

while True:
    text = input("Enter word ('stop' to exit): ")
    if text == "stop":
        break  # Immediately exits the loop!
    print("Echo:", text)
