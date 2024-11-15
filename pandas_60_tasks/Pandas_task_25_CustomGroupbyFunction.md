This code demonstrates how to use the groupby() method in pandas to perform a custom aggregation on grouped data. The DataFrame contains two columns: Category and Value, where values are grouped based on the Category column. The custom operation is performed using a lambda function within the apply() method. Specifically, for each group in the Category column, the maximum and minimum values of the Value column are calculated, and their difference is returned. The result is a Series showing the range of values for each category, with Category as the index. This approach highlights the flexibility of groupby() in performing advanced aggregations with custom logic.







