# Example 18: NumPy - Meshgrid Creation
import numpy as np

# Creating 1D arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Creating a meshgrid
# np.meshgrid(x, y): Generates two 2D arrays, `X` and `Y`, from the 1D arrays `x` and `y`.
# The resulting grids represent a coordinate matrix, where each pair of (X, Y) values covers all combinations of `x` and `y`.

X, Y = np.meshgrid(x, y)

print('Meshgrid X:\n', X)
# Output:
# Meshgrid X:
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]

print('Meshgrid Y:\n', Y)
# Output:
# Meshgrid Y:
# [[4 4 4]
#  [5 5 5]
#  [6 6 6]]
