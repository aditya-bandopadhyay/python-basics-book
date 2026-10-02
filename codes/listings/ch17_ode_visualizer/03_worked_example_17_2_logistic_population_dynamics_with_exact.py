# Building an ODE Solver Visualizer -- Worked Example 17.2: Logistic Population Dynamics with Exact Comparison
# (book source: ch17_ode_visualizer.tex, line 297)

import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LogisticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Logistic Population Growth")
        self.root.geometry("620x460")
        
        # Header controls
        pnl = tk.Frame(root, padx=10, pady=10)
        pnl.pack(side="top", fill="x")
        
        tk.Label(pnl, text="Growth Rate r:").pack(side="left")
        self.ent_r = tk.Entry(pnl, width=6)
        self.ent_r.insert(0, "0.5")
        self.ent_r.pack(side="left", padx=5)
        
        tk.Label(pnl, text="Carrying Capacity K:").pack(side="left", padx=(10, 0))
        self.ent_k = tk.Entry(pnl, width=6)
        self.ent_k.insert(0, "100")
        self.ent_k.pack(side="left", padx=5)
        
        btn = tk.Button(pnl, text="Simulate", font=("Arial", 9, "bold"),
                        bg="#27ae60", fg="white", command=self.simulate)
        btn.pack(side="left", padx=15)
        
        # Plot canvas
        self.fig = Figure(figsize=(6, 3.8), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.simulate()

    def simulate(self):
        r = float(self.ent_r.get())
        K = float(self.ent_k.get())
        P0 = 5.0
        t = np.linspace(0, 15, 200)
        
        # Exact analytical solution
        P_exact = (K * P0 * np.exp(r * t)) / (K + P0 * (np.exp(r * t) - 1))
        
        # Numerical Euler solution with coarse step
        dt = 0.5
        t_num = np.arange(0, 15 + dt, dt)
        P_num = np.zeros(len(t_num))
        P_num[0] = P0
        for i in range(len(t_num) - 1):
            dP = r * P_num[i] * (1 - P_num[i] / K)
            P_num[i + 1] = P_num[i] + dP * dt
            
        self.ax.clear()
        self.ax.plot(t, P_exact, "b-", lw=2, label="Exact Analytical")
        self.ax.plot(t_num, P_num, "ro--", label="Numerical Euler (dt=0.5)")
        self.ax.axhline(K, color="green", linestyle=":", label=f"Carrying Capacity K={K}")
        self.ax.set_title("Logistic Growth: Numerical vs. Analytical", fontweight="bold")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Population P(t)")
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = LogisticApp(root)
    root.mainloop()
