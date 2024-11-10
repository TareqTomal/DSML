# This example demonstrates the use of NumPy's statistical functions to calculate the mean, median, standard deviation, and variance of an array.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Calculating statistical values
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)
variance = np.var(array)

print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', std_dev)
print('Variance:', variance)

# Explanation:
        np.mean(array): Calculates the mean (average) of the array elements.
        np.median(array): Calculates the median (middle value) of the array elements.
        np.std(array): Calculates the standard deviation, indicating the spread of the array elements from the mean.
        np.var(array): Calculates the variance, which is the square of the standard deviation.

# Output:
    Displays the mean, median, standard deviation, and variance of the array, resulting in:
        Mean: 3.0
        Median: 3.0
        Standard Deviation: 1.414
        Variance: 2.0