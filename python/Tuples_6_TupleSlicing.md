Tuple Slicing:

This code example demonstrates how to extract a part of a tuple using slicing syntax in Python. Slicing allows specific sections of a tuple to be accessed without modifying the original tuple.

01. Creating a Tuple

chocolete_list = ('white chocoletes', 'dark chocoletes', 'hazelnut chocoletes', 'nutella', 'Milk chocoletes', 'ruby chocoletes')

--> A tuple called chocolete_list is created with six different chocolate types.

02. Slicing the Tuple

sliced_chocolete_list = chocolete_list[2:5]

--> Slicing Syntax: tuple[start:stop]
	--> start: The index where slicing begins (inclusive).
	--> stop: The index where slicing ends (exclusive).
--> Operation: chocolete_list[2:5] creates a new tuple, starting from index 2 and ending before index 5.
--> Result: The new tuple sliced_chocolete_list contains the elements from indices 2, 3, and 4 of chocolete_list, which are ('hazelnut chocoletes', 'nutella', 'Milk chocoletes').


03. Printing the Sliced Tuple

print('The Sliced chocolete list is:', sliced_chocolete_list)

--> Output: Displays the sliced section of the chocolete_list tuple.

Example Output
The Sliced chocolete list is: ('hazelnut chocoletes', 'nutella', 'Milk chocoletes')

--> Tuple Slicing: Enables access to a portion of a tuple using [start:stop] notation.
--> Usage: This code demonstrates how to extract specific elements from a tuple without modifying it, showing a practical way to use slicing on immutable data structures like tuples.
















