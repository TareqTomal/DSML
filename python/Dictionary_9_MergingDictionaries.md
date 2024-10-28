Merging Dictionaries:

This code example demonstrates how to merge two dictionaries in Python using the update() method. The update() method adds key-value pairs from one dictionary to another. 

01. Creating Example Dictionaries

gio_info1 = {'place': 'Dhaka', 'postal_code': 1219}
gio_info2 = {'country': 'BD', 'population': 70000000}


--> Two dictionaries are created:
	gio_info1 contains key-value pairs for 'place' and 'postal_code'.
	gio_info2 contains key-value pairs for 'country' and 'population'.

02. Merging Dictionaries Using update()

gio_info1.update(gio_info2)

--> update() Method: gio_info1.update(gio_info2) merges gio_info2 into gio_info1.
	Any new key-value pairs from gio_info2 are added to gio_info1.
	If there were duplicate keys, gio_info2 values would overwrite those in gio_info1.

--> Result: gio_info1 now contains all key-value pairs from both dictionaries.

03. Printing the Merged Dictionary

print('Merged gio information:', gio_info1)

--> Output: Displays the merged dictionary, now containing all entries from gio_info1 and gio_info2.


Example Output

Merged gio information: {'place': 'Dhaka', 'postal_code': 1219, 'country': 'BD', 'population': 70000000}

--> update() Method: Merges another dictionary into the current one, adding new key-value pairs and updating any existing keys.
--> Alternative Merge: In Python 3.9+, dictionaries can be merged using {**gio_info1, **gio_info2}.
--> Usage: This code demonstrates combining two dictionaries into one using update() and printing the result.





















