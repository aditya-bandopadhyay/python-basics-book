# Building a Logarithm & Antilogarithm Calculator -- Worked Example 16.2: Compound Interest Calculator with Tabular Grid Alignment
# (book source: ch16_calculator.tex, line 441)

import tkinter as tk
from tkinter import messagebox

class CompoundInterestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compound Interest Calculator")
        self.root.geometry("380x280")
        self.root.configure(padx=15, pady=15)
        
        fields = [
            ("Principal Amount (Rs):", "10000"),
            ("Annual Interest Rate (%):", "7.5"),
            ("Investment Period (Years):", "5"),
            ("Compounding Times/Year (n):", "4"),
        ]
        
        self.entries = {}
        for row_idx, (label_text, default_val) in enumerate(fields):
            tk.Label(root, text=label_text, font=("Arial", 10)).grid(row=row_idx, column=0, sticky="w", pady=4)
            entry = tk.Entry(root, font=("Arial", 10))
            entry.insert(0, default_val)
            entry.grid(row=row_idx, column=1, sticky="ew", padx=(10, 0), pady=4)
            self.entries[label_text] = entry
            
        root.columnconfigure(1, weight=1)
        
        btn_calc = tk.Button(root, text="Calculate Growth", font=("Arial", 10, "bold"),
                             bg="#27ae60", fg="white", pady=5, command=self.calculate)
        btn_calc.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(12, 10))
        
        self.lbl_output = tk.Label(root, text="Final Amount: --\nTotal Interest: --",
                                   font=("Arial", 11, "bold"), fg="#2c3e50", justify="center")
        self.lbl_output.grid(row=5, column=0, columnspan=2, pady=5)

    def calculate(self):
        try:
            p = float(self.entries["Principal Amount (Rs):"].get())
            r = float(self.entries["Annual Interest Rate (%):"].get()) / 100.0
            t = float(self.entries["Investment Period (Years):"].get())
            n = float(self.entries["Compounding Times/Year (n):"].get())
            
            if p <= 0 or r <= 0 or t <= 0 or n <= 0:
                raise ValueError("All values must be strictly greater than zero.")
                
            amount = p * ((1 + r / n) ** (n * t))
            interest = amount - p
            
            self.lbl_output.config(
                text=f"Final Amount: Rs {amount:,.2f}\nTotal Interest: Rs {interest:,.2f}"
            )
        except ValueError as err:
            messagebox.showerror("Calculation Error", f"Invalid input: {err}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompoundInterestApp(root)
    root.mainloop()
