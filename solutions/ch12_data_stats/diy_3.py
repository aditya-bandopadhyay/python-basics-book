"""D3: Bootstrap 95% confidence interval for a mean."""
import numpy as np

rng = np.random.default_rng(42)
data = np.array([72, 85, 91, 60, 78, 85, 67, 94, 55, 85, 70, 88, 63, 79, 90])

boot_means = np.empty(10_000)
for i in range(10_000):
    sample = rng.choice(data, size=len(data), replace=True)
    boot_means[i] = sample.mean()

low, high = np.percentile(boot_means, [2.5, 97.5])
print(f"Sample mean: {data.mean():.2f}")
print(f"95% bootstrap CI: [{low:.2f}, {high:.2f}]")
