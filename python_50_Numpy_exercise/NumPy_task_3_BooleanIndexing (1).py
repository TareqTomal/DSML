
# Example 3: NumPy - Boolean Indexing

import numpy as np

# Creating an array
array = np.array([10, 25, 30, 65, 70, 90])

# Boolean indexing
greater_than_20 = array[array > 50]

print('Elements Greater Than 20:', greater_than_20)
