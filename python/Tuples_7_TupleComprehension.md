Creating a Tuple Using a Generator Expression:

This code example demonstrates how to generate a tuple in Python by using a generator expression. Although tuples do not support comprehension directly like lists, you can achieve a similar effect by converting a generator expression into a tuple.

01. Creating a Tuple Using a Generator Expression

squared_list_items = tuple(x**2 for x in range(10))

--> Generator Expression: (x**2 for x in range(10))
	--> Expression: x**2 (calculates the square of each number x).
	--> Iterable: range(10) generates numbers from 0 to 9.
--> Operation: Each number in range(10) is squared, and the generator expression produces these squared values.
--> Conversion to Tuple: tuple(...) converts the output of the generator expression into a tuple, resulting in squared_list_items.
--> Result: squared_list_items contains the squares of numbers from 0 to 9, resulting in (0, 1, 4, 9, 16, 25, 36, 49, 64, 81).


02. Printing the Tuple

print('Squared list items are :', squared_list_items)

--> Output: Displays the tuple of squared values.

Example Output
Squared list items are : (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

--> Generator Expression: Allows creating tuples by generating values on the fly and converting them to a tuple.
--> Usage: This code demonstrates using a generator expression to compute the squares of numbers from 0 to 9 and store them in an immutable tuple.












