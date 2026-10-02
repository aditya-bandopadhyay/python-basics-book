"""D3: Centred login window."""
import tkinter as tk

root = tk.Tk()
root.title("Login")
w, h = 320, 200
x = (root.winfo_screenwidth() - w) // 2          # centre on the screen
y = (root.winfo_screenheight() - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")
root.configure(bg="#ecf0f1")

form = tk.Frame(root, bg="#ecf0f1", padx=20, pady=20)
form.pack(expand=True)
tk.Label(form, text="Username", bg="#ecf0f1", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=4)
user = tk.Entry(form, font=("Arial", 11))
user.grid(row=0, column=1, pady=4)
tk.Label(form, text="Password", bg="#ecf0f1", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=4)
tk.Entry(form, font=("Arial", 11), show="*").grid(row=1, column=1, pady=4)

status = tk.Label(root, text="", bg="#ecf0f1")
buttons = tk.Frame(form, bg="#ecf0f1")
buttons.grid(row=2, column=0, columnspan=2, pady=(12, 0))
tk.Button(buttons, text="Log in", width=10, bg="#27ae60", fg="white",
          command=lambda: status.config(text=f"Welcome, {user.get() or 'guest'}!")).pack(side="left", padx=4)
tk.Button(buttons, text="Cancel", width=10, command=root.destroy).pack(side="left", padx=4)
status.pack(pady=(0, 8))
root.mainloop()
