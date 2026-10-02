"""Bug 15.5 -- a scrollbar and a listbox must be linked both ways:
the listbox reports its position to the scrollbar (yscrollcommand=sb.set) and
the scrollbar moves the listbox (command=lb.yview).
"""
import tkinter as tk
root = tk.Tk()
lb = tk.Listbox(root)
sb = tk.Scrollbar(root)
lb.pack(side='left'); sb.pack(side='right', fill='y')
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
for i in range(50):
    lb.insert(tk.END, f'Item {i}')
root.mainloop()
