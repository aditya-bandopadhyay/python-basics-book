# Desktop Audio Player and Frequency Visualizer -- Code 19.4: Canvas spectrum visualizer animation loop
# (book source: ch19_music_player.tex, line 120)

import random

def animate_spectrum(canvas, bar_ids):
    for bar_id in bar_ids:
        new_height = random.randint(10, 85)
        x1, _, x2, _ = canvas.coords(bar_id)
        canvas.coords(bar_id, x1, 95 - new_height, x2, 95)   # move the top edge
    # Run again after 50 ms (20 frames per second)
    canvas.after(50, lambda: animate_spectrum(canvas, bar_ids))
