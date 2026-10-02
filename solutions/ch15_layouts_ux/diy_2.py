"""D2: Responsive dashboard: header, fixed-width sidebar, expanding content."""
import tkinter as tk

root = tk.Tk()
root.title("Dashboard")
root.geometry("640x400")

header = tk.Label(root, text="My Dashboard", bg="#2c3e50", fg="white", font=("Arial", 14, "bold"), pady=8)
header.pack(side="top", fill="x")

sidebar = tk.Frame(root, bg="#34495e", width=150)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)
content = tk.Label(root, text="Welcome!", font=("Arial", 16), bg="white")
content.pack(side="right", fill="both", expand=True)

for name in ["Home", "Reports", "Settings"]:
    tk.Button(sidebar, text=name, command=lambda n=name: content.config(text=f"{n} page")
              ).pack(fill="x", padx=8, pady=4)
root.mainloop()
