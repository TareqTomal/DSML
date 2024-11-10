# This example demonstrates how to transpose a 2D NumPy array, which switches its rows and columns.


import numpy as np

# Creating a 2D array
array = np.array([[1, 2], [3, 4]])

# Transposing the array
transposed_array = np.transpose(array)

print('Original Array:\n', array)
print('Transposed Array:\n', transposed_array)

# Explanation:

np.transpose(array): Transposes the array, swapping rows and columns. The first row becomes the first column, the second row becomes the second column, and so on.