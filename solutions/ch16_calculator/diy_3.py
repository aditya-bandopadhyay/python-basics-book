"""D3: Keyboard support: digits/operators type into the display, Enter evaluates."""
import tkinter as tk
from _app import LogCalculatorApp


class KeyboardCalculator(LogCalculatorApp):
    def __init__(self, root):
        super().__init__(root)
        root.bind("<Return>", lambda event: self.evaluate())
        root.bind("<KP_Enter>", lambda event: self.evaluate())
        root.bind("<BackSpace>", self.backspace)
        root.bind("<Escape>", lambda event: self.clear_screen())
        root.bind("<Key>", self.on_key)

    def on_key(self, event):
        if event.char and event.char in "0123456789+-*/().":
            self.append_char(event.char)

    def backspace(self, event=None):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression or "0")


if __name__ == "__main__":
    root = tk.Tk()
    KeyboardCalculator(root)
    root.mainloop()
