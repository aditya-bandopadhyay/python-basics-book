# Building a Logarithm & Antilogarithm Calculator -- Code 16.1: Logarithm and Antilogarithm Calculator GUI
# (book source: ch16_calculator.tex, line 36)

import tkinter as tk
from tkinter import messagebox
import math

class LogCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Log & Antilog Calculator (Class 8-9 Homework Helper)")
        self.root.geometry("360x480")
        self.expression = ""

        # --- Native Menu Bar ---
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Clear Screen", command=self.clear_screen)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menubar)

        # --- Display Screen ---
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(
            root, textvariable=self.display_var, font=("Arial", 20),
            bd=5, justify="right", state="readonly"
        )
        self.display.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        # --- Button Frame ---
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for i in range(4):
            self.btn_frame.columnconfigure(i, weight=1)
        for i in range(6):
            self.btn_frame.rowconfigure(i, weight=1)

        self.create_buttons()

    def create_buttons(self):
        # Specialized homework function buttons (Row 0)
        func_buttons = [
            ("log10", self.calc_log10, 0, 0),
            ("ln", self.calc_ln, 0, 1),
            ("10^x", self.calc_antilog10, 0, 2),
            ("e^x", self.calc_antilog_e, 0, 3),
        ]
        for text, cmd, r, c in func_buttons:
            btn = tk.Button(
                self.btn_frame, text=text, font=("Arial", 11, "bold"),
                bg="#E0E0E0", command=cmd
            )
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        # Standard keypad (Rows 1-5)
        buttons = [
            ("sqrt", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("C", 5, 2), ("=", 5, 3)
        ]

        for text, row, col in buttons:
            if text == "=":
                btn = tk.Button(
                    self.btn_frame, text=text, font=("Arial", 13, "bold"),
                    bg="#4CAF50", fg="white", command=self.evaluate
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            elif text == "C":
                btn = tk.Button(
                    self.btn_frame, text=text, font=("Arial", 13, "bold"),
                    bg="#f44336", fg="white", command=self.clear_screen
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            elif text == "sqrt":
                btn = tk.Button(
                    self.btn_frame, text=text, font=("Arial", 11),
                    command=self.calc_sqrt
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            else:
                btn = tk.Button(
                    self.btn_frame, text=text, font=("Arial", 13),
                    command=lambda t=text: self.append_char(t)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    def append_char(self, char):
        self.expression += str(char)
        self.display_var.set(self.expression)

    def clear_screen(self):
        self.expression = ""
        self.display_var.set("0")

    def get_current_val(self):
        val_str = self.expression if self.expression else self.display_var.get()
        try:
            return float(val_str)
        except ValueError:
            raise ValueError("Press = to finish the calculation first.")

    def calc_log10(self):
        try:
            val = self.get_current_val()
            if val <= 0:
                raise ValueError("Logarithm undefined for numbers <= 0.")
            res = math.log10(val)
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except Exception as err:
            messagebox.showerror("Math Error", str(err))

    def calc_ln(self):
        try:
            val = self.get_current_val()
            if val <= 0:
                raise ValueError("Natural log undefined for numbers <= 0.")
            res = math.log(val)
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except Exception as err:
            messagebox.showerror("Math Error", str(err))

    def calc_antilog10(self):
        try:
            val = self.get_current_val()
            res = 10 ** val
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except Exception as err:
            messagebox.showerror("Math Error", str(err))

    def calc_antilog_e(self):
        try:
            val = self.get_current_val()
            res = math.exp(val)
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except Exception as err:
            messagebox.showerror("Math Error", str(err))

    def calc_sqrt(self):
        try:
            val = self.get_current_val()
            if val < 0:
                raise ValueError("Square root undefined for negative numbers.")
            res = math.sqrt(val)
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except Exception as err:
            messagebox.showerror("Math Error", str(err))

    def evaluate(self):
        try:
            safe_expr = "".join(
                c for c in self.expression if c in "0123456789+-*/.()"
            )
            result = str(eval(safe_expr))
            self.expression = result
            self.display_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear_screen()

    def show_about(self):
        messagebox.showinfo(
            "About", "Log & Antilog Calculator\nClass 8 & 9 Homework Companion"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = LogCalculatorApp(root)
    root.mainloop()
