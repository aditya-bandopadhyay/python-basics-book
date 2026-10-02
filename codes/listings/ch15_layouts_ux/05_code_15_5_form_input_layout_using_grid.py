# Layouts and User Experience -- Code 15.5: Form input layout using .grid()
# (book source: ch15_layouts_ux.tex, line 287)

import tkinter as tk

root = tk.Tk()
root.title('Grid Example')

tk.Label(root, text='Name:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

tk.Label(root, text='Email:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

btn = tk.Button(root, text='Submit')
btn.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

root.columnconfigure(1, weight=1)  # column 1 expands
root.mainloop()
