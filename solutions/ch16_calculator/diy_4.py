"""D4: A 1/x (reciprocal) button with a check for zero."""
import tkinter as tk
from tkinter import messagebox
from _app import LogCalculatorApp


class ReciprocalCalculator(LogCalculatorApp):
    def create_buttons(self):
        super().create_buttons()
        self.btn_frame.rowconfigure(6, weight=1)
        tk.Button(self.btn_frame, text="1/x", font=("Arial", 11, "bold"),
                  command=self.calc_reciprocal).grid(row=6, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

    def calc_reciprocal(self):
        try:
            val = self.get_current_val()
            if val == 0:
                messagebox.showerror("Math Error", "Cannot take 1/x of zero.")
                return
            res = 1 / val
            self.expression = str(res)
            self.display_var.set(f"{res:.6g}")
        except ValueError as err:
            messagebox.showerror("Math Error", str(err))


if __name__ == "__main__":
    root = tk.Tk()
    ReciprocalCalculator(root)
    root.mainloop()
