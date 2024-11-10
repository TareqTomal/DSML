"""
# Tuple Unpacking Example

This script demonstrates unpacking a tuple into multiple variables in Python.

## Structure
- `person_info`: A tuple containing personal information (name, age, job, and address).

## Operations

1. **Unpacking Tuple into Variables**
   - Unpacks specific elements of the tuple into variables (`name` and `age`).
   - Uses the `*` operator to capture remaining elements into `other_details`.
   - `name, age, *other_details = person_info` assigns 'Ruben' to `name`, 18 to `age`, and the remaining items to `other_details`.

## Output
- Prints the unpacked values: `Name`, `Age`, and `Other Details` for verification.

"""
