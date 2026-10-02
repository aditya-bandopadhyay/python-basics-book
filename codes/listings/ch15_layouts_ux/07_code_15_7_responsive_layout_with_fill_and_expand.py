# Layouts and User Experience -- Code 15.7: Responsive layout with fill and expand
# (book source: ch15_layouts_ux.tex, line 371)
# NOTE: A fragment from the book; a minimal window has been added around it so it runs.

import tkinter as tk
root = tk.Tk()   # added so the fragment can run

root = tk.Tk()
root.title('Responsive')
root.geometry('400x300')

# Main content area grows with window
content = tk.Frame(root, bg='blue')
content.pack(fill='both', expand=True, padx=10, pady=10)

tk.Label(content, text='Resizable content', bg='blue', fg='white').pack()

# Footer stays at bottom
footer = tk.Frame(root, bg='gray', height=50)
footer.pack(side='bottom', fill='x')
tk.Label(footer, text='Footer', bg='gray').pack()

root.mainloop()

root.mainloop()  # added so the fragment can run
