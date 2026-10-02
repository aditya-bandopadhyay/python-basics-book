# Chapter 16 — Building a Logarithm & Antilogarithm Calculator — Solutions

## Multiple-choice answers

Q1: (b), Q2: (a), Q3: (b), Q4: (a), Q5: (a).

## Short-answer hints

- **S1.** Homework function buttons (`log10`, `ln`, `10^x`, `e^x`) occupy Row 0, while numeric digit keys and standard operators are arranged systematically across Rows 1–5.
- **S2.** Domain boundaries cause Python math functions to raise a `ValueError`. Trapping these inside `try-except` blocks prevents crashes and displays error dialogs via `messagebox.showerror()`.
- **S3.** Base-10 antilogarithms are computed using `10 ** x`, while natural antilogarithms are computed using `math.exp(x)`.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Add a log2 button to the Chapter 16 calculator. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Keep the last 5 results and show them from Edit > History. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Keyboard support: digits/operators type into the display, Enter evaluates. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: A 1/x (reciprocal) button with a check for zero. |
| Debugging Bugs 1–5 | [`bugs_fixed.py`](bugs_fixed.py) | Bugs 16.1-16.5, fixed. Each fix is a corrected method of the Chapter 16 app. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 16: Expanded scientific logarithm calculator. |

Helper module(s) used by the solutions above: `_app.py`.
