# This example demonstrates how to generate arrays with random values using NumPy.

import numpy as np

# Generating random arrays
random_array = np.random.rand(3, 3)  # Random values in a 3x3 array
normal_array = np.random.randn(3, 3)  # Random values with a normal distribution

print('Random Array:\n', random_array)
print('Normal Distribution Array:\n', normal_array)

# Explanation:
    np.random.rand(3, 3): Generates a 3x3 array with random values uniformly distributed between 0 and 1.
    np.random.randn(3, 3): Generates a 3x3 array with random values from a normal (Gaussian) distribution centered around 0 with a standard deviation of 1.

# Output:
    Displays a 3x3 array with uniformly random values and a 3x3 array with normally distributed random values.
