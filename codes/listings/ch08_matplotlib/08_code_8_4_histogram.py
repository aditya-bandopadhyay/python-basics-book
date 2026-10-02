# Visualizing Data with Matplotlib -- Code 8.4: Histogram
# (book source: ch08_matplotlib.tex, line 381)

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
data = rng.normal(170, 10, 500)   # heights in cm

fig, ax = plt.subplots()
ax.hist(data, bins=20, color='mediumseagreen', edgecolor='white',
        density=True)
ax.set_xlabel('Height (cm)')
ax.set_ylabel('Probability density')
ax.set_title('Distribution of Heights (n=500)')
fig.savefig('histogram.pdf', bbox_inches='tight')
plt.show()
