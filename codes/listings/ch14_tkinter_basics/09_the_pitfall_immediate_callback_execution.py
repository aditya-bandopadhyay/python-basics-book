# Tkinter Basics -- The Pitfall (Immediate Callback Execution)
# (book source: ch14_tkinter_basics.tex, line 417)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with NameError.

# Correct: Passes reference; executes only when clicked!
btn = tk.Button(root, text="Submit", command=on_click)
