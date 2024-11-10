
# Example 11: NumPy - Indexing with Negative Indices
import numpy as np

# Creating an array
array = np.array([100, 200, 300, 70, 20])

# Accessing elements from the end using negative indices
last_element = array[-1]
second_last_element = array[-2]

print('Last Element:', last_element)
print('Second Last Element:', second_last_element)
