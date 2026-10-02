# Solving Nonlinear Equations -- Worked Example 9.2: Newton-Raphson Method & Quadratic Convergence
# (book source: ch09_equations.tex, line 406)

import numpy as np

def newton_raphson(f, df, x0, tol=1e-10, max_iter=20):
    x = float(x0)
    print(f"{'k':<3} | {'x_k':<12} | {'f(x_k)':<12} | {'Correction dx':<12}")
    print("-" * 46)
    
    for k in range(max_iter):
        fx = f(x)
        dfx = df(x)
        dx = fx / dfx
        
        print(f"{k:<3} | {x:<12.8f} | {fx:<12.4e} | {dx:<12.4e}")
        
        if abs(fx) < tol:
            return x, k            # k updates were needed
            
        x -= dx
        
    return x, max_iter

# f(x) = cos(x) - x, f'(x) = -sin(x) - 1
f = lambda x: np.cos(x) - x
df = lambda x: -np.sin(x) - 1.0

root, steps = newton_raphson(f, df, x0=0.5)
print(f"\nNewton-Raphson Root: x = {root:.10f} in {steps} iterations.")

# Output:
# k   | x_k          | f(x_k)       | Correction dx
# ----------------------------------------------
# 0   | 0.50000000   | 3.7758e-01   | -2.5522e-01
# 1   | 0.75522242   | -2.7103e-02  | 1.6081e-02
# 2   | 0.73914167   | -9.4615e-05  | 5.6532e-05
# 3   | 0.73908513   | -1.1810e-09  | 7.0565e-10
# 4   | 0.73908513   | 0.0000e+00   | -0.0000e+00
# 
# Newton-Raphson Root: x = 0.7390851332 in 4 iterations.
