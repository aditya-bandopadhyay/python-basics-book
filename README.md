# Python by Curiosity: From First Loops to Scientific Modeling and Interactive Apps

**Companion Code Repository, Jupyter Notebooks, and Datasets**

**Authors:**
- **Dr. Aditya Bandopadhyay**, Associate Professor, Department of Mechanical Engineering, Indian Institute of Technology Kharagpur
- **Dr. Subhasree Pradhan**, Assistant Professor, Department of Physics, Jhargram Raj College

---

## Overview

This repository hosts all companion code resources for the textbook **Python by Curiosity**. It contains:
- **`codes/`**: 19 standalone, executable Python scripts (`ch01_why_computers.py` through `ch19_music_player.py`).
- **`notebooks/`**: 19 interactive Jupyter notebooks with step-by-step mathematical formulations, executable code cells, and inline figures.
- **`data/`**: Sample experimental CSV datasets and telemetry sensor logs.
- **`figures/`**: Graphical UI assets (such as `trophy.png` and interface mockups).

---

## Quickstart & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/aditya-bandopadhyay/python-basics-book.git
cd python-basics-book
```

### 2. Create a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate      # On Linux / macOS
# or: .\venv\Scripts\activate # On Windows
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Directory Layout

```
python-basics-book/
├── codes/                      # Standalone Python scripts (.py)
│   ├── ch01_why_computers.py
│   ├── ch02_numbers.py
│   ├── ...
│   └── ch19_music_player.py
├── notebooks/                  # Interactive Jupyter notebooks (.ipynb)
│   ├── ch01_why_computers.ipynb
│   ├── ch02_numbers.ipynb
│   ├── ...
│   └── ch19_music_player.ipynb
├── data/                       # CSV datasets and telemetry logs
│   ├── sensor_log.csv
│   ├── telemetry_speed.csv
│   ├── grades.csv
│   └── weather_telemetry.csv
├── figures/                    # Application image assets
│   └── trophy.png
├── requirements.txt            # Python package dependencies
├── .gitignore                  # Git ignore rules for Python/Jupyter
└── README.md                   # This documentation
```

---

## Master Directory of Chapters & Programs

### Part I: Python Basics

| Chapter | Script | Notebook | Topic / Practical Project |
| :--- | :--- | :--- | :--- |
| **01. Why Computers Follow Rules** | [`ch01_why_computers.py`](codes/ch01_why_computers.py) | [`ch01_why_computers.ipynb`](notebooks/ch01_why_computers.ipynb) | Environment verification & string output |
| **02. Playing with Numbers** | [`ch02_numbers.py`](codes/ch02_numbers.py) | [`ch02_numbers.ipynb`](notebooks/ch02_numbers.ipynb) | Monthly loan installment (EMI) calculator |
| **03. Making Decisions** | [`ch03_decisions.py`](codes/ch03_decisions.py) | [`ch03_decisions.ipynb`](notebooks/ch03_decisions.ipynb) | Automated discount validation & traffic light logic |
| **04. Loops and Repetition** | [`ch04_loops.py`](codes/ch04_loops.py) | [`ch04_loops.ipynb`](notebooks/ch04_loops.ipynb) | Arithmetic & geometric sequence sums |
| **05. Lists, Tuples, Sets & Dicts** | [`ch05_lists.py`](codes/ch05_lists.py) | [`ch05_lists.ipynb`](notebooks/ch05_lists.ipynb) | Examination marks rank & summary analysis |
| **06. Functions and Code Reuse** | [`ch06_functions.py`](codes/ch06_functions.py) | [`ch06_functions.ipynb`](notebooks/ch06_functions.ipynb) | Modular scientific converters & scopes |

### Part II: Scientific Computing & Modeling

| Chapter | Script | Notebook | Topic / Practical Project |
| :--- | :--- | :--- | :--- |
| **07. Scientific Arrays with NumPy** | [`ch07_arrays_numpy.py`](codes/ch07_arrays_numpy.py) | [`ch07_arrays_numpy.ipynb`](notebooks/ch07_arrays_numpy.ipynb) | Numerical differentiation of velocity signals |
| **08. Visualizing Data with Matplotlib** | [`ch08_matplotlib.py`](codes/ch08_matplotlib.py) | [`ch08_matplotlib.ipynb`](notebooks/ch08_matplotlib.ipynb) | Multi-panel figures & Challenger O-ring analysis |
| **09. Solving Nonlinear Equations** | [`ch09_equations.py`](codes/ch09_equations.py) | [`ch09_equations.ipynb`](notebooks/ch09_equations.ipynb) | Bisection, Newton--Raphson & trajectory roots |
| **10. Numerical Integration & Centroids**| [`ch10_integration.py`](codes/ch10_integration.py) | [`ch10_integration.ipynb`](notebooks/ch10_integration.ipynb) | CAN-bus vehicle distance & riverbank centroid |
| **11. Ordinary Differential Equations** | [`ch11_odes.py`](codes/ch11_odes.py) | [`ch11_odes.ipynb`](notebooks/ch11_odes.ipynb) | Euler, RK4 & water tank draining dynamics |
| **12. Data Wrangling and Statistics** | [`ch12_data_stats.py`](codes/ch12_data_stats.py) | [`ch12_data_stats.ipynb`](notebooks/ch12_data_stats.ipynb) | Marble simulation, dice rolls & paired $t$-test |
| **13. Optimization and Curve Fitting** | [`ch13_optimization.py`](codes/ch13_optimization.py) | [`ch13_optimization.ipynb`](notebooks/ch13_optimization.ipynb) | Gradient descent, Hooke's law & Snell's optics |

### Part III: Graphical User Interfaces & Applications

| Chapter | Script | Notebook | Topic / Practical Project |
| :--- | :--- | :--- | :--- |
| **14. Tkinter Basics** | [`ch14_tkinter_basics.py`](codes/ch14_tkinter_basics.py) | [`ch14_tkinter_basics.ipynb`](notebooks/ch14_tkinter_basics.ipynb) | Two-number adder & stateful click counter GUI |
| **15. Layouts and User Experience** | [`ch15_layouts_ux.py`](codes/ch15_layouts_ux.py) | [`ch15_layouts_ux.ipynb`](notebooks/ch15_layouts_ux.ipynb) | Mini Image Studio (edges, sliders, grayscale) |
| **16. Log & Antilog Calculator** | [`ch16_calculator.py`](codes/ch16_calculator.py) | [`ch16_calculator.ipynb`](notebooks/ch16_calculator.ipynb) | Scientific Logarithm/Antilogarithm desktop helper |
| **17. ODE Solver Visualizer** | [`ch17_ode_visualizer.py`](codes/ch17_ode_visualizer.py) | [`ch17_ode_visualizer.ipynb`](notebooks/ch17_ode_visualizer.ipynb) | Interactive RK4 solver with live plot canvas |
| **18. CSV Data Explorer Dashboard** | [`ch18_data_explorer.py`](codes/ch18_data_explorer.py) | [`ch18_data_explorer.ipynb`](notebooks/ch18_data_explorer.ipynb) | Multi-panel CSV table, summary cards & plots |
| **19. Desktop Audio Player** | [`ch19_music_player.py`](codes/ch19_music_player.py) | [`ch19_music_player.ipynb`](notebooks/ch19_music_player.ipynb) | Audio player with live spectrum visualizer |

---

## How to Run

### Running Python Scripts
Navigate to the repository root and run any script directly:
```bash
python codes/ch02_numbers.py
python codes/ch15_layouts_ux.py
python codes/ch16_calculator.py
```

### Launching JupyterLab
To open the interactive notebooks:
```bash
jupyter lab notebooks/
```
In JupyterLab or VS Code, click **Run All Cells** or execute cells sequentially with `Shift + Enter`.

---

## License & Citation

If you use these examples in academic coursework or research, please cite the textbook:

```bibtex
@book{bandopadhyay2026python,
  title     = {Python by Curiosity: From First Loops to Scientific Modeling and Interactive Apps},
  author    = {Bandopadhyay, Aditya and Pradhan, Subhasree},
  year      = {2026}
}
```
