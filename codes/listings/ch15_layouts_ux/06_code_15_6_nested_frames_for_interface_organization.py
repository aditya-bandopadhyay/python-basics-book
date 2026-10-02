# Layouts and User Experience -- Code 15.6: Nested frames for interface organization
# (book source: ch15_layouts_ux.tex, line 333)

import tkinter as tk

root = tk.Tk()
root.title('Organized Layout')

# Top frame for inputs
input_frame = tk.Frame(root, bg='lightgray', padx=10, pady=10)
input_frame.pack(side='top', fill='x', expand=False)

tk.Label(input_frame, text='Enter data:', bg='lightgray').pack()
entry = tk.Entry(input_frame)
entry.pack(fill='x')

# Bottom frame for buttons
btn_frame = tk.Frame(root, bg='white', padx=10, pady=10)
btn_frame.pack(side='bottom', fill='x', expand=False)

tk.Button(btn_frame, text='OK').pack(side='left', padx=5)
tk.Button(btn_frame, text='Cancel').pack(side='left', padx=5)

root.mainloop()
