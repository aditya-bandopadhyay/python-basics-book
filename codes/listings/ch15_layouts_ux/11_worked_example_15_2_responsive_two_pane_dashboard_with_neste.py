# Layouts and User Experience -- Worked Example 15.2: Responsive Two-Pane Dashboard with Nested Frames
# (book source: ch15_layouts_ux.tex, line 669)

import tkinter as tk

def select_tab(tab_name):
    lbl_content.config(text=f"Active View: {tab_name}\n\nContent dynamically populated here.")

root = tk.Tk()
root.title("Responsive Two-Pane Dashboard")
root.geometry("600x350")
root.minsize(450, 250)

# 1. Left Sidebar Navigation Frame (fixed width, fills vertically)
sidebar = tk.Frame(root, bg="#1a252f", width=160, padx=10, pady=15)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)  # Enforce fixed width regardless of child contents

tk.Label(sidebar, text="DASHBOARD", font=("Arial", 11, "bold"), fg="#ecf0f1", bg="#1a252f").pack(pady=(0, 20))

tabs = ["Overview", "Analytics", "Reports", "Settings"]
for tab in tabs:
    btn = tk.Button(sidebar, text=tab, font=("Arial", 10), bg="#2c3e50", fg="white",
                    bd=0, activebackground="#34495e", activeforeground="white",
                    command=lambda t=tab: select_tab(t))
    btn.pack(fill="x", pady=4)

# 2. Right Content Card (expands in both directions)
content_frame = tk.Frame(root, bg="#ecf0f1", padx=20, pady=20)
content_frame.pack(side="right", fill="both", expand=True)

card = tk.Frame(content_frame, bg="white", bd=1, relief="solid", padx=20, pady=20)
card.pack(fill="both", expand=True)

lbl_content = tk.Label(card, text="Active View: Overview\n\nWelcome to the Analytics Dashboard!",
                       font=("Arial", 12), bg="white", fg="#2c3e50", justify="center")
lbl_content.pack(expand=True)

root.mainloop()
