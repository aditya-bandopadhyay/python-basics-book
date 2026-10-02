"""Bug 14.1 -- command=say_hello() CALLS the function while the button is being
built and passes its return value (None) as the command.

Fix: pass the function itself, without brackets.
"""
import tkinter as tk

def say_hello():
    print('Hello!')

root = tk.Tk()
btn = tk.Button(root, text='Click', command=say_hello)
btn.pack(padx=40, pady=20)
root.mainloop()
