"""Bug 14.5 -- after() schedules ONE call. To repeat, tick() must schedule the
next call itself.
"""
import tkinter as tk
root = tk.Tk()
count = [0]

def tick():
    count[0] += 1
    lbl.config(text=str(count[0]))
    root.after(1000, tick)        # schedule the next tick

lbl = tk.Label(root, text='0', font=("Arial", 24))
lbl.pack(padx=40, pady=20)
root.after(1000, tick)
root.mainloop()
