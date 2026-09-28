"""
ch15_calculator.py

A simple GUI Calculator implementing grid layouts, button actions,
and a main menu bar (File, Edit, Help).
"""

import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")

        # Calculator state
        self.expression = ""

        # Create Menu Bar
        self.create_menu()

        # Display screen
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 20),
            bd=5,
            insertwidth=4,
            width=14,
            borderwidth=2,
            justify="right",
            state="readonly",
        )
        self.display.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        # Button Layout Frame
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Configure row/column weights for responsiveness
        for i in range(4):
            self.btn_frame.columnconfigure(i, weight=1)
        for i in range(5):
            self.btn_frame.rowconfigure(i, weight=1)

        self.create_buttons()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Clear", command=self.clear_screen)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def create_buttons(self):
        buttons = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("/", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("*", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("-", 2, 3),
            ("0", 3, 0),
            (".", 3, 1),
            ("C", 3, 2),
            ("+", 3, 3),
            ("=", 4, 0),
        ]

        for text, row, col in buttons:
            if text == "=":
                btn = tk.Button(
                    self.btn_frame,
                    text=text,
                    font=("Arial", 14),
                    command=self.evaluate,
                )
                btn.grid(
                    row=row,
                    column=col,
                    columnspan=4,
                    sticky="nsew",
                    padx=2,
                    pady=2,
                )
            else:
                action = (
                    self.clear_screen
                    if text == "C"
                    else lambda t=text: self.append_char(t)
                )
                btn = tk.Button(
                    self.btn_frame,
                    text=text,
                    font=("Arial", 14),
                    command=action,
                )
                btn.grid(
                    row=row, column=col, sticky="nsew", padx=2, pady=2
                )

    def append_char(self, char):
        self.expression += str(char)
        self.display_var.set(self.expression)

    def clear_screen(self):
        self.expression = ""
        self.display_var.set("0")

    def evaluate(self):
        try:
            # Simple safe evaluation containing basic chars
            safe_expr = "".join(
                c
                for c in self.expression
                if c in "0123456789+-*/."
            )
            result = str(eval(safe_expr))
            self.expression = result
            self.display_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear_screen()

    def show_about(self):
        messagebox.showinfo(
            "About Calculator",
            "A standard grid-layout calculator\nillustrating Tkinter grids.",
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
