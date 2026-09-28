"""
ch16_ode_visualizer.py

An interactive scientific GUI that solves ODEs using the RK4 method
and plots the dynamic trajectory in an embedded Matplotlib canvas.
"""

import tkinter as tk
from tkinter import messagebox
import numpy as np

# Matplotlib embedding imports
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# RK4 Solver Function from Chapter 10
def rk4(f, y0, t_start, t_end, h):
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


class OdeVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ODE Solver Visualizer")
        self.root.geometry("600x500")

        # Define default system model: dy/dt = -0.3 * y (exponential decay)
        self.model = lambda t, y: -0.3 * y

        # Left panel: parameters input
        self.left_panel = tk.Frame(root, width=200, bg="lightgrey")
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        self.create_inputs()

        # Right panel: matplotlib canvas
        self.right_panel = tk.Frame(root)
        self.right_panel.pack(
            side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5
        )

        self.setup_plot()

    def create_inputs(self):
        # Initial Condition (y0)
        tk.Label(
            self.left_panel, text="y0 (Initial):", bg="lightgrey"
        ).pack(pady=(10, 2))
        self.ent_y0 = tk.Entry(self.left_panel, width=15)
        self.ent_y0.insert(0, "10.0")
        self.ent_y0.pack()

        # Step Size (h)
        tk.Label(self.left_panel, text="Step Size (h):", bg="lightgrey").pack(
            pady=2
        )
        self.ent_h = tk.Entry(self.left_panel, width=15)
        self.ent_h.insert(0, "0.5")
        self.ent_h.pack()

        # t Start
        tk.Label(self.left_panel, text="t Start:", bg="lightgrey").pack(
            pady=2
        )
        self.ent_tstart = tk.Entry(self.left_panel, width=15)
        self.ent_tstart.insert(0, "0.0")
        self.ent_tstart.pack()

        # t End
        tk.Label(self.left_panel, text="t End:", bg="lightgrey").pack(pady=2)
        self.ent_tend = tk.Entry(self.left_panel, width=15)
        self.ent_tend.insert(0, "15.0")
        self.ent_tend.pack()

        # Solve Button
        self.btn_solve = tk.Button(
            self.left_panel, text="Solve & Plot", command=self.solve_and_plot
        )
        self.btn_solve.pack(pady=20)

    def setup_plot(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("System Trajectory y(t)")
        self.ax.set_xlabel("t")
        self.ax.set_ylabel("y")
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_panel)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def solve_and_plot(self):
        try:
            # Extract inputs and validate
            y0 = float(self.ent_y0.get())
            h = float(self.ent_h.get())
            t_start = float(self.ent_tstart.get())
            t_end = float(self.ent_tend.get())

            if h <= 0:
                raise ValueError("Step size h must be strictly positive.")
            if t_end <= t_start:
                raise ValueError("t End must be greater than t Start.")

            # Run solver
            t, y = rk4(self.model, y0, t_start, t_end, h)

            # Update Matplotlib plot
            self.ax.clear()
            self.ax.plot(
                t, y, marker="o", linestyle="-", label=f"RK4 (h={h})"
            )
            self.ax.set_title("System Trajectory y(t)")
            self.ax.set_xlabel("t")
            self.ax.set_ylabel("y")
            self.ax.grid(True)
            self.ax.legend()
            self.canvas.draw()

        except ValueError as err:
            messagebox.showerror("Input Error", f"Invalid parameters:\n{err}")


if __name__ == "__main__":
    root = tk.Tk()
    app = OdeVisualizerApp(root)
    root.mainloop()
