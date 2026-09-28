"""
Code 19.5: Complete Desktop Audio Player & Spectrum Visualizer
Companion script for Chapter 19: Desktop Audio Player and Frequency Visualizer
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import random
import time

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Music Player & Spectrum Visualizer")
        self.root.geometry("520x420")
        self.root.configure(bg="#1e272c")
        
        self.playlist_files = []
        self.current_idx = 0
        self.is_playing = False
        self.speed = 1.0
        
        self.build_ui()
        self.animate_visualizer()

    def build_ui(self):
        # Header Banner
        hdr = tk.Label(self.root, text="DESKTOP AUDIO PLAYER & SPECTRUM ANALYZER", 
                       font=("Arial", 11, "bold"), bg="#101820", fg="#00ffcc", pady=6)
        hdr.pack(fill="x")

        body = tk.Frame(self.root, bg="#1e272c", padx=10, pady=10)
        body.pack(fill="both", expand=True)

        # Left Panel: Folder Playlist
        left_frame = tk.Frame(body, bg="#263238", width=180, padx=8, pady=8, bd=1, relief="ridge")
        left_frame.pack(side="left", fill="y", padx=5)

        tk.Label(left_frame, text="Folder Playlist (MP3/WAV)", font=("Arial", 9, "bold"), 
                 bg="#263238", fg="white").pack(anchor="w", pady=2)
        
        self.listbox = tk.Listbox(left_frame, font=("Arial", 9), bg="#1c2833", fg="#00ffcc", 
                                  selectbackground="#27ae60", bd=1)
        self.listbox.pack(fill="both", expand=True, pady=5)
        
        # Populate sample playlist
        sample_songs = ["01_acoustic_sunset.mp3", "02_quantum_beat.wav", "03_lofi_study.mp3", 
                        "04_synth_wave.mp3", "05_ambient_space.wav"]
        for song in sample_songs:
            self.listbox.insert(tk.END, song)
        self.listbox.select_set(1)

        # Right Panel: Player & Controls
        right_frame = tk.Frame(body, bg="#263238", padx=10, pady=10, bd=1, relief="ridge")
        right_frame.pack(side="right", fill="both", expand=True, padx=5)

        self.lbl_now = tk.Label(right_frame, text="Playing: 02_quantum_beat.wav", 
                                font=("Arial", 10, "bold"), bg="#263238", fg="#f1c40f")
        self.lbl_now.pack(anchor="w")

        # Visualizer Canvas
        self.canvas = tk.Canvas(right_frame, height=100, bg="#101820", 
                                highlightthickness=1, highlightbackground="#00ffcc")
        self.canvas.pack(fill="x", pady=8)

        # Create 16 spectrum bars
        self.bars = []
        bar_x = 10
        colors = ["#27ae60", "#2ef078", "#f1c40f", "#e74c3c", "#3498db", "#9b59b6"]
        for i in range(16):
            col = colors[i % len(colors)]
            b_id = self.canvas.create_rectangle(bar_x, 95 - 30, bar_x + 14, 95, fill=col, outline="")
            self.bars.append(b_id)
            bar_x += 17

        # Track Scrub Bar & Timer
        time_frame = tk.Frame(right_frame, bg="#263238")
        time_frame.pack(fill="x", pady=2)
        tk.Label(time_frame, text="01:45", font=("Arial", 8, "bold"), bg="#263238", fg="#00ffcc").pack(side="left")
        self.scrub = ttk.Scale(time_frame, from_=0, to=100, value=45)
        self.scrub.pack(side="left", fill="x", expand=True, padx=8)
        tk.Label(time_frame, text="03:30", font=("Arial", 8, "bold"), bg="#263238", fg="#00ffcc").pack(side="right")

        # Control Buttons
        btn_frame = tk.Frame(right_frame, bg="#263238")
        btn_frame.pack(pady=8)

        tk.Button(btn_frame, text="[|< Prev]", font=("Arial", 9, "bold"), bg="#37474f", fg="white", width=7).pack(side="left", padx=2)
        tk.Button(btn_frame, text="[|| Pause]", font=("Arial", 9, "bold"), bg="#e67e22", fg="white", width=8).pack(side="left", padx=2)
        tk.Button(btn_frame, text="[Next >|]", font=("Arial", 9, "bold"), bg="#37474f", fg="white", width=7).pack(side="left", padx=2)
        
        self.btn_speed = tk.Button(btn_frame, text="Speed: 1.5x", font=("Arial", 8, "bold"), 
                                   bg="#2980b9", fg="white", command=self.toggle_speed)
        self.btn_speed.pack(side="left", padx=4)

        # Equalizer Sliders
        eq_frame = tk.Frame(right_frame, bg="#263238")
        eq_frame.pack(fill="x", pady=5)
        tk.Label(eq_frame, text="Equalizer (dB):", font=("Arial", 8, "bold"), bg="#263238", fg="#bdc3c7").pack(anchor="w")

        eq_box = tk.Frame(eq_frame, bg="#263238")
        eq_box.pack(fill="x")
        bands = [("31Hz", 3), ("250Hz", -1), ("1kHz", 4), ("4kHz", 2), ("16kHz", 5)]
        for b_name, b_val in bands:
            bf = tk.Frame(eq_box, bg="#263238")
            bf.pack(side="left", expand=True)
            tk.Scale(bf, from_=10, to=-10, length=50, showvalue=0, bg="#263238", fg="white", highlightthickness=0).pack()
            tk.Label(bf, text=b_name, font=("Arial", 7), bg="#263238", fg="#00ffcc").pack()

        # Status Bar
        self.lbl_status = tk.Label(self.root, text="Status: Playing track 2 of 5 | Shuffle: ON | Repeat: OFF", 
                                   bd=1, relief="sunken", anchor="w", font=("Arial", 8, "italic"), bg="#101820", fg="#00ffcc")
        self.lbl_status.pack(side="bottom", fill="x")

    def toggle_speed(self):
        speeds = [1.0, 1.5, 2.0]
        curr_idx = speeds.index(self.speed)
        self.speed = speeds[(curr_idx + 1) % len(speeds)]
        self.btn_speed.config(text=f"Speed: {self.speed}x")

    def animate_visualizer(self):
        for b_id in self.bars:
            h = random.randint(12, 88)
            coords = self.canvas.coords(b_id)
            self.canvas.coords(b_id, coords[0], 95 - h, coords[2], 95)
        self.root.after(60, self.animate_visualizer)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
