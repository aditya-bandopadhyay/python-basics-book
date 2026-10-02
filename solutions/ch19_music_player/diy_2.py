"""D2: Repeat button cycling Off -> Repeat All -> Repeat One."""
import tkinter as tk
from _app import MusicPlayerApp, TRACK_SECONDS

MODES = ["Off", "All", "One"]


class RepeatPlayer(MusicPlayerApp):
    def __init__(self, root):
        self.repeat = "Off"
        super().__init__(root)
        self.btn_repeat = tk.Button(self.root, text="Repeat: Off", command=self.toggle_repeat)
        self.btn_repeat.pack(before=self.lbl_status, pady=2)

    def toggle_repeat(self):
        self.repeat = MODES[(MODES.index(self.repeat) + 1) % 3]
        self.btn_repeat.config(text=f"Repeat: {self.repeat}")
        self.update_status()

    def track_finished(self):
        """Decide what happens at the end of a track."""
        if self.repeat == "One":
            self.load_track()                       # same track again
        elif self.current_idx == len(self.tracks) - 1 and self.repeat == "Off" and not self.is_shuffle:
            self.is_playing = False                 # end of the playlist: stop
            self.btn_play.config(text="Play")
            self.load_track()
        else:
            self.next_track()                       # wraps round for "All"

    def tick(self):
        if self.is_playing and self.position + 0.1 * self.speed >= TRACK_SECONDS:
            self.track_finished()
        super().tick()

    def update_status(self):
        super().update_status()
        if hasattr(self, "repeat"):
            self.lbl_status.config(text=self.lbl_status.cget("text") + f" | Repeat: {self.repeat}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x470")
    RepeatPlayer(root)
    root.mainloop()
