# Tkinter Basics -- Code 14.6: Listbox
# (book source: ch14_tkinter_basics.tex, line 385)
# NOTE: A fragment from the book; a minimal window has been added around it so it runs.

import tkinter as tk
root = tk.Tk()   # added so the fragment can run

listbox = tk.Listbox(root, height=5)
for item in ['Apple', 'Banana', 'Cherry', 'Date']:
    listbox.insert(tk.END, item)
listbox.pack()

def on_select():
    selected = listbox.curselection()
    if selected:
        print(f'Selected: {listbox.get(selected[0])}')

btn = tk.Button(root, text='Select', command=on_select)
btn.pack()

root.mainloop()  # added so the fragment can run
