# Chapter 14 — Tkinter Basics — Solutions

## Multiple-choice answers

Q1: (b), Q2: (b), Q3: (c), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** Sequential programming executes top-to-bottom and exits. Event-driven programming enters an active loop waiting for user interactions (like keypresses or clicks) to run specific callbacks.
- **S2.** Storing application data directly in UI widgets tightly couples model and view, making code fragile and difficult to maintain.
- **S3.** Call `widget.bind('<Button-1>', callback_func)` to bind the left mouse click to a callback function.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Celsius -> Fahrenheit converter in a 300x150 window. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: To-do list with Add and Remove buttons. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Roll two dice (2d6) and count the rolls. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Three-question quiz: pick a question in the listbox, answer with radio buttons. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 14.1 -- command=say_hello() CALLS the function while the button is being |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 14.2 -- creating a widget does not show it; it must be placed with a |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 14.3 -- the label shows fixed text; it is not connected to the StringVar. |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 14.4 -- geometry strings are 'WIDTHxHEIGHT' in pixels with no units: |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 14.5 -- after() schedules ONE call. To repeat, tick() must schedule the |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 14: Unit converter GUI (km/miles, kg/lb, C/F) with error handling. |
