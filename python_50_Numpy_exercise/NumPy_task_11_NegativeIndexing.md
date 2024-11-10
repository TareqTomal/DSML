# This example demonstrates accessing elements from the end of a NumPy array using negative indices.

import numpy as np

# Creating an array
array = np.array([100, 200, 300, 70, 20])

# Accessing elements from the end using negative indices
last_element = array[-1]
second_last_element = array[-2]

print('Last Element:', last_element)
print('Second Last Element:', second_last_element)

# Explanation:
    array[-1]: Accesses the last element of the array.
    array[-2]: Accesses the second-to-last element of the array.

# Output:
    Prints the last and second-to-last elements of the array.
