"""D3: An "Export Plot" button that saves the figure wherever the user chooses."""
import tkinter as tk
from tkinter import filedialog, messagebox
from _app import OdeVisualizerApp


class ExportApp(OdeVisualizerApp):
    def create_inputs(self):
        super().create_inputs()
        tk.Button(self.left_panel, text="Export Plot", command=self.export_plot).pack()

    def export_plot(self):
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG image", "*.png"), ("PDF", "*.pdf")])
        if not path:                 # user pressed Cancel
            return
        self.fig.savefig(path, dpi=150)
        messagebox.showinfo("Saved", f"Plot saved to\n{path}")


if __name__ == "__main__":
    root = tk.Tk()
    ExportApp(root)
    root.mainloop()
