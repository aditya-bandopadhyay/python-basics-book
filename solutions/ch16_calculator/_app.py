"""Helper: import the chapter's calculator from codes/ch16_calculator.py."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "codes"))
from ch16_calculator import LogCalculatorApp   # noqa: E402,F401
