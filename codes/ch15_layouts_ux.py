"""
ch14_layouts_ux.py

Demonstrates simple Tkinter layout (frames and packing) as an example of
layout concepts from the chapter.
"""

try:
    import tkinter as tk
except Exception:
    tk = None


def layout_example_window():
    if tk is None:
        print("Tkinter not available; layout example cannot run here.")
        return
    root = tk.Tk()
    root.title("Layout example")
    top_frame = tk.Frame(root, bg="lightgrey")
    top_frame.pack(fill=tk.BOTH, expand=True)
    left_label = tk.Label(
        top_frame, text="Left pane", width=20, bg="white"
    )
    left_label.pack(side=tk.LEFT, padx=5, pady=5)
    right_label = tk.Label(
        top_frame, text="Right pane", width=40, bg="white"
    )
    right_label.pack(side=tk.RIGHT, padx=5, pady=5)
    root.mainloop()


if __name__ == "__main__":
    layout_example_window()
