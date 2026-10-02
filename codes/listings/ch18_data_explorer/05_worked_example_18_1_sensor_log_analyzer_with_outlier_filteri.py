# Building a CSV Data Explorer Dashboard -- Worked Example 18.1: Sensor Log Analyzer with Outlier Filtering
# (book source: ch18_data_explorer.tex, line 365)

import tkinter as tk
from tkinter import messagebox
import numpy as np

class SensorAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensor Log Outlier Analyzer")
        self.root.geometry("450x320")
        self.root.configure(padx=15, pady=15)
        
        # Simulated temperature sensor telemetry
        self.data = np.array([21.4, 21.8, 22.1, 21.9, 28.5, 22.0, 21.7, 31.2, 22.3, 21.5])
        
        tk.Label(root, text="SENSOR TELEMETRY OUTLIER FILTER", font=("Arial", 11, "bold"), fg="#2c3e50").pack(pady=(0, 10))
        
        # Raw Data Display Box
        self.txt_data = tk.Text(root, height=4, font=("Courier", 9))
        self.txt_data.insert(tk.END, ", ".join(f"{v:.1f}" for v in self.data))
        self.txt_data.pack(fill="x", pady=5)
        
        # Threshold Input
        ctrl_frame = tk.Frame(root)
        ctrl_frame.pack(fill="x", pady=8)
        
        tk.Label(ctrl_frame, text="Outlier Threshold (deg C):", font=("Arial", 10)).pack(side="left")
        self.ent_thresh = tk.Entry(ctrl_frame, width=8, font=("Arial", 10))
        self.ent_thresh.insert(0, "25.0")
        self.ent_thresh.pack(side="left", padx=10)
        
        btn_filter = tk.Button(ctrl_frame, text="Filter Outliers", font=("Arial", 9, "bold"),
                               bg="#e67e22", fg="white", command=self.apply_filter)
        btn_filter.pack(side="left")
        
        # Results Card
        self.lbl_result = tk.Label(root, text="Results: Click 'Filter Outliers' to analyze.",
                                   font=("Arial", 10), justify="left", bg="#ecf0f1", padx=10, pady=10, relief="solid", bd=1)
        self.lbl_result.pack(fill="both", expand=True, pady=10)

    def apply_filter(self):
        try:
            thresh = float(self.ent_thresh.get())
            outliers = self.data[self.data > thresh]
            normal = self.data[self.data <= thresh]
            
            res_str = (
                f"Total Readings: {len(self.data)}\n"
                f"Normal Readings: {len(normal)} (Mean: {np.mean(normal):.2f} C)\n"
                f"Outliers Detected: {len(outliers)} (Mean: {np.mean(outliers) if len(outliers) else 0.0:.2f} C)\n"
                f"Outlier Values: {list(outliers)}"
            )
            self.lbl_result.config(text=res_str)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric threshold.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SensorAnalyzerApp(root)
    root.mainloop()
