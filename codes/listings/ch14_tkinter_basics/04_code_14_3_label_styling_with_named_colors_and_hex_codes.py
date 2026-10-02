# Tkinter Basics -- Code 14.3: Label styling with named colors and hex codes
# (book source: ch14_tkinter_basics.tex, line 297)
# NOTE: A fragment from the book; a minimal window has been added around it so it runs.

import tkinter as tk
root = tk.Tk()   # added so the fragment can run

# 1. Styling with predefined X11 color names:
lbl1 = tk.Label(root, text="System Online", bg="lightblue", fg="navy")
lbl1.pack(fill="x", pady=2)

# 2. Styling with universal 6-digit hex codes (#RRGGBB):
lbl2 = tk.Label(root, text="Battery: 98%", bg="#e8f8f5", fg="#117864")
lbl2.pack(fill="x", pady=2)

root.mainloop()  # added so the fragment can run
