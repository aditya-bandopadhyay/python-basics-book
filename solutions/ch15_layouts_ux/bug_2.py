"""Bug 15.2 -- pack() with no options keeps the frame at its natural size.

Fix: fill='both' stretches it to the space it is given, and expand=True gives it
all the extra space when the window grows.
"""
import tkinter as tk
root = tk.Tk()
root.geometry("400x300")
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)
root.mainloop()
