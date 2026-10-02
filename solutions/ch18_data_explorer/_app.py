"""Helper: import the chapter's app (Code 18.3) from codes/ch18_data_explorer.py."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "codes"))
from ch18_data_explorer import DataExplorerApp   # noqa: E402,F401


def column_numbers(rows, col_idx):
    """Numeric values of one column (header row skipped, bad cells ignored)."""
    out = []
    for row in rows[1:]:
        if len(row) > col_idx:
            try:
                out.append(float(row[col_idx]))
            except ValueError:
                pass
    return out
