"""D1: sin^2 + cos^2 = 1 on 50 points from 0 to 2*pi."""
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
identity = np.sin(x) ** 2 + np.cos(x) ** 2
print("All close to 1?", np.allclose(identity, 1.0))
print("Largest deviation from 1:", np.max(np.abs(identity - 1)))
