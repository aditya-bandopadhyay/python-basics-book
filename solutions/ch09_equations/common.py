"""Root-finding helpers shared by the Chapter 9 solutions (Codes 9.1 and 9.2)."""

def bisect(f, a, b, tol=1e-10, max_iter=200, verbose=False):
    """Find a root of f in [a, b] by bisection. Returns (root, number_of_steps)."""
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for k in range(1, max_iter + 1):
        m = (a + b) / 2
        if verbose:
            print(f"step {k:2d}: a = {a:.6f}, b = {b:.6f}, m = {m:.6f}, f(m) = {f(m):+.3e}")
        if f(m) == 0 or (b - a) / 2 < tol:
            return m, k
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2, max_iter


def newton(f, df, x0, tol=1e-12, max_iter=50):
    """Newton-Raphson. Returns (root, number_of_steps)."""
    x = float(x0)
    for k in range(1, max_iter + 1):
        step = f(x) / df(x)
        x -= step
        if abs(step) < tol:
            return x, k
    return x, max_iter
