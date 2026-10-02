"""D4: A menu bar with File, Edit and Help menus."""
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Menus")
root.geometry("360x200")
label = tk.Label(root, text="Use the menus above", font=("Arial", 12))
label.pack(expand=True)

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=lambda: label.config(text="New file"))
file_menu.add_command(label="Open...", command=lambda: label.config(text="Open clicked"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Copy", command=lambda: label.config(text="Copy clicked"))
edit_menu.add_command(label="Paste", command=lambda: label.config(text="Paste clicked"))
menubar.add_cascade(label="Edit", menu=edit_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Menu demo"))
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)
root.mainloop()
