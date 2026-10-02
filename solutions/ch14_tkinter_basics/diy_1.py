"""D1: Celsius -> Fahrenheit converter in a 300x150 window."""
import tkinter as tk

def convert():
    try:
        c = float(entry.get())
        result.config(text=f"{c:g} C = {9 / 5 * c + 32:.1f} F", fg="black")
    except ValueError:
        result.config(text="Please type a number", fg="red")

root = tk.Tk()
root.title("C to F")
root.geometry("300x150")

tk.Label(root, text="Temperature in Celsius:").pack(pady=(10, 2))
entry = tk.Entry(root, width=10)
entry.pack()
tk.Button(root, text="Convert", command=convert).pack(pady=5)
result = tk.Label(root, text="", font=("Arial", 12, "bold"))
result.pack()

root.mainloop()
