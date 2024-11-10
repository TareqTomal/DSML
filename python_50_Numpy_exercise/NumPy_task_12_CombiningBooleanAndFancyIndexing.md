# Example 12: NumPy - Combining Boolean and Fancy Indexing
import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# Boolean condition combined with specific indices
# Step 1: (array > 10) & (array < 30) creates a Boolean mask, filtering the array for values between 10 and 30 (exclusive).
#         Resulting values from the filter are [15, 20, 25].
# Step 2: [[0, 2]] uses fancy indexing on the filtered result to select elements at index positions 0 and 2.
#         This selects the first and third values from the filtered result, resulting in [15, 25].

result = array[(array > 10) & (array < 30)][[0, 2]]

print('Combined Boolean and Fancy Indexing Result:', result)
# Output: Combined Boolean and Fancy Indexing Result: [15 25]

# Explanation:

    Boolean Indexing: Filters elements that satisfy the condition (array > 10) & (array < 30), producing [15, 20, 25].
    Fancy Indexing: Selects specific positions [0, 2] from the filtered array, giving [15, 25] as the final result. 