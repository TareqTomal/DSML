
# Example 20: NumPy - Cumulative Sum and Product
import numpy as np

# Creating an array
array = np.array([11, 22, 33, 44])

# Calculating cumulative sum and product
cumulative_sum = np.cumsum(array)
cumulative_product = np.cumprod(array)

print('Cumulative Sum:', cumulative_sum)
print('Cumulative Product:', cumulative_product)
