#  use of fancy indexing in NumPy:

# Example 4: NumPy - Fancy Indexing
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Selecting specific indices
# array[[1, 3, 4]]: Uses fancy indexing to select elements at specific positions in `array`.
# In this example, it selects the elements at indices 1, 3, and 4 from `array`.

selected_elements = array[[1, 3, 4]]

print('Selected Elements:', selected_elements)
# Output: Selected Elements: [20 40 50]
