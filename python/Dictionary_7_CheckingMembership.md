 Checking Membership in a Dictionary:

This code example demonstrates how to check if a specific key exists in a Python dictionary using the in keyword.

01. Creating a Dictionary

gio_info = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': 70000000}


--> A dictionary called gio_info is created with four key-value pairs:

	'place': Represents a place, with the value 'Dhaka'.
	'postal_code': Represents a postal code, with the value 1219.
	'country': Represents a country, with the abbreviated value 'BD'.
	'population': Represents the population, with the value 70000000.

02. Checking for Key Membership with in

if 'place' in gio_info:
    print('Key "place" exists in the dictionary')
else:
    print('Key "place" does not exist in the dictionary')


--> Membership Check: The in keyword checks if the key 'place' exists in the gio_info dictionary.

--> Condition:

	If 'place' is found as a key in the dictionary, it prints "Key 'place' exists in the 	dictionary".
	If 'place' is not a key in the dictionary, it prints "Key 'place' does not exist in the 	dictionary".

--> Result: Since 'place' is indeed a key in gio_info, the output will confirm its presence.

03. Printing the Result

--> Based on the membership check, a message is printed indicating whether the key 'place' exists in the dictionary.


Example Output

Key "place" exists in the dictionary

--> in Keyword: Checks if a specific key is present in a dictionary, returning True if it exists and False if it does not.

-->Usage: This code demonstrates a simple way to verify if a key exists in a dictionary and print a message based on the result.












