Iterating Over a Dictionary

This code example demonstrates how to iterate over a dictionary in Python to access its keys and values. By using a for loop with the items() method, you can retrieve both the keys and values in each iteration.

01. Creating a Dictionary

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': 70000000}

--> A dictionary called gio_info is created with four key-value pairs:

	'place': Represents a place, with the value 'Dhaka'.
	'postal_code': Represents a postal code, with the value 1219.
	'country': Represents a country, with the abbreviated value 'BD'.
	'population': Represents the population, with the value 70000000.

02. Iterating Over the Dictionary Using items()

for key, value in gio_info.items():
    print(f'Key: {key}, Value: {value}')


--> items() Method: gio_info.items() returns a view object containing all key-value pairs in the dictionary as tuples.

--> For Loop: The for loop iterates over each key-value pair in gio_info. In each iteration:
	key holds the current dictionary key.
	value holds the corresponding value for that key.

--> Operation: For each key-value pair, the loop prints the key and its associated value.

03. Printing Each Key-Value Pair

--> The code uses an f-string to format and print each key and value.

Example Output

Key: place, Value: Dhaka
Key: postal_code, Value: 1219
Key: country, Value: BD
Key: population, Value: 70000000

--> items() Method: Used to retrieve all key-value pairs as tuples for iteration.
--> Iteration Over Dictionaries: Allows accessing and printing each key-value pair in the dictionary.
--> Usage: This code demonstrates iterating through a dictionary to display each key and its corresponding value.









