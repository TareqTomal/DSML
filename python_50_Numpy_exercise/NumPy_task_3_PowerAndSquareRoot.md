# This example demonstrates the use of NumPy functions to calculate the power and square root of each element in an array.

import numpy as np

# Creating an array
array = np.array([1, 4, 9, 16])

# Power and square root
squared = np.power(array, 2)
sqrt = np.sqrt(array)

print('Squared Array:', squared)
print('Square Root of Array:', sqrt)

# Explanation:
    np.power(array, 2): Raises each element in the array to the power of 2.
    np.sqrt(array): Calculates the square root of each element in the array.

# Output:
    Prints the squared values and square roots of each element in the original array.
