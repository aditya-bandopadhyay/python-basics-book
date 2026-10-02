# Chapter 17 — Building an ODE Solver Visualizer — Solutions

## Multiple-choice answers

Q1: (b), Q2: (b), Q3: (c), Q4: (b), Q5: (a).

## Short-answer hints

- **S1.** Pass `Figure` to `FigureCanvasTkAgg(fig, master=frame)`, call `canvas.get_tk_widget().pack()`, and call `canvas.draw()` to refresh.
- **S2.** Validation prevents invalid parameters (like negative step size $h 0$) from causing infinite loops or math domain errors.
- **S3.** Storing Entry references as instance variables (`self.ent_h`) allows callback methods to access user values anytime.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Choose the model from a tk.OptionMenu: decay, logistic, or harmonic motion. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: An Entry for the rate constant k in y' = -k y. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: An "Export Plot" button that saves the figure wherever the user chooses. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Overlay the exact solution y0 * exp(-0.3 t) on the RK4 curve. |
| Debugging Bugs 1–5 | [`bugs_fixed.py`](bugs_fixed.py) | Bugs 17.1-17.5, fixed, as a working variant of the Chapter 17 app. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 17: Lotka-Volterra predator-prey explorer. |

Helper module(s) used by the solutions above: `_app.py`.
