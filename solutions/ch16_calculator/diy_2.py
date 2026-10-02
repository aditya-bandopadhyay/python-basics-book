"""D2: Keep the last 5 results and show them from Edit > History."""
import tkinter as tk
from tkinter import messagebox
from _app import LogCalculatorApp


class HistoryCalculator(LogCalculatorApp):
    def __init__(self, root):
        self.history = []
        super().__init__(root)
        # Add "History" to the existing Edit menu (index 1 of the menu bar)
        menubar = root.nametowidget(root["menu"])
        edit_menu = menubar.nametowidget(menubar.entrycget(1, "menu"))
        edit_menu.add_command(label="History", command=self.show_history)

    def remember(self):
        value = self.display_var.get()
        self.history = (self.history + [value])[-5:]      # keep only the last 5

    # Record a result after every operation that produces one
    def evaluate(self):
        super().evaluate();      self.remember()
    def calc_log10(self):
        super().calc_log10();    self.remember()
    def calc_ln(self):
        super().calc_ln();       self.remember()
    def calc_antilog10(self):
        super().calc_antilog10(); self.remember()
    def calc_antilog_e(self):
        super().calc_antilog_e(); self.remember()
    def calc_sqrt(self):
        super().calc_sqrt();     self.remember()

    def show_history(self):
        text = "\n".join(self.history) if self.history else "No calculations yet."
        messagebox.showinfo("Last 5 results", text)


if __name__ == "__main__":
    root = tk.Tk()
    HistoryCalculator(root)
    root.mainloop()
