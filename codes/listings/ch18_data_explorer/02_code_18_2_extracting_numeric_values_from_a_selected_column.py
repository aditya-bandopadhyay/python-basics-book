# Building a CSV Data Explorer Dashboard -- Code 18.2: Extracting numeric values from a selected column
# (book source: ch18_data_explorer.tex, line 105)

def extract_column_data(rows, col_index):
    numbers = []
    # Skip header row (rows[0])
    for row in rows[1:]:
        if len(row) > col_index:
            try:
                val = float(row[col_index])
                numbers.append(val)
            except ValueError:
                continue # Skip non-numeric values or missing entries
    return numbers
