Adding Key-Value Pairs to a Dictionary:

This code example demonstrates how to add new key-value pairs to a Python dictionary. New entries can be added by assigning a value to a new key.

01. Creating a Dictionary

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD'}

--> A dictionary called gio_info is created with three initial key-value pairs:

	'place': Represents a place, with the value 'Dhaka'.
	'postal_code': Represents a postal code, with the value 1219.
	'country': Represents a country, with the abbreviated value 'BD'.

02 Adding a New Key-Value Pair

gio_info['population'] = '70000000'

--> Adding a New Entry: By assigning a value to a new key, a new key-value pair is added to the dictionary.

	gio_info['population'] = '70000000' adds a new entry with 'population' as the key and '70000000' as the value.

--> Result: The dictionary now includes the new key-value pair.

03. Printing the Updated Dictionary

print('The Updated gio_info:', gio_info)

--> Output: Displays the dictionary with the added key-value pair.

Example Output

The Updated gio_info: {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': '70000000'}

--> Adding Key-Value Pairs: New entries can be added to a dictionary by assigning a value to a new key.
--> Usage: This code demonstrates how to expand a dictionary by adding new data and printing the updated dictionary to display the changes.








