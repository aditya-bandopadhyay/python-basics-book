"""Mini-Project 16: Expanded scientific logarithm calculator.

Features: log10, ln, log2, log base b; 10^x, e^x, 2^x; sin/cos/tan with a
degrees/radians switch; a history "tape" in a sidebar that can be hidden; and
error dialogs for domain errors, overflow and division by zero.
"""
import math
import tkinter as tk
from tkinter import messagebox, simpledialog


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Scientific Logarithm Calculator")
        root.geometry("620x460")
        self.expression = ""
        self.angle_mode = tk.StringVar(value="deg")

        main = tk.Frame(root, padx=8, pady=8)
        main.pack(side="left", fill="both", expand=True)
        self.sidebar = tk.Frame(root, padx=6, pady=8, bg="#ecf0f1")
        self.sidebar.pack(side="right", fill="y")
        tk.Label(self.sidebar, text="History", bg="#ecf0f1", font=("Arial", 10, "bold")).pack()
        self.tape = tk.Listbox(self.sidebar, width=26)
        self.tape.pack(fill="y", expand=True)

        self.display_var = tk.StringVar(value="0")
        tk.Entry(main, textvariable=self.display_var, font=("Consolas", 20), justify="right",
                 state="readonly").pack(fill="x", pady=(0, 6))

        modes = tk.Frame(main)
        modes.pack(fill="x")
        tk.Radiobutton(modes, text="Degrees", value="deg", variable=self.angle_mode).pack(side="left")
        tk.Radiobutton(modes, text="Radians", value="rad", variable=self.angle_mode).pack(side="left")
        tk.Button(modes, text="Hide/Show History", command=self.toggle_tape).pack(side="right")

        grid = tk.Frame(main)
        grid.pack(fill="both", expand=True, pady=6)
        functions = [
            ("log10", lambda x: math.log10(self.positive(x))), ("ln", lambda x: math.log(self.positive(x))),
            ("log2", lambda x: math.log2(self.positive(x))), ("log_b", None),
            ("10^x", lambda x: 10 ** x), ("e^x", math.exp), ("2^x", lambda x: 2 ** x), ("1/x", lambda x: 1 / x),
            ("sin", lambda x: math.sin(self.to_rad(x))), ("cos", lambda x: math.cos(self.to_rad(x))),
            ("tan", self.safe_tan), ("sqrt", lambda x: math.sqrt(x)),
        ]
        keys = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "C", "+", "(", ")", "=", ""]
        for i, (name, fn) in enumerate(functions):
            cmd = self.calc_log_base if name == "log_b" else (lambda n=name, f=fn: self.apply(n, f))
            tk.Button(grid, text=name, bg="#dfe6e9", command=cmd).grid(row=i // 4, column=i % 4, sticky="nsew", padx=1, pady=1)
        for j, key in enumerate(keys):
            if not key:
                continue
            r, c = 3 + j // 4, j % 4
            cmd = {"C": self.clear, "=": self.evaluate}.get(key, lambda k=key: self.append(k))
            tk.Button(grid, text=key, font=("Arial", 12), command=cmd).grid(row=r, column=c, sticky="nsew", padx=1, pady=1)
        for c in range(4):
            grid.columnconfigure(c, weight=1)
        for r in range(8):
            grid.rowconfigure(r, weight=1)

    # ---- helpers ----
    def positive(self, x):
        if x <= 0:
            raise ValueError("Logarithm undefined for numbers <= 0.")
        return x

    def to_rad(self, x):
        return math.radians(x) if self.angle_mode.get() == "deg" else x

    def safe_tan(self, x):
        if abs(math.cos(self.to_rad(x))) < 1e-12:
            raise ValueError("tan is undefined here (cos = 0).")
        return math.tan(self.to_rad(x))

    def current_value(self):
        text = self.expression or self.display_var.get()
        try:
            return float(text)
        except ValueError:
            raise ValueError("Press = to finish the calculation first.")

    def show(self, label, value):
        self.expression = repr(value)
        self.display_var.set(f"{value:.10g}")
        self.tape.insert(tk.END, f"{label} = {value:.8g}")
        self.tape.see(tk.END)

    # ---- actions ----
    def apply(self, name, fn):
        try:
            x = self.current_value()
            self.show(f"{name}({x:g})", fn(x))
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Division by zero.")
        except OverflowError:
            messagebox.showerror("Math Error", "Result is too large to represent.")
        except ValueError as err:
            messagebox.showerror("Math Error", str(err) or "Invalid input for this function.")

    def calc_log_base(self):
        try:
            x = self.positive(self.current_value())
        except ValueError as err:
            messagebox.showerror("Math Error", str(err))
            return
        b = simpledialog.askfloat("Logarithm base", "Base b (b > 0, b != 1):", parent=self.root)
        if b is None:
            return
        if b <= 0 or b == 1:
            messagebox.showerror("Math Error", "The base must be positive and not equal to 1.")
            return
        self.show(f"log_{b:g}({x:g})", math.log(x, b))

    def append(self, ch):
        self.expression += ch
        self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("0")

    def evaluate(self):
        expr = "".join(c for c in self.expression if c in "0123456789+-*/.()")
        try:
            value = eval(expr) if expr else 0
            self.show(expr, float(value))
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Division by zero."); self.clear()
        except (SyntaxError, TypeError, ValueError, OverflowError):
            messagebox.showerror("Error", "Invalid expression."); self.clear()

    def toggle_tape(self):
        if self.sidebar.winfo_ismapped():
            self.sidebar.pack_forget()
        else:
            self.sidebar.pack(side="right", fill="y")


if __name__ == "__main__":
    root = tk.Tk()
    ScientificCalculator(root)
    root.mainloop()
