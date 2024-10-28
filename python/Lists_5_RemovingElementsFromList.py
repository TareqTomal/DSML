
# Example 5: Removing Elements from a List
# You can remove elements from a list using remove() and pop().
# remove() deletes the first occurrence of a value, while pop() removes an element by index.


ice_cream_flavors = ['vanilla', 'chocolet', 'mango', 'lemon', 'cherry']                  # Example list


ice_cream_flavors.remove('mango')                             # Removing elements
popped_item = ice_cream_flavors.pop(3)

# Printing the list after removal
print('The ice cream flavors list  after removal:', ice_cream_flavors)
print('Popped ice cream flavors:', ice_cream_flavors)
