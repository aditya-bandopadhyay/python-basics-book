"""Bug 12.5 -- axis=1 works ALONG each row (one result per row).
To get one result per column, work down the rows: axis=0.
"""
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]])
q75 = np.percentile(data, 75, axis=0)
print(q75)   # Output: [3.25 4.25 5.25]
