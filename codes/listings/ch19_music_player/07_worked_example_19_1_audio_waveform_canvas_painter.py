# Desktop Audio Player and Frequency Visualizer -- Worked Example 19.1: Audio Waveform Canvas Painter
# (book source: ch19_music_player.tex, line 389)

import tkinter as tk
import numpy as np

class WaveformPainterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Waveform Canvas Painter")
        self.root.geometry("540x360")
        self.root.configure(bg="#1a1a2e")
        
        # Header Controls
        ctrl = tk.Frame(root, bg="#16213e", padx=10, pady=8)
        ctrl.pack(side="top", fill="x")
        
        tk.Label(ctrl, text="Freq 1 (Hz):", fg="white", bg="#16213e", font=("Arial", 9)).pack(side="left")
        self.scale_f1 = tk.Scale(ctrl, from_=1, to=10, orient="horizontal", bg="#16213e", fg="white",
                                 highlightthickness=0, command=self.redraw)
        self.scale_f1.set(2)
        self.scale_f1.pack(side="left", padx=5)
        
        tk.Label(ctrl, text="Freq 2 (Hz):", fg="white", bg="#16213e", font=("Arial", 9)).pack(side="left", padx=(10, 0))
        self.scale_f2 = tk.Scale(ctrl, from_=1, to=20, orient="horizontal", bg="#16213e", fg="white",
                                 highlightthickness=0, command=self.redraw)
        self.scale_f2.set(6)
        self.scale_f2.pack(side="left", padx=5)
        
        # Waveform Canvas
        self.canvas = tk.Canvas(root, bg="#0f3460", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.redraw()

    def redraw(self, event=None):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w <= 1:
            w, h = 520, 260
            
        mid_y = h / 2.0
        # Draw central zero-axis
        self.canvas.create_line(0, mid_y, w, mid_y, fill="#533483", dash=(4, 4))
        
        f1 = self.scale_f1.get()
        f2 = self.scale_f2.get()
        t = np.linspace(0, 1, w)
        # Superposition of two harmonic tones
        signal = 0.6 * np.sin(2 * np.pi * f1 * t) + 0.3 * np.sin(2 * np.pi * f2 * t)
        
        # Convert mathematical coordinates to canvas pixel points
        points = []
        for x_pixel, val in enumerate(signal):
            y_pixel = mid_y - (val * (h * 0.4))
            points.extend([x_pixel, y_pixel])
            
        if len(points) >= 4:
            self.canvas.create_line(points, fill="#00fff5", width=2, smooth=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = WaveformPainterApp(root)
    root.mainloop()
