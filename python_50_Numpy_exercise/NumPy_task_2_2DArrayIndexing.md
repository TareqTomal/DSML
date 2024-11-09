# NumPy 2D Array Indexing and Slicing Example

# Explanation:

01. creating a 2D Array:
        array_2d: A 3x3 NumPy array containing characters.

02. Accessing Individual Elements:
        element = array_2d[1, 2]: Accesses the element at row index 1 and column index 2, which is 'f'.

03. Row and Column Slicing:
        row_slice = array_2d[0, :]: Selects all elements in the first row (['a', 'b', 'c']).

        column_slice = array_2d[:, 1]: Selects all elements in the second column (['b', 'e', 'h']).


# Output is -
        Element at (1,2): f
        First Row: ['a' 'b' 'c']
        Second Column: ['b' 'e' 'h']

