# Visualizing Data with Matplotlib -- Code 8.1: A basic line plot
# (book source: ch08_matplotlib.tex, line 141)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='steelblue', linewidth=2, label='sin(x)')
ax.set_xlabel('x (radians)')
ax.set_ylabel('Amplitude')
ax.set_title('Sine Wave')
ax.legend()
fig.savefig('sine_wave.pdf', bbox_inches='tight')
plt.show()
