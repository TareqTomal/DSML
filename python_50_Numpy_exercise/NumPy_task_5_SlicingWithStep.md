# This example demonstrates how to slice a NumPy array with a specified step size.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slicing with a step
step_slice = array[::2]  # Every second element

print('Sliced Array with Step 2:', step_slice)

# Explanation:
    array[::2]: Uses slicing with a step of 2 to select every second element from the array, starting from the first element.

# Output:
    Prints the array with every second element, resulting in [1, 3, 5, 7, 9].
