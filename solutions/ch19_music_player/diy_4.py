"""D4: Peak-hold markers: a white line above each bar that falls slowly."""
import tkinter as tk
from _app import MusicPlayerApp

FALL_PER_TICK = 1.5          # pixels per 100 ms tick


class PeakHoldPlayer(MusicPlayerApp):
    def __init__(self, root):
        self.peaks = []
        super().__init__(root)
        for bar in self.bars:
            x1, y1, x2, y2 = self.canvas.coords(bar)
            marker = self.canvas.create_line(x1, y1 - 2, x2, y1 - 2, fill="white", width=2)
            self.peaks.append([marker, y1 - 2])       # [canvas id, current top y]

    def tick(self):
        super().tick()                                # moves the bars (while playing)
        for bar, peak in zip(self.bars, self.peaks):
            bar_top = self.canvas.coords(bar)[1]
            marker, y = peak
            y = min(y + FALL_PER_TICK, 95)            # fall slowly (larger y is lower)
            if bar_top - 2 < y:                       # a taller bar pushes the marker up
                y = bar_top - 2
            peak[1] = y
            x1, _, x2, _ = self.canvas.coords(marker)
            self.canvas.coords(marker, x1, y, x2, y)


if __name__ == "__main__":
    root = tk.Tk()
    PeakHoldPlayer(root)
    root.mainloop()
