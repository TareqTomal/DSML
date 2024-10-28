
# Example 5: Removing Key-Value Pairs from a Dictionary
# You can remove key-value pairs using the pop() method, which removes the specified key and returns its value.
# The del keyword can also be used to remove a specific key or clear() to remove all items.

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': 70000000}      # Example dictionary

population = gio_info.pop('population')                                              # Removing a key-value pair

# Printing the dictionary after removal
print('gio info after Removal:', gio_info)
print('Removed population:', population)
