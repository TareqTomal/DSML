"""
# List of Tuples to Dictionary Conversion Example

This script demonstrates converting a list of tuples into a dictionary using a loop.

## Structure
- `tuple_list`: A list of tuples where each tuple contains a key (bird type) and a value (quantity).

## Operations

1. **Converting List of Tuples to Dictionary**
   - Uses dictionary comprehension to convert `tuple_list` into `result_dict`.
   - `{key: value for key, value in tuple_list}` iterates over each tuple, assigning `key` to the first element and `value` to the second element, storing them in `result_dict`.

## Output
- Prints the dictionary created from the list of tuples, displaying each bird type with its corresponding quantity.

"""
