# Example 17: NumPy - Indexing with np.where()
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Using np.where to find indices where elements are greater than 25
# np.where(array > 25): Returns the indices of elements in `array` that satisfy the condition (greater than 25).
# This is useful for finding locations of specific values in the array.

indices = np.where(array > 25)

print('Indices where elements > 25:', indices)
# Output: Indices where elements > 25: (array([2, 3, 4]),)

# Accessing elements at the found indices
# array[indices]: Retrieves the elements in `array` at the specified indices.
print('Values where elements > 25:', array[indices])
# Output: Values where elements > 25: [30 40 50]
