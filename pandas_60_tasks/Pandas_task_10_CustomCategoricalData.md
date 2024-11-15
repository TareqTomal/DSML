This code demonstrates how to categorize numerical data into meaningful groups using the pd.cut() function in Python. A DataFrame is created with two columns: Name and Score, where Score represents numeric values for individual performance. A new column, Performance, is added by dividing the Score data into predefined bins [0, 70, 90, 100], representing categories such as "Poor," "Average," and "Excellent." Each score is assigned a label based on the bin it falls into. For instance, scores between 0–70 are labeled "Poor," 70–90 as "Average," and 90–100 as "Excellent." This results in a DataFrame with categorical insights, making it easier to analyze performance levels systematically.






