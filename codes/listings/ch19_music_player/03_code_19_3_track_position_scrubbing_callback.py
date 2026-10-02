# Desktop Audio Player and Frequency Visualizer -- Code 19.3: Track position scrubbing callback
# (book source: ch19_music_player.tex, line 90)

def on_scrub(self, value):
    self.position = float(value)          # Scale passes a string
    self.lbl_elapsed.config(text=format_time(self.position))
