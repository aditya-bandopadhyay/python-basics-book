# Tkinter Basics -- Code 14.1: A minimal Tkinter window
# (book source: ch14_tkinter_basics.tex, line 136)

import tkinter as tk

root = tk.Tk()
root.title('My First App')
root.geometry('320x180')

label = tk.Label(root, text='Hello, Tkinter!', font=('Arial', 14, 'bold'))
label.pack(pady=40)

root.mainloop()
