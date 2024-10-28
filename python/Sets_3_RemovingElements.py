
# Example 3: Removing Elements from a Set
# You can remove elements using the remove() or discard() methods.
# The remove() method raises an error if the element is not found, while discard() does not.

ice_cream_flavors = {'vanilla', 'chocolet', 'mango', 'lemon', 'cherry', 'kulfi', 'pistachio'}                  # Example set

ice_cream_flavors.remove('mango')                                                                         # Removing an element

# Discarding an element (no error if element not found)
ice_cream_flavors.discard('lemon')

# Printing the set after removal
print('Thw set of ice cream flavors after Removal:', ice_cream_flavors)
