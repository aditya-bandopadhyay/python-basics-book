# Layouts and User Experience -- Code 15.9: Mini Image Studio App (Grayscale, Edge Detection & Thresholding Slider)
# (book source: ch15_layouts_ux.tex, line 455)

import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from PIL import Image, ImageTk

class ImageStudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Image Studio: Grayscale & Edge Detection")
        self.root.geometry("850x550")
        
        self.orig_image = None
        self.curr_array = None
        
        # 1. Top Control Bar Frame (Grid layout inside frame)
        control_frame = tk.Frame(self.root, bg="#2E4A7A", padx=10, pady=10)
        control_frame.pack(side="top", fill="x")
        
        btn_open = tk.Button(control_frame, text="Open Image...", font=("Arial", 10, "bold"), command=self.open_image)
        btn_open.pack(side="left", padx=5)
        
        btn_gray = tk.Button(control_frame, text="Convert Grayscale", font=("Arial", 10), command=self.make_grayscale)
        btn_gray.pack(side="left", padx=5)
        
        btn_edge = tk.Button(control_frame, text="Detect Edges", font=("Arial", 10), command=self.detect_edges)
        btn_edge.pack(side="left", padx=5)
        
        tk.Label(control_frame, text="Edge Threshold:", bg="#2E4A7A", fg="white", font=("Arial", 10)).pack(side="left", padx=(20, 5))
        
        self.slider = tk.Scale(control_frame, from_=0, to=255, orient="horizontal", command=self.update_threshold)
        self.slider.set(100)
        self.slider.pack(side="left", padx=5)
        
        # 2. Main Display Area (2 Side-by-side Panes)
        display_frame = tk.Frame(self.root, bg="gray20", padx=10, pady=10)
        display_frame.pack(fill="both", expand=True)
        
        # Left Pane: Original Image
        left_pane = tk.Frame(display_frame, bg="black")
        left_pane.pack(side="left", fill="both", expand=True, padx=5)
        tk.Label(left_pane, text="Original Image", bg="black", fg="white", font=("Arial", 11, "bold")).pack(side="top", pady=2)
        self.lbl_orig = tk.Label(left_pane, bg="black")
        self.lbl_orig.pack(fill="both", expand=True)
        
        # Right Pane: Processed View
        right_pane = tk.Frame(display_frame, bg="black")
        right_pane.pack(side="right", fill="both", expand=True, padx=5)
        tk.Label(right_pane, text="Processed View", bg="black", fg="white", font=("Arial", 11, "bold")).pack(side="top", pady=2)
        self.lbl_proc = tk.Label(right_pane, bg="black")
        self.lbl_proc.pack(fill="both", expand=True)

    def open_image(self):
        filepath = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if not filepath:
            return
        self.orig_image = Image.open(filepath).convert("RGB")
        self.curr_array = np.array(self.orig_image)
        self.display_images(self.orig_image, self.orig_image)

    def make_grayscale(self):
        if self.curr_array is None:
            messagebox.showwarning("Warning", "Please open an image first!")
            return
        r, g, b = self.curr_array[:,:,0], self.curr_array[:,:,1], self.curr_array[:,:,2]
        gray = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
        gray_img = Image.fromarray(gray)
        self.display_images(self.orig_image, gray_img)

    def detect_edges(self):
        if self.curr_array is None:
            messagebox.showwarning("Warning", "Please open an image first!")
            return
        gray = np.mean(self.curr_array, axis=2)
        gx, gy = np.zeros_like(gray), np.zeros_like(gray)
        gx[:, :-1] = np.diff(gray, axis=1)
        gy[:-1, :] = np.diff(gray, axis=0)
        edge_mag = np.sqrt(gx**2 + gy**2)
        max_v = np.max(edge_mag)
        self.edge_array = ((edge_mag / max_v) * 255).astype(np.uint8) if max_v > 0 else edge_mag.astype(np.uint8)
        self.update_threshold(self.slider.get())

    def update_threshold(self, val):
        if not hasattr(self, 'edge_array'):
            return
        thresh = int(val)
        binary_edges = np.where(self.edge_array > thresh, 255, 0).astype(np.uint8)
        self.display_images(self.orig_image, Image.fromarray(binary_edges))

    def display_images(self, img1, img2):
        p1, p2 = img1.copy(), img2.copy()
        p1.thumbnail((380, 380))
        p2.thumbnail((380, 380))
        self.tk_img1, self.tk_img2 = ImageTk.PhotoImage(p1), ImageTk.PhotoImage(p2)
        self.lbl_orig.config(image=self.tk_img1)
        self.lbl_proc.config(image=self.tk_img2)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageStudioApp(root)
    root.mainloop()
