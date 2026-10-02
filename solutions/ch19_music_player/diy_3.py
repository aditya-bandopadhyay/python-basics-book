"""D3: Dropdown to switch the visualizer colour palette."""
import tkinter as tk
from _app import MusicPlayerApp

PALETTES = {
    "Matrix Green":   ["#00ff41", "#00cc33", "#008f11"],
    "Sunset Gold":    ["#ffd166", "#f4a261", "#e76f51"],
    "Cyberpunk Neon": ["#ff00ff", "#00ffff", "#7b2cbf"],
}


class PalettePlayer(MusicPlayerApp):
    def __init__(self, root):
        super().__init__(root)
        self.palette = tk.StringVar(value="Matrix Green")
        row = tk.Frame(self.root, bg="#1e272c")
        row.pack(before=self.lbl_status, pady=2)
        tk.Label(row, text="Visualizer colours:", bg="#1e272c", fg="white").pack(side="left")
        tk.OptionMenu(row, self.palette, *PALETTES, command=self.apply_palette).pack(side="left")
        self.apply_palette()

    def apply_palette(self, *args):
        colours = PALETTES[self.palette.get()]
        for i, bar in enumerate(self.bars):
            self.canvas.itemconfig(bar, fill=colours[i % len(colours)])


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x470")
    PalettePlayer(root)
    root.mainloop()
