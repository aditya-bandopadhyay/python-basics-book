"""D4: Bisection with a verbose=True option (see common.bisect)."""
from common import bisect

root, steps = bisect(lambda x: x ** 3 - x - 2, 1, 2, tol=1e-4, verbose=True)
print(f"Root = {root:.6f} after {steps} steps")
