# Chapter 15 — Layouts and User Experience — Solutions

## Multiple-choice answers

Q1: (a), Q2: (a), Q3: (b), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** Visual hierarchy organizes information using font sizes, weight, spacing, and color contrast.
- **S2.** External padding (`padx`/`pady`) adds space outside a widget. Internal padding (`ipadx`/`ipady`) adds space inside a widget.
- **S3.** Use `columnspan=3` when placing a widget via `.grid()`.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Contact form laid out with grid(). |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Responsive dashboard: header, fixed-width sidebar, expanding content. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Centred login window. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: A menu bar with File, Edit and Help menus. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 15.1 -- both widgets were placed in the same cell (row 0, column 0), so the |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 15.2 -- pack() with no options keeps the frame at its natural size. |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 15.3 -- pack and grid cannot both manage widgets in the same container |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 15.4 -- sticky='ew' lets the entry fill its cell, but the column itself |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 15.5 -- a scrollbar and a listbox must be linked both ways: |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 15: Survey and feedback form. |
