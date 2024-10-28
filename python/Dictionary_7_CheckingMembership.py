
# Example 7: Checking Membership in a Dictionary
# You can use the 'in' keyword to check if a key exists in a dictionary.

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': 70000000}      # Example dictionary


if 'place' in gio_info:                                                                   # Checking for membership
    print('Key "place" exists in the dictionary')
else:
    print('Key "place" does not exist in the dictionary')
