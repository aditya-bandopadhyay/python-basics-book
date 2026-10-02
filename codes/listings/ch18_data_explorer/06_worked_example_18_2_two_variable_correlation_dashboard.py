# Building a CSV Data Explorer Dashboard -- Worked Example 18.2: Two-Variable Correlation Dashboard
# (book source: ch18_data_explorer.tex, line 444)

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

class CorrelationDashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Two-Variable Correlation Dashboard")
        self.root.geometry("420x220")
        self.root.configure(padx=15, pady=15)
        
        # Paired datasets: Study Hours (X) vs Exam Score (Y)
        self.x = np.array([2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7])
        self.y = np.array([30,   54,  41,  92,  45,  22,  98,  60,  88,  33])
        
        tk.Label(root, text="BIVARIATE CORRELATION WORKBENCH", font=("Arial", 11, "bold"), fg="#2c3e50").pack(pady=(0, 10))
        
        r = np.corrcoef(self.x, self.y)[0, 1]
        if abs(r) >= 0.7:
            strength = "Strong"
        elif abs(r) >= 0.4:
            strength = "Moderate"
        else:
            strength = "Weak"
        direction = "Positive" if r > 0 else "Negative"
        self.lbl_stats = tk.Label(root, text=f"Pearson Correlation (r): {r:.4f}\nStrength: {strength} {direction} Linear Relationship",
                                  font=("Arial", 10, "bold"), fg="#27ae60", bg="#ecf0f1", padx=10, pady=8, bd=1, relief="ridge")
        self.lbl_stats.pack(fill="x", pady=10)
        
        btn_plot = tk.Button(root, text="Plot Scatter & Trendline", font=("Arial", 10, "bold"),
                             bg="#2980b9", fg="white", pady=6, command=self.plot_scatter)
        btn_plot.pack(fill="x", pady=5)

    def plot_scatter(self):
        m, c = np.polyfit(self.x, self.y, 1)  # Linear regression fit
        plt.figure(figsize=(6, 4))
        plt.scatter(self.x, self.y, color="#e74c3c", s=50, label="Observations")
        plt.plot(self.x, m * self.x + c, color="#2980b9", lw=2, label=f"Fit: y = {m:.2f}x + {c:.2f}")
        plt.title("Study Hours vs. Exam Score Correlation", fontweight="bold")
        plt.xlabel("Study Hours (X)")
        plt.ylabel("Exam Score (Y)")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = CorrelationDashboardApp(root)
    root.mainloop()
