"""D2: Export the statistics of the selected column to a text file."""
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from _app import DataExplorerApp, column_numbers


class ReportApp(DataExplorerApp):
    def build_ui(self):
        super().build_ui()
        tk.Button(self.root, text="Export Summary Report", command=self.export_report).pack(before=self.stats_card, pady=2)

    def export_report(self):
        if len(self.rows) < 2:
            messagebox.showwarning("Warning", "Please load a CSV file first!"); return
        col = self.combo_cols.current()
        values = np.array(column_numbers(self.rows, col))
        if values.size == 0:
            messagebox.showwarning("Warning", "That column has no numbers."); return
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text", "*.txt")])
        if not path:
            return
        lines = [f"Summary of column '{self.headers[col]}'",
                 f"Count:   {values.size}",
                 f"Mean:    {values.mean():.4f}",
                 f"Median:  {np.median(values):.4f}",
                 f"Std dev: {values.std(ddof=1):.4f}" if values.size > 1 else "Std dev: n/a",
                 f"Min:     {values.min():.4f}",
                 f"Max:     {values.max():.4f}"]
        with open(path, "w") as f:
            f.write("\n".join(lines) + "\n")
        self.lbl_status.config(text=f"Status: report saved to {path}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x520")
    ReportApp(root)
    root.mainloop()
