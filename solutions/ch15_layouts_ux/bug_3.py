"""Bug 15.3 -- pack and grid cannot both manage widgets in the same container
(TclError: cannot use geometry manager grid inside . which already has slaves
managed by pack). Use one of them for everything in root.
"""
import tkinter as tk
root = tk.Tk()
tk.Label(root, text='Name').grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)
root.mainloop()
