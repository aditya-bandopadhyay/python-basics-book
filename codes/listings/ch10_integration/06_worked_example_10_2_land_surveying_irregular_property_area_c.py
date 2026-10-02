# Numerical Integration and Centroids -- Worked Example 10.2: Land Surveying - Irregular Property Area & Centroid Location
# (book source: ch10_integration.tex, line 316)

import numpy as np
from scipy.integrate import trapezoid

# Surveyor field measurements along riverbank (meters)
x_survey = np.array([0, 5, 10, 15, 20, 25, 30])
y_survey = np.array([4.2, 6.8, 8.1, 7.5, 5.9, 3.0, 0.0])

# 1. Total Land Area: Integral of y dx
land_area = trapezoid(y_survey, x_survey)

# 2. First Moment of Area: Integral of x * y dx
first_moment_x = trapezoid(x_survey * y_survey, x_survey)

# 3. Centroid x-coordinate: First Moment / Area
x_centroid = first_moment_x / land_area

print(f"Total Property Land Area: {land_area:.2f} m^2")
print(f"Centroid x-coordinate:    {x_centroid:.2f} meters")

# Output:
# Total Property Land Area: 167.00 m^2
# Centroid x-coordinate:    12.59 meters
