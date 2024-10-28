
# Example 5: Removing Elements from a Tuple
# Tuples are immutable, so elements cannot be removed directly.
# To remove elements, you need to convert the tuple to a list and back to a tuple.

cloth_items = ('pants', 'shirt', 't-shirt', 'jacket', 'pull over', 'sweat shirt')                                             # Example tuple


remove_items = list(cloth_items)                                          # Converting to a list and removing an element
remove_items.remove('pull over')
cloth_items = tuple(remove_items)

print('The cloth items after Removal:', cloth_items)                             # Printing the tuple after removal



