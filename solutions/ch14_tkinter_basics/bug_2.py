"""Bug 14.2 -- creating a widget does not show it; it must be placed with a
geometry manager (pack, grid or place).
"""
import tkinter as tk
root = tk.Tk()
entry = tk.Entry(root)
entry.pack(padx=20, pady=20)
root.mainloop()
