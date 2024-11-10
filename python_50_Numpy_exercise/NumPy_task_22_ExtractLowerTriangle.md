# how to extract both the lower and upper triangular parts of a matrix in NumPy:

# Example 22: NumPy - Extract Lower and Upper Triangles of a Matrix
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the lower triangle (below and including the main diagonal)
# np.tril(matrix): Extracts the lower triangle of the matrix.
# All elements above the main diagonal are set to zero.
lower_triangle = np.tril(matrix)

# Extracting the upper triangle (above and including the main diagonal)
# np.triu(matrix): Extracts the upper triangle of the matrix.
# All elements below the main diagonal are set to zero.
upper_triangle = np.triu(matrix)

print('Lower Triangle of the Matrix:\n', lower_triangle)
# Output:
# Lower Triangle of the Matrix:
# [[1 0 0]
#  [4 5 0]
#  [7 8 9]]

print('Upper Triangle of the Matrix:\n', upper_triangle)
# Output:
# Upper Triangle of the Matrix:
# [[1 2 3]
#  [0 5 6]
#  [0 0 9]]
