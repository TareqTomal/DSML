#  how to extract both the main diagonal and the reverse diagonal (anti-diagonal) elements of a matrix in NumPy

# Example 16: NumPy - Extracting Diagonal Elements
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the main diagonal
# np.diag(matrix): Extracts the main diagonal elements of `matrix`, where row index equals column index.
diagonal_elements = np.diag(matrix)

# Extracting the reverse diagonal (anti-diagonal)
# np.fliplr(matrix): Flips the matrix horizontally, reversing the columns.
# np.diag(np.fliplr(matrix)): Extracts the main diagonal from the horizontally flipped matrix,
#                             which corresponds to the reverse diagonal of the original matrix.
reverse_diagonal_elements = np.diag(np.fliplr(matrix))

print('Diagonal Elements:', diagonal_elements)
# Output: Diagonal Elements: [1 5 9]

print('Reverse Diagonal Elements:', reverse_diagonal_elements)
# Output: Reverse Diagonal Elements: [3 5 7]

# Explanation:

    Main Diagonal (np.diag(matrix)): Extracts elements [1, 5, 9], located where the row and column indices match in the original matrix.

    Reverse Diagonal (Anti-diagonal):

        np.fliplr(matrix): Flips the matrix left-to-right, resulting in a reversed column order.

        np.diag(np.fliplr(matrix)): Extracts the main diagonal of the flipped matrix, which corresponds to the reverse diagonal [3, 5, 7] in the original matrix.

