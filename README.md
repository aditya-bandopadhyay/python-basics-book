# Python by Curiosity — companion code

Companion repository for the textbook **Python by Curiosity: From First Loops to Scientific
Modeling and Interactive Apps** by Aditya Bandopadhyay (IIT Kharagpur) and Subhasree Pradhan
(Jhargram Raj College).

Everything here is generated from the book itself, so the code matches the printed listings.

| Folder | What is in it |
| --- | --- |
| [`codes/`](codes/) | One script per chapter. Chapters 1–13: all of the chapter's listings in book order. Chapters 14–19: the chapter's main desktop app. |
| [`codes/listings/`](codes/listings/) | Every listing in the book as its own file, numbered in book order (e.g. `codes/listings/ch02_numbers/04_code_2_1_creating_and_printing_variables.py`). |
| [`notebooks/`](notebooks/) | One Jupyter notebook per chapter, one code cell per listing. Chapters 1–13 are saved with their outputs and plots. |
| [`solutions/`](solutions/) | Tested solutions to every DIY task, debugging task and mini-project, plus MCQ answers and short-answer hints. |
| [`data/`](data/) | Data files used in the book (Chapters 7, 8, 10, 12 and 18). |
| [`figures/`](figures/) | Images used by the programs (e.g. `trophy.png`) and screenshots of the apps. |

## Getting started

