# Documentation: Applying Operations to Each Element in a DataFrame

# Creating a DataFrame:

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

- data is a dictionary with keys A and B, representing columns with lists of numbers.
- df is created using pd.DataFrame(data).

# Applying an Operation to Each Element:

df_transformed = df.applymap(lambda x: x**2)

- applymap(lambda x: x**2) squares each element in df.
- The modified DataFrame, df_transformed, stores these squared values.

# Outputting the Result:

print('DataFrame with Squared Values:\n', df_transformed)

- Displays df_transformed, showing each element squared.

# Note

- applymap is ideal for element-wise operations across the entire DataFrame.

