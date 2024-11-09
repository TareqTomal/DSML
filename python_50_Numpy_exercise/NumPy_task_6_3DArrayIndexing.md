# NumPy 3D Array Indexing and Slicing Example

# Explanation

01. Creating a 3D Array:
        array_3d: A 3D NumPy array with shape (2, 2, 2) that contains characters.

02. Accessing an Element in 3D:
        element = array_3d[1, 0, 1]: Retrieves the element at position [1, 0, 1] in the 3D array, which is 'f'.

03. 3D Slicing:
        slice_3d = array_3d[:, 0, :]: Selects the first row from each 2D array along the first dimension, resulting in a 2D slice of [['a', 'b'], ['e', 'f']].

# Output

Element at (1,0,1): f
Sliced 3D Array:
 [['a' 'b']
  ['e' 'f']]
