# Layouts and User Experience -- Code 15.8: Visual hierarchy through typography and contrast
# (book source: ch15_layouts_ux.tex, line 397)
# NOTE: A fragment from the book; a minimal window has been added around it so it runs.

import tkinter as tk
root = tk.Tk()   # added so the fragment can run

title = tk.Label(root, text='My App', font=('Arial', 18, 'bold'))
title.pack()

subtitle = tk.Label(root, text='A simple tool', font=('Arial', 10))
subtitle.pack()

root.mainloop()  # added so the fragment can run
