"""Bug 15.4 -- sticky='ew' lets the entry fill its cell, but the column itself
never grows. Give column 1 a weight so it receives the extra width.
"""
import tkinter as tk
root = tk.Tk()
tk.Label(root, text='Email').grid(row=0, column=0)
e = tk.Entry(root)
e.grid(row=0, column=1, sticky='ew')
root.columnconfigure(1, weight=1)
root.mainloop()
