# Layouts and User Experience -- Code 15.4: Lucky Lotto Ticket Generator App with Trophy Asset
# (book source: ch15_layouts_ux.tex, line 205)

import tkinter as tk
import random
import time

def generate_ticket():
    series_num = random.randint(10, 99)
    series_char = random.choice(['A', 'B', 'C', 'D', 'E', 'H', 'J', 'K', 'L'])
    ticket_num = random.randint(10000, 99999)
    
    ticket_str = f"Series: {series_num}{series_char}   -   Ticket #: {ticket_num}"
    lbl_ticket.config(text=ticket_str)
    
    current_time = time.strftime("%I:%M:%S %p")
    lbl_status.config(text=f"Status: New ticket successfully drawn at {current_time}")

root = tk.Tk()
root.title("Lucky Lotto Ticket Generator")
root.geometry("480x340")
root.configure(bg="#f5f6fa")

# Load Graphic Image Asset (Trophy Icon)
trophy_img = tk.PhotoImage(file="figures/trophy.png")
root.trophy_img = trophy_img  # Store reference to prevent garbage collection!

# Header Banner with Embedded Image Asset
hdr_frame = tk.Frame(root, bg="#8e44ad", pady=6)
hdr_frame.pack(fill="x")

lbl_trophy = tk.Label(hdr_frame, image=trophy_img, bg="#8e44ad")
lbl_trophy.pack(side="left", padx=15)

lbl_title = tk.Label(hdr_frame, text="LUCKY LOTTO TICKET GENERATOR", 
                     font=("Arial", 13, "bold"), bg="#8e44ad", fg="white")
lbl_title.pack(side="left")

# Main Card Frame
card = tk.Frame(root, bg="#ffffff", bd=2, relief="groove", padx=20, pady=15)
card.pack(fill="both", expand=True, padx=20, pady=12)

tk.Label(card, text="YOUR LUCKY DRAW TICKET:", font=("Arial", 9, "bold"), 
         fg="#7f8c8d", bg="#ffffff").pack(anchor="w")

# Display Ticket Label (Expanded width for clean fit)
lbl_ticket = tk.Label(card, text="Series: 84A   -   Ticket #: 49201", font=("Courier", 14, "bold"), 
                      bg="#f1c40f", fg="#2c3e50", padx=12, pady=10, bd=2, relief="solid")
lbl_ticket.pack(fill="x", pady=10)

# Action Button
btn_spin = tk.Button(card, text="GENERATE LUCKY TICKET!", font=("Arial", 11, "bold"), 
                     bg="#27ae60", fg="white", padx=15, pady=6, command=generate_ticket)
btn_spin.pack()

# Bottom Status Bar
lbl_status = tk.Label(root, text="Status: Ready to draw ticket...", bd=1, relief="sunken", 
                      anchor="w", font=("Arial", 9, "italic"), bg="#eaeded", fg="#34495e")
lbl_status.pack(side="bottom", fill="x")

root.mainloop()
