"""
# Stationeries Nested List Manipulation

This script demonstrates various operations on a nested list structure in Python.

## Structure
- `stationaries`: A nested list containing categories of stationery items.

## Operations

1. **Accessing a Nested Element**
   - Retrieves a specific nested element within the list.
   - `nested_element = stationaries[1][2][1]` accesses 'stapler' within the nested list.

2. **Modifying a Nested Element**
   - Updates a specific element within the list.
   - `stationaries[2][1] = 'BOXES'` replaces 'calculator' with 'BOXES'.

3. **Flattening the Nested List**
   - Converts the nested list into a single-level list.
   - `flattened_list` uses a nested list comprehension to flatten `stationaries`.

## Output
- Prints the accessed element, the modified list, and the flattened list for verification.

"""
