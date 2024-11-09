# NumPy Advanced Slicing with Step in 2D Array


# Explanation

01. Creating a 2D Array:
        array_2d is a 3x4 NumPy array with elements in a grid.

02. Advanced Slicing with Step:
        array_2d[::2, ::2]: Slices the array with a step of 2 in both rows and columns.
            
            ::2 for rows: Selects every second row, starting from the first row (rows 0 and 2).
            ::2 for columns: Selects every second column within those rows, starting from the first column (columns 0 and 2).

03. Result:
The slicing operation results in a downsampled 2D array.

# Output
Advanced Sliced Array with Step:
 [['a' 'c']
  ['i' 'k']]
