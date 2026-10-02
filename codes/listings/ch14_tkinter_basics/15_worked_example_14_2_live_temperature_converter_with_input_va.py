# Tkinter Basics -- Worked Example 14.2: Live Temperature Converter with Input Validation
# (book source: ch14_tkinter_basics.tex, line 618)

import tkinter as tk

def convert_celsius():
    raw_input = entry_celsius.get().strip()
    if not raw_input:
        lbl_result.config(text="-- deg F", fg="#7f8c8d")
        lbl_status.config(text="Status: Please enter a temperature in Celsius.", fg="#e67e22")
        return
    try:
        celsius = float(raw_input)
        fahrenheit = (celsius * 9.0 / 5.0) + 32.0
        lbl_result.config(text=f"{fahrenheit:.1f} deg F", fg="#27ae60")
        lbl_status.config(text=f"Status: Converted {celsius:.1f} deg C = {fahrenheit:.1f} deg F", fg="#2c3e50")
    except ValueError:
        lbl_result.config(text="Error", fg="#e74c3c")
        lbl_status.config(text="Status: Invalid input! Please enter a valid number.", fg="#e74c3c")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("340x220")
root.configure(bg="#ffffff")

# Header
tk.Label(root, text="Celsius to Fahrenheit Converter", font=("Arial", 11, "bold"),
         bg="#2980b9", fg="white", pady=6).pack(fill="x")

# Content Frame
content = tk.Frame(root, bg="#ffffff", padx=15, pady=15)
content.pack(fill="both", expand=True)

tk.Label(content, text="Temperature (deg C):", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
entry_celsius = tk.Entry(content, font=("Arial", 10), width=10, bd=2, relief="groove")
entry_celsius.insert(0, "37.0")
entry_celsius.grid(row=0, column=1, padx=8, pady=5)

btn_calc = tk.Button(content, text="Convert to Fahrenheit", font=("Arial", 10, "bold"),
                     bg="#3498db", fg="white", padx=8, pady=4, command=convert_celsius)
btn_calc.grid(row=1, column=0, columnspan=2, pady=10)

lbl_result = tk.Label(content, text="98.6 deg F", font=("Arial", 16, "bold"), fg="#27ae60", bg="#ffffff")
lbl_result.grid(row=2, column=0, columnspan=2, pady=4)

# Status bar
lbl_status = tk.Label(root, text="Status: Ready", bd=1, relief="sunken", anchor="w",
                      font=("Arial", 8, "italic"), bg="#f0f0f0")
lbl_status.pack(side="bottom", fill="x")

root.mainloop()