```bash
git clone https://github.com/aditya-bandopadhyay/python-basics-book.git
cd python-basics-book
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Tkinter (Part III) comes with Python on Windows and macOS. On Debian/Ubuntu install it with
`sudo apt install python3-tk`.

**Run everything from the repository root**, so that paths such as `data/grades.csv` work:

```bash
python codes/ch02_numbers.py                                   # a whole chapter
python codes/listings/ch11_odes/03_code_11_3_rk4_solver_from_scratch.py   # one listing
python codes/ch16_calculator.py                                # a desktop app
python solutions/ch09_equations/mini_project.py                # a solution
jupyter lab notebooks/                                          # the notebooks
```

A few listings are fragments or deliberate mistakes shown in the book (for example
`if score = 100:`); their files say so in a `NOTE` comment, and the chapter scripts skip them.
Listings that read keyboard input are skipped by the chapter scripts too but can be run on
their own. Some listings save figures (e.g. `sine_wave.pdf`) into the folder you run them from.

## Chapters

| Ch | Title | Script | Listings | Notebook | Solutions | Highlights |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Why Computers Follow Rules | [`ch01_why_computers.py`](codes/ch01_why_computers.py) | [4 listings](codes/listings/ch01_why_computers/) | [notebook](notebooks/ch01_why_computers.ipynb) | [solutions](solutions/ch01_why_computers/) | Cooking-assistant algorithm; the Mars Climate Orbiter unit mix-up |
| 2 | Playing with Numbers | [`ch02_numbers.py`](codes/ch02_numbers.py) | [13 listings](codes/listings/ch02_numbers/) | [notebook](notebooks/ch02_numbers.ipynb) | [solutions](solutions/ch02_numbers/) | Floating-point arithmetic, f-strings; the Patriot clock-drift simulation |
| 3 | Making Decisions | [`ch03_decisions.py`](codes/ch03_decisions.py) | [10 listings](codes/listings/ch03_decisions/) | [notebook](notebooks/ch03_decisions.ipynb) | [solutions](solutions/ch03_decisions/) | if/elif/else, Boolean logic; Petrov's false alarm |
| 4 | Loops and Repetition | [`ch04_loops.py`](codes/ch04_loops.py) | [11 listings](codes/listings/ch04_loops/) | [notebook](notebooks/ch04_loops.ipynb) | [solutions](solutions/ch04_loops/) | for/while loops, AP and GP series; Tower of Hanoi move counts |
| 5 | Lists, Tuples, Sets, and Dictionaries | [`ch05_lists.py`](codes/ch05_lists.py) | [14 listings](codes/listings/ch05_lists/) | [notebook](notebooks/ch05_lists.ipynb) | [solutions](solutions/ch05_lists/) | Lists, dictionaries, strings; class report card |
| 6 | Functions and Code Reuse | [`ch06_functions.py`](codes/ch06_functions.py) | [17 listings](codes/listings/ch06_functions/) | [notebook](notebooks/ch06_functions.ipynb) | [solutions](solutions/ch06_functions/) | Functions, recursion, lambda, exceptions, files; statistics library |
| 7 | Scientific Arrays with NumPy | [`ch07_arrays_numpy.py`](codes/ch07_arrays_numpy.py) | [16 listings](codes/listings/ch07_arrays_numpy/) | [notebook](notebooks/ch07_arrays_numpy.ipynb) | [solutions](solutions/ch07_arrays_numpy/) | NumPy arrays, masks, broadcasting; mesh-current solver, telescope image |
| 8 | Visualizing Data with Matplotlib | [`ch08_matplotlib.py`](codes/ch08_matplotlib.py) | [17 listings](codes/listings/ch08_matplotlib/) | [notebook](notebooks/ch08_matplotlib.ipynb) | [solutions](solutions/ch08_matplotlib/) | Line, scatter, bar, histogram, contour, error-bar plots; Challenger O-ring data |
| 9 | Solving Nonlinear Equations | [`ch09_equations.py`](codes/ch09_equations.py) | [9 listings](codes/listings/ch09_equations/) | [notebook](notebooks/ch09_equations.ipynb) | [solutions](solutions/ch09_equations/) | Bisection, Newton-Raphson, brentq, fsolve; shot-put release angles |
| 10 | Numerical Integration and Centroids | [`ch10_integration.py`](codes/ch10_integration.py) | [8 listings](codes/listings/ch10_integration/) | [notebook](notebooks/ch10_integration.ipynb) | [solutions](solutions/ch10_integration/) | Trapezoid/Simpson rules, centroids, quad/dblquad; telemetry distance, land survey |
| 11 | Ordinary Differential Equations | [`ch11_odes.py`](codes/ch11_odes.py) | [9 listings](codes/listings/ch11_odes/) | [notebook](notebooks/ch11_odes.ipynb) | [solutions](solutions/ch11_odes/) | Euler, RK4, solve_ivp; coffee cooling, RC circuit, SIR epidemic, pendulum |
| 12 | Data Wrangling and Statistics | [`ch12_data_stats.py`](codes/ch12_data_stats.py) | [12 listings](codes/listings/ch12_data_stats/) | [notebook](notebooks/ch12_data_stats.ipynb) | [solutions](solutions/ch12_data_stats/) | Simulation, statistics, correlation, t-test, outliers; placement-salary mystery |
| 13 | Optimization and Curve Fitting | [`ch13_optimization.py`](codes/ch13_optimization.py) | [12 listings](codes/listings/ch13_optimization/) | [notebook](notebooks/ch13_optimization.ipynb) | [solutions](solutions/ch13_optimization/) | Gradient descent, curve_fit, minimize; Fermat's least-time refraction |
| 14 | Tkinter Basics | [`ch14_tkinter_basics.py`](codes/ch14_tkinter_basics.py) | [16 listings](codes/listings/ch14_tkinter_basics/) | [notebook](notebooks/ch14_tkinter_basics.ipynb) | [solutions](solutions/ch14_tkinter_basics/) | Tkinter windows, widgets, events, classes; two-number adder |
| 15 | Layouts and User Experience | [`ch15_layouts_ux.py`](codes/ch15_layouts_ux.py) | [11 listings](codes/listings/ch15_layouts_ux/) | [notebook](notebooks/ch15_layouts_ux.ipynb) | [solutions](solutions/ch15_layouts_ux/) | pack/grid layouts, frames, image studio with edge detection |
| 16 | Building a Logarithm & Antilogarithm Calculator | [`ch16_calculator.py`](codes/ch16_calculator.py) | [5 listings](codes/listings/ch16_calculator/) | [notebook](notebooks/ch16_calculator.ipynb) | [solutions](solutions/ch16_calculator/) | Logarithm & antilogarithm desktop calculator |
| 17 | Building an ODE Solver Visualizer | [`ch17_ode_visualizer.py`](codes/ch17_ode_visualizer.py) | [3 listings](codes/listings/ch17_ode_visualizer/) | [notebook](notebooks/ch17_ode_visualizer.ipynb) | [solutions](solutions/ch17_ode_visualizer/) | ODE solver with an embedded Matplotlib plot |
| 18 | Building a CSV Data Explorer Dashboard | [`ch18_data_explorer.py`](codes/ch18_data_explorer.py) | [6 listings](codes/listings/ch18_data_explorer/) | [notebook](notebooks/ch18_data_explorer.ipynb) | [solutions](solutions/ch18_data_explorer/) | CSV data explorer with statistics and histograms |
| 19 | Desktop Audio Player and Frequency Visualizer | [`ch19_music_player.py`](codes/ch19_music_player.py) | [8 listings](codes/listings/ch19_music_player/) | [notebook](notebooks/ch19_music_player.ipynb) | [solutions](solutions/ch19_music_player/) | Music player interface with playlist, scrub bar and visualizer |

## Data files

| File | Used in | Contents |
| --- | --- | --- |
| `data/sensor_log.csv` | Ch 7, Code 7.8 | Time, temperature and pressure: the file that listing writes |
| `data/sensor_log.dat` | Ch 8, Gnuplot example | Time, measured and theoretical displacement of a damped oscillator |
| `data/telemetry_speed.csv` | Ch 10, Worked Example 10.1 | Vehicle speed every 5 s over a 40 s run |
| `data/grades.csv` | Ch 12, Code 12.5 and Mini-Project 12 | 20 students: Maths, Science, English |
| `data/marks.csv` | Ch 12, DIY D4 | 20 students: Maths and Physics (with one outlier) |
| `data/weather_telemetry.csv` | Ch 18 data explorer | Hourly temperature, humidity, pressure and wind speed |

## Citation

If you use these examples in academic coursework or research, please cite the textbook:

```bibtex
@book{bandopadhyay2026python,
  title  = {Python by Curiosity: From First Loops to Scientific Modeling and Interactive Apps},
  author = {Bandopadhyay, Aditya and Pradhan, Subhasree},
  year   = {2026}
}
```
