"""D1: Threshold filter -- highlight rows whose selected column exceeds a value."""
import tkinter as tk
from tkinter import messagebox
from _app import DataExplorerApp


class ThresholdApp(DataExplorerApp):
    def build_ui(self):
        super().build_ui()
        bar = tk.Frame(self.root, bg="#f4f6f9", padx=10)
        bar.pack(fill="x", before=self.stats_card)
        tk.Label(bar, text="Highlight rows where value >", bg="#f4f6f9").pack(side="left")
        self.ent_thresh = tk.Entry(bar, width=8)
        self.ent_thresh.pack(side="left", padx=4)
        tk.Button(bar, text="Apply", command=self.highlight).pack(side="left")
        self.txt.tag_config("over", foreground="red", font=("Courier", 9, "bold"))

    def highlight(self):
        self.txt.tag_remove("over", "1.0", tk.END)
        try:
            limit = float(self.ent_thresh.get())
        except ValueError:
            messagebox.showerror("Input Error", "Threshold must be a number."); return
        col = self.combo_cols.current()
        count = 0
        for i, row in enumerate(self.rows[1:], start=2):     # text line 1 is the header
            try:
                if len(row) > col and float(row[col]) > limit:
                    self.txt.tag_add("over", f"{i}.0", f"{i}.end")
                    count += 1
            except ValueError:
                pass
        self.lbl_status.config(text=f"Status: {count} rows above {limit:g} highlighted in red")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x520")
    ThresholdApp(root)
    root.mainloop()
