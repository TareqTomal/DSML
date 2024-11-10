# This example demonstrates the use of NumPy's trigonometric functions to calculate the sine, cosine, and tangent of angles.

import numpy as np

# Creating an array
angles = np.array([0, np.pi/2, np.pi])

# Trigonometric functions
sin_array = np.sin(angles)
cos_array = np.cos(angles)
tan_array = np.tan(angles)

print('Sine of Angles:', sin_array)
print('Cosine of Angles:', cos_array)
print('Tangent of Angles:', tan_array)

# Explanation:
np.sin(angles): Calculates the sine of each angle in the array.
np.cos(angles): Calculates the cosine of each angle in the array.
np.tan(angles): Calculates the tangent of each angle in the array.

# Angles:
The array contains angles in radians: [0, π/2, π].

# Output:
Displays the sine, cosine, and tangent values for each angle:
    Sine of Angles: [0.0, 1.0, 0.0]
    Cosine of Angles: [1.0, 0.0, -1.0]
    Tangent of Angles: [0.0, large number (undefined), 0.0] (note: tan(π/2) is theoretically undefined and results in a very large number in practice).
