# This example demonstrates how to modify specific elements in a NumPy array using indexing.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Setting specific values using indexing
array[[1, 3]] = [100, 200]

print('Array after Setting Values:', array)

# Explanation:
    array[[1, 3]] = [100, 200]: Sets the element at index 1 to 100 and the element at index 3 to 200. This is done by providing an index list [1, 3] and a list of corresponding values [100, 200].

# Output:
Displays the array after modifying specific values, resulting in [1, 100, 3, 200, 5].