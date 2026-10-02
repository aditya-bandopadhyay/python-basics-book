"""Bug 9.3 -- the updates are swapped.

For f(a) < 0 < f(b): if f(m) > 0 the root is to the LEFT of m, so b = m.
Tracing f(x) = x - 1 on [0, 2] with the buggy code: m = 1, f(1) = 0 -> b = 1;
m = 0.5, f(0.5) < 0 -> b = 0.5; ... it slides towards 0 instead of 1.
"""
def bisect_fixed(f, a, b, tol=1e-6):
    while (b - a) > tol:
        m = (a + b) / 2
        if f(m) > 0:
            b = m
        else:
            a = m
    return (a + b) / 2

print(round(bisect_fixed(lambda x: x - 1, 0, 2), 6))   # Output: 1.0
