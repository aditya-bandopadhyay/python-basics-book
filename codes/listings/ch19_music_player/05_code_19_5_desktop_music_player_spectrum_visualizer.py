# Desktop Audio Player and Frequency Visualizer -- Code 19.5: Desktop Music Player & Spectrum Visualizer
# (book source: ch19_music_player.tex, line 142)

import tkinter as tk
from tkinter import ttk, filedialog
import os
import random

TRACK_SECONDS = 210          # pretend length of every track (3:30)


def format_time(seconds):
    return f"{int(seconds // 60):02d}:{int(seconds % 60):02d}"


class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Music Player & Spectrum Visualizer")
        self.root.geometry("700x440")
        self.root.configure(bg="#1e272c")

        # --- Application state (the "model") ---
        self.tracks = []          # list of (file name, full path)
        self.current_idx = 0
        self.is_playing = False
        self.is_shuffle = False
        self.speed = 1.0
        self.position = 0.0       # seconds into the current track

        self.build_ui()
        self.tick()               # start the timer/animation loop

    # ------------------------------------------------------------------
    def build_ui(self):
        tk.Label(self.root, text="DESKTOP AUDIO PLAYER & SPECTRUM VISUALIZER",
                 font=("Arial", 11, "bold"), bg="#101820", fg="#00ffcc",
                 pady=6).pack(fill="x")

        body = tk.Frame(self.root, bg="#1e272c", padx=10, pady=10)
        body.pack(fill="both", expand=True)

        # Left panel: playlist
        left = tk.Frame(body, bg="#263238", padx=8, pady=8, bd=1, relief="ridge")
        left.pack(side="left", fill="y", padx=5)
        tk.Button(left, text="Open Folder...", command=self.open_folder).pack(fill="x")
        self.listbox = tk.Listbox(left, width=24, bg="#1c2833", fg="#00ffcc",
                                  selectbackground="#27ae60")
        self.listbox.pack(fill="both", expand=True, pady=5)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # Right panel: now playing, visualizer, scrub bar, controls
        right = tk.Frame(body, bg="#263238", padx=10, pady=10, bd=1, relief="ridge")
        right.pack(side="right", fill="both", expand=True, padx=5)

        self.lbl_now = tk.Label(right, text="No folder loaded", font=("Arial", 10, "bold"),
                                bg="#263238", fg="#f1c40f")
        self.lbl_now.pack(anchor="w")

        self.canvas = tk.Canvas(right, height=100, bg="#101820", highlightthickness=0)
        self.canvas.pack(fill="x", pady=8)
        self.bars = []
        for i in range(16):
            x = 10 + 17 * i
            self.bars.append(self.canvas.create_rectangle(
                x, 90, x + 14, 95, fill="#27ae60", outline=""))

        time_row = tk.Frame(right, bg="#263238")
        time_row.pack(fill="x")
        self.lbl_elapsed = tk.Label(time_row, text="00:00", bg="#263238", fg="#00ffcc")
        self.lbl_elapsed.pack(side="left")
        self.scrub = ttk.Scale(time_row, from_=0, to=TRACK_SECONDS, command=self.on_scrub)
        self.scrub.pack(side="left", fill="x", expand=True, padx=8)
        tk.Label(time_row, text=format_time(TRACK_SECONDS), bg="#263238",
                 fg="#00ffcc").pack(side="right")

        buttons = tk.Frame(right, bg="#263238")
        buttons.pack(pady=8)
        tk.Button(buttons, text="|< Prev", width=7, command=self.prev_track).pack(side="left", padx=2)
        self.btn_play = tk.Button(buttons, text="Play", width=7, command=self.toggle_play)
        self.btn_play.pack(side="left", padx=2)
        tk.Button(buttons, text="Next >|", width=7, command=self.next_track).pack(side="left", padx=2)
        self.btn_shuffle = tk.Button(buttons, text="Shuffle: OFF", command=self.toggle_shuffle)
        self.btn_shuffle.pack(side="left", padx=2)
        self.btn_speed = tk.Button(buttons, text="Speed: 1.0x", command=self.toggle_speed)
        self.btn_speed.pack(side="left", padx=2)

        # Equalizer sliders (interface only: see the text)
        eq = tk.Frame(right, bg="#263238")
        eq.pack(fill="x")
        for band in ["31Hz", "250Hz", "1kHz", "4kHz", "16kHz"]:
            box = tk.Frame(eq, bg="#263238")
            box.pack(side="left", expand=True)
            tk.Scale(box, from_=10, to=-10, length=50, showvalue=0,
                     bg="#263238", highlightthickness=0).pack()
            tk.Label(box, text=band, font=("Arial", 7), bg="#263238", fg="#00ffcc").pack()

        self.lbl_status = tk.Label(self.root, text="Status: open a folder to begin",
                                   anchor="w", relief="sunken", bg="#101820", fg="#00ffcc")
        self.lbl_status.pack(side="bottom", fill="x")

    # ------------------------------------------------------------------
    def open_folder(self):
        folder = filedialog.askdirectory(title="Choose a music folder")
        if not folder:                       # user pressed Cancel
            return
        valid = ('.mp3', '.wav', '.ogg', '.flac')
        self.tracks = [(f, os.path.join(folder, f))
                       for f in sorted(os.listdir(folder))
                       if f.lower().endswith(valid)]
        self.listbox.delete(0, tk.END)
        for name, _ in self.tracks:
            self.listbox.insert(tk.END, name)
        self.current_idx = 0
        self.load_track()

    def load_track(self):
        self.position = 0.0
        self.scrub.set(0)
        if not self.tracks:
            self.lbl_now.config(text="No audio files in that folder")
        else:
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(self.current_idx)
            self.lbl_now.config(text=f"Track: {self.tracks[self.current_idx][0]}")
        self.update_status()

    def on_select(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        self.current_idx = sel[0]
        self.load_track()

    def next_track(self):
        if not self.tracks:
            return
        if self.is_shuffle:
            self.current_idx = random.randint(0, len(self.tracks) - 1)
        else:
            self.current_idx = (self.current_idx + 1) % len(self.tracks)
        self.load_track()

    def prev_track(self):
        if not self.tracks:
            return
        self.current_idx = (self.current_idx - 1) % len(self.tracks)
        self.load_track()

    def toggle_play(self):
        if not self.tracks:
            return
        self.is_playing = not self.is_playing
        self.btn_play.config(text="Pause" if self.is_playing else "Play")
        self.update_status()

    def toggle_shuffle(self):
        self.is_shuffle = not self.is_shuffle
        self.btn_shuffle.config(text=f"Shuffle: {'ON' if self.is_shuffle else 'OFF'}")
        self.update_status()

    def toggle_speed(self):
        speeds = [1.0, 1.5, 2.0]
        self.speed = speeds[(speeds.index(self.speed) + 1) % len(speeds)]
        self.btn_speed.config(text=f"Speed: {self.speed}x")

    def on_scrub(self, value):
        self.position = float(value)         # Scale passes a string
        self.lbl_elapsed.config(text=format_time(self.position))

    def update_status(self):
        if not self.tracks:
            text = "Status: no tracks loaded"
        else:
            state = "Playing" if self.is_playing else "Paused"
            shuffle = "ON" if self.is_shuffle else "OFF"
            text = (f"Status: {state} track {self.current_idx + 1} of "
                    f"{len(self.tracks)} | Shuffle: {shuffle}")
        self.lbl_status.config(text=text)

    # ------------------------------------------------------------------
    def tick(self):
        """Runs every 100 ms: advance the clock and animate the bars."""
        if self.is_playing:
            self.position += 0.1 * self.speed
            if self.position >= TRACK_SECONDS:
                self.next_track()
            self.scrub.set(self.position)
            for bar in self.bars:
                h = random.randint(12, 88)   # simulated spectrum
                x1, _, x2, _ = self.canvas.coords(bar)
                self.canvas.coords(bar, x1, 95 - h, x2, 95)
        self.root.after(100, self.tick)


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
