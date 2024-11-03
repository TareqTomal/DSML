
# Example 1: Nested Lists Operations
# Working with nested lists by accessing elements, modifying values, and flattening the list.

# Example nested list
stationaries = [['pen', 'paper', 'pencil'], ['glue', 'super glue', ['eraser', 'stapler']], ['roller', 'calculator']]

# Accessing a nested element
nested_element = stationaries[1][2][1]  # Accessing eraser

# Modifying a nested element
stationaries[2][1] = 'BOXES'  # Changing calculator to BOXES

# Flattening the nested list
flattened_list = [element for sublist in stationaries for item in sublist for element in (item if isinstance(item, list) else [item])]

print('Nested Element:', nested_element)
print('Modified Nested List:', stationaries)
print('Flattened List:', flattened_list)
