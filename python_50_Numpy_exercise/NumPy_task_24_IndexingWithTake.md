# Example 24: NumPy - Indexing with np.take
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Using np.take to select elements at specific indices
# indices = [0, 2, 4]: Specifies the indices of the elements to be selected from `array`.
# np.take(array, indices): Selects elements at the specified indices, returning a new array with these values.
# This method is useful for flexible indexing when working with fixed index lists.

indices = [0, 2, 4]
result = np.take(array, indices)

print('Selected Elements using np.take:', result)
# Output: Selected Elements using np.take: [10 30 50]
