
# Example 7: Tuple Comprehension (using generator expression)
# Tuples do not support comprehension like lists.
# However, you can use a generator expression to create a tuple.

squared_list_items = tuple(x**2 
                            for x in range(10))          # Creating a tuple of squares of numbers from 0 to 9


# Printing the tuple
print('Squared list items are :', squared_list_items)
