"""D1: Volume slider plus a Mute button that remembers the previous level."""
import tkinter as tk
from _app import MusicPlayerApp


class VolumePlayer(MusicPlayerApp):
    def __init__(self, root):
        self.volume = tk.IntVar(value=70)
        self.saved_volume = 70
        super().__init__(root)
        row = tk.Frame(self.root, bg="#1e272c")
        row.pack(fill="x", before=self.lbl_status, padx=10)
        tk.Label(row, text="Volume", bg="#1e272c", fg="white").pack(side="left")
        tk.Scale(row, from_=0, to=100, orient="horizontal", variable=self.volume, length=200,
                 command=lambda v: self.update_status()).pack(side="left", padx=6)
        self.btn_mute = tk.Button(row, text="Mute", width=8, command=self.toggle_mute)
        self.btn_mute.pack(side="left")
        self.update_status()

    def toggle_mute(self):
        if self.volume.get() > 0:
            self.saved_volume = self.volume.get()
            self.volume.set(0)
            self.btn_mute.config(text="Unmute")
        else:
            self.volume.set(self.saved_volume or 70)
            self.btn_mute.config(text="Mute")
        self.update_status()

    def update_status(self):
        super().update_status()
        if hasattr(self, "volume"):
            self.lbl_status.config(text=self.lbl_status.cget("text") + f" | Volume: {self.volume.get()}%")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x480")
    VolumePlayer(root)
    root.mainloop()
