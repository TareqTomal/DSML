# This example demonstrates how to split a NumPy array into multiple parts.


import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Splitting the array into three parts
split_arrays = np.array_split(array, 3)

print('Split Arrays:', split_arrays)

# Explanation:
    np.array_split(array, 3): Splits the original array into three equal parts. If the array length is not perfectly divisible, the last part will contain fewer elements.

# Output:
Displays the array split into three parts, resulting in [array([1, 2]), array([3, 4]), array([5, 6])].
