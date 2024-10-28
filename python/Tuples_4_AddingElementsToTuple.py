
# Example 4: Adding Elements to a Tuple
# Tuples are immutable, so you cannot add elements directly.
# However, you can create a new tuple by concatenating the existing one with another tuple.


chocoletes = ('white chocoletes', 'dark chocoletes', 'hazelnut chocoletes', 'nutella')                            # Example tuple


chocoletes = chocoletes + ('Milk chocoletes', 'ruby chocoletes',)                      # Adding elements by creating a new tuple


print('The Updated chocolet list is :', chocoletes)               # Printing the updated tuple
