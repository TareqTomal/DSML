Accessing Dictionary Values:

This code example demonstrates how to access values in a Python dictionary using keys. The values in a dictionary are accessed by referring to their keys. If a key is not found, a KeyError is raised, unless the .get() method is used, which returns None if the key does not exist.

01. Creating a Dictionary

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'Bangladesh'}

--> A dictionary called gio_info is created with three key-value pairs:
	'place': Key representing a place, with the value 'Dhaka'.
	'postal_code': Key representing the postal code, with the value 1219.
	'country': Key representing a country, with the value 'Bangladesh'.

02. Accessing Values Using Keys

place = gio_info['place']
postal_code = gio_info.get('postal_code')
country = gio_info['country']

--> Direct Key Access: gio_info['place'] and gio_info['country'] directly retrieve the values associated with the keys 'place' and 'country'.

--> Using .get() Method: gio_info.get('postal_code') retrieves the value for 'postal_code'. If the key does not exist, .get() will return None instead of raising an error.

--> Result: The values for 'place', 'postal_code', and 'country' are stored in the variables place, postal_code, and country, respectively.

03. Printing Accessed Values

print('place:', place)
print('postal code:', postal_code)
print('country:', country)

--> Output: Displays the values retrieved from the dictionary.

Example Output

place: Dhaka
postal code: 1219
country: Bangladesh

--> Accessing Dictionary Values: Values are accessed using their keys, either directly or with the .get() method.

--> Error Handling with .get(): Using .get() avoids KeyError if a key is missing, returning None instead.

--> Usage: This code demonstrates accessing values from a dictionary and printing them, showcasing the difference between direct access and the .get() method.















