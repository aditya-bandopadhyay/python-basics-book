"""Mini-Project 8: Climate dashboard (monthly normals for Kolkata, approximate)."""
import numpy as np
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rainfall_mm = np.array([11, 23, 31, 55, 128, 300, 375, 340, 320, 160, 28, 6])
temp_c = np.array([20.0, 23.0, 27.5, 30.5, 31.0, 30.5, 29.5, 29.5, 29.5, 28.0, 24.5, 20.5])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)

ax1.bar(months, rainfall_mm, color="steelblue", edgecolor="white")
ax1.set_ylabel("Rainfall (mm)")
ax1.set_ylim(0, 400)
ax1.set_title("Monthly rainfall")
ax1.grid(True, axis="y", linestyle=":")

ax2.plot(months, temp_c, "o-", color="crimson")
ax2.fill_between(months, temp_c, temp_c.min() - 2, color="crimson", alpha=0.2)
ax2.set_ylabel("Mean temperature (deg C)")
ax2.set_ylim(15, 35)
ax2.set_title("Monthly mean temperature")
ax2.set_xlabel("Month")
ax2.grid(True, linestyle=":")

fig.suptitle("Kolkata climate at a glance (approximate monthly normals)", fontsize=13)
fig.text(0.5, 0.005, "Most rain falls in the June-September monsoon; May is the hottest month.",
         ha="center", fontsize=9, style="italic")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig("climate_dashboard.pdf")
plt.show()
