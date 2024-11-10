# Example 23: NumPy - Multi-dimensional Array Indexing with Mixed Types
import numpy as np

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], 
                     [[5, 6], [7, 8]], 
                     [[9, 10], [11, 12]]])

# Mixing slicing with direct indexing
# array_3d[1:, 0, 1]: Uses a combination of slicing and direct indexing.
# 1: selects all 2D sub-arrays from index 1 onward.
# 0 selects the first element (sub-array) along the second dimension in each 2D sub-array.
# 1 selects the second element along the last dimension in 
