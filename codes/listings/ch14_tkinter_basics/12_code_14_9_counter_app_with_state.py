# Tkinter Basics -- Code 14.9: Counter app with state
# (book source: ch14_tkinter_basics.tex, line 472)

import tkinter as tk

root = tk.Tk()
root.title('Counter')

count = 0
label = tk.Label(root, text='0', font=('Arial', 24))
label.pack()

def increment():
    global count
    count += 1
    label.config(text=str(count))

btn = tk.Button(root, text='++', command=increment)
btn.pack()

root.mainloop()
