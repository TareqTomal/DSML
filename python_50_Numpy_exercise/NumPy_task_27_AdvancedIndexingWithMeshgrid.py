
# Example 27: NumPy - Advanced Indexing with Meshgrid

import numpy as np

x = np.array(['g', 'w', 'y']) # Creating 1D arrays
y = np.array(['s', 'p'])

# Creating meshgrid for advanced indexing
X, Y = np.meshgrid(x, y)
indices = np.vstack([X.ravel(), Y.ravel()])

print('Indices for Meshgrid Advanced Indexing:\n', indices)
