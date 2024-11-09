
# Example 18: NumPy - Advanced Slicing with Step in 2D Array
import numpy as np

# Creating a 2D array
array_2d = np.array([['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']])

# Slicing every second element in rows and columns
result = array_2d[::2, ::2]

print('Advanced Sliced Array with Step:\n', result)
