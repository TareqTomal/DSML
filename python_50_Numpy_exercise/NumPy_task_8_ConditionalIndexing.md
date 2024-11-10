# Example 8: NumPy - Conditional Indexing
import numpy as np

# Creating an array
array = np.array([10, 21, 30, 45, 57, 60])

# Setting elements that satisfy a condition
# array[array % 5 == 0] = -1: Sets elements divisible by 5 to -1.
# This operation uses conditional indexing to modify only those elements.

array[array % 5 == 0] = -1

print('Array after Conditional Indexing:', array)
# Output: Array after Conditional Indexing: [-1 21 -1 -1 57 -1]

# Explanation:

    Conditional Indexing: The condition array % 5 == 0 identifies elements in array that are divisible by 5.
    Setting Values: The code sets all elements that meet this condition to -1.
