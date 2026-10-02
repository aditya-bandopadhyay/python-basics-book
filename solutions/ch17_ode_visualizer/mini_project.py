"""Mini-Project 17: Lotka-Volterra predator-prey explorer.

  prey:      x' = alpha x - beta x y
  predators: y' = delta x y - gamma y
"""
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from _app import rk4_system

DEFAULTS = {"alpha (prey birth)": 1.0, "beta (predation)": 0.1,
            "delta (predator gain)": 0.075, "gamma (predator death)": 1.5,
            "prey x0": 10.0, "predators y0": 5.0, "t end": 30.0}


class LotkaVolterraApp:
    def __init__(self, root):
        self.root = root
        root.title("Predator-Prey Simulator")
        root.geometry("980x520")
        self.t = self.y = None

        panel = tk.Frame(root, padx=8, pady=8, bg="#ecf0f1")
        panel.pack(side="left", fill="y")
        self.entries = {}
        for name, value in DEFAULTS.items():
            tk.Label(panel, text=name, bg="#ecf0f1").pack(anchor="w")
            e = tk.Entry(panel, width=12)
            e.insert(0, str(value))
            e.pack(anchor="w", pady=(0, 4))
            self.entries[name] = e
        tk.Button(panel, text="Simulate", bg="#27ae60", fg="white", command=self.simulate).pack(fill="x", pady=4)
        tk.Button(panel, text="Reset Parameters", command=self.reset).pack(fill="x", pady=2)
        tk.Button(panel, text="Export Data to CSV", command=self.export_csv).pack(fill="x", pady=2)

        self.fig = Figure(figsize=(8, 4), dpi=100)
        self.ax_t = self.fig.add_subplot(121)
        self.ax_p = self.fig.add_subplot(122)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side="right", fill="both", expand=True)
        self.simulate()

    def read(self):
        return {k: float(e.get()) for k, e in self.entries.items()}

    def simulate(self):
        try:
            p = self.read()
            if p["t end"] <= 0:
                raise ValueError("t end must be positive")
        except ValueError as err:
            messagebox.showerror("Input Error", f"Please enter numbers only.\n{err}")
            return
        a, b, d, g = (p["alpha (prey birth)"], p["beta (predation)"],
                      p["delta (predator gain)"], p["gamma (predator death)"])
        f = lambda t, s: [a * s[0] - b * s[0] * s[1], d * s[0] * s[1] - g * s[1]]
        self.t, self.y = rk4_system(f, [p["prey x0"], p["predators y0"]], 0, p["t end"], 0.01)

        self.ax_t.clear(); self.ax_p.clear()
        self.ax_t.plot(self.t, self.y[:, 0], label="Prey x(t)")
        self.ax_t.plot(self.t, self.y[:, 1], label="Predators y(t)")
        self.ax_t.set_xlabel("Time"); self.ax_t.set_ylabel("Population"); self.ax_t.legend(); self.ax_t.grid(alpha=0.3)
        self.ax_p.plot(self.y[:, 0], self.y[:, 1], color="purple")
        self.ax_p.set_xlabel("Prey x"); self.ax_p.set_ylabel("Predators y"); self.ax_p.set_title("Phase orbit")
        self.ax_p.grid(alpha=0.3)
        self.fig.tight_layout()
        self.canvas.draw()

    def reset(self):
        for name, value in DEFAULTS.items():
            self.entries[name].delete(0, tk.END)
            self.entries[name].insert(0, str(value))
        self.simulate()

    def export_csv(self):
        if self.t is None:
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if not path:
            return
        with open(path, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["t", "prey", "predators"])
            for ti, (xi, yi) in zip(self.t, self.y):
                w.writerow([f"{ti:.4f}", f"{xi:.6f}", f"{yi:.6f}"])
        messagebox.showinfo("Exported", f"Saved {len(self.t)} rows to\n{path}")


if __name__ == "__main__":
    root = tk.Tk()
    LotkaVolterraApp(root)
    root.mainloop()
