"""
ch13_tkinter_basics.py

Very small Tkinter example that creates a window with a label and a button.
Running this requires a GUI environment.
"""

try:
    import tkinter as tk
except Exception:
    tk = None


def create_simple_window():
    if tk is None:
        print("Tkinter is not available in this environment.")
        return
    root_window = tk.Tk()
    root_window.title("Simple Tkinter Example")
    label_widget = tk.Label(root_window, text="Hello from Tkinter!")
    label_widget.pack(padx=10, pady=10)
    button_widget = tk.Button(
        root_window, text="Close", command=root_window.destroy
    )
    button_widget.pack(padx=10, pady=5)
    root_window.mainloop()


if __name__ == "__main__":
    create_simple_window()
