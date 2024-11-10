# This example demonstrates how to extract the upper triangular part of a square matrix using NumPy.

import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the upper triangle (above the main diagonal)
upper_triangle = np.triu(matrix)

print('Upper Triangle of the Matrix:\n', upper_triangle)

# Explanation:

np.triu(matrix): Extracts the upper triangular part of the matrix, which includes the elements on and above the main diagonal. All other elements are set to zero.