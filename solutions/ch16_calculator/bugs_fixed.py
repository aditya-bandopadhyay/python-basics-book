"""Bugs 16.1-16.5, fixed. Each fix is a corrected method of the Chapter 16 app.

Bug 16.1 -- the menu bar was built but never attached: add
            self.root.config(menu=menubar).
Bug 16.2 -- the test was backwards: 'if val > 0' raised the error for POSITIVE
            numbers; the check must be 'if val < 0'.
Bug 16.3 -- the result was print()ed to the terminal; it must be stored in
            self.display_var (and in self.expression for the next operation).
Bug 16.4 -- 'expression = ""' created a new LOCAL variable; use self.expression.
Bug 16.5 -- the filter dropped "." so 3.14 became 314; keep "." in the allowed
            characters.
Run this file to try the calculator with all five fixes in place.
"""
import math
import tkinter as tk
from tkinter import messagebox
from _app import LogCalculatorApp


class FixedCalculator(LogCalculatorApp):
    def __init__(self, root):
        super().__init__(root)
        # Bug 16.1: build a menu bar and ATTACH it to the window
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def calc_sqrt(self):                              # Bug 16.2
        try:
            val = self.get_current_val()
            if val < 0:
                raise ValueError("Square root undefined for negative numbers.")
            res = math.sqrt(val)
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except Exception as err:
            messagebox.showerror("Math Error", str(err))

    def calc_log10(self):                             # Bug 16.3
        try:
            val = self.get_current_val()
            if val <= 0:
                raise ValueError("Logarithm undefined for numbers <= 0.")
            res = math.log10(val)
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except Exception as err:
            messagebox.showerror("Math Error", str(err))

    def clear_screen(self):                           # Bug 16.4
        self.expression = ""
        self.display_var.set("0")

    def evaluate(self):                               # Bug 16.5
        try:
            safe_expr = "".join(c for c in self.expression if c in "0123456789+-*/.()")
            result = str(eval(safe_expr))
            self.expression = result
            self.display_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear_screen()


if __name__ == "__main__":
    root = tk.Tk()
    FixedCalculator(root)
    root.mainloop()
