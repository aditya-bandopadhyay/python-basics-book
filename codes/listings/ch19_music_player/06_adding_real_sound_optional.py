# Desktop Audio Player and Frequency Visualizer -- Adding Real Sound (Optional)
# (book source: ch19_music_player.tex, line 352)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with ModuleNotFoundError.

import pygame
pygame.mixer.init()                      # once, in __init__

# in load_track():
pygame.mixer.music.load(self.tracks[self.current_idx][1])

# in toggle_play():
if self.is_playing:
    pygame.mixer.music.play(start=self.position)
else:
    pygame.mixer.music.pause()
