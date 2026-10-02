# Tkinter Basics -- Code 14.4: Buttons and callbacks
# (book source: ch14_tkinter_basics.tex, line 355)
# NOTE: A fragment from the book; a minimal window has been added around it so it runs.

import tkinter as tk
root = tk.Tk()   # added so the fragment can run

def on_click():
    print('Button was clicked!')

btn = tk.Button(root, text='Click me', command=on_click)
btn.pack()

root.mainloop()  # added so the fragment can run
