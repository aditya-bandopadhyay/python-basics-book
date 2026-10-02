"""D4: Benchmark a Python loop against np.sum on a million numbers."""
import random
import time
import numpy as np

values = [random.random() for _ in range(1_000_000)]
arr = np.array(values)

start = time.time()
total = 0.0
for v in values:
    total += v
loop_time = time.time() - start

start = time.time()
np_total = np.sum(arr)
numpy_time = time.time() - start

print(f"Loop sum:  {total:.4f} in {loop_time * 1000:.1f} ms")
print(f"NumPy sum: {np_total:.4f} in {numpy_time * 1000:.2f} ms")
print(f"Speed-up:  about {loop_time / numpy_time:.0f}x")
# Timings vary from computer to computer; NumPy is typically tens of times faster.
