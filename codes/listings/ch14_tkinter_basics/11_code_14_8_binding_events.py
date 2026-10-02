# Tkinter Basics -- Code 14.8: Binding events
# (book source: ch14_tkinter_basics.tex, line 452)
# NOTE: A fragment from the book; a minimal window has been added around it so it runs.

import tkinter as tk
root = tk.Tk()   # added so the fragment can run

def on_key_press(event):
    print(f'Key pressed: {event.char}')

root.bind('<Key>', on_key_press)

def on_mouse_click(event):
    print(f'Mouse clicked at ({event.x}, {event.y})')

root.bind('<Button-1>', on_mouse_click)

root.mainloop()  # added so the fragment can run
