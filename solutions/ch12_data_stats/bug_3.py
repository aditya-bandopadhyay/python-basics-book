"""Bug 12.3 -- np.var is the variance; the standard deviation is its square root."""
import numpy as np
data = [2, 4, 4, 4, 5, 5, 7, 9]
std = np.std(data)
print(std)   # Output: 2.0
