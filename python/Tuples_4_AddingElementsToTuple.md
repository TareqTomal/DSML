Adding Elements to a Tuple:

This code example demonstrates how to "add" elements to a tuple in Python, even though tuples are immutable. Since tuples cannot be modified directly, a new tuple is created by concatenating the original tuple with additional elements.

01. Creating a Tuple

chocoletes = ('white chocoletes', 'dark chocoletes', 'hazelnut chocoletes', 'nutella')

--> A tuple called chocoletes is created with four elements representing different chocolate types.

02. Adding Elements by Concatenation

chocoletes = chocoletes + ('Milk chocoletes', 'ruby chocoletes',)

--> Concatenation: To "add" new elements, a new tuple ('Milk chocoletes', 'ruby chocoletes',) is created and concatenated with the existing chocoletes tuple.

--> Result: This operation does not modify the original tuple but creates a new one with the added elements, which is reassigned to chocoletes.

--> Updated Tuple: The new tuple chocoletes now contains six elements: ('white chocoletes', 'dark chocoletes', 'hazelnut chocoletes', 'nutella', 'Milk chocoletes', 'ruby chocoletes').

03. Printing the Updated Tuple

print('The Updated chocolet list is :', chocoletes)

--> Output: Displays the updated tuple with the additional elements.

Example Output
The Updated chocolet list is : ('white chocoletes', 'dark chocoletes', 'hazelnut chocoletes', 'nutella', 'Milk chocoletes', 'ruby chocoletes')


--> Tuple Immutability: Tuples cannot be modified directly. To "add" elements, a new tuple must be created by concatenating the original tuple with additional elements.

--> Usage: This code illustrates how to expand a tuple indirectly by reassigning a new tuple that includes the desired elements.






















