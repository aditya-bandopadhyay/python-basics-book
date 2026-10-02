# Desktop Audio Player and Frequency Visualizer -- Code 19.2: Playlist queue navigation logic
# (book source: ch19_music_player.tex, line 57)

import random

class PlaylistManager:
    def __init__(self, track_list):
        self.tracks = track_list
        self.current_idx = 0
        self.is_shuffle = False

    def next_track(self):
        if not self.tracks:
            return None
        if self.is_shuffle:
            self.current_idx = random.randint(0, len(self.tracks) - 1)
        else:
            self.current_idx = (self.current_idx + 1) % len(self.tracks)
        return self.tracks[self.current_idx]

    def prev_track(self):
        if not self.tracks:
            return None
        self.current_idx = (self.current_idx - 1) % len(self.tracks)
        return self.tracks[self.current_idx]
