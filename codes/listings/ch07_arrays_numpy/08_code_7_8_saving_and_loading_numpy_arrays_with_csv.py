# Scientific Arrays with NumPy -- Code 7.8: Saving and loading NumPy arrays with CSV
# (book source: ch07_arrays_numpy.tex, line 447)

import numpy as np

# 1. Create a 2D array of sensor data (Time, Temp, Pressure)
data = np.array([
    [1.0, 23.4, 101.3],
    [2.0, 24.1, 101.5],
    [3.0, 23.8, 101.2]
])

# 2. Save array to a CSV file with a header row
np.savetxt("sensor_log.csv", data, delimiter=",", 
           fmt="%.2f", header="Time(s),Temp(C),Pressure(kPa)")

# 3. Load array back from the CSV file into Python
loaded_data = np.loadtxt("sensor_log.csv", delimiter=",", skiprows=1)
print("Loaded Array Shape:", loaded_data.shape)
print("Loaded Data:\n", loaded_data)
