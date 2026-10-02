# Tkinter Basics -- Try It Yourself: Building a Digital Counter Clicker App
# (book source: ch14_tkinter_basics.tex, line 31)

import tkinter as tk

count = 0

def add_click():
    global count
    count += 1
    label_count.config(text=f"Count: {count}")

root = tk.Tk()
root.title("Digital Clicker")
root.geometry("300x200")

label_count = tk.Label(root, text="Count: 0", font=("Arial", 20, "bold"))
label_count.pack(pady=20)

btn_click = tk.Button(root, text="CLICK ME!", font=("Arial", 14), command=add_click)
btn_click.pack(pady=10)

root.mainloop()
