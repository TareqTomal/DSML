"""
This script demonstrates how to access elements in a Python list using both positive and negative indices.
The list contains elements of various data types, including integers and strings.

Description:
    Elements in a list are accessed using indices, with indexing starting at 0 for the first element.
    Negative indexing can be used to access elements from the end of the list, with -1 representing the last element.

Example:
    my_list = [10, 'Frankfurt', 'München', 347, 590]

Accessed Elements:
    - First Element (Index 0): 10
    - Third Element (Index 2): 'München'
    - Last Element (Index -1): 590

Output:
    The First Element is: 10
    The Third Element is: München
    The Last Element is: 590
"""

# Creating a list with various data types
my_list = [10, 'Frankfurt', 'München', 347, 590]

# Accessing elements using positive and negative indices
first_element = my_list[0]
third_element = my_list[2]
last_element = my_list[-1]

# Printing accessed elements
print('The First Element is:', first_element)
print('The Third Element is:', third_element)
print('The Last Element is:', last_element)


-------------------


Explanation:
- The explanation of the code is to describe how a list indexing works in Python, and includes an example with the expected output.

- The comments within the code clarify the purpose of each line, from creating the list to printing accessed elements.