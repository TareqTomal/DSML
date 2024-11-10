 # how to use np.where for conditional replacement in NumPy:

# Example 28: NumPy - Conditional Replacement with np.where
import numpy as np

# Creating an array
array = np.array([31, 15, 12, 25, 30, 37, 43, 17, 67])

# Replacing values based on condition
# np.where(array > 30, 0, array): Checks each element of `array`.
# If the element is greater than 30, it is replaced with 0; otherwise, it retains its original value.

result = np.where(array > 30, 0, array)

print('Array with Values Greater Than 30 Replaced with 0:', result)
# Output: Array with Values Greater Than 30 Replaced with 0: [ 0 15 12 25 30  0  0 17  0]

# Explanation:

    np.where Function: Takes three arguments – a condition (array > 30), a value to replace elements meeting the condition (0), and a value to retain elements not meeting the condition (array).

    Condition: array > 30 identifies elements greater than 30.

    Replacement: Replaces elements greater than 30 with 0 while retaining others.