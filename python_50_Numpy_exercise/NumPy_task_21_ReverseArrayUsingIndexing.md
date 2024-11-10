# This example demonstrates how to reverse a NumPy array using slicing.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Reversing the array using slicing
reversed_array = array[::-1]

print('Reversed Array:', reversed_array)

# Explanation:
array[::-1]: Uses slicing with a step of -1 to reverse the order of elements in the array.

# Output:
Prints the array in reversed order.