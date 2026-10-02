"""D1: Contact form laid out with grid()."""
import tkinter as tk

root = tk.Tk()
root.title("Contact Form")
root.columnconfigure(1, weight=1)

tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w", padx=8, pady=4)
tk.Entry(root).grid(row=0, column=1, sticky="ew", padx=8, pady=4)
tk.Label(root, text="Email:").grid(row=1, column=0, sticky="w", padx=8, pady=4)
tk.Entry(root).grid(row=1, column=1, sticky="ew", padx=8, pady=4)
tk.Label(root, text="Message:").grid(row=2, column=0, sticky="nw", padx=8, pady=4)
tk.Text(root, height=5, width=30).grid(row=2, column=1, sticky="nsew", padx=8, pady=4)
root.rowconfigure(2, weight=1)

buttons = tk.Frame(root)
buttons.grid(row=3, column=0, columnspan=2, pady=8)
tk.Button(buttons, text="Send", width=10).pack(side="left", padx=4)
tk.Button(buttons, text="Cancel", width=10, command=root.destroy).pack(side="left", padx=4)
root.mainloop()
