# Scientific Arrays with NumPy -- Worked Example 7.3: Linear Algebra - Electrical Circuit Mesh Solver
# (book source: ch07_arrays_numpy.tex, line 690)

import numpy as np

# Resistance matrix A (Ohms) and Voltage vector v (Volts)
A = np.array([
    [12.0, -4.0,  0.0],
    [-4.0, 15.0, -5.0],
    [ 0.0, -5.0, 10.0]
])
v = np.array([24.0, 0.0, 0.0])
print(f"[DEBUG] Matrix A shape: {A.shape}, det(A): {np.linalg.det(A):.2f}")

# Step 1: Solve for currents i = A^(-1) * v
i = np.linalg.solve(A, v)
print(f"[DEBUG] Solved loop current vector i: {i}")

# Step 2: Compute residual error vector and 2-norm
residual = np.dot(A, i) - v
residual_norm = np.linalg.norm(residual)
print(f"[DEBUG] Computed residual norm ||A*i - v||: {residual_norm:.2e}")

print(f"Mesh Current i1: {i[0]:.4f} A")
print(f"Mesh Current i2: {i[1]:.4f} A")
print(f"Mesh Current i3: {i[2]:.4f} A")
print(f"Residual Norm:   {residual_norm:.2e}")

# Output:
# [DEBUG] Matrix A shape: (3, 3), det(A): 1340.00
# [DEBUG] Solved loop current vector i: [2.23880597 0.71641791 0.35820896]
# [DEBUG] Computed residual norm ||A*i - v||: 3.62e-15
# Mesh Current i1: 2.2388 A
# Mesh Current i2: 0.7164 A
# Mesh Current i3: 0.3582 A
# Residual Norm:   3.62e-15
# (The residual's last digits may differ slightly on your computer.)
