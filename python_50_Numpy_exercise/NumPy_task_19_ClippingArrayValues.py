
# Example 19: NumPy - Clipping Array Values
import numpy as np

# Creating an array
array = np.array([5, 2, 4, 1, 9])

# Clipping values to be between 2 and 4
clipped_array = np.clip(array, 2, 4)

print('Original Array:', array)
print('Clipped Array:', clipped_array)
