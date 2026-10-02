"""D4: Three-question quiz: pick a question in the listbox, answer with radio buttons."""
import tkinter as tk

QUESTIONS = [
    ("What does range(5) start at?", ["1", "0", "5"], "0"),
    ("Which keyword leaves a loop at once?", ["continue", "break", "pass"], "break"),
    ("What does 7 // 2 give?", ["3.5", "3", "4"], "3"),
]

root = tk.Tk()
root.title("Python Quiz")
answers = [tk.StringVar(value="") for _ in QUESTIONS]

listbox = tk.Listbox(root, height=3, width=45, exportselection=False)
for i, (q, _, _) in enumerate(QUESTIONS, 1):
    listbox.insert(tk.END, f"Q{i}. {q}")
listbox.pack(padx=10, pady=10)

options_frame = tk.Frame(root)
options_frame.pack(padx=10, anchor="w")

def show_options(event=None):
    for w in options_frame.winfo_children():
        w.destroy()
    sel = listbox.curselection()
    if not sel:
        return
    i = sel[0]
    question, options, _ = QUESTIONS[i]
    tk.Label(options_frame, text=question, font=("Arial", 10, "bold")).pack(anchor="w")
    for opt in options:
        tk.Radiobutton(options_frame, text=opt, value=opt, variable=answers[i]).pack(anchor="w")

def check_score():
    score = sum(1 for (q, o, correct), var in zip(QUESTIONS, answers) if var.get() == correct)
    result.config(text=f"Score: {score} / {len(QUESTIONS)}")

listbox.bind("<<ListboxSelect>>", show_options)
listbox.selection_set(0)
show_options()
tk.Button(root, text="Check score", command=check_score).pack(pady=8)
result = tk.Label(root, text="", font=("Arial", 12, "bold"))
result.pack(pady=(0, 10))
root.mainloop()
