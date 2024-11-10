# Example 7: NumPy - Indexing with Arrays
import numpy as np

# Creating a 2D array
array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Using arrays for indexing
# rows = np.array([0, 1, 2]): Specifies the row indices for the elements to be selected.
# cols = np.array([2, 1, 0]): Specifies the column indices for the elements to be selected.
# array_2d[rows, cols]: Uses `rows` and `cols` arrays to select specific elements.
#                       Each pair of (row, column) indices selects one element:
#                       (0, 2) -> 30, (1, 1) -> 50, (2, 0) -> 
