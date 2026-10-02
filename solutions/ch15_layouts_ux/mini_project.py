"""Mini-Project 15: Survey and feedback form."""
import tkinter as tk
from tkinter import messagebox

class SurveyApp:
    def __init__(self, root):
        self.root = root
        root.title("Book Feedback Survey")
        root.geometry("460x420")
        root.minsize(380, 360)

        form = tk.Frame(root, padx=15, pady=10)
        form.pack(fill="both", expand=True)
        form.columnconfigure(1, weight=1)       # inputs stretch sideways
        form.rowconfigure(4, weight=1)          # the comment box takes extra height

        self.entries = {}
        for row, field in enumerate(["Name", "Email", "Age"]):
            tk.Label(form, text=field + ":").grid(row=row, column=0, sticky="w", pady=4)
            e = tk.Entry(form)
            e.grid(row=row, column=1, sticky="ew", pady=4)
            self.entries[field] = e

        tk.Label(form, text="How satisfied are you with this book?").grid(
            row=3, column=0, columnspan=2, sticky="w", pady=(10, 2))
        self.rating = tk.IntVar(value=0)
        stars = tk.Frame(form)
        stars.grid(row=3, column=1, sticky="e")
        for r in range(1, 6):
            tk.Radiobutton(stars, text=str(r), value=r, variable=self.rating).pack(side="left")

        self.comments = tk.Text(form, height=6, wrap="word")
        self.comments.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=(8, 4))

        buttons = tk.Frame(root, pady=8)
        buttons.pack(side="bottom")
        tk.Button(buttons, text="Submit", width=12, bg="#27ae60", fg="white",
                  command=self.submit).pack(side="left", padx=6)
        tk.Button(buttons, text="Clear", width=12, command=self.clear).pack(side="left", padx=6)

    def submit(self):
        name = self.entries["Name"].get().strip()
        age_text = self.entries["Age"].get().strip()
        if not name or self.rating.get() == 0:
            messagebox.showwarning("Incomplete", "Please give your name and a rating.")
            return
        if age_text and not age_text.isdigit():
            messagebox.showerror("Invalid age", "Age must be a whole number.")
            return
        messagebox.showinfo("Thank you", f"Thanks, {name}! You rated the book {self.rating.get()}/5.")

    def clear(self):
        for e in self.entries.values():
            e.delete(0, tk.END)
        self.rating.set(0)
        self.comments.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    SurveyApp(root)
    root.mainloop()
