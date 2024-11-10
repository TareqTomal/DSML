# how to calculate the cumulative sum and product of an array in NumPy:

# Example 20: NumPy - Cumulative Sum and Product
import numpy as np

# Creating an array
array = np.array([11, 22, 33, 44])

# Calculating cumulative sum and product
# np.cumsum(array): Calculates the cumulative sum of the elements in `array`.
# Each element in the result is the sum of all previous elements up to that index.
cumulative_sum = np.cumsum(array)

# np.cumprod(array): Calculates the cumulative product of the elements in `array`.
# Each element in the result is the product of all previous elements up to that index.
cumulative_product = np.cumprod(array)

print('Cumulative Sum:', cumulative_sum)
# Output: Cumulative Sum: [11 33 66 110]

print('Cumulative Product:', cumulative_product)
# Output: Cumulative Product: [   11   242  7986 351384]

# Explanation:

    Cumulative Sum (np.cumsum): Produces an array where each element at index i is the sum of all elements from the start up to index i.

    Cumulative Product (np.cumprod): Produces an array where each element at index i is the product of all elements from the start up to index i.
