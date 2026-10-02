"""Mini-Project 14: Unit converter GUI (km/miles, kg/lb, C/F) with error handling."""
import tkinter as tk

CONVERSIONS = {
    "km -> miles": lambda v: (v * 0.621371, "miles"),
    "miles -> km": lambda v: (v / 0.621371, "km"),
    "kg -> lb":    lambda v: (v * 2.20462, "lb"),
    "lb -> kg":    lambda v: (v / 2.20462, "kg"),
    "C -> F":      lambda v: (9 / 5 * v + 32, "deg F"),
    "F -> C":      lambda v: ((v - 32) * 5 / 9, "deg C"),
}

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Unit Converter")
        root.geometry("360x360")

        tk.Label(root, text="Value:", font=("Arial", 11, "bold")).pack(pady=(12, 2))
        self.entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.entry.pack()

        self.choice = tk.StringVar(value="km -> miles")
        box = tk.Frame(root)
        box.pack(pady=8)
        for i, name in enumerate(CONVERSIONS):
            tk.Radiobutton(box, text=name, value=name, variable=self.choice
                           ).grid(row=i // 2, column=i % 2, sticky="w", padx=10)

        buttons = tk.Frame(root)
        buttons.pack(pady=4)
        tk.Button(buttons, text="Convert", width=10, command=self.convert).pack(side="left", padx=4)
        tk.Button(buttons, text="Clear / Reset", width=12, command=self.reset).pack(side="left", padx=4)

        self.result = tk.Label(root, text="--", font=("Arial", 20, "bold"), fg="#2c3e50")
        self.result.pack(pady=12)
        self.status = tk.Label(root, text="Status: Ready", anchor="w", relief="sunken")
        self.status.pack(side="bottom", fill="x")

    def convert(self):
        try:
            value = float(self.entry.get())
        except ValueError:
            self.status.config(text="Status: please type a number (e.g. 12.5)", fg="red")
            self.result.config(text="--")
            return
        out, unit = CONVERSIONS[self.choice.get()](value)
        self.result.config(text=f"{out:,.4g} {unit}")
        self.status.config(text=f"Status: converted using {self.choice.get()}", fg="black")

    def reset(self):
        self.entry.delete(0, tk.END)
        self.result.config(text="--")
        self.status.config(text="Status: Ready", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    UnitConverterApp(root)
    root.mainloop()
