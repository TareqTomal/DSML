# This example demonstrates how to reshape a 1D NumPy array into a 2D array with specified dimensions.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Reshaping to different dimensions
reshaped_array = array.reshape((2, 3))

print('Original Array:', array)
print('Reshaped Array:\n', reshaped_array)

# Explanation:
    array.reshape((2, 3)): Reshapes the original 1D array of 6 elements into a 2D array with 2 rows and 3 columns.

# Output:
    Displays the original 1D array and the reshaped 2D array.
