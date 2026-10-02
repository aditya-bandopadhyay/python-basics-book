# Tkinter Basics -- Code 14.7: Check and radio buttons
# (book source: ch14_tkinter_basics.tex, line 427)
# NOTE: A fragment from the book; a minimal window has been added around it so it runs.

import tkinter as tk
root = tk.Tk()   # added so the fragment can run

agree = tk.IntVar(value=0)                 # 0 = off, 1 = on
tk.Checkbutton(root, text="I agree", variable=agree).pack()

unit = tk.StringVar(value="km")            # the selected option
for choice in ["km", "miles"]:
    tk.Radiobutton(root, text=choice, value=choice, variable=unit).pack()

def show_choices():
    print("Agreed:", agree.get() == 1, "| Unit:", unit.get())

tk.Button(root, text="Show", command=show_choices).pack()

root.mainloop()  # added so the fragment can run
