"""D4: Overlay the exact solution y0 * exp(-0.3 t) on the RK4 curve."""
import tkinter as tk
import numpy as np
from _app import OdeVisualizerApp


class ExactOverlayApp(OdeVisualizerApp):
    def solve_and_plot(self):
        super().solve_and_plot()            # draws the RK4 curve (or shows an error)
        try:
            y0 = float(self.ent_y0.get())
            t0, t1 = float(self.ent_tstart.get()), float(self.ent_tend.get())
        except ValueError:
            return
        t = np.linspace(t0, t1, 300)
        self.ax.plot(t, y0 * np.exp(-0.3 * (t - t0)), "k--", label="Exact")
        self.ax.legend()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    ExactOverlayApp(root)
    root.mainloop()
