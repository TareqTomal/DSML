# how to flatten a multi-dimensional array in NumPy:

# Example 26: NumPy - Flattening a Multi-dimensional Array
import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Flattening the array
# array_2d.flatten(): Converts the 2D array `array_2d` into a 1D array by flattening all elements along a single axis.
# This method returns a copy of the original array in a 1D format.

flattened_array = array_2d.flatten()

print('Flattened Array:', flattened_array)
# Output: Flattened Array: [1 2 3 4 5 6]
