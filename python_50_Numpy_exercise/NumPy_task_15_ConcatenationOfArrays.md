# how to concatenate arrays in NumPy:

# Example 15: NumPy - Concatenation of Arrays
import numpy as np

# Creating arrays
array1 = np.array([11, 52, 33])
array2 = np.array([47, 15, 86])

# Concatenating arrays
# np.concatenate((array1, array2)) combines array1 and array2 into a single array along the specified axis.
# By default, axis=0 for 1D arrays, resulting in a single array with elements of both array1 and array2 in sequence.

concatenated_array = np.concatenate((array1, array2))

print('Concatenated Array:', concatenated_array)
# Output: Concatenated Array: [11 52 33 47 15 86]

# Explanation:

np.concatenate Function: Combines multiple arrays along a specified axis. For 1D arrays, it appends elements sequentially, creating a single array that includes elements from both array1 and array2.


