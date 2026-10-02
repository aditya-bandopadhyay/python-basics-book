"""Bug 14.3 -- the label shows fixed text; it is not connected to the StringVar.

Fix: give the label textvariable=text. Then every text.set() updates it.
"""
import tkinter as tk
root = tk.Tk()
text = tk.StringVar(value='hello')
lbl = tk.Label(root, textvariable=text, font=("Arial", 14))
lbl.pack(padx=30, pady=20)
text.set('updated')
root.mainloop()
