"""Bugs 17.1-17.5, fixed, as a working variant of the Chapter 17 app.

Bug 17.1 -- after changing the axes you must call self.canvas.draw(), otherwise
            the window keeps showing the old picture.
Bug 17.2 -- without self.ax.clear() every click adds another line on top.
Bug 17.3 -- float("abc") raises ValueError, not TypeError, so the except branch
            never ran; catch ValueError.
Bug 17.4 -- k2 and k3 must be evaluated at the MIDDLE of the step:
            f(t + h/2, y + h/2 * k1) and f(t + h/2, y + h/2 * k2).
Bug 17.5 -- the canvas widget was never placed: add
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True).
"""
import tkinter as tk
from tkinter import messagebox
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def rk4_fixed(f, y0, t_start, t_end, h):                      # Bug 17.4
    t = np.arange(t_start, t_end + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(len(t) - 1):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(t[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(t[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, y


class FixedApp:
    def __init__(self, root):
        self.root = root
        root.title("Chapter 17 bugs fixed")
        self.model = lambda t, y: -0.3 * y
        panel = tk.Frame(root); panel.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        tk.Label(panel, text="Step size h:").pack()
        self.ent_h = tk.Entry(panel, width=10); self.ent_h.insert(0, "0.5"); self.ent_h.pack()
        tk.Button(panel, text="Solve & Plot", command=self.solve_and_plot).pack(pady=10)
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)   # Bug 17.5

    def solve_and_plot(self):
        try:
            h = float(self.ent_h.get())
            if h <= 0:
                raise ValueError("h must be positive")
        except ValueError as err:                                     # Bug 17.3
            messagebox.showerror("Input Error", str(err))
            return
        t, y = rk4_fixed(self.model, 10.0, 0.0, 15.0, h)
        self.ax.clear()                                               # Bug 17.2
        self.ax.plot(t, y, marker="o", linestyle="-", label=f"RK4 (h={h})")
        self.ax.legend()
        self.canvas.draw()                                            # Bug 17.1


if __name__ == "__main__":
    root = tk.Tk()
    FixedApp(root)
    root.mainloop()
