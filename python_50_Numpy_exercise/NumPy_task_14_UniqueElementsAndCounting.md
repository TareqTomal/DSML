# This example demonstrates how to find unique elements in a NumPy array and count their occurrences.

import numpy as np

# Creating an array with duplicate values
array = np.array([1, 2, 2, 3, 4, 4, 4, 5])

# Finding unique elements and their counts
unique_elements, counts = np.unique(array, return_counts=True)

print('Unique Elements:', unique_elements)
print('Counts of Unique Elements:', counts)

# Explanation:
np.unique(array, return_counts=True): Returns the unique elements in the array and the number of times each element appears.
unique_elements: An array of unique values.
counts: An array of counts corresponding to each unique value.

# Output:

Displays the unique elements and their respective counts:
Unique Elements: [1, 2, 3, 4, 5]
Counts of Unique Elements: [1, 2, 1, 3, 1]
