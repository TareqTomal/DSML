Removing Key-Value Pairs from a Dictionary:

This code example demonstrates how to remove key-value pairs from a Python dictionary using the pop() method. The pop() method removes a specified key and returns its value. Additionally, the del keyword can remove specific keys, and clear() can remove all items in a dictionary.

01. Creating a Dictionary

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': 70000000}


--> A dictionary called gio_info is created with four key-value pairs:

	'place': Represents a place, with the value 'Dhaka'.
	'postal_code': Represents a postal code, with the value 1219.
	'country': Represents a country, with the abbreviated value 'BD'.
	'population': Represents the population, with the value 70000000.

02. Removing a Key-Value Pair Using pop()

population = gio_info.pop('population')

--> pop() Method: gio_info.pop('population') removes the key 'population' from the dictionary and returns its value.

--> Result: The key-value pair 'population': 70000000 is removed, and population stores the removed value (70000000).

03. Printing the Updated Dictionary and Removed Value

print('gio info after Removal:', gio_info)
print('Removed population:', population)

--> Output: Displays the updated dictionary without the 'population' key and the removed value.

Example Output

gio info after Removal: {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD'}
Removed population: 70000000
 
--> Removing Key-Value Pairs: The pop() method removes a specified key and returns its value. The del keyword can also remove keys, while clear() empties the entire dictionary.

--> Usage: This code demonstrates removing a key-value pair from a dictionary and printing both the updated dictionary and the removed value.










