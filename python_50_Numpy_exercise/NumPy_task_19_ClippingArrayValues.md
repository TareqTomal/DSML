# NumPy Clipping Array Values

# Explanation

01. Array Creation:
        array = np.array([5, 2, 4, 1, 9]): An array with integer values.

02. Using np.clip:
        
        np.clip(array, 2, 4): Clips values in array to the range [2, 4].

            Values below 2 are set to 2.
            Values above 4 are set to 4.
            Values within [2, 4] remain unchanged.

# Output

Original Array: [5 2 4 1 9]
Clipped Array: [4 2 4 2 4]

