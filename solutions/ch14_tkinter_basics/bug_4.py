"""Bug 14.4 -- geometry strings are 'WIDTHxHEIGHT' in pixels with no units:
'400x300px' gives TclError: bad geometry specifier.
"""
import tkinter as tk
root = tk.Tk()
root.geometry('400x300')
root.mainloop()
