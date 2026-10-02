# Tkinter Basics -- Code 14.5: Text entry
# (book source: ch14_tkinter_basics.tex, line 368)
# NOTE: A fragment from the book; a minimal window has been added around it so it runs.

import tkinter as tk
root = tk.Tk()   # added so the fragment can run

entry = tk.Entry(root, width=30)
entry.pack()

def on_submit():
    user_text = entry.get()
    print(f'You typed: {user_text}')

btn = tk.Button(root, text='Submit', command=on_submit)
btn.pack()

root.mainloop()  # added so the fragment can run
