# Example 15: NumPy - Masked Indexing
import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5])

# Creating a mask for positive values
# mask = array > 0: Creates a Boolean mask where each element is True if the element in `array` is positive.
mask = array > 0

# Applying mask to get only positive values
# array[mask]: Uses the Boolean mask to select only elements where the mask is True, resulting in positive values from `array`.
positive_values = array[mask]

print('Positive Values:', positive_values)
# Output: Positive Values: [1 3 5]
