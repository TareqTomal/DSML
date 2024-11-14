# Documentation: Adding Prefix and Suffix to DataFrame Columns

import pandas as pd

- pandas is imported as pd for creating and manipulating data structures like DataFrames.

## Code Explanation

- Creating a DataFrame:

data = {'Math': [90, 80], 'Science': [85, 88]}
df = pd.DataFrame(data)

- A dictionary data is created with subject names as keys and lists of scores as values.
- df is created using pd.DataFrame(data), which converts the dictionary into a DataFrame with columns Math and Science.

## Adding a Prefix to Column Names:

df_prefixed = df.add_prefix('Grade_')

- add_prefix('Grade_') method adds "Grade_" to the beginning of each column name.
- The resulting DataFrame df_prefixed will have columns Grade_Math and Grade_Science.

## Adding a Suffix to Column Names:

df_suffixed = df.add_suffix('_Score')


- add_suffix('_Score') method adds "_Score" to the end of each column name.
- The resulting DataFrame df_suffixed will have columns Math_Score and Science_Score

## Printing the Results:

print('DataFrame with Prefix:\n', df_prefixed)
print('DataFrame with Suffix:\n', df_suffixed)

- The DataFrames with prefixed and suffixed column names are printed to the console.

## add_prefix and add_suffix are useful for modifying column names without manually renaming each one.
## These methods do not alter the original DataFrame (df) but return modified copies (df_prefixed and df_suffixed).