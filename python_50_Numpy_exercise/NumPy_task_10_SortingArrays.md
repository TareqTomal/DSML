# This example demonstrates how to sort a NumPy array in ascending order.

import numpy as np

# Creating an array
array = np.array([3, 1, 2, 5, 4])

# Sorting the array
sorted_array = np.sort(array)

print('Original Array:', array)
print('Sorted Array:', sorted_array)

# Explanation:
    np.sort(array): Creates a sorted copy of the array in ascending order without modifying the original array.

# Output:
    Displays the original array and a sorted version of the array, resulting in [1, 2, 3, 4, 5] for the sorted array.