# Layouts and User Experience -- Code 15.1: Digits 0-9 arranged in a horizontal row
# (book source: ch15_layouts_ux.tex, line 88)

import tkinter as tk

root = tk.Tk()
root.title("Horizontal Row Layout")
root.geometry("460x100")

frame_row = tk.Frame(root)
frame_row.pack(pady=10)

# Pack buttons left to right
for digit in range(10):
    btn = tk.Button(frame_row, text=str(digit), font=("Arial", 11, "bold"), width=3)
    btn.pack(side="left", padx=2)

root.mainloop()
