"""Mini-Project 19: Audio synthesizer and waveform studio.

Choose a waveform and a frequency, shape the note with ADSR sliders, see the
waveform and its spectrum update live, and save the note as a .wav file using
only NumPy and Python's built-in wave module.
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import wave
import numpy as np

RATE = 44100            # samples per second
DURATION = 1.5          # seconds per note


def oscillator(kind, freq, t):
    phase = (freq * t) % 1.0                       # position within each cycle, 0..1
    if kind == "Sine":
        return np.sin(2 * np.pi * freq * t)
    if kind == "Square":
        return np.where(phase < 0.5, 1.0, -1.0)
    if kind == "Sawtooth":
        return 2 * phase - 1
    return 4 * np.abs(phase - 0.5) - 1             # Triangle


def adsr(n, attack, decay, sustain, release):
    """Envelope with attack/decay/release in seconds and sustain level 0..1."""
    a, d, r = int(attack * RATE), int(decay * RATE), int(release * RATE)
    s = max(n - a - d - r, 0)
    env = np.concatenate([np.linspace(0, 1, a, endpoint=False),
                          np.linspace(1, sustain, d, endpoint=False),
                          np.full(s, sustain),
                          np.linspace(sustain, 0, r)])
    return np.pad(env, (0, max(n - len(env), 0)))[:n]


class SynthStudio:
    def __init__(self, root):
        self.root = root
        root.title("Waveform Studio")
        root.geometry("780x560")
        root.configure(bg="#1a1a2e")
        self.offset = 0

        ctrl = tk.Frame(root, bg="#16213e", padx=8, pady=6)
        ctrl.pack(fill="x")
        self.kind = tk.StringVar(value="Sine")
        for k in ["Sine", "Square", "Sawtooth", "Triangle"]:
            tk.Radiobutton(ctrl, text=k, value=k, variable=self.kind, command=self.refresh,
                           bg="#16213e", fg="white", selectcolor="#0f3460").pack(side="left")
        self.freq = self.slider(ctrl, "Freq (Hz)", 110, 880, 440, 1)

        env = tk.Frame(root, bg="#16213e", padx=8, pady=4)
        env.pack(fill="x")
        self.attack = self.slider(env, "Attack (s)", 0.0, 0.5, 0.05, 0.01)
        self.decay = self.slider(env, "Decay (s)", 0.0, 0.5, 0.15, 0.01)
        self.sustain = self.slider(env, "Sustain", 0.0, 1.0, 0.6, 0.05)
        self.release = self.slider(env, "Release (s)", 0.0, 1.0, 0.4, 0.01)

        self.wave_canvas = tk.Canvas(root, height=180, bg="#0f3460", highlightthickness=0)
        self.wave_canvas.pack(fill="x", padx=10, pady=(10, 4))
        self.spec_canvas = tk.Canvas(root, height=160, bg="#101820", highlightthickness=0)
        self.spec_canvas.pack(fill="x", padx=10, pady=4)

        tk.Button(root, text="Save note as .wav", command=self.save_wav).pack(pady=6)
        self.refresh()
        self.animate()

    def slider(self, parent, label, lo, hi, value, step):
        var = tk.DoubleVar(value=value)
        box = tk.Frame(parent, bg=parent["bg"])
        box.pack(side="left", padx=6)
        tk.Label(box, text=label, bg=parent["bg"], fg="white").pack()
        tk.Scale(box, from_=lo, to=hi, resolution=step, orient="horizontal", variable=var,
                 length=120, command=lambda v: self.refresh(), bg=parent["bg"], fg="white",
                 highlightthickness=0).pack()
        return var

    def make_note(self):
        t = np.arange(int(RATE * DURATION)) / RATE
        tone = oscillator(self.kind.get(), self.freq.get(), t)
        return 0.8 * tone * adsr(len(t), self.attack.get(), self.decay.get(),
                                 self.sustain.get(), self.release.get())

    def refresh(self):
        self.note = self.make_note()
        self.draw_spectrum()

    def draw_wave(self):
        c = self.wave_canvas
        c.delete("all")
        w, h = max(c.winfo_width(), 760), max(c.winfo_height(), 180)
        window = self.note[self.offset:self.offset + RATE // 50]          # 20 ms of sound
        if len(window) < 2:
            return
        xs = np.linspace(0, w, len(window))
        ys = h / 2 - window * h * 0.45
        c.create_line(0, h / 2, w, h / 2, fill="#533483", dash=(4, 4))
        c.create_line(*np.column_stack([xs, ys]).ravel(), fill="#00fff5", width=2)
        c.create_text(8, 8, anchor="nw", fill="white",
                      text=f"{self.kind.get()} {self.freq.get():.0f} Hz  t = {self.offset / RATE:.2f} s")

    def draw_spectrum(self):
        c = self.spec_canvas
        c.delete("all")
        w, h = max(c.winfo_width(), 760), max(c.winfo_height(), 160)
        spectrum = np.abs(np.fft.rfft(self.note))
        freqs = np.fft.rfftfreq(len(self.note), 1 / RATE)
        edges = np.linspace(0, 5000, 41)                                  # 40 bands up to 5 kHz
        levels = np.array([spectrum[(freqs >= a) & (freqs < b)].max(initial=0) for a, b in zip(edges[:-1], edges[1:])])
        levels = levels / levels.max() if levels.max() > 0 else levels
        bw = w / len(levels)
        for i, lev in enumerate(levels):
            c.create_rectangle(i * bw + 2, h - 15 - lev * (h - 30), (i + 1) * bw - 2, h - 15, fill="#27ae60", outline="")
        c.create_text(4, h - 2, anchor="sw", fill="white", text="0 Hz")
        c.create_text(w - 4, h - 2, anchor="se", fill="white", text="5 kHz")

    def animate(self):
        self.offset = (self.offset + RATE // 100) % (len(self.note) - RATE // 50)
        self.draw_wave()
        self.root.after(50, self.animate)

    def save_wav(self):
        path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV audio", "*.wav")])
        if not path:
            return
        samples = (self.note * 32767).astype(np.int16)
        with wave.open(path, "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)            # 16-bit samples
            f.setframerate(RATE)
            f.writeframes(samples.tobytes())
        messagebox.showinfo("Saved", f"Saved {DURATION} s note to\n{path}")


if __name__ == "__main__":
    root = tk.Tk()
    SynthStudio(root)
    root.mainloop()
