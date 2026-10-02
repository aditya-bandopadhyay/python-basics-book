"""D3: Roll two dice (2d6) and count the rolls."""
import random
import tkinter as tk

rolls = 0

def roll():
    global rolls
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    rolls += 1
    result.config(text=f"{d1} + {d2} = {d1 + d2}")
    counter.config(text=f"Rolls so far: {rolls}")

root = tk.Tk()
root.title("Dice Roller")
result = tk.Label(root, text="Press Roll", font=("Arial", 24, "bold"))
result.pack(padx=30, pady=15)
tk.Button(root, text="Roll 2d6", font=("Arial", 12), command=roll).pack()
counter = tk.Label(root, text="Rolls so far: 0")
counter.pack(pady=10)
root.mainloop()
