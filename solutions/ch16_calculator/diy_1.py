"""D1: Add a log2 button to the Chapter 16 calculator."""
import math
import tkinter as tk
from tkinter import messagebox
from _app import LogCalculatorApp


class Log2Calculator(LogCalculatorApp):
    def create_buttons(self):
        super().create_buttons()
        self.btn_frame.rowconfigure(6, weight=1)
        tk.Button(self.btn_frame, text="log2", font=("Arial", 11, "bold"), bg="#E0E0E0",
                  command=self.calc_log2).grid(row=6, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

    def calc_log2(self):
        try:
            val = self.get_current_val()
            if val <= 0:
                raise ValueError("Logarithm undefined for numbers <= 0.")
            res = math.log(val, 2)
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except Exception as err:
            messagebox.showerror("Math Error", str(err))


if __name__ == "__main__":
    root = tk.Tk()
    Log2Calculator(root)
    root.mainloop()
