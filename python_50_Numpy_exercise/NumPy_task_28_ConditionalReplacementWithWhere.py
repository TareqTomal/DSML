
# Example 28: NumPy - Conditional Replacement with np.where
import numpy as np

# Creating an array
array = np.array([31, 15, 12, 25, 30, 37, 43, 17, 67])

# Replacing values based on condition
result = np.where(array > 30, 0, array)

print('Array with Values Greater Than 20 Replaced with 0:', result)
