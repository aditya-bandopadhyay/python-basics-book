# Chapter 18 — Building a CSV Data Explorer Dashboard — Solutions

## Multiple-choice answers

Q1: (b), Q2: (b), Q3: (a), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** Connect text widget to scrollbar using `yscrollcommand=scrollbar.set` and link scrollbar command using `scrollbar.config(command=txt.yview)`.
- **S2.** Tkinter Text widgets use `"line.column"` indexing strings, where `"1.0"` represents line 1, character 0.
- **S3.** Read CSV rows with `csv.reader()`, display text in the text view, and convert numeric columns into a NumPy array to calculate mean and median.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Threshold filter -- highlight rows whose selected column exceeds a value. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Export the statistics of the selected column to a text file. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Search box -- highlight every line containing a keyword in yellow. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: A box-plot button next to the histogram. |
| Debugging Bugs 1–5 | [`bugs_fixed.py`](bugs_fixed.py) | Bugs 18.1-18.5, fixed, in one small working program. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 18: Multi-file CSV workbench with tabs. |

Helper module(s) used by the solutions above: `_app.py`.
