# Layouts and User Experience -- Worked Example 15.1: Student Admission Form with Grid Layout and Alignment
# (book source: ch15_layouts_ux.tex, line 603)

import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = entry_name.get().strip()
    roll = entry_roll.get().strip()
    stream = stream_var.get()
    
    if not name or not roll:
        messagebox.showwarning("Incomplete Data", "Please fill in all required fields!")
        return
    
    messagebox.showinfo("Success", f"Admission Registered:\nName: {name}\nRoll: {roll}\nStream: {stream}")

root = tk.Tk()
root.title("Student Admission Registration")
root.geometry("420x240")
root.configure(padx=15, pady=15)

# Row 0: Form Header
lbl_header = tk.Label(root, text="STUDENT ADMISSION FORM", font=("Arial", 12, "bold"), fg="#2c3e50")
lbl_header.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Row 1: Student Name
tk.Label(root, text="Student Name:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
entry_name = tk.Entry(root, font=("Arial", 10))
entry_name.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=5)

# Row 2: Roll Number
tk.Label(root, text="Roll Number:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
entry_roll = tk.Entry(root, font=("Arial", 10))
entry_roll.grid(row=2, column=1, sticky="ew", padx=(10, 0), pady=5)

# Row 3: Academic Stream Dropdown
tk.Label(root, text="Stream / Track:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
stream_var = tk.StringVar(value="Science")
combo_stream = ttk.Combobox(root, textvariable=stream_var, values=["Science", "Commerce", "Humanities/Arts"], state="readonly")
combo_stream.grid(row=3, column=1, sticky="ew", padx=(10, 0), pady=5)

# Row 4: Submit Button
btn_submit = tk.Button(root, text="Register Admission", font=("Arial", 10, "bold"),
                       bg="#27ae60", fg="white", padx=10, pady=5, command=submit_form)
btn_submit.grid(row=4, column=0, columnspan=2, pady=(15, 0), sticky="ew")

# Make column 1 (inputs) expand horizontally with window resize
root.columnconfigure(1, weight=1)

root.mainloop()
