# Tkinter Basics -- The Pitfall (Immediate Callback Execution)
# (book source: ch14_tkinter_basics.tex, line 411)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with NameError.

# Pitfall: Executes on_click() immediately at launch!
btn = tk.Button(root, text="Submit", command=on_click())
