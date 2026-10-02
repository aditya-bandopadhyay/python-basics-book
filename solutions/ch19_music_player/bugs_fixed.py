"""Bugs 19.1-19.5, fixed.

Bug 19.1 -- the animation must schedule its next frame:
            self.root.after(60, self.animate_visualizer) at the end.
Bug 19.2 -- time.sleep() blocks Tkinter's event loop (and the recursive call
            never returns). Use after() to schedule the next call instead.
Bug 19.3 -- curselection() is an empty tuple when nothing is selected; check it.
Bug 19.4 -- endswith() is case-sensitive; compare file.lower().
Bug 19.5 -- a Scale passes its value as a STRING; convert with float().
"""
import os
import random
import tkinter as tk


def scan_folder(folder):                                   # Bug 19.4
    return [f for f in os.listdir(folder) if f.lower().endswith(('.mp3', '.wav'))]


class FixedDemo:
    def __init__(self, root):
        self.root = root
        root.title("Chapter 19 bugs fixed")
        self.playlist = ["song_a.mp3", "SONG_B.MP3", "song_c.wav"]
        self.canvas = tk.Canvas(root, width=300, height=100, bg="black")
        self.canvas.pack()
        self.bars = [self.canvas.create_rectangle(10 + 17 * i, 60, 24 + 17 * i, 95, fill="lime")
                     for i in range(16)]
        self.listbox = tk.Listbox(root, height=4)
        for s in self.playlist:
            self.listbox.insert(tk.END, s)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        self.lbl_time = tk.Label(root, text="0 min 0 s")
        self.lbl_time.pack()
        tk.Scale(root, from_=0, to=210, orient="horizontal", command=self.on_scrub).pack(fill="x")
        self.animate_visualizer()

    def animate_visualizer(self):                           # Bugs 19.1 and 19.2
        for i, b_id in enumerate(self.bars):
            h = random.randint(12, 88)
            self.canvas.coords(b_id, 10 + 17 * i, 95 - h, 24 + 17 * i, 95)
        self.root.after(60, self.animate_visualizer)

    def on_select(self, event):                             # Bug 19.3
        sel = self.listbox.curselection()
        if not sel:
            return
        print("Selected:", self.playlist[sel[0]])

    def on_scrub(self, val):                                # Bug 19.5
        seconds = float(val)
        self.lbl_time.config(text=f"{int(seconds // 60)} min {int(seconds % 60)} s")


if __name__ == "__main__":
    root = tk.Tk()
    FixedDemo(root)
    root.mainloop()
