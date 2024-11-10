# Example 10: NumPy - Modifying Array Values using Indexing
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Modifying values at specific indices
# array[[1, 3]] = [100, 200]: Changes the values at indices 1 and 3.
# The value at index 1 is updated to 100, and the value at index 3 is updated to 200.

array[[1, 3]] = [100, 200]

print('Modified Array:', array)
# Output: Modified Array: [ 10 100  30 200  50]
