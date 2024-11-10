# use of exponential and logarithmic functions in NumPy:

# Example 4: NumPy - Exponential and Logarithmic Functions
import numpy as np

# Creating an array
array = np.array([1, 2, 3])

# Exponential and logarithmic functions
# np.exp(array): Calculates the exponential of each element in `array`, using e (approximately 2.718) as the base.
# Each element in `exp_array` is computed as e^x, where x is each element in `array`.
exp_array = np.exp(array)

# np.log(array): Calculates the natural logarithm (base e) of each element in `array`.
# Each element in `log_array` is computed as ln(x), which gives the power to which e must be raised to obtain x.
# Note: Logarithm is only defined for positive numbers.
log_array = np.log(array)

print('Exponential of Array:', exp_array)
# Output: Exponential of Array: [ 2.71828183  7.3890561  20.08553692]

print('Logarithm of Array:', log_array)
# Output: Logarithm of Array: [0.         0.69314718 1.09861229]

