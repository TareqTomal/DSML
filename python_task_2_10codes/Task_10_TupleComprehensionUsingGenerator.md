"""
# Tuple Comprehension using Generator Expression Example

This script demonstrates creating a tuple using a generator expression to include elements that meet a specific condition.

## Structure
- `numbers`: A range of integers from 1 to 19.

## Operations

1. **Creating a Tuple of Squares of Even Numbers Divisible by 3**
   - Uses a generator expression to calculate squares of numbers in `numbers` that are divisible by 3.
   - `even_squares = tuple(x**2 for x in numbers if x % 3 == 0)`:
     - Loops over each number in `numbers`, checks if it’s divisible by 3, and, if true, calculates its square.
     - Wraps the result in `tuple()` to create a tuple from the generator expression.

## Output
- Prints the tuple containing squares of numbers divisible by 3 from the specified range.

"""
