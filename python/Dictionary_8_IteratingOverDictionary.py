
# Example 8: Iterating Over a Dictionary
# You can iterate over a dictionary to access its keys, values, or key-value pairs.

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': 70000000}      # Example dictionary


for key, value in gio_info.items():                                              # Iterating over keys and values
    print(f'Key: {key}, Value: {value}')
