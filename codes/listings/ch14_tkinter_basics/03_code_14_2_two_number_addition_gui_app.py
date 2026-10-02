# Tkinter Basics -- Code 14.2: Two-Number Addition GUI App
# (book source: ch14_tkinter_basics.tex, line 163)

import tkinter as tk

def calculate_sum():
    try:
        n1 = float(entry_num1.get())
        n2 = float(entry_num2.get())
        total = n1 + n2
        lbl_result.config(text=f"Result: {total:g}", fg="#27ae60")
        lbl_status.config(text=f"Status: Calculation successful ({n1:g} + {n2:g} = {total:g})")
    except ValueError:
        lbl_result.config(text="Result: Error", fg="#e74c3c")
        lbl_status.config(text="Status: Please enter valid numbers!")

root = tk.Tk()
root.title("Two-Number Adder")
root.geometry("360x260")
root.configure(bg="#ffffff")

# Title Header
tk.Label(root, text="Simple Addition Calculator", font=("Arial", 12, "bold"), 
         bg="#34495e", fg="white", pady=6).pack(fill="x")

# Main Container Frame
frame_main = tk.Frame(root, bg="#ffffff", padx=20, pady=15)
frame_main.pack(fill="both", expand=True)

# First Number Entry
tk.Label(frame_main, text="First Number:", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
entry_num1 = tk.Entry(frame_main, font=("Arial", 10), width=12, bd=2, relief="groove")
entry_num1.insert(0, "42")
entry_num1.grid(row=0, column=1, sticky="w", padx=10, pady=5)

# Second Number Entry
tk.Label(frame_main, text="Second Number:", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
entry_num2 = tk.Entry(frame_main, font=("Arial", 10), width=12, bd=2, relief="groove")
entry_num2.insert(0, "58")
entry_num2.grid(row=1, column=1, sticky="w", padx=10, pady=5)

# Calculate Button
btn_add = tk.Button(frame_main, text="Add Numbers (+)", font=("Arial", 10, "bold"), 
                    bg="#2980b9", fg="white", padx=10, pady=4, command=calculate_sum)
btn_add.grid(row=2, column=0, columnspan=2, pady=12)

# Result Display Label
lbl_result = tk.Label(frame_main, text="Result: 100", font=("Arial", 13, "bold"), fg="#27ae60", bg="#ffffff")
lbl_result.grid(row=3, column=0, columnspan=2, pady=2)

# Bottom Status Bar
lbl_status = tk.Label(root, text="Status: Ready", bd=1, relief="sunken", anchor="w", 
                      font=("Arial", 8, "italic"), bg="#f0f0f0")
lbl_status.pack(side="bottom", fill="x")

root.mainloop()
