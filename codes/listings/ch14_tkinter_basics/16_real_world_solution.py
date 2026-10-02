# Tkinter Basics -- Real-World Solution
# (book source: ch14_tkinter_basics.tex, line 725)

import tkinter as tk

count = 0
def register_click():
    global count
    count += 1
    lbl_display.config(text=f"Tally: {count}")

root = tk.Tk()
root.title("Xerox Clicker")
root.geometry("260x140")

lbl_display = tk.Label(root, text="Tally: 0", font=("Arial", 18, "bold"))
lbl_display.pack(pady=15)

btn_click = tk.Button(root, text="Click Mouse!", font=("Arial", 11, "bold"),
                      bg="#2980b9", fg="white", command=register_click)
btn_click.pack(pady=5)

root.mainloop()
