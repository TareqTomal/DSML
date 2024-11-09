# NumPy Advanced Indexing with Meshgrid Example

# Explanation

01. Creating Arrays:
        x and y are 1D arrays representing sets of elements for indexing.

02. Using meshgrid:
        X, Y = np.meshgrid(x, y) generates two 2D arrays (X and Y) containing all possible pairings of elements from x 
        and y.

03. Flattening and Stacking:
        X.ravel() and Y.ravel() flatten the arrays into 1D, while np.vstack([...]) stacks them vertically to create a single 2D array of pairs for advanced indexing.


# Output

Indices for Meshgrid Advanced Indexing:
 [['g' 'w' 'y' 'g' 'w' 'y']
  ['s' 's' 's' 'p' 'p' 'p']]
