# Functions and Code Reuse -- Code 6.9: Writing and reading a text file
# (book source: ch06_functions.tex, line 491)

marks = [72, 85, 91]

# Write one mark per line
with open("marks.txt", "w") as f:
    for m in marks:
        f.write(f"{m}\n")          # write() does not add a newline itself

# Read them back: looping over a file gives one line (a string) at a time
total = 0
with open("marks.txt") as f:
    for line in f:
        total += int(line.strip())   # remove the newline, convert to int

print("Total from file:", total)   # Output: Total from file: 248
