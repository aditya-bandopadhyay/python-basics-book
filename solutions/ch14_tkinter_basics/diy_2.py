"""D2: To-do list with Add and Remove buttons."""
import tkinter as tk

def add_item():
    text = entry.get().strip()
    if text:
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)

def remove_selected():
    sel = listbox.curselection()
    if sel:                       # nothing selected -> do nothing
        listbox.delete(sel[0])

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=(10, 4))
entry.bind("<Return>", lambda event: add_item())    # Enter key also adds

buttons = tk.Frame(root)
buttons.pack()
tk.Button(buttons, text="Add", width=10, command=add_item).pack(side="left", padx=4)
tk.Button(buttons, text="Remove", width=10, command=remove_selected).pack(side="left", padx=4)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(padx=10, pady=10)

root.mainloop()
