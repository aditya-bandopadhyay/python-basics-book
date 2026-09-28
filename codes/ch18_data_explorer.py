"""
ch17_data_explorer.py

A CSV Data Explorer GUI demonstrating Tkinter file dialogs, Scrollbar,
and integrations with NumPy for descriptive statistics calculation.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import csv


class DataExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Data Explorer")
        self.root.geometry("500x400")

        # Top Control Frame
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(fill=tk.X, padx=10, pady=5)

        self.btn_load = tk.Button(
            self.top_frame, text="Load CSV File", command=self.load_csv
        )
        self.btn_load.pack(side=tk.LEFT)

        self.lbl_filename = tk.Label(
            self.top_frame, text="No file loaded", fg="gray"
        )
        self.lbl_filename.pack(side=tk.LEFT, padx=10)

        # Content Area (Text area containing a scrollbar)
        self.content_frame = tk.Frame(root)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.scrollbar = tk.Scrollbar(self.content_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.txt_display = tk.Text(
            self.content_frame,
            wrap=tk.NONE,
            xscrollcommand=self.scrollbar.set,
            font=("Courier", 10),
        )
        self.txt_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.txt_display.yview)

        # Statistics Summary Frame (Bottom Panel)
        self.stats_frame = tk.LabelFrame(root, text="Summary Statistics")
        self.stats_frame.pack(fill=tk.X, padx=10, pady=10)

        self.lbl_mean = tk.Label(self.stats_frame, text="Mean: N/A")
        self.lbl_mean.grid(row=0, column=0, padx=15, pady=5)

        self.lbl_median = tk.Label(self.stats_frame, text="Median: N/A")
        self.lbl_median.grid(row=0, column=1, padx=15, pady=5)

        self.lbl_std = tk.Label(self.stats_frame, text="Std Dev: N/A")
        self.lbl_std.grid(row=0, column=2, padx=15, pady=5)

    def load_csv(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if not filepath:
            return

        self.lbl_filename.config(
            text=filepath.split("/")[-1], fg="black"
        )
        self.txt_display.delete("1.0", tk.END)

        try:
            with open(filepath, "r", newline="") as file:
                reader = csv.reader(file)
                rows = list(reader)

            if not rows:
                raise ValueError("The selected CSV file is empty.")

            # Display rows in Text widget
            formatted_txt = ""
            for row in rows:
                formatted_txt += ", ".join(row) + "\n"
            self.txt_display.insert(tk.END, formatted_txt)

            # Attempt to parse numerical data from the last column for stats
            numbers = []
            for row in rows[1:]:  # skip header
                if len(row) > 0:
                    try:
                        numbers.append(float(row[-1]))
                    except ValueError:
                        continue

            # Update stats if numerical column found
            if numbers:
                data_arr = np.array(numbers)
                self.lbl_mean.config(
                    text=f"Mean: {np.mean(data_arr):.4f}"
                )
                self.lbl_median.config(
                    text=f"Median: {np.median(data_arr):.4f}"
                )
                self.lbl_std.config(
                    text=f"Std Dev: {np.std(data_arr, ddof=1):.4f}"
                )
            else:
                self.lbl_mean.config(text="Mean: No numeric column")
                self.lbl_median.config(text="Median: No numeric column")
                self.lbl_std.config(text="Std Dev: No numeric column")

        except Exception as err:
            messagebox.showerror(
                "File Error", f"Could not parse CSV:\n{err}"
            )
            self.lbl_filename.config(text="Error loading file", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataExplorerApp(root)
    root.mainloop()
