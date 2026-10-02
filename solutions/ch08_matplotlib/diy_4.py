"""D4: Dual-axis chart of temperature and pressure with ax.twinx()."""
import numpy as np
import matplotlib.pyplot as plt

hours = np.arange(8, 19)
temperature = np.array([21.5, 23.2, 25.8, 28.4, 30.1, 31.2, 30.8, 29.5, 27.9, 25.4, 23.8])
pressure = np.array([1013, 1014, 1012, 1011, 1009, 1008, 1009, 1010, 1012, 1014, 1015])

fig, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(hours, temperature, "o-", color="tab:red")
ax1.set_xlabel("Hour of day")
ax1.set_ylabel("Temperature (deg C)", color="tab:red")
ax1.tick_params(axis="y", labelcolor="tab:red")

ax2 = ax1.twinx()                      # second y-axis sharing the same x-axis
ax2.plot(hours, pressure, "s--", color="tab:blue")
ax2.set_ylabel("Pressure (hPa)", color="tab:blue")
ax2.tick_params(axis="y", labelcolor="tab:blue")

ax1.set_title("Temperature and pressure through the day")
fig.tight_layout()
fig.savefig("dual_axis.png", dpi=150)
plt.show()
