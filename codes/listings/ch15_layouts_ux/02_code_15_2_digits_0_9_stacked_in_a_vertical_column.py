# Layouts and User Experience -- Code 15.2: Digits 0-9 stacked in a vertical column
# (book source: ch15_layouts_ux.tex, line 118)

import tkinter as tk

root = tk.Tk()
root.title("Vertical Stack Layout")
root.geometry("200x360")

tk.Label(root, text="Digits 0-9 Stacked\n(side=TOP)", font=("Arial", 10, "bold")).pack(pady=5)

for digit in range(10):
    btn = tk.Button(root, text=f"Button {digit}", font=("Arial", 9, "bold"), width=15)
    btn.pack(side="top", pady=2)

root.mainloop()
