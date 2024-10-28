Modifying Dictionary Values:

This code example demonstrates how to modify values in a Python dictionary. Dictionaries are mutable, meaning their values can be updated by assigning a new value to a specific key.

01. Creating a Dictionary

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD'}

--> A dictionary called gio_info is created with three key-value pairs:

	'place': Represents a place, with the value 'Dhaka'.
	'postal_code': Represents a postal code, with the value 1219.
	'country': Represents a country, with the abbreviated value 'BD'.

02. Modifying Dictionary Values

gio_info['postal_code'] = 1200
gio_info['country'] = 'Bangladesh'

--> Updating Values: Values associated with specific keys can be updated by assigning new values.

	gio_info['postal_code'] = 1200 changes the postal code to 1200.
	gio_info['country'] = 'Bangladesh' updates the country value from 'BD' to 'Bangladesh'.

--> Result: The dictionary now contains the updated values for 'postal_code' and 'country'.


03. Printing the Modified Dictionary

print('Modified gio information:', gio_info)

--> Output: Displays the modified dictionary with the updated key-value pairs.


Example Output

Modified gio information: {'place': 'Dhaka', 'postal_code': 1200, 'country': 'Bangladesh'}

--> Modifying Dictionary Values: Dictionary values can be changed by assigning new values to existing keys.

--> Mutability of Dictionaries: Dictionaries are mutable, allowing direct modification of their contents.

--> Usage: This code demonstrates how to update values in a dictionary and print the modified dictionary to reflect the changes.














