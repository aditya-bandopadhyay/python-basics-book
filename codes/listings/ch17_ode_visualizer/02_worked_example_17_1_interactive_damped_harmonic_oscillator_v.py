# Building an ODE Solver Visualizer -- Worked Example 17.1: Interactive Damped Harmonic Oscillator Visualizer
# (book source: ch17_ode_visualizer.tex, line 194)

import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def solve_oscillator(zeta, omega_n=2.0, t_max=10.0, dt=0.02):
    t = np.arange(0, t_max, dt)
    # State vector: Y = [position x, velocity v]
    # dY/dt = [v, -2*zeta*omega_n*v - omega_n^2*x]
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0], v[0] = 1.0, 0.0  # Initial displacement of 1.0 unit
    
    for i in range(len(t) - 1):
        # Semi-implicit Euler: update v first, then use the NEW v for x.
        a = -2.0 * zeta * omega_n * v[i] - (omega_n ** 2) * x[i]
        v[i + 1] = v[i] + a * dt
        x[i + 1] = x[i] + v[i + 1] * dt
    return t, x

class OscillatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Damped Oscillator Visualizer")
        self.root.geometry("640x480")
        
        # Control Panel
        ctrl = tk.Frame(root, bg="#2c3e50", padx=10, pady=10)
        ctrl.pack(side="top", fill="x")
        
        tk.Label(ctrl, text="Damping Ratio (zeta):", font=("Arial", 10, "bold"),
                 fg="white", bg="#2c3e50").pack(side="left", padx=5)
                 
        self.slider_zeta = tk.Scale(ctrl, from_=0.0, to=2.0, resolution=0.05,
                                    orient="horizontal", length=250, command=self.update_plot)
        self.slider_zeta.set(0.15)
        self.slider_zeta.pack(side="left", padx=10)
        
        self.lbl_regime = tk.Label(ctrl, text="Regime: Underdamped", font=("Arial", 10, "bold"),
                                   fg="#f39c12", bg="#2c3e50")
        self.lbl_regime.pack(side="left", padx=10)
        
        # Matplotlib Canvas
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        self.update_plot(self.slider_zeta.get())

    def update_plot(self, val):
        zeta = float(val)
        if zeta < 1.0:
            regime = "Underdamped (Oscillatory)"
            color = "#e74c3c"
        elif np.isclose(zeta, 1.0, atol=0.05):
            regime = "Critically Damped"
            color = "#27ae60"
        else:
            regime = "Overdamped (No Oscillation)"
            color = "#2980b9"
        self.lbl_regime.config(text=f"Regime: {regime}", fg=color)
        
        t, x = solve_oscillator(zeta)
        self.ax.clear()
        self.ax.plot(t, x, color=color, lw=2, label=f"zeta = {zeta:.2f}")
        self.ax.axhline(0, color="gray", linestyle="--", alpha=0.6)
        self.ax.set_title("Oscillator Displacement x(t)", fontsize=11, fontweight="bold")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Displacement x")
        self.ax.set_ylim(-1.2, 1.2)
        self.ax.grid(True, alpha=0.3)
        self.ax.legend(loc="upper right")
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = OscillatorApp(root)
    root.mainloop()
