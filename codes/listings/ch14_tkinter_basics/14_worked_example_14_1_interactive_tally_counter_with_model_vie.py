# Tkinter Basics -- Worked Example 14.1: Interactive Tally Counter with Model-View Separation
# (book source: ch14_tkinter_basics.tex, line 552)

import tkinter as tk

class TallyCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Tally Counter")
        self.root.geometry("300x220")
        self.root.configure(bg="#f8f9fa")

        # Application State (Model)
        self.count = 0

        # Title Label
        tk.Label(root, text="Stadium Turnstile Counter", font=("Arial", 11, "bold"),
                 bg="#2c3e50", fg="white", pady=6).pack(fill="x")

        # Main Numerical Display (View)
        self.lbl_count = tk.Label(root, text="0", font=("Arial", 36, "bold"),
                                  bg="#f8f9fa", fg="#2c3e50")
        self.lbl_count.pack(pady=15)

        # Button Container Frame
        btn_frame = tk.Frame(root, bg="#f8f9fa")
        btn_frame.pack(pady=10)

        # Control Buttons (Controller)
        tk.Button(btn_frame, text=" -1 ", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
                  width=5, relief="groove", command=self.decrement).grid(row=0, column=0, padx=6)
        tk.Button(btn_frame, text="Reset", font=("Arial", 11), bg="#95a5a6", fg="white",
                  width=6, relief="groove", command=self.reset).grid(row=0, column=1, padx=6)
        tk.Button(btn_frame, text=" +1 ", font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                  width=5, relief="groove", command=self.increment).grid(row=0, column=2, padx=6)

    def increment(self):
        self.count += 1
        self.update_display()

    def decrement(self):
        if self.count > 0:
            self.count -= 1
            self.update_display()

    def reset(self):
        self.count = 0
        self.update_display()

    def update_display(self):
        self.lbl_count.config(text=str(self.count))

root = tk.Tk()
app = TallyCounterApp(root)
root.mainloop()
