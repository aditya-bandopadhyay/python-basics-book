"""D4: A box-plot button next to the histogram."""
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from _app import DataExplorerApp, column_numbers


class BoxPlotApp(DataExplorerApp):
    def build_ui(self):
        super().build_ui()
        tk.Button(self.root, text="[Plot Column Box Plot]", bg="#16a085", fg="white",
                  command=self.plot_boxplot).pack(before=self.stats_card, pady=2)

    def plot_boxplot(self):
        if len(self.rows) < 2:
            messagebox.showwarning("Warning", "Please load a CSV file first!"); return
        col = self.combo_cols.current()
        numbers = column_numbers(self.rows, col)
        if not numbers:
            messagebox.showwarning("Warning", "That column has no numbers."); return
        plt.figure(figsize=(5, 4))
        plt.boxplot(numbers)
        plt.xticks([1], [self.headers[col]])
        plt.title(f"Box plot: {self.headers[col]}")
        plt.grid(True, axis="y", alpha=0.3)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x520")
    BoxPlotApp(root)
    root.mainloop()
