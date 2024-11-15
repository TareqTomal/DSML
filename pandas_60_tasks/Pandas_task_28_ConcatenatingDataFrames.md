This code demonstrates how to concatenate two pandas DataFrames into a single DataFrame using the pd.concat() function.

Creating DataFrames:
    - Two separate DataFrames, df1 and df2, are created. Both DataFrames share the same columns, A and B, but have different row values.

Concatenating DataFrames:
    - The pd.concat() function combines the rows of df1 and df2 into a single DataFrame.
    - The parameter ignore_index=True resets the index in the concatenated DataFrame, creating a new sequential index for the combined rows.