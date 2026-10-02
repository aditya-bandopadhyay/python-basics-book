"""D1: Choose the model from a tk.OptionMenu: decay, logistic, or harmonic motion."""
import tkinter as tk
from tkinter import messagebox
from _app import OdeVisualizerApp, rk4, rk4_system

MODELS = {
    "Exponential decay  y' = -0.3 y": ("single", lambda t, y: -0.3 * y),
    "Logistic growth  y' = 0.4 y (1 - y/50)": ("single", lambda t, y: 0.4 * y * (1 - y / 50)),
    "Harmonic motion  x'' = -x": ("system", lambda t, s: [s[1], -s[0]]),
}


class ModelChooserApp(OdeVisualizerApp):
    def create_inputs(self):
        tk.Label(self.left_panel, text="Model:", bg="lightgrey").pack(pady=(10, 2))
        self.model_name = tk.StringVar(value=list(MODELS)[0])
        menu = tk.OptionMenu(self.left_panel, self.model_name, *MODELS)
        menu.config(width=18)
        menu.pack()
        super().create_inputs()

    def solve_and_plot(self):
        try:
            y0 = float(self.ent_y0.get()); h = float(self.ent_h.get())
            t0 = float(self.ent_tstart.get()); t1 = float(self.ent_tend.get())
            if h <= 0 or t1 <= t0:
                raise ValueError("Need h > 0 and t End > t Start.")
        except ValueError as err:
            messagebox.showerror("Input Error", str(err)); return
        kind, f = MODELS[self.model_name.get()]
        self.ax.clear()
        if kind == "single":
            t, y = rk4(f, y0, t0, t1, h)
            self.ax.plot(t, y, marker="o", ms=3, label="y(t)")
        else:                                   # x(0) = y0, v(0) = 0
            t, y = rk4_system(f, [y0, 0.0], t0, t1, h)
            self.ax.plot(t, y[:, 0], label="x(t)")
            self.ax.plot(t, y[:, 1], "--", label="v(t)")
        self.ax.set_title(self.model_name.get()); self.ax.set_xlabel("t")
        self.ax.grid(True); self.ax.legend()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("760x520")
    ModelChooserApp(root)
    root.mainloop()
