import numpy as np

# Corrected array to use valid indices
array = np.array([0, 1, 2, 0])  # Now array contains only valid indices for choices
choices = [array * 2, array + 10, array ** 2]

# Using np.choose to apply different conditions
result = np.choose(array, choices)

print('Result using np.choose:', result)

