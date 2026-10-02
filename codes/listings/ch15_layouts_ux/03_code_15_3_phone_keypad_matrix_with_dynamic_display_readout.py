# Layouts and User Experience -- Code 15.3: Phone Keypad matrix with dynamic display readout
# (book source: ch15_layouts_ux.tex, line 146)

import tkinter as tk

def press_key(key):
    lbl_display.config(text=f"You Pressed Key: {key}")

root = tk.Tk()
root.title("Phone Keypad Layout")
root.geometry("300x320")
root.configure(bg="#2c3e50")

# Top Display Box Readout
lbl_display = tk.Label(root, text="You Pressed Key: None", font=("Arial", 14, "bold"),
                       bg="#16a085", fg="white", pady=10, bd=2, relief="ridge")
lbl_display.pack(fill="x", padx=15, pady=15)

# Keypad Grid Frame
frame_grid = tk.Frame(root, bg="#2c3e50")
frame_grid.pack()

keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

for row_idx, row in enumerate(keys):
    for col_idx, val in enumerate(row):
        btn = tk.Button(frame_grid, text=val, font=("Arial", 14, "bold"), width=4, height=1,
                        bg="#34495e", fg="white", relief="raised", bd=3,
                        command=lambda k=val: press_key(k))
        btn.grid(row=row_idx, column=col_idx, padx=5, pady=5)

root.mainloop()
