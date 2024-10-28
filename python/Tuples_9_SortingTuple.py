
# Example 9: Sorting a Tuple
# Tuples are immutable and cannot be sorted directly.
# To sort a tuple, you need to convert it to a list, sort it, and convert it back to a tuple.

names = ['Ruben', 'Matthias', 'Lina', 'Daniel', 'Timo', 'Benedikt']                        # Example list                       

# Sorting by converting to a list
sorted_names = sorted(names)
sorted_tuple = tuple(sorted_names)

# Printing the sorted tuple
print('The Sorted names are :', sorted_tuple)

