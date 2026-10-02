# Desktop Audio Player and Frequency Visualizer -- Worked Example 19.2: Playlist Duration Calculator with Metadata
# (book source: ch19_music_player.tex, line 468)

import tkinter as tk

def format_duration(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

class PlaylistSummaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Album Playlist Metadata Summary")
        self.root.geometry("420x280")
        self.root.configure(padx=15, pady=15)
        
        # Album track database: (Title, Duration in Seconds)
        self.album = [
            ("Track 1: Morning Light", 214),
            ("Track 2: Quantum Cascade", 185),
            ("Track 3: Midnight Drift", 342),
            ("Track 4: Solar Wind", 198),
            ("Track 5: Velvet Horizon", 276)
        ]
        
        tk.Label(root, text="ALBUM METADATA & DURATION AUDIT", font=("Arial", 11, "bold"), fg="#2c3e50").pack(pady=(0, 10))
        
        # Track Listbox
        self.lb = tk.Listbox(root, font=("Courier", 9), height=6)
        for title, dur in self.album:
            self.lb.insert(tk.END, f"{title:<28} [{format_duration(dur)}]")
        self.lb.pack(fill="x", pady=5)
        
        # Calculate Album Statistics
        total_sec = sum(dur for _, dur in self.album)
        longest = max(self.album, key=lambda item: item[1])
        shortest = min(self.album, key=lambda item: item[1])
        
        summary_text = (
            f"Total Tracks: {len(self.album)}\n"
            f"Total Album Playtime: {format_duration(total_sec)} ({total_sec} sec)\n"
            f"Longest Track: {longest[0]} ({format_duration(longest[1])})\n"
            f"Shortest Track: {shortest[0]} ({format_duration(shortest[1])})"
        )
        
        lbl_info = tk.Label(root, text=summary_text, font=("Arial", 10), justify="left",
                            bg="#ecf0f1", padx=10, pady=8, relief="groove", bd=1)
        lbl_info.pack(fill="both", expand=True, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlaylistSummaryApp(root)
    root.mainloop()
