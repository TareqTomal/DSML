# Example 13: NumPy - Indexing Multi-dimensional Arrays with Slices
import numpy as np

# Creating a 3x4 array
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Selecting specific rows and columns using slices
# array_2d[1:, :2]: Uses slicing to select a subset of rows and columns.
# 1: selects rows starting from index 1 (second row) to the end.
# :2 selects columns up to index 2 (first two columns).
# The result is a 2x2 array containing elements from the specified rows and columns.

selected_slice = array_2d[1:, :2]

print('Selected Slice:\n', selected_slice)
# Output:
# Selected Slice:
# [[ 5  6]
#  [ 9 10]]
