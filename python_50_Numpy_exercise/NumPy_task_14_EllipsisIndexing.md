# Use of ellipsis (...) in indexing a 3D NumPy array:

# Example 14: NumPy - Using Ellipsis (...) in Indexing
import numpy as np

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Using ellipsis to select all elements along specific axes
# array_3d[..., 1]: The ellipsis (...) represents all preceding dimensions,
# allowing selection of the second element (index 1) along the last axis.
# This extracts the second "column" from each 2D array within array_3d.

result = array_3d[..., 1]  # Selecting the second column in each 2D slice

print('array_3d:\n', array_3d)
# Output:
# array_3d:
# [[[ 1  2]
#   [ 3  4]]
#
#  [[ 5  6]
#   [ 7  8]]
#
#  [[ 9 10]
#   [11 12]]]

print('Result using Ellipsis (...):\n', result)
# Output:
# Result using Ellipsis (...):
# [[ 2  4]
#  [ 6  8]
#  [10 12]]


# Explanation:

    Ellipsis (...) in Indexing: The ellipsis allows you to select all elements along preceding dimensions, so array_3d[..., 1] means "select all elements along the first and second dimensions, and take the second element (index 1) along the last dimension."

    Result: The code extracts the second element from each innermost 1D array within each 2D slice of array_3d.

