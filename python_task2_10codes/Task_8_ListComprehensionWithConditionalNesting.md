"""
# List Comprehension with Conditional Nesting Example

This script demonstrates using list comprehension with nested loops and conditions to filter and flatten elements from a nested list (matrix).

## Structure
- `matrix`: A 2D list (matrix) with three rows of numbers.

## Operations

1. **Flattening and Filtering Even Numbers**
   - Uses list comprehension to iterate over each row and each number within `matrix`.
   - `[num for row in matrix for num in row if num % 2 == 0]`:
     - Loops over each `row` in `matrix` and then each `num` in `row`.
     - Includes `num` in `even_flattened` only if `num` is even (`num % 2 == 0`).

## Output
- Prints a flattened list containing only the even numbers from the matrix.

"""
