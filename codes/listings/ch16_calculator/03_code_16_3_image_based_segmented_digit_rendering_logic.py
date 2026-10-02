# Building a Logarithm & Antilogarithm Calculator -- Code 16.3: Image-based segmented digit rendering logic
# (book source: ch16_calculator.tex, line 261)

DIGIT_IMAGES = {}   # filled in after the root window exists

def load_digit_images(folder="digits"):
    """Map each character to its seven-segment PhotoImage."""
    names = {str(d): f"segment_{d}" for d in range(10)}
    names["."] = "segment_dot"
    names["-"] = "segment_minus"
    for char, name in names.items():
        DIGIT_IMAGES[char] = tk.PhotoImage(file=f"{folder}/{name}.png")

# root = tk.Tk()
# load_digit_images()     # only now can images be created

def update_lcd_image_display(display_frame, number_str):
    # Clear existing digit image labels
    for widget in display_frame.winfo_children():
        widget.destroy()
        
    # Dynamically render image labels for each character in result
    for char in number_str:
        if char in DIGIT_IMAGES:
            lbl_img = tk.Label(display_frame, image=DIGIT_IMAGES[char], bg="#101820", bd=0)
            lbl_img.pack(side="left")
        else:
            # Fallback for unrecognized symbols
            lbl_txt = tk.Label(display_frame, text=char, font=("Consolas", 20), fg="#00ffcc", bg="#101820")
            lbl_txt.pack(side="left")
