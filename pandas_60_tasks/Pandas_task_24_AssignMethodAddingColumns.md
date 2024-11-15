This code demonstrates how to use the pandas library to create a DataFrame, manipulate it,
and add a new column using the assign method. 

A dictionary is first used to define data containing names and scores, which is converted into a DataFrame.

The assign method dynamically adds a new column, Grade, based on the values in the Score column.

A lambda function with a list comprehension assigns 'A' for scores ≥ 90 and 'B' otherwise.

Finally, the updated DataFrame, including the new Grade column, is printed. This approach ensures concise and efficient DataFrame manipulation.
