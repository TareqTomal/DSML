
# Example 16: NumPy - Extracting Diagonal Elements
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the main diagonal
diagonal_elements = np.diag(matrix)

# Extracting the reverse diagonal (anti-diagonal)
reverse_diagonal_elements = np.diag(np.fliplr(matrix))

print('Diagonal Elements:', diagonal_elements)
print('Reverse Diagonal Elements:', reverse_diagonal_elements)