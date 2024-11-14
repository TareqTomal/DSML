# Documentation: Applying Functions to Rows and Columns in a DataFrame

## Creating a DataFrame:
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

- A dictionary data with keys A and B contains lists of integers.
- df is created from data, resulting in a DataFrame with columns A and B.

## Applying a Function to Rows and Columns:
row_sum = df.apply(lambda x: x.sum(), axis=1)
col_sum = df.apply(lambda x: x.sum(), axis=0)

- df.apply(lambda x: x.sum(), axis=1) calculates the sum across each row (i.e., row-wise) by setting axis=1. The result is stored in row_sum
- df.apply(lambda x: x.sum(), axis=0) calculates the sum across each column (i.e., column-wise) by setting axis=0. The result is stored in col_sum.

## Outputting the Results:
print('Row-wise Sum:\n', row_sum)
print('Column-wise Sum:\n', col_sum)

- row_sum and col_sum are printed, showing the row and column sums.
- apply with axis=1 operates on rows, and axis=0 operates on columns, making it flexible for various aggregations and transformations.

