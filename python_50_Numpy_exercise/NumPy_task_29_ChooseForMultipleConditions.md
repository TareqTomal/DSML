# NumPy np.choose for Multiple Conditions

# Explanation

01. Creating Arrays:

    array: Contains indices [0, 1, 2, 0], which are valid for referencing elements in choices.
    
    choices: A list of arrays calculated as:
            array * 2
            array + 10
            array ** 2

02. Using np.choose:

        np.choose(array, choices): Uses each value in array as an index to select the corresponding element from choices.

    For example:
            Index 0 selects from array * 2
            Index 1 selects from array + 10
            Index 2 selects from array ** 2

# Output

Result using np.choose: [ 0 11 4  0]
