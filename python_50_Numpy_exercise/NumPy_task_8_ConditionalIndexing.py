
# Example 8: NumPy - Conditional Indexing
import numpy as np

# Creating an array
array = np.array([10, 21, 30, 45, 57, 60])

# Setting elements that satisfy a condition
array[array % 5 == 0] = -1  # Set even numbers to -1

print('Array after Conditional Indexing:', array)
