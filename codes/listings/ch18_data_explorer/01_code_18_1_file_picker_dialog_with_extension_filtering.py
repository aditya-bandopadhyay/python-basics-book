# Building a CSV Data Explorer Dashboard -- Code 18.1: File picker dialog with extension filtering
# (book source: ch18_data_explorer.tex, line 76)

from tkinter import filedialog

filepath = filedialog.askopenfilename(
    title="Select Scientific CSV Dataset",
    filetypes=[("CSV Files", "*.csv"), ("Text Files", "*.txt"), ("All Files", "*.*")]
)

if filepath:
    print(f"Loading file: {filepath}")
else:
    print("User cancelled file selection.")
