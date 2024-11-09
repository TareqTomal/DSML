# NumPy Boolean Indexing

# Explanation

01. Boolean Indexing:
        array % 3 == 0 creates a Boolean array where each element is True if it is divisible by 3.

        array[array % 3 == 0] uses this Boolean array to filter elements that meet the condition.

02. Result:
        Only elements divisible by 3 are selected: [3, 6].

# output

Original Array: [1 2 3 4 5 6]
Numbers Divisible by 3: [3 6]
