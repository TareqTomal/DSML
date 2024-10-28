Dictionary Keys, Values, and Items

This code example demonstrates how to retrieve all keys, values, or key-value pairs from a Python dictionary using the keys(), values(), and items() methods.

01. Creating a Dictionary

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': 70000000}

--> A dictionary called gio_info is created with four key-value pairs:

	'place': Represents a place, with the value 'Dhaka'.
	'postal_code': Represents a postal code, with the value 1219.
	'country': Represents a country, with the abbreviated value 'BD'.
	'population': Represents the population, with the value 70000000.

02. Retrieving Keys, Values, and Items

keys = gio_info.keys()
values = gio_info.values()
items = gio_info.items()


--> keys() Method: gio_info.keys() returns a view object containing all the keys in the dictionary.
--> values() Method: gio_info.values() returns a view object containing all the values in the dictionary.
--> items() Method: gio_info.items() returns a view object containing all key-value pairs as tuples within a list-like structure.

03. Printing Keys, Values, and Items

print('Keys:', keys)
print('Values:', values)
print('Items:', items)

--> Output: Displays all keys, values, and key-value pairs in the dictionary.

Example Output

Keys: dict_keys(['place', 'postal_code', 'country', 'population'])
Values: dict_values(['Dhaka', 1219, 'BD', 70000000])
Items: dict_items([('place', 'Dhaka'), ('postal_code', 1219), ('country', 'BD'), ('population', 70000000)])


--> keys() Method: Retrieves all keys in the dictionary.
--> values() Method: Retrieves all values in the dictionary.
--> items() Method: Retrieves all key-value pairs as tuples.
--> Usage: This code demonstrates how to retrieve and print the keys, values, and items from a dictionary.















