"""D3: Search box -- highlight every line containing a keyword in yellow."""
import tkinter as tk
from _app import DataExplorerApp


class SearchApp(DataExplorerApp):
    def build_ui(self):
        super().build_ui()
        bar = tk.Frame(self.root, bg="#f4f6f9", padx=10)
        bar.pack(fill="x", before=self.stats_card)
        tk.Label(bar, text="Search:", bg="#f4f6f9").pack(side="left")
        self.ent_search = tk.Entry(bar, width=20)
        self.ent_search.pack(side="left", padx=4)
        self.ent_search.bind("<Return>", lambda e: self.search())
        tk.Button(bar, text="Find", command=self.search).pack(side="left")
        self.txt.tag_config("found", background="yellow")

    def search(self):
        self.txt.tag_remove("found", "1.0", tk.END)
        word = self.ent_search.get().strip().lower()
        if not word:
            return
        lines = self.txt.get("1.0", tk.END).split("\n")
        hits = 0
        for n, line in enumerate(lines, start=1):
            if word in line.lower():
                self.txt.tag_add("found", f"{n}.0", f"{n}.end")
                hits += 1
        self.lbl_status.config(text=f"Status: '{word}' found on {hits} lines")
        first = self.txt.tag_nextrange("found", "1.0")
        if first:
            self.txt.see(first[0])


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x520")
    SearchApp(root)
    root.mainloop()
