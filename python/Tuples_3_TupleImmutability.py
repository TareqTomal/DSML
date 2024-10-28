
# Example 3: Tuple Immutability
# Tuples are immutable, meaning their values cannot be changed once created.
# Trying to modify an element of a tuple will result in an error.

roll_number = (20, 52, 63, 77, 82, 95)                                                    # Example tuple

try:                                                                    # Trying to modify an element (this will raise an error)
    roll_number[0] = 17
except TypeError as e:
    print('Error:', e)
