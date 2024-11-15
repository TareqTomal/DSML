This code demonstrates how to filter rows in a pandas DataFrame based on multiple conditions.

Creating a DataFrame:
    - A DataFrame is created with three columns:
        Name: Contains the names of individuals.
        Score: Numeric scores assigned to each individual.
        Passed: A boolean column indicating whether the individual passed or not.
    
    - Filtering with Multiple Conditions:
        The DataFrame is filtered using a boolean mask created by combining two conditions:
            (df['Score'] > 80): Selects rows where the Score is greater than 80.
            (df['Passed'] == True): Selects rows where Passed is True.
        
        The & operator combines these conditions, ensuring that only rows meeting both criteria are included in the filtered DataFrame.
    - The filtered DataFrame contains rows where the individual's score is greater than 80 and they passed.






