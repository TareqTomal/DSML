# Example 25: NumPy - Masked Indexing with np.ma.masked_where
import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5])

# Masking elements where values are negative
# np.ma.masked_where(array < 0, array): Creates a masked array where elements in `array` are masked (hidden) if they are negative.
# This is useful when you want to hide certain values without removing them from the array.

masked_array = np.ma.masked_where(array < 0, array)

print('Masked Array with Negative Values Hidden:', masked_array)
# Output: Masked Array with Negative Values Hidden: [1 -- 3 -- 5]

