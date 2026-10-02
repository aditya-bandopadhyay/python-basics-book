# Building a Logarithm & Antilogarithm Calculator -- Worked Example 16.1: Metric Unit Converter with Native Menu Bar and Status Guard
# (book source: ch16_calculator.tex, line 360)

import tkinter as tk
from tkinter import messagebox

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Distance Unit Converter")
        self.root.geometry("380x260")
        self.root.configure(padx=15, pady=15)
        
        # 1. Native Menu Bar
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Formula Info", command=self.show_formula)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menubar)
        
        # 2. Input Entry Field
        tk.Label(root, text="Enter Distance Value:", font=("Arial", 10, "bold")).pack(anchor="w")
        self.entry_val = tk.Entry(root, font=("Arial", 12))
        self.entry_val.pack(fill="x", pady=6)
        
        # 3. Conversion Direction Mode
        self.mode_var = tk.StringVar(value="km_to_mi")
        tk.Radiobutton(root, text="Kilometers to Miles (km -> mi)", variable=self.mode_var,
                       value="km_to_mi", font=("Arial", 10)).pack(anchor="w")
        tk.Radiobutton(root, text="Miles to Kilometers (mi -> km)", variable=self.mode_var,
                       value="mi_to_km", font=("Arial", 10)).pack(anchor="w")
        
        # 4. Convert Action Button
        btn_calc = tk.Button(root, text="Convert Distance", font=("Arial", 10, "bold"),
                             bg="#2980b9", fg="white", padx=10, pady=5, command=self.convert)
        btn_calc.pack(fill="x", pady=10)
        
        # 5. Result Display Label
        self.lbl_result = tk.Label(root, text="Result: --", font=("Arial", 11, "bold"), fg="#27ae60")
        self.lbl_result.pack()

    def convert(self):
        val_str = self.entry_val.get().strip()
        try:
            val = float(val_str)
            if val < 0:
                raise ValueError("Distance cannot be negative.")
            if self.mode_var.get() == "km_to_mi":
                res = val * 0.621371
                self.lbl_result.config(text=f"Result: {val:.2f} km = {res:.4f} miles")
            else:
                res = val / 0.621371
                self.lbl_result.config(text=f"Result: {val:.2f} miles = {res:.4f} km")
        except ValueError as err:
            messagebox.showerror("Input Error", f"Invalid input: {err}")

    def show_formula(self):
        messagebox.showinfo("Conversion Formula", "1 kilometer = 0.621371 miles\n1 mile = 1.60934 kilometers")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
