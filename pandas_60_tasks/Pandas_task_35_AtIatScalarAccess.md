This code demonstrates how to access specific elements in a pandas DataFrame using the at and iat functions. A DataFrame is created from a dictionary with two columns, A and B, and three rows of data.

    - The at function retrieves a single value using row and column labels. For example, df.at[1, 'A'] fetches the value from row with index 1 and column 'A'.

    - The iat function retrieves a single value using row and column integer positions. For example, df.iat[1, 0] fetches the value from row 1 and column 0.

The script prints the values retrieved by these methods, illustrating how to access data efficiently with labels and integer positions.






