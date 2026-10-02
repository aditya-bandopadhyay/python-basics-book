"""
Building a CSV Data Explorer Dashboard -- companion script for Chapter 18.
This is the chapter's main application (Code 18.3: Scientific CSV Data Explorer Dashboard).
Every other listing from the chapter is in codes/listings/ch18_data_explorer/.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

class DataExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Data Explorer & Statistical Workbench")
        self.root.geometry("560x480")
        self.root.configure(bg="#f4f6f9")
        
        self.rows = []
        self.headers = []
        
        self.build_ui()

    def build_ui(self):
        # Header Banner
        hdr = tk.Label(self.root, text="SCIENTIFIC CSV DATA EXPLORER & WORKBENCH", 
                       font=("Arial", 11, "bold"), bg="#2c3e50", fg="white", pady=6)
        hdr.pack(fill="x")

        # BLOCK 1: File Ingestion Header
        f_top = tk.Frame(self.root, bg="#f4f6f9", padx=10, pady=5)
        f_top.pack(fill="x")

        btn_load = tk.Button(f_top, text="[Open CSV File]", font=("Arial", 9, "bold"), 
                            bg="#2980b9", fg="white", padx=8, pady=3, command=self.load_csv)
        btn_load.pack(side="left")

        self.lbl_file = tk.Label(f_top, text="No file loaded", font=("Arial", 9, "bold"), 
                                 fg="gray", bg="#f4f6f9")
        self.lbl_file.pack(side="left", padx=10)

        # BLOCK 2: Scrollable Raw Data Text View
        f_content = tk.Frame(self.root, bg="#f4f6f9", padx=10, pady=2)
        f_content.pack(fill="both", expand=True)

        sb = tk.Scrollbar(f_content)
        sb.pack(side="right", fill="y")

        self.txt = tk.Text(f_content, wrap="none", yscrollcommand=sb.set, 
                           font=("Courier", 9), height=10, bg="#ffffff", fg="#2c3e50", bd=1, relief="solid")
        self.txt.pack(side="left", fill="both", expand=True)
        sb.config(command=self.txt.yview)

        # BLOCK 3: Dynamic Column & Filter Controls
        f_ctrl = tk.Frame(self.root, bg="#eaeded", bd=1, relief="groove", padx=10, pady=6)
        f_ctrl.pack(fill="x", padx=10, pady=5)

        tk.Label(f_ctrl, text="Target Column:", font=("Arial", 9, "bold"), bg="#eaeded").grid(row=0, column=0, sticky="w")
        
        self.combo_cols = ttk.Combobox(f_ctrl, state="readonly", width=20)
        self.combo_cols.grid(row=0, column=1, padx=5, sticky="w")
        self.combo_cols.bind("<<ComboboxSelected>>", self.analyze_selected_column)

        btn_plot = tk.Button(f_ctrl, text="[Plot Column Histogram]", font=("Arial", 9, "bold"), 
                             bg="#8e44ad", fg="white", padx=8, pady=2, command=self.plot_histogram)
        btn_plot.grid(row=0, column=2, padx=12)

        # BLOCK 4: Summary Statistics Card
        self.stats_card = tk.LabelFrame(self.root, text="NumPy Summary Statistics", 
                                       font=("Arial", 9, "bold"), bg="#ffffff", fg="#2c3e50", padx=10, pady=6)
        self.stats_card.pack(fill="x", padx=10, pady=5)

        self.lbl_mean = tk.Label(self.stats_card, text="Mean: N/A", font=("Arial", 9, "bold"), fg="#2980b9", bg="#ffffff")
        self.lbl_mean.grid(row=0, column=0, padx=10, pady=3)
        
        self.lbl_median = tk.Label(self.stats_card, text="Median: N/A", font=("Arial", 9, "bold"), fg="#27ae60", bg="#ffffff")
        self.lbl_median.grid(row=0, column=1, padx=10, pady=3)
        
        self.lbl_std = tk.Label(self.stats_card, text="Std Dev: N/A", font=("Arial", 9, "bold"), fg="#e67e22", bg="#ffffff")
        self.lbl_std.grid(row=0, column=2, padx=10, pady=3)

        self.lbl_min = tk.Label(self.stats_card, text="Min: N/A", font=("Arial", 9, "bold"), fg="#7f8c8d", bg="#ffffff")
        self.lbl_min.grid(row=0, column=3, padx=10, pady=3)

        self.lbl_max = tk.Label(self.stats_card, text="Max: N/A", font=("Arial", 9, "bold"), fg="#e74c3c", bg="#ffffff")
        self.lbl_max.grid(row=0, column=4, padx=10, pady=3)

        # BLOCK 5: Status Bar
        self.lbl_status = tk.Label(self.root, text="Status: Ready | Load a CSV file to begin", 
                                   bd=1, relief="sunken", anchor="w", font=("Arial", 8, "italic"), bg="#e0e0e0", fg="#333333")
        self.lbl_status.pack(side="bottom", fill="x")

    def load_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        if not filepath:
            return
        
        filename = os.path.basename(filepath)
        self.lbl_file.config(text=f"Loaded: {filename}", fg="#27ae60")
        self.txt.delete("1.0", tk.END)

        try:
            with open(filepath, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                self.rows = list(reader)

            if not self.rows:
                raise ValueError("The selected CSV file is empty.")

            self.headers = self.rows[0]
            self.combo_cols['values'] = [f"{h} (Col {i+1})" for i, h in enumerate(self.headers)]
            if self.headers:
                self.combo_cols.current(0)

            # Insert formatted rows into text widget
            formatted_txt = ""
            for row in self.rows:
                formatted_txt += ",  ".join(row) + "\n"
            self.txt.insert(tk.END, formatted_txt)

            self.analyze_selected_column()
        except Exception as err:
            messagebox.showerror("File Error", f"Could not parse CSV:\n{err}")
            self.lbl_file.config(text="Error loading file", fg="red")

    def analyze_selected_column(self, event=None):
        if not self.rows or len(self.rows) < 2:
            return

        col_idx = self.combo_cols.current()
        if col_idx < 0:
            col_idx = 0

        numbers = []
        for row in self.rows[1:]:
            if len(row) > col_idx:
                try:
                    numbers.append(float(row[col_idx]))
                except ValueError:
                    continue

        if numbers:
            arr = np.array(numbers)
            self.lbl_mean.config(text=f"Mean: {np.mean(arr):.2f}")
            self.lbl_median.config(text=f"Median: {np.median(arr):.2f}")
            self.lbl_std.config(text=f"Std Dev: {np.std(arr, ddof=1):.2f}")
            self.lbl_min.config(text=f"Min: {np.min(arr):.2f}")
            self.lbl_max.config(text=f"Max: {np.max(arr):.2f}")
            self.lbl_status.config(text=f"Status: Analyzed {len(numbers)} numeric rows in '{self.headers[col_idx]}'")
        else:
            self.lbl_mean.config(text="Mean: N/A")
            self.lbl_median.config(text="Median: N/A")
            self.lbl_std.config(text="Std Dev: N/A")
            self.lbl_min.config(text="Min: N/A")
            self.lbl_max.config(text="Max: N/A")
            self.lbl_status.config(text="Status: Selected column contains no numeric data.")

    def plot_histogram(self):
        if not self.rows or len(self.rows) < 2:
            messagebox.showwarning("Warning", "Please load a CSV file first!")
            return

        col_idx = self.combo_cols.current()
        numbers = []                   # same rule as analyze_selected_column
        for row in self.rows[1:]:
            if len(row) > col_idx:
                try:
                    numbers.append(float(row[col_idx]))
                except ValueError:
                    continue

        if not numbers:
            messagebox.showwarning("Warning", "Selected column contains no valid numeric data to plot!")
            return

        plt.figure(figsize=(6, 4))
        plt.hist(numbers, bins=15, color="#2980b9", edgecolor="white")
        plt.title(f"Distribution Histogram: {self.headers[col_idx]}")
        plt.xlabel(self.headers[col_idx])
        plt.ylabel("Frequency")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataExplorerApp(root)
    root.mainloop()
