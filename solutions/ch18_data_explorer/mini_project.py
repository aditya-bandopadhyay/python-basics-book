"""Mini-Project 18: Multi-file CSV workbench with tabs.

Each opened file gets its own tab with: a statistics table that also counts
missing / non-numeric cells, a scatter plot with a regression line for any two
columns, and an "Export Cleaned CSV" button that drops incomplete rows.
"""
import csv
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def to_float(cell):
    try:
        return float(cell)
    except ValueError:
        return np.nan


class DatasetTab:
    def __init__(self, notebook, path):
        with open(path, newline="") as f:
            rows = [r for r in csv.reader(f) if r]
        self.headers, self.raw = rows[0], rows[1:]
        width = len(self.headers)
        self.raw = [(r + [""] * width)[:width] for r in self.raw]          # pad short rows
        self.data = np.array([[to_float(c) for c in r] for r in self.raw])
        self.path = path

        self.frame = tk.Frame(notebook)
        notebook.add(self.frame, text=os.path.basename(path))

        stats = ttk.Treeview(self.frame, columns=("n", "nan", "mean", "std", "min", "max"), height=6)
        for col, title in zip(("#0", "n", "nan", "mean", "std", "min", "max"),
                              ("Column", "Values", "Missing/NaN", "Mean", "Std", "Min", "Max")):
            stats.heading(col, text=title)
            stats.column(col, width=90, anchor="center")
        for j, name in enumerate(self.headers):
            col = self.data[:, j]
            good = col[~np.isnan(col)]
            if good.size:
                stats.insert("", "end", text=name, values=(good.size, int(np.isnan(col).sum()),
                             f"{good.mean():.3g}", f"{good.std(ddof=1):.3g}" if good.size > 1 else "-",
                             f"{good.min():.3g}", f"{good.max():.3g}"))
            else:
                stats.insert("", "end", text=name, values=(0, len(col), "-", "-", "-", "-"))
        stats.pack(fill="x", padx=6, pady=6)

        numeric = [h for j, h in enumerate(self.headers) if np.sum(~np.isnan(self.data[:, j])) >= 2]
        bar = tk.Frame(self.frame); bar.pack(fill="x", padx=6)
        self.xcol = ttk.Combobox(bar, values=numeric, state="readonly", width=14)
        self.ycol = ttk.Combobox(bar, values=numeric, state="readonly", width=14)
        tk.Label(bar, text="x:").pack(side="left"); self.xcol.pack(side="left", padx=2)
        tk.Label(bar, text="y:").pack(side="left"); self.ycol.pack(side="left", padx=2)
        tk.Button(bar, text="Scatter + fit", command=self.plot).pack(side="left", padx=6)
        tk.Button(bar, text="Export Cleaned CSV", command=self.export_clean).pack(side="right")
        if len(numeric) >= 2:
            self.xcol.set(numeric[0]); self.ycol.set(numeric[1])

        self.fig = Figure(figsize=(6, 3.2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def plot(self):
        if not self.xcol.get() or not self.ycol.get():
            return
        x = self.data[:, self.headers.index(self.xcol.get())]
        y = self.data[:, self.headers.index(self.ycol.get())]
        ok = ~np.isnan(x) & ~np.isnan(y)
        self.ax.clear()
        self.ax.scatter(x[ok], y[ok], s=25)
        if ok.sum() >= 2 and np.ptp(x[ok]) > 0:
            m, c = np.polyfit(x[ok], y[ok], 1)
            r = np.corrcoef(x[ok], y[ok])[0, 1]
            xs = np.linspace(x[ok].min(), x[ok].max(), 50)
            self.ax.plot(xs, m * xs + c, "r-", label=f"y = {m:.3g}x + {c:.3g}  (r = {r:.2f})")
            self.ax.legend(fontsize=8)
        self.ax.set_xlabel(self.xcol.get()); self.ax.set_ylabel(self.ycol.get()); self.ax.grid(alpha=0.3)
        self.fig.tight_layout()
        self.canvas.draw()

    def export_clean(self):
        numeric_cols = [j for j in range(len(self.headers)) if np.sum(~np.isnan(self.data[:, j])) > 0]
        keep = [r for r, vals in zip(self.raw, self.data)
                if all(c.strip() for c in r) and not np.isnan(vals[numeric_cols]).any()]
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")],
                                            initialfile="cleaned_" + os.path.basename(self.path))
        if not path:
            return
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(self.headers)
            w.writerows(keep)
        messagebox.showinfo("Exported", f"Kept {len(keep)} of {len(self.raw)} rows.")


class WorkbenchApp:
    def __init__(self, root):
        self.root = root
        root.title("CSV Comparative Workbench")
        root.geometry("820x600")
        tk.Button(root, text="Open CSV...", command=self.open_file).pack(anchor="w", padx=6, pady=4)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)
        self.tabs = []

    def open_file(self, path=None):
        path = path or filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        if not path:
            return
        try:
            tab = DatasetTab(self.notebook, path)
        except Exception as err:
            messagebox.showerror("File Error", f"Could not read {path}:\n{err}")
            return
        self.tabs.append(tab)
        self.notebook.select(tab.frame)
        tab.plot()


if __name__ == "__main__":
    root = tk.Tk()
    WorkbenchApp(root)
    root.mainloop()
