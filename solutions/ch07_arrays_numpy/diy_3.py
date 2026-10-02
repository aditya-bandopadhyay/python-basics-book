"""D3: k-point running mean, with a loop and with np.convolve."""
import numpy as np

def running_mean(arr, k):
    """Mean of arr[i:i+k] for every starting position i."""
    arr = np.asarray(arr, dtype=float)
    out = np.zeros(len(arr) - k + 1)
    for i in range(len(out)):
        out[i] = np.mean(arr[i:i + k])
    return out

def running_mean_fast(arr, k):
    return np.convolve(arr, np.ones(k) / k, mode="valid")

data = np.array([2, 4, 6, 8, 10, 12, 14])
print(running_mean(data, 3))        # Output: [ 4.  6.  8. 10. 12.]
print(running_mean_fast(data, 3))   # Output: [ 4.  6.  8. 10. 12.]
