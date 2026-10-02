"""Bug 15.1 -- both widgets were placed in the same cell (row 0, column 0), so the
entry is drawn on top of the label. Give each widget its own column.
"""
import tkinter as tk
root = tk.Tk()
tk.Label(root, text='Name:').grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)
root.mainloop()
