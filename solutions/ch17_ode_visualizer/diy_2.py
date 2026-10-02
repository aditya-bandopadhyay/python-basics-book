"""D2: An Entry for the rate constant k in y' = -k y."""
import tkinter as tk
from tkinter import messagebox
from _app import OdeVisualizerApp


class RateConstantApp(OdeVisualizerApp):
    def create_inputs(self):
        super().create_inputs()
        tk.Label(self.left_panel, text="Rate constant k:", bg="lightgrey").pack(pady=2)
        self.ent_k = tk.Entry(self.left_panel, width=15)
        self.ent_k.insert(0, "0.3")
        self.ent_k.pack()

    def solve_and_plot(self):
        try:
            k = float(self.ent_k.get())
        except ValueError:
            messagebox.showerror("Input Error", "k must be a number."); return
        self.model = lambda t, y: -k * y          # rebuild the model with the new k
        super().solve_and_plot()


if __name__ == "__main__":
    root = tk.Tk()
    RateConstantApp(root)
    root.mainloop()
