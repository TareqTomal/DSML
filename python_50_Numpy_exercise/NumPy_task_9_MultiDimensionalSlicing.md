# Example 9: NumPy - Multi-dimensional Slicing
import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3, 4], 
                     [5, 6, 7, 8], 
                     [9, 10, 11, 12]])

# Multi-dimensional slicing
# array_2d[1:, 1:3]: Uses slicing to select a subset of rows and columns.
# 1: selects rows starting from index 1 (second row) to the end of the array.
# 1:3 selects columns from index 1 up to (but not including) index 3.
# The result is a subarray with elements from these specified rows and columns.

sub_array = array_2d[1:, 1:3]

print('Sub Array (Slicing Rows and Columns):\n', sub_array)
# Output:
# Sub Array (Slicing Rows and Columns):
# [[ 6  7]
#  [10 11]]
