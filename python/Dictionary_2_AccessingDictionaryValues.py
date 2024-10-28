
# Example 2: Accessing Dictionary Values
# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless you use the get() method, which returns None.


gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'Bangladesh'}      # Example dictionary

place = gio_info['place']                                         # Accessing values using keys
postal_code = gio_info.get('postal_code')
country = gio_info['country']


print('place:', place)                                           # Printing accessed values
print('postal code:', postal_code)
print('country:', country)
