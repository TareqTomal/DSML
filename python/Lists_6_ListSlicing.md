This code shows that how to extract a portion of a list in Python using slicing syntax, allowing us to specify a range within the list to create a new list.

01. Creating a List

item_list = ['mango', 'avocado', 'pitch', 'water melon', 'banana', 'palm', 'dates']

--> A list called item_list is created with various fruit names as elements.

02. Slicing the List

sliced_list = item_list[2:5]

--> Slicing Syntax: list[start:stop]
-----> start: The index where slicing begins (inclusive).
-----> stop: The index where slicing ends (exclusive).

--> Operation: item_list[2:5] creates a new list starting from index 2 and ending before index 5.
--> Result: The new list, sliced_list, contains the elements from indices 2, 3, and 4 of item_list, which are ['pitch', 'water melon', 'banana'].


03. Printing the Sliced List

print('Sliced List is:', sliced_list)
--> Output: Displays the newly created sliced_list.

Example Output
Sliced List is : ['pitch', 'water melon', 'banana']

--> List Slicing: Allows extraction of a subset of elements from a list using [start:stop] syntax.
--> Usage: This code demonstrates how to create a new list containing a specific range of elements from an existing list.
