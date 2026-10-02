"""Bugs 18.1-18.5, fixed, in one small working program.

Bug 18.1 -- the scrollbar must also be told what to scroll:
            sb.config(command=txt.yview).
Bug 18.2 -- clear the text box before inserting a new file:
            self.txt.delete("1.0", tk.END).
Bug 18.3 -- the combobox needs a binding for its selection event:
            self.combo_cols.bind("<<ComboboxSelected>>", self.analyze_column).
Bug 18.4 -- csv gives strings; convert with float() (skipping bad cells)
            before handing the numbers to NumPy.
Bug 18.5 -- askopenfilename() returns "" when the user cancels; return early.
"""
import csv
import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np


class FixedExplorer:
    def __init__(self, root):
        self.root = root
        root.title("Chapter 18 bugs fixed")
        self.rows = []
        tk.Button(root, text="Open CSV", command=self.load_csv).pack()
        self.combo_cols = ttk.Combobox(root, state="readonly")
        self.combo_cols.pack()
        self.combo_cols.bind("<<ComboboxSelected>>", self.analyze_column)      # Bug 18.3
        self.lbl = tk.Label(root, text="Mean: N/A")
        self.lbl.pack()
        frame = tk.Frame(root); frame.pack(fill="both", expand=True)
        sb = tk.Scrollbar(frame)
        sb.pack(side="right", fill="y")
        self.txt = tk.Text(frame, yscrollcommand=sb.set, height=12)
        self.txt.pack(side="left", fill="both", expand=True)
        sb.config(command=self.txt.yview)                                      # Bug 18.1

    def load_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if not filepath:                                                       # Bug 18.5
            return
        with open(filepath, newline="") as f:
            self.rows = list(csv.reader(f))
        self.txt.delete("1.0", tk.END)                                         # Bug 18.2
        for row in self.rows:
            self.txt.insert(tk.END, ", ".join(row) + "\n")
        self.combo_cols["values"] = self.rows[0]
        self.combo_cols.current(0)
        self.analyze_column()

    def analyze_column(self, event=None):
        col_idx = self.combo_cols.current()
        numbers = []
        for row in self.rows[1:]:
            try:
                numbers.append(float(row[col_idx]))                            # Bug 18.4
            except (ValueError, IndexError):
                continue
        self.lbl.config(text=f"Mean: {np.mean(numbers):.2f}" if numbers else "Mean: N/A")


if __name__ == "__main__":
    root = tk.Tk()
    FixedExplorer(root)
    root.mainloop()
