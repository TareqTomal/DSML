
# Example 2: Adding Elements to a Set
# You can add elements to a set using the add() method.
# Sets do not allow duplicate elements.


product_name = {'Book', 'Pencil', 'Marker', 'Box', 'Eraser'}                    # Example set

product_name.add('Sharpner')                                                    # Adding a new element

product_name.add('Sharpner')                                                    # Trying to add a duplicate element (this will have no effect)

print('The Updated product name:', product_name)                                # Printing the updated set
